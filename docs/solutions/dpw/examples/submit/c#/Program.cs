using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

public class Program
{
    public static async Task<Dictionary<string, string>> GetBasicAuthHeaderAsync(string clientId, string clientSecret)
    {
        var userPass = $"{clientId}:{clientSecret}";
        var authString = Convert.ToBase64String(Encoding.UTF8.GetBytes(userPass));
        var authHeaders = new Dictionary<string, string>
        {
            { "Authorization", "Basic " + authString }
        };
        return authHeaders;
    }

    public static async Task<Dictionary<string, string>> GetAuthHeaderAsync(string url, string clientId, string clientSecret)
    {
        var authHeaders = await GetBasicAuthHeaderAsync(clientId, clientSecret);

        var tokenRequestData = new Dictionary<string, string>
        {
            { "grant_type", "client_credentials" },
        };

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new FormUrlEncodedContent(tokenRequestData),
        };

        foreach (var header in authHeaders)
        {
            request.Headers.Add(header.Key, header.Value);
        }

        var response = await client.SendAsync(request);

        if (!response.IsSuccessStatusCode)
        {
            throw new Exception($"Failed to get JWT token: {await response.Content.ReadAsStringAsync()}");
        }

        Console.WriteLine("Authentication successful");

        var responseContent = await response.Content.ReadAsStringAsync();
        var identityPayload = JsonConvert.DeserializeObject<Dictionary<string, string>>(responseContent);

        return new Dictionary<string, string> { { "Authorization", $"Bearer {identityPayload["access_token"]}" } };
    }

    public static async Task<HttpResponseMessage> SubmitDataAsync(
        string url,
        Dictionary<string, string> headers,
        Dictionary<string, string> data)
    {
        using var client = new HttpClient();

        var jsonData = JsonConvert.SerializeObject(data);
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json"); // Correct placement of 'Content-Type'

        foreach (var header in headers)
        {
            client.DefaultRequestHeaders.Add(header.Key, header.Value); // Only request headers here
        }

        var response = await client.PostAsync(url, content); // Content with correct 'Content-Type'
        return response;
    }

    public static async Task Main(string[] args)
    {
        string clientId = Environment.GetEnvironmentVariable("CLIENT_ID");
        string clientSecret = Environment.GetEnvironmentVariable("CLIENT_SECRET");
        string loginUrl = "https://auth-dev.grasp-daas.com/oauth/token/";
        string submitUrl = "https://grasp-daas.com/api/subscription-dev/v1/submit/";

        var authHeaders = await GetAuthHeaderAsync(loginUrl, clientId, clientSecret);

        var data = new Dictionary<string, string>
        {
            { "dataset_id", "12345" },
            { "data", ""}
        };

        var headers = new Dictionary<string, string>(authHeaders);

        var response = await SubmitDataAsync(submitUrl, headers, data);

        Console.WriteLine(response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}

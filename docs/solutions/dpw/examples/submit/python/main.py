import base64
import json
import os
import typing

import requests


def get_basic_auth_header(client_id, client_secret) -> dict:
    """
    Return a dict containing the correct headers to set to make HTTP Basic
    Auth request
    @param client_id: client_id
    @param client_secret: client_secret
    @return: dict
    """
    user_pass = "{0}:{1}".format(client_id, client_secret)
    auth_string = base64.b64encode(user_pass.encode("utf-8"))
    auth_headers = {
        "AUTHORIZATION": "Basic " + auth_string.decode("utf-8"),
    }
    return auth_headers


def get_auth_header(url: str, client_id: str, client_secret: str) -> typing.Dict:
    """
    Function returning JWT token Auth Header OAuth2 client credentials flow.
    @param url: url
    @param client_id: client_id
    @param client_secret: client_secret
    @return: str
    """
    token_request_data = {
        "grant_type": "client_credentials",
    }
    auth_headers = get_basic_auth_header(client_id, client_secret)

    response = requests.post(url, data=token_request_data, headers=auth_headers)

    if response.status_code != 200:
        raise PermissionError(f"Failed to get JWT token: {response.content}")

    print("Authentication successful")

    identity_payload = json.loads(response.content.decode("utf-8"))
    return {"Authorization": f"Bearer {identity_payload['access_token']}"}


def submit_data(
    url: str,
    headers: typing.Dict,
    data: typing.Dict,
) -> requests.Response:
    """
    Function to submit data to API.
    @param url: url
    @param headers: headers
    @param data: data
    @return: requests.Response
    """
    return requests.post(url, data=json.dumps(data), headers=headers)


if __name__ == "__main__":
    """
    # When data is invalid, 422 response is returned with instruction on how
    # to fix the data
    <Response [422]> {
      'detail': [
        {
          'loc': ['body', 0],
          'msg': 'Expecting value: line 1 column 1 (char 0)', 'type': 'value_error.jsondecode',
          'ctx': {
            'msg': 'Expecting value',
            'doc': 'dataset_id=',
            'pos': 0,
            'lineno': 1,
            'colno': 1
          }
        }
      ]
    }

    # 404 response is returned when dataset_id is invalid (cannot be found)
    <Response [404]> {
      'detail': 'No dataset definition found: workflows/eae3b2be-f377-445e-86b0-ead33827daae/datasets/.json'
    }

    # 200 response is returned when data is successfully submitted
    <Response [200]> {
      "status": "pending",
      "dataset_id": "<uuid>",
      "session_id": "<uuid>"
    }
    """

    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    LOGIN_URL = "https://auth-dev.grasp-daas.com/oauth/token/"
    SUBMIT_URL = "https://grasp-daas.com/api/subscription-dev/v1/submit/"
    DATASET_ID = ""

    data = [{}]
    auth_headers = get_auth_header(
        url=LOGIN_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )

    extra_headers = {"Content-Type": "application/json"}

    headers = {**auth_headers, **extra_headers}

    payload = {"dataset_id": DATASET_ID, "data": data}

    response = submit_data(
        url=SUBMIT_URL,
        headers=headers,
        data=payload,
    )
    print(response, response.json())

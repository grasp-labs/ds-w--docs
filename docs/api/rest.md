# REST API Guidelines

This guidelines are focused on a set of core topics, and not intended to cover all aspects of REST API design. 

Just want to mention as in other documents, this is guidelines, not rules.

## REST

REST APIs should be created with a minimum of [REST maturity level 2](https://martinfowler.com/articles/richardsonMaturityModel.html#level2). In our practices, it means:
- HTTPS as transport protocol
- APIs are modeled around resources with URIs that uniquely identifies the resource.
- Resources are accessed and manipulated through the standard HTTP methods.
- APIs respond with standard Http status codes.

## Avoid verbs

The URL should only be used to address the resource model, and not contain any operation/verbs. The only operations available in APIs are HTTP methods.


| Avoid this | Instead, do something like this |
| ---- | ---- |
| `GET /create-product` | `POST /product` |
| `GET /execute-job` | `POST /jobs/{job-id}/execution/`<br/>`PUT /jobs/{job-id}/start-execution`<br/>`GET /jobs/{job-id}/execution/result`|

## HTTP Methods

The list below shows the most common HTTP methods used in REST APIs. 

| HTTP Method | CRUD | Description |
| --- | --- | --- |
| GET | Read | Request a representation of the specified resource or resource collection. GET requests should only retrieve data. `GET` is safe, idempotent & cacheable. |
| POST | Create | Submit an entity to the specified resource. `POST` is not safe, idempotent or cacheable. |
| PUT | Update (replace) | Replace all representations of the target resource with the request payload. `PUT` is idempotent, but not safe or cacheable. |
| PATCH | Update (modify) | Apply partial modifications to a resource. `PATCH` is not safe, idempotent or cacheable. | 
| DELETE | Delete | Deletes the specified resource. `DELETE` is idempotent, but not safe or cacheable.|

## HTTP Status codes

HTTP Status codes are returned from the server in response to an HTTP request, to indicate whether the request has completed successfully. HTTP status codes should be used accurately and consistently with the semantics of the HTTP standard. The OpenAPI specification should document all possible HTTP Status codes for each endpoint so that consumers can understand which responses they can expect.

The status codes are grouped in five classes:

* 1xx informational response – the request was received, continuing process
* 2xx successful – the request was successfully received, understood, and accepted
* 3xx redirection – further action needs to be taken in order to complete the request
* 4xx client error – the request contains bad syntax or cannot be fulfilled
* 5xx server error – the server failed to fulfill an apparently valid request

In total there are over 60 possible HTTP Status codes, but APIs should focus on using a limited set in a consistent manner.

Commonly used HTTP Status codes are: 
* 200 OK - The request completed successfully
* 201 Created - The request completed successfully and one or more new resources were created
* 204 No Content - The request completed successfully and there is no additional content in the response (commonly used for HTTP PATCH)
* 307/308 Temporary/Permanent redirect - Redirect to other location for resource (use 307/308 in order to retain HTTP verb on redirect)
* 400 Bad Request - The request is not compliant with the OpenAPI specification (for example missing parameters in the query string or request body invalid)
* 403 Forbidden - User does not have sufficient authorizations
* 404 Not Found - The resource does not exist or an non-existing endpoint has been called
* 409 Conflict - The request cannot be completed due to conflict with resource current state
* 500 Internal Server Error - The server failed to fulfill an apparently valid request
* 503 Service unavailable - API or a service it depends on is temporarily unavailable

Links to status code lists:
* [Hypertext Transfer Protocol (HTTP) Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
* [MDN web docs - HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* [REST API Tutorial - HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)

## Query parameters

Query parameters are suitable for non-hierarchical search, filter and pagination parameters of `GET` requests. Sensitive data like session tokens shall not be places in query parameters, as request URIs are often stored in server logs and browser caches and are vulnerable to [HTTP referrer leakage](https://portswigger.net/kb/issues/00500400_cross-domain-referer-leakage). 


## Data formats

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) should be used for encoding text and textual representation of data.

JSON is the preferred data format for REST APIs. Other formats like XML, WITSML, etc. can be used in cases where it gives a clear benefit. Offering multiple formats should then be considered, by supporting [content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation).

### Dates

[RFC3339](https://tools.ietf.org/html/rfc3339) with UTC is the recommended date format.<br/> Example: `1956-02-08T12:34:56Z` = February 8th, 1956. 12:34:56 UTC

## API Versioning and API Evolution

API versioning can come with a significant cost. Supporting multiple versions of the API can make development, testing, operation and evolving the API much more complex. Therefore, versioning may be avoided whenever possible.

API Evolution is the concept of striving to not make breaking changes to the API until there are absolutely no other options.

Eventually, when breaking changes _must_ happen, the API developers should communicate the changes clearly  before implementing them in a predictable manner. Client developers should be contacted directly and mechanisms like the `deprecated` field of the OpenAPI specification should be applied.

## Deprecation

When planning a phase out, API developers should set a sunset date, which is the planned date when the endpoint/version/feature becomes unavailable. The endpoint/version/feature should be marked as deprecated at the same time as the sunset date is published. 

All deprecated items should be marked in the OpenAPI specification, by setting the deprecated field and adding a comment in the corresponding description field.

All endpoints containing deprecated elements should return the [`Deprecation: <deprecation date>|"true"`](https://tools.ietf.org/html/draft-dalal-deprecation-header-02) and [`Sunset: <sunset date>`](https://tools.ietf.org/html/rfc8594) HTTP headers.

More reading could be found here: [Zalando REST API Guidelines](https://opensource.zalando.com/restful-api-guidelines/#deprecation).
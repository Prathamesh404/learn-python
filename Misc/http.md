### What happens when ...

#### When you type google.com?

1. DNS lookup -> Finding a correct ip address which maps to `google.com`.
  - It's like phonebook for the internet.
  - When the human-readable address hits a DNS lookup/server, it maps to its corresponding IP address.
  - `google.com --> 172.217.9.142`
  - `facebook.com --> 157.240.2.35`
2. Computer makes a REQUEST to a server.
3. Server processes the REQUEST.
4. Server issues a response.
5. Step 2-3-4 indicates the Request-Response cycle.


#### What is Request and Responses?
- Put a image to proper explanation.
-

#### What are HTTP Headers?
- Metadata about the requests / responses. Sent with both requests and responses.
- Provide additional information about the request or response.

|Request Headers.|
|-------|
|  `Accept`-  Acceptable content-types for response (e.g. HTML, JSON, XML)|
|`Cache-Control` - Specify Caching Behaviour. |
|`User-agent` - Information about the software used to make the request. |

|Response Headers.|
|-----------------
|`Access-Control-Allow-Origin` - specify domains that can make requests.|
|`Allowed` - HTTP verbs that are allowed in requests.|

#### HTTP Verbs.

|Get|Post|
|------|------|
|Useful for retrieving data.| Useful for writing data.|
|Data passed in query string| Data passed is in request body|
|Should have no side-effects|Can have "Side-effects"|
|Can be cached | Not cached |
|Can be Bookmarked| Can't be Bookmark|

#### Application Programming Interface.

- Allows you to get data from another application without needing to understand how the application works.
- Can send data back in different formats. e.g. JSON, XML.
- Examples of companies with APIs: Github, Spotify, Google.
- 

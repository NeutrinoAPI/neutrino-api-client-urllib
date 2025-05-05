# NeutrinoAPI Python Native SDK

Neutrino API Python client using native urllib HTTP library

The official API client and SDK built by [NeutrinoAPI](https://www.neutrinoapi.com/)

| Feature          |        |
|------------------|--------|
| Platform Version | >= 3   |
| HTTP Library     | Native |
| JSON Library     | Native |
| HTTP/2           | No     |
| HTTP/3           | No     |
| CodeGen Version  | 4.7.1  |

## Getting started

First you will need a user ID and API key pair: [SignUp](https://www.neutrinoapi.com/signup/)

## To Initialize 
```python
from neutrino_api.neutrino_api_client import *

client = NeutrinoAPIClient("<USER_ID>", "<API_KEY>")
```

## Running Examples

```sh
$ python3 -m neutrino_api.examples.ip_info
```
You can find examples of all APIs in _neutrino_api/examples/_

Set the __'your-user-id'__ and __'your-api-key'__ values in the example to retrieve real API responses

## For Support 
[Contact us](https://www.neutrinoapi.com/contact-us/)

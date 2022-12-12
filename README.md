# NeutrinoAPI Python Native SDK

Python client using native urllib HTTP client

The official API client and SDK built by [NeutrinoAPI](https://www.neutrinoapi.com/)

| Feature          |       |
|------------------|-------|
| Platform Version | >= 3  |
| HTTP Library     |       |
| JSON Library     |       |
| HTTP/2           | false |
| HTTP/3           | false |
| CodeGen Version  | 4.6.8 |

## Getting started

First you will need a user ID and API key pair: [SignUp](https://www.neutrinoapi.com/signup/)

## To Initialize 
```python
from neutrino_api.neutrino_api_client import *

client = NeutrinoAPIClient("<USER_ID>", "<API_KEY>")
```

## Running Examples

```sh
$ python3 -m "examples.ip_info"
```
You can find examples of all APIs in _examples/_

## For Support 
[Contact us](https://www.neutrinoapi.com/contact-us/)
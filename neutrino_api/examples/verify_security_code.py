"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The security code to verify
    "security_code": "123456",

    # If set then enable additional brute-force protection by limiting the number of attempts by the
    # supplied value. This can be set to any unique identifier you would like to limit by, for example a
    # hash of the users email, phone number or IP address. Requests to this API will be ignored after
    # approximately 10 failed verification attempts
    "limit_by": ""
}
response = client.verify_security_code(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # True if the code is valid
    print("verified:", data.get("verified"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

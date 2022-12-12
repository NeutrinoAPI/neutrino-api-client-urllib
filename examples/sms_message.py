"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The phone number to send a message to
    "number": "+12106100045",

    # ISO 2-letter country code, assume numbers are based in this country. If not set numbers are
    # assumed to be in international format (with or without the leading + sign)
    "country_code": "",

    # Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within
    # the TTL then error code 14 will be returned
    "limit": "10",

    # The SMS message to send. Messages are truncated to a maximum of 150 characters for ASCII content
    # OR 70 characters for UTF content
    "message": "Hello, this is a test message!",

    # Set the TTL in number of days that the 'limit' option will remember a phone number (the default is
    # 1 day and the maximum is 365 days)
    "limit_ttl": "1"
}
response = client.sms_message(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # True if this a valid phone number
    print("number-valid:", data.get("number-valid"))

    # True if the SMS has been sent
    print("sent:", data.get("sent"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

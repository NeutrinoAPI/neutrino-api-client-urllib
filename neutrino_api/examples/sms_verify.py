"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The phone number to send a verification code to
    "number": "+12106100045",

    # ISO 2-letter country code, assume numbers are based in this country. If not set numbers are
    # assumed to be in international format (with or without the leading + sign)
    "country_code": "",

    # Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA
    # methods. If not set then we will generate a secure random code
    "security_code": "",

    # The language to send the verification code in, available languages are:
    # • de - German
    # • en - English
    # • es - Spanish
    # • fr - French
    # • it - Italian
    # • pt - Portuguese
    # • ru - Russian
    "language_code": "en",

    # The number of digits to use in the security code (must be between 4 and 12)
    "code_length": "5",

    # Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within
    # the TTL then error code 14 will be returned
    "limit": "10",

    # Set a custom brand or product name in the verification message
    "brand_name": "",

    # Set the TTL in number of days that the 'limit' option will remember a phone number (the default is
    # 1 day and the maximum is 365 days)
    "limit_ttl": "1"
}
response = client.sms_verify(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # True if this a valid phone number
    print("number-valid:", data.get("number-valid"))

    # The security code generated, you can save this code to perform your own verification or you can
    # use the Verify Security Code API
    print("security-code:", "'{0}'".format(data.get("security-code")))

    # True if the SMS has been sent
    print("sent:", data.get("sent"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

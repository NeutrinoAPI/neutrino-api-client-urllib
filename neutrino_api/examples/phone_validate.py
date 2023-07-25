"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # A phone number. This can be in international format (E.164) or local format. If passing local
    # format you must also set either the 'country-code' OR 'ip' options as well
    "number": "+6495552000",

    # ISO 2-letter country code, assume numbers are based in this country. If not set numbers are
    # assumed to be in international format (with or without the leading + sign)
    "country_code": "",

    # Pass in a users IP address and we will assume numbers are based in the country of the IP address
    "ip": ""
}
response = client.phone_validate(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The phone number country
    print("country:", "'{0}'".format(data.get("country")))

    # The phone number country as an ISO 2-letter country code
    print("country-code:", "'{0}'".format(data.get("country-code")))

    # The phone number country as an ISO 3-letter country code
    print("country-code3:", "'{0}'".format(data.get("country-code3")))

    # ISO 4217 currency code associated with the country
    print("currency-code:", "'{0}'".format(data.get("currency-code")))

    # The international calling code
    print("international-calling-code:", "'{0}'".format(data.get("international-calling-code")))

    # The number represented in full international format (E.164)
    print("international-number:", "'{0}'".format(data.get("international-number")))

    # True if this is a mobile number. If the number type is unknown this value will be false
    print("is-mobile:", data.get("is-mobile"))

    # The number represented in local dialing format
    print("local-number:", "'{0}'".format(data.get("local-number")))

    # The phone number location. Could be the city, region or country depending on the type of number
    print("location:", "'{0}'".format(data.get("location")))

    # The network/carrier who owns the prefix (this only works for some countries, use HLR lookup for
    # global network detection)
    print("prefix-network:", "'{0}'".format(data.get("prefix-network")))

    # The number type based on the number prefix. Possible values are:
    # • mobile
    # • fixed-line
    # • premium-rate
    # • toll-free
    # • voip
    # • unknown (use HLR lookup)
    print("type:", "'{0}'".format(data.get("type")))

    # Is this a valid phone number
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

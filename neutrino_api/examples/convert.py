"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The value to convert from (e.g. 10.95)
    "from_value": "100",

    # The type of the value to convert from (e.g. USD)
    "from_type": "USD",

    # The type to convert to (e.g. EUR)
    "to_type": "EUR"
}
response = client.convert(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The full name of the type being converted from
    print("from-name:", "'{0}'".format(data.get("from-name")))

    # The standard UTF-8 symbol used to represent the type being converted from
    print("from-symbol:", "'{0}'".format(data.get("from-symbol")))

    # The type of the value being converted from
    print("from-type:", "'{0}'".format(data.get("from-type")))

    # The value being converted from
    print("from-value:", "'{0}'".format(data.get("from-value")))

    # The result of the conversion in string format
    print("result:", "'{0}'".format(data.get("result")))

    # The result of the conversion as a floating-point number
    print("result-float:", data.get("result-float"))

    # The full name of the type being converted to
    print("to-name:", "'{0}'".format(data.get("to-name")))

    # The standard UTF-8 symbol used to represent the type being converted to
    print("to-symbol:", "'{0}'".format(data.get("to-symbol")))

    # The type being converted to
    print("to-type:", "'{0}'".format(data.get("to-type")))

    # True if the conversion was successful and produced a valid result
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

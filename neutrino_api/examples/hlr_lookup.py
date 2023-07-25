"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # A phone number
    "number": "+12106100045",

    # ISO 2-letter country code, assume numbers are based in this country. If not set numbers are
    # assumed to be in international format (with or without the leading + sign)
    "country_code": ""
}
response = client.hlr_lookup(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The phone number country
    print("country:", "'{0}'".format(data.get("country")))

    # The number location as an ISO 2-letter country code
    print("country-code:", "'{0}'".format(data.get("country-code")))

    # The number location as an ISO 3-letter country code
    print("country-code3:", "'{0}'".format(data.get("country-code3")))

    # ISO 4217 currency code associated with the country
    print("currency-code:", "'{0}'".format(data.get("currency-code")))

    # The currently used network/carrier name
    print("current-network:", "'{0}'".format(data.get("current-network")))

    # The HLR lookup status, possible values are:
    # • ok - the HLR lookup was successful and the device is connected
    # • absent - the number was once registered but the device has been switched off or out of network
    #   range for some time
    # • unknown - the number is not known by the mobile network
    # • invalid - the number is not a valid mobile MSISDN number
    # • fixed-line - the number is a registered fixed-line not mobile
    # • voip - the number has been detected as a VOIP line
    # • failed - the HLR lookup has failed, we could not determine the real status of this number
    print("hlr-status:", "'{0}'".format(data.get("hlr-status")))

    # Was the HLR lookup successful. If true then this is a working and registered cell-phone or mobile
    # device (SMS and phone calls will be delivered)
    print("hlr-valid:", data.get("hlr-valid"))

    # The mobile IMSI number (International Mobile Subscriber Identity)
    print("imsi:", "'{0}'".format(data.get("imsi")))

    # The international calling code
    print("international-calling-code:", "'{0}'".format(data.get("international-calling-code")))

    # The number represented in full international format
    print("international-number:", "'{0}'".format(data.get("international-number")))

    # True if this is a mobile number (only true with 100% certainty, if the number type is unknown this
    # value will be false)
    print("is-mobile:", data.get("is-mobile"))

    # Has this number been ported to another network
    print("is-ported:", data.get("is-ported"))

    # Is this number currently roaming from its origin country
    print("is-roaming:", data.get("is-roaming"))

    # The number represented in local dialing format
    print("local-number:", "'{0}'".format(data.get("local-number")))

    # The number location. Could be a city, region or country depending on the type of number
    print("location:", "'{0}'".format(data.get("location")))

    # The mobile MCC number (Mobile Country Code)
    print("mcc:", "'{0}'".format(data.get("mcc")))

    # The mobile MNC number (Mobile Network Code)
    print("mnc:", "'{0}'".format(data.get("mnc")))

    # The mobile MSC number (Mobile Switching Center)
    print("msc:", "'{0}'".format(data.get("msc")))

    # The mobile MSIN number (Mobile Subscription Identification Number)
    print("msin:", "'{0}'".format(data.get("msin")))

    # The number type, possible values are:
    # • mobile
    # • fixed-line
    # • premium-rate
    # • toll-free
    # • voip
    # • unknown
    print("number-type:", "'{0}'".format(data.get("number-type")))

    # True if this a valid phone number
    print("number-valid:", data.get("number-valid"))

    # The origin network/carrier name
    print("origin-network:", "'{0}'".format(data.get("origin-network")))

    # The ported to network/carrier name (only set if the number has been ported)
    print("ported-network:", "'{0}'".format(data.get("ported-network")))

    # If the number is currently roaming, the ISO 2-letter country code of the roaming in country
    print("roaming-country-code:", "'{0}'".format(data.get("roaming-country-code")))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

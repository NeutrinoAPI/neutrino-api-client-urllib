"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The BIN or IIN number. This is the first 6, 8 or 10 digits of a card number, use 8 (or more)
    # digits for the highest level of accuracy
    "bin_number": "48334884",

    # Pass in the customers IP address and we will return some extra information about them
    "customer_ip": ""
}
response = client.bin_lookup(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The BIN number returned. You may count the number of digits in this field to determine if the BIN
    # is likely to be based on an 8-digit or 6-digit card
    print("bin-number:", "'{0}'".format(data.get("bin-number")))

    # The card brand (e.g. Visa or Mastercard)
    print("card-brand:", "'{0}'".format(data.get("card-brand")))

    # The card category. There are many different card categories the most common card categories are:
    # CLASSIC, BUSINESS, CORPORATE, PLATINUM, PREPAID
    print("card-category:", "'{0}'".format(data.get("card-category")))

    # The card type, will always be one of: DEBIT, CREDIT, CHARGE CARD
    print("card-type:", "'{0}'".format(data.get("card-type")))

    # The full country name of the issuer
    print("country:", "'{0}'".format(data.get("country")))

    # The ISO 2-letter country code of the issuer
    print("country-code:", "'{0}'".format(data.get("country-code")))

    # The ISO 3-letter country code of the issuer
    print("country-code3:", "'{0}'".format(data.get("country-code3")))

    # ISO 4217 currency code associated with the country of the issuer
    print("currency-code:", "'{0}'".format(data.get("currency-code")))

    # True if the customers IP is listed on one of our blocklists, see the IP Blocklist API
    print("ip-blocklisted:", data.get("ip-blocklisted"))

    # An array of strings indicating which blocklists this IP is listed on
    print("ip-blocklists:", data.get("ip-blocklists"))

    # The city of the customers IP (if detectable)
    print("ip-city:", "'{0}'".format(data.get("ip-city")))

    # The country of the customers IP
    print("ip-country:", "'{0}'".format(data.get("ip-country")))

    # The ISO 2-letter country code of the customers IP
    print("ip-country-code:", "'{0}'".format(data.get("ip-country-code")))

    # The ISO 3-letter country code of the customers IP
    print("ip-country-code3:", "'{0}'".format(data.get("ip-country-code3")))

    # True if the customers IP country matches the BIN country
    print("ip-matches-bin:", data.get("ip-matches-bin"))

    # The region of the customers IP (if detectable)
    print("ip-region:", "'{0}'".format(data.get("ip-region")))

    # Is this a commercial/business use card
    print("is-commercial:", data.get("is-commercial"))

    # Is this a prepaid or prepaid reloadable card
    print("is-prepaid:", data.get("is-prepaid"))

    # The card issuer
    print("issuer:", "'{0}'".format(data.get("issuer")))

    # The card issuers phone number
    print("issuer-phone:", "'{0}'".format(data.get("issuer-phone")))

    # The card issuers website
    print("issuer-website:", "'{0}'".format(data.get("issuer-website")))

    # Is this a valid BIN or IIN number
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

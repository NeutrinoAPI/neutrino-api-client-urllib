"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The full address, partial address or name of a place to try and locate. Comma separated address
    # components are preferred.
    "address": "1 Molesworth Street, Thorndon, Wellington 6011",

    # The house/building number to locate
    "house_number": "",

    # The street/road name to locate
    "street": "",

    # The city/town name to locate
    "city": "",

    # The county/region name to locate
    "county": "",

    # The state name to locate
    "state": "",

    # The postal code to locate
    "postal_code": "",

    # Limit result to this country (the default is no country bias)
    "country_code": "",

    # The language to display results in, available languages are:
    # • de, en, es, fr, it, pt, ru, zh
    "language_code": "en",

    # If no matches are found for the given address, start performing a recursive fuzzy search until a
    # geolocation is found. This option is recommended for processing user input or implementing
    # auto-complete. We use a combination of approximate string matching and data cleansing to find
    # possible location matches
    "fuzzy_search": "false"
}
response = client.geocode_address(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The number of possible matching locations found
    print("found:", data.get("found"))

    # Array of matching location objects
    print("locations:", end=None)
    for item in data.get("locations"):

        # The complete address using comma-separated values
        print("    address:", "'{0}'".format(item.get("address")))

        # The components which make up the address such as road, city, state, etc
        print("    address-components:", item.get("address-components"))

        # The city of the location
        print("    city:", "'{0}'".format(item.get("city")))

        # The country of the location
        print("    country:", "'{0}'".format(item.get("country")))

        # The ISO 2-letter country code of the location
        print("    country-code:", "'{0}'".format(item.get("country-code")))

        # The ISO 3-letter country code of the location
        print("    country-code3:", "'{0}'".format(item.get("country-code3")))

        # ISO 4217 currency code associated with the country
        print("    currency-code:", "'{0}'".format(item.get("currency-code")))

        # The location latitude
        print("    latitude:", item.get("latitude"))

        # Array of strings containing any location tags associated with the address. Tags are additional
        # pieces of metadata about a specific location, there are thousands of different tags. Some examples
        # of tags: shop, office, cafe, bank, pub
        print("    location-tags:", item.get("location-tags"))

        # The detected location type ordered roughly from most to least precise, possible values are:
        # • address - indicates a precise street address
        # • street - accurate to the street level but may not point to the exact location of the
        #   house/building number
        # • city - accurate to the city level, this includes villages, towns, suburbs, etc
        # • postal-code - indicates a postal code area (no house or street information present)
        # • railway - location is part of a rail network such as a station or railway track
        # • natural - indicates a natural feature, for example a mountain peak or a waterway
        # • island - location is an island or archipelago
        # • administrative - indicates an administrative boundary such as a country, state or province
        print("    location-type:", "'{0}'".format(item.get("location-type")))

        # The location longitude
        print("    longitude:", item.get("longitude"))

        # The formatted address using local standards suitable for printing on an envelope
        print("    postal-address:", "'{0}'".format(item.get("postal-address")))

        # The postal code for the location
        print("    postal-code:", "'{0}'".format(item.get("postal-code")))

        # The ISO 3166-2 region code for the location
        print("    region-code:", "'{0}'".format(item.get("region-code")))

        # The state of the location
        print("    state:", "'{0}'".format(item.get("state")))

        # Structure of a ip-info -> timezone response
        print("    timezone:", item.get("timezone"))
        print("")
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

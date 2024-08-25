"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The location latitude in decimal degrees format
    "latitude": "-41.2775847",

    # The location longitude in decimal degrees format
    "longitude": "174.7775229",

    # The language to display results in, available languages are:
    # • de, en, es, fr, it, pt, ru
    "language_code": "en",

    # The zoom level to respond with:
    # • address - the most precise address available
    # • street - the street level
    # • city - the city level
    # • state - the state level
    # • country - the country level
    "zoom": "address"
}
response = client.geocode_reverse(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The complete address using comma-separated values
    print("address:", "'{0}'".format(data.get("address")))

    # The components which make up the address such as road, city, state, etc
    print("address-components:", data.get("address-components"))

    # The city of the location
    print("city:", "'{0}'".format(data.get("city")))

    # The country of the location
    print("country:", "'{0}'".format(data.get("country")))

    # The ISO 2-letter country code of the location
    print("country-code:", "'{0}'".format(data.get("country-code")))

    # The ISO 3-letter country code of the location
    print("country-code3:", "'{0}'".format(data.get("country-code3")))

    # ISO 4217 currency code associated with the country
    print("currency-code:", "'{0}'".format(data.get("currency-code")))

    # True if these coordinates map to a real location
    print("found:", data.get("found"))

    # The location latitude
    print("latitude:", data.get("latitude"))

    # Array of strings containing any location tags associated with the address. Tags are additional
    # pieces of metadata about a specific location, there are thousands of different tags. Some examples
    # of tags: shop, office, cafe, bank, pub
    print("location-tags:", data.get("location-tags"))

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
    print("location-type:", "'{0}'".format(data.get("location-type")))

    # The location longitude
    print("longitude:", data.get("longitude"))

    # The formatted address using local standards suitable for printing on an envelope
    print("postal-address:", "'{0}'".format(data.get("postal-address")))

    # The postal code for the location
    print("postal-code:", "'{0}'".format(data.get("postal-code")))

    # The ISO 3166-2 region code for the location
    print("region-code:", "'{0}'".format(data.get("region-code")))

    # The state of the location
    print("state:", "'{0}'".format(data.get("state")))

    # Structure of a ip-info -> timezone response
    print("timezone:", data.get("timezone"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

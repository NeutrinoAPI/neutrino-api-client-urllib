"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The full address, partial address or name of a place to try and locate. Comma separated address
    # components are preferred.
    "address": "1 Molesworth Street, Thorndon, Wellington 6011",

    # The house/building number to locate (for structured address searches)
    "house_number": "",

    # The street/road name to locate (for structured address searches)
    "street": "",

    # The city/town name to locate (for structured address searches)
    "city": "",

    # The county/region name to locate (for structured address searches)
    "county": "",

    # The state name to locate (for structured address searches)
    "state": "",

    # The postal code to locate (for structured address searches)
    "postal_code": "",

    # Prefer results from this country code (the default is no country bias)
    "country_code": "",

    # Prefer results from this list of country codes (space or comma separated values). Preference is in
    # the order supplied, you can use the 'country-code' parameter to also set a dynamic or user
    # supplied country code which takes precedence
    "country_codes": "",

    # The language to display results in, available languages are:
    # • ar, de, en, es, fr, it, ja, nl, pt, ru, zh
    "language_code": "en",

    # Enable auto-complete for search-as-you-type and search suggestions. This option can find addresses
    # based on partial search terms, combine with 'country-code' for country specific searches.
    # Auto-complete works best with 'fuzzy-search' disabled for the fastest response times but can be
    # combined if required
    "auto_complete": "false",

    # If no matches are found for the given address, start performing a recursive fuzzy search until a
    # geolocation is found. This option is useful for processing user supplied input that may be
    # incomplete or have typos and where you do not mind some potential loss in precision
    "fuzzy_search": "false",

    # Limit search results to this many locations (between 1 and a maximum of 32)
    "limit": "8"
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

        # The full address string using comma-separated values, use 'postal-address' for the address string
        # formatted using country/region specific rules
        print("    address:", "'{0}'".format(item.get("address")))

        # The components which make up the address such as road, city, state, etc. These are country/region
        # specific values, use 'address-structured' for a strict address structure which is the same for all
        # locations globally
        print("    address-components:", item.get("address-components"))

        # Structure of address-structured
        print("    address-structured:", item.get("address-structured"))

        # The detected building type for the address, possible values are:
        # • none - no building type was detected for this location
        # • house - a residential house/property
        # • apartment - a residential apartment complex
        # • office - a commercial/business office
        # • accommodation - a hotel/motel or other type of accommodation
        # • education - a school or university
        # • food - a restaurant or place where food can be purchased
        # • shop - a shop selling any type of goods
        # • attraction - an attraction such as theme parks or tourist activities
        # • medical - a hospital or other medical facility
        # • transport - a transportation building such as a bus or train depot
        # • commercial - a commercial/industrial building
        # • government - a government or military facility
        # • public - a public building such as a townhall or community centre
        print("    building-type:", "'{0}'".format(item.get("building-type")))

        # The city of the location
        print("    city:", "'{0}'".format(item.get("city")))

        # ISO 2-letter continent code
        print("    continent-code:", "'{0}'".format(item.get("continent-code")))

        # The country of the location
        print("    country:", "'{0}'".format(item.get("country")))

        # The ISO 2-letter country code of the location
        print("    country-code:", "'{0}'".format(item.get("country-code")))

        # The ISO 3-letter country code of the location
        print("    country-code3:", "'{0}'".format(item.get("country-code3")))

        # ISO 4217 currency code associated with the country
        print("    currency-code:", "'{0}'".format(item.get("currency-code")))

        # The location geohash
        print("    geohash:", "'{0}'".format(item.get("geohash")))

        # The ISO 2-letter language code for the official language spoken in the country
        print("    language-code:", "'{0}'".format(item.get("language-code")))

        # The location latitude
        print("    latitude:", item.get("latitude"))

        # Map containing any external metadata linked to the location. Currently supports the following
        # values which are only set if known: website-url, phone-number, org-name, wikipedia-title,
        # wikidata-entity
        print("    location-profile:", item.get("location-profile"))

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

        # Structure of timezone
        print("    timezone:", item.get("timezone"))
        print("")
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

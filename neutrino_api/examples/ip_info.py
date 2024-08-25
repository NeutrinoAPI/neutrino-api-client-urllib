"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # An IPv4 or IPv6 address. Accepts standard IP notation and also CIDR notation
    "ip": "1.1.1.1",

    # Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if
    # you need it
    "reverse_lookup": "false"
}
response = client.ip_info(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # Name of the city (if detectable)
    print("city:", "'{0}'".format(data.get("city")))

    # ISO 2-letter continent code
    print("continent-code:", "'{0}'".format(data.get("continent-code")))

    # Full country name
    print("country:", "'{0}'".format(data.get("country")))

    # ISO 2-letter country code
    print("country-code:", "'{0}'".format(data.get("country-code")))

    # ISO 3-letter country code
    print("country-code3:", "'{0}'".format(data.get("country-code3")))

    # ISO 4217 currency code associated with the country
    print("currency-code:", "'{0}'".format(data.get("currency-code")))

    # The IPs host domain (only set if reverse-lookup has been used)
    print("host-domain:", "'{0}'".format(data.get("host-domain")))

    # The IPs full hostname (only set if reverse-lookup has been used)
    print("hostname:", "'{0}'".format(data.get("hostname")))

    # The IPv4 or IPv6 address returned
    print("ip:", "'{0}'".format(data.get("ip")))

    # True if this is a bogon IP address such as a private network, local network or reserved address
    print("is-bogon:", data.get("is-bogon"))

    # True if this is a IPv4 mapped IPv6 address
    print("is-v4-mapped:", data.get("is-v4-mapped"))

    # True if this is a IPv6 address. False if IPv4
    print("is-v6:", data.get("is-v6"))

    # Location latitude
    print("latitude:", data.get("latitude"))

    # Location longitude
    print("longitude:", data.get("longitude"))

    # Name of the region (if detectable)
    print("region:", "'{0}'".format(data.get("region")))

    # ISO 3166-2 region code (if detectable)
    print("region-code:", "'{0}'".format(data.get("region-code")))

    # Structure of a ip-info -> timezone response
    print("timezone:", data.get("timezone"))

    # True if this is a valid IPv4 or IPv6 address
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

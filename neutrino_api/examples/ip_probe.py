"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # An IPv4 or IPv6 address. Accepts standard IP notation and also CIDR notation
    "ip": "194.233.98.38"
}
response = client.ip_probe(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The age of the autonomous system (AS) in number of years since registration
    print("as-age:", data.get("as-age"))

    # The autonomous system (AS) CIDR range
    print("as-cidr:", "'{0}'".format(data.get("as-cidr")))

    # The autonomous system (AS) ISO 2-letter country code
    print("as-country-code:", "'{0}'".format(data.get("as-country-code")))

    # The autonomous system (AS) ISO 3-letter country code
    print("as-country-code3:", "'{0}'".format(data.get("as-country-code3")))

    # The autonomous system (AS) description / company name
    print("as-description:", "'{0}'".format(data.get("as-description")))

    # Array of all the domains associated with the autonomous system (AS)
    print("as-domains:", data.get("as-domains"))

    # The autonomous system (AS) number
    print("asn:", "'{0}'".format(data.get("asn")))

    # Full city name (if detectable)
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

    # The IPs host domain
    print("host-domain:", "'{0}'".format(data.get("host-domain")))

    # The IPs full hostname (PTR)
    print("hostname:", "'{0}'".format(data.get("hostname")))

    # The IPv4 or IPv6 address returned
    print("ip:", "'{0}'".format(data.get("ip")))

    # True if this is a bogon IP address such as a private network, local network or reserved address
    print("is-bogon:", data.get("is-bogon"))

    # True if this IP belongs to a hosting company. Note that this can still be true even if the
    # provider type is VPN/proxy, this occurs in the case that the IP is detected as both types
    print("is-hosting:", data.get("is-hosting"))

    # True if this IP belongs to an internet service provider. Note that this can still be true even if
    # the provider type is VPN/proxy, this occurs in the case that the IP is detected as both types
    print("is-isp:", data.get("is-isp"))

    # True if this IP is a proxy
    print("is-proxy:", data.get("is-proxy"))

    # True if this is a IPv4 mapped IPv6 address
    print("is-v4-mapped:", data.get("is-v4-mapped"))

    # True if this is a IPv6 address. False if IPv4
    print("is-v6:", data.get("is-v6"))

    # True if this IP ia a VPN
    print("is-vpn:", data.get("is-vpn"))

    # A description of the provider (usually extracted from the providers website)
    print("provider-description:", "'{0}'".format(data.get("provider-description")))

    # The domain name of the provider
    print("provider-domain:", "'{0}'".format(data.get("provider-domain")))

    # The detected provider type, possible values are:
    # • isp - IP belongs to an internet service provider. This includes both mobile, home and business
    #   internet providers
    # • hosting - IP belongs to a hosting company. This includes website hosting, cloud computing
    #   platforms and colocation facilities
    # • vpn - IP belongs to a VPN provider
    # • proxy - IP belongs to a proxy service. This includes HTTP/SOCKS proxies and browser based
    #   proxies
    # • university - IP belongs to a university/college/campus
    # • government - IP belongs to a government department. This includes military facilities
    # • commercial - IP belongs to a commercial entity such as a corporate headquarters or company
    #   office
    # • unknown - could not identify the provider type
    print("provider-type:", "'{0}'".format(data.get("provider-type")))

    # The website URL for the provider
    print("provider-website:", "'{0}'".format(data.get("provider-website")))

    # Full region name (if detectable)
    print("region:", "'{0}'".format(data.get("region")))

    # ISO 3166-2 region code (if detectable)
    print("region-code:", "'{0}'".format(data.get("region-code")))

    # True if this is a valid IPv4 or IPv6 address
    print("valid:", data.get("valid"))

    # The domain of the VPN provider (may be empty if the VPN domain is not detectable)
    print("vpn-domain:", "'{0}'".format(data.get("vpn-domain")))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

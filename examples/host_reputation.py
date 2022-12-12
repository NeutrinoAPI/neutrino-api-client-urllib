"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # An IP address, domain name, FQDN or URL. If you supply a domain/URL it will be checked against the
    # URI DNSBL lists
    "host": "neutrinoapi.com",

    # Only check lists with this rating or better
    "list_rating": "3",

    # Only check these DNSBL zones/hosts. Multiple zones can be supplied as comma-separated values
    "zones": ""
}
response = client.host_reputation(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The IP address or host name
    print("host:", "'{0}'".format(data.get("host")))

    # Is this host blacklisted
    print("is-listed:", data.get("is-listed"))

    # The number of DNSBLs the host is listed on
    print("list-count:", data.get("list-count"))

    # Array of objects for each DNSBL checked
    print("lists:", end=None)
    for item in data.get("lists"):

        # True if the host is currently black-listed
        print("    is-listed:", item.get("is-listed"))

        # The hostname of the DNSBL
        print("    list-host:", "'{0}'".format(item.get("list-host")))

        # The name of the DNSBL
        print("    list-name:", "'{0}'".format(item.get("list-name")))

        # The list rating [1-3] with 1 being the best rating and 3 the lowest rating
        print("    list-rating:", item.get("list-rating"))

        # The DNSBL server response time in milliseconds
        print("    response-time:", item.get("response-time"))

        # The specific return code for this listing (only set if listed)
        print("    return-code:", "'{0}'".format(item.get("return-code")))

        # The TXT record returned for this listing (only set if listed)
        print("    txt-record:", "'{0}'".format(item.get("txt-record")))
        print("")
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".csv", prefix="ip-blocklist-download-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The data format. Can be either CSV or TXT
    "format": "csv",

    # Include public VPN provider addresses, this option is only available for Tier 3 or higher
    # accounts. Adds any IPs which are solely listed as VPN providers, IPs that are listed on multiple
    # sensors will still be included without enabling this option. WARNING: This adds at least an
    # additional 8 million IP addresses to the download if not using CIDR notation
    "include_vpn": "false",

    # Output IPs using CIDR notation. This option should be preferred but is off by default for
    # backwards compatibility
    "cidr": "false",

    # Output the IPv6 version of the blocklist, the default is to output IPv4 only. Note that this
    # option enables CIDR notation too as this is the only notation currently supported for IPv6
    "ip6": "false"
}
response = client.ip_blocklist_download(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

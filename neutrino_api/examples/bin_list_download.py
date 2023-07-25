"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".png", prefix="bin-list-download-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # Include ISO 3-letter country codes and ISO 3-letter currency codes in the data. These will be
    # added to columns 10 and 11 respectively
    "include_iso3": "false",

    # Include 8-digit and higher BIN codes. This option includes all 6-digit BINs and all 8-digit and
    # higher BINs (including some 9, 10 and 11 digit BINs where available)
    "include_8digit": "false"
}
response = client.bin_list_download(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

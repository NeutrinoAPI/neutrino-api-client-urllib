"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".png", prefix="qr-code-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The barcode format to output. Accepted formats are: qr, c128
    "code_format": "qr",

    # The width of the QR code (in px)
    "width": "256",

    # The QR code foreground color
    "fg_color": "#000000",

    # The QR code background color
    "bg_color": "#ffffff",

    # The content to encode into the QR code (e.g. a URL or a phone number)
    "content": "https://www.neutrinoapi.com/signup/",

    # The height of the QR code (in px)
    "height": "256"
}
response = client.qr_code(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

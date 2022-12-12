"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".png", prefix="image-resize-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The width to resize to (in px) while preserving aspect ratio
    "width": "32",

    # The output image format, can be either png or jpg
    "format": "png",

    # The URL or Base64 encoded Data URL for the source image (you can also upload an image file
    # directly in which case this field is ignored)
    "image_url": "https://www.neutrinoapi.com/img/LOGO.png",

    # The height to resize to (in px) while preserving aspect ratio. If you don't set this field then
    # the height will be automatic based on the requested width and images aspect ratio
    "height": "32"
}
response = client.image_resize(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

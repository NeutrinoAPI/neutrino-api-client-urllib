"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".png", prefix="image-watermark-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The output image format, can be either png or jpg
    "format": "png",

    # If set resize the resulting image to this width (in px) while preserving aspect ratio
    "width": "",

    # The URL or Base64 encoded Data URL for the source image (you can also upload an image file
    # directly in which case this field is ignored)
    "image_url": "https://www.neutrinoapi.com/img/LOGO.png",

    # The position of the watermark image, possible values are: center, top-left, top-center, top-right,
    # bottom-left, bottom-center, bottom-right
    "position": "center",

    # The URL or Base64 encoded Data URL for the watermark image (you can also upload an image file
    # directly in which case this field is ignored)
    "watermark_url": "https://www.neutrinoapi.com/img/icons/security.png",

    # The opacity of the watermark (0 to 100)
    "opacity": "50",

    # If set resize the resulting image to this height (in px) while preserving aspect ratio
    "height": ""
}
response = client.image_watermark(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

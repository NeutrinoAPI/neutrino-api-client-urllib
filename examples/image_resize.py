"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".png", prefix="image-resize-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The resize mode to use, we support 3 main resizing modes:
    # • scale Resize to within the width and height specified while preserving aspect ratio. In this
    #   mode the width or height will be automatically adjusted to fit the aspect ratio
    # • pad Resize to exactly the width and height specified while preserving aspect ratio and pad any
    #   space left over. Any padded space will be filled in with the 'bg-color' value
    # • crop Resize to exactly the width and height specified while preserving aspect ratio and crop
    #   any space which fall outside the area. The cropping window is centered on the original image
    "resize_mode": "scale",

    # The width to resize to (in px)
    "width": "32",

    # The output image format, can be either png or jpg
    "format": "png",

    # The URL or Base64 encoded Data URL for the source image. You can also upload an image file
    # directly using multipart/form-data
    "image_url": "https://www.neutrinoapi.com/img/LOGO.png",

    # The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special
    # value of 'transparent' can also be used. For JPG output the default is black (#000000)
    "bg_color": "transparent",

    # The height to resize to (in px). If you don't set this field then the height will be automatic
    # based on the requested width and image aspect ratio
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

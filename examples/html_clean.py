"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".txt", prefix="html-clean-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The level of sanitization, possible values are: plain-text: reduce the content to plain text only
    # (no HTML tags at all) simple-text: allow only very basic text formatting tags like b, em, i,
    # strong, u basic-html: allow advanced text formatting and hyper links basic-html-with-images: same
    # as basic html but also allows image tags advanced-html: same as basic html with images but also
    # allows many more common HTML tags like table, ul, dl, pre
    "output_type": "plain-text",

    # The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an
    # HTML content string
    "content": "<div>Some HTML to clean...</div><script>alert()</script>"
}
response = client.html_clean(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

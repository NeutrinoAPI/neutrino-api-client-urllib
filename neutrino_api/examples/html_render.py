"""NeutrinoAPIClient Example"""

import sys
import tempfile
from neutrino_api.neutrino_api_client import *

output_file_path = tempfile.mkstemp(suffix=".pdf", prefix="html-render-")[1]

client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # Inject custom CSS into the HTML. e.g. 'body { background-color: red;}'
    "css": "",

    # The footer HTML to insert into each page. The following dynamic tags are supported: {date},
    # {title}, {url}, {pageNumber}, {totalPages}
    "footer": "",

    # The document title
    "title": "",

    # The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an
    # HTML content string
    "content": "<h1>TEST DOCUMENT</h1><p>Hello, this is a test page...</p>",

    # Set the PDF page width explicitly (in mm)
    "page_width": "",

    # Timeout in seconds. Give up if still trying to load the HTML content after this number of seconds
    "timeout": "300",

    # Render the final document in grayscale
    "grayscale": "false",

    # The document left margin (in mm)
    "margin_left": "0",

    # Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter
    "page_size": "A4",

    # Ignore any TLS/SSL certificate errors
    "ignore_certificate_errors": "false",

    # Set the PDF page height explicitly (in mm)
    "page_height": "",

    # The document top margin (in mm)
    "margin_top": "0",

    # For image rendering set the background color in hexadecimal notation (e.g. #0000ff). For PNG
    # output the special value of 'transparent' can be used to create a transparent PNG
    "bg_color": "",

    # The document margin (in mm)
    "margin": "0",

    # If rendering to an image format (PNG or JPG) use this image width (in pixels)
    "image_width": "1024",

    # Which format to output, available options are: PDF, PNG, JPG
    "format": "PDF",

    # Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size)
    "zoom": "1",

    # The document right margin (in mm)
    "margin_right": "0",

    # Number of seconds to wait before rendering the page (can be useful for pages with animations etc)
    "delay": "0",

    # If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is
    # automatic which dynamically sets the image height based on the content
    "image_height": "",

    # The header HTML to insert into each page. The following dynamic tags are supported: {date},
    # {title}, {url}, {pageNumber}, {totalPages}
    "header": "<div style='width: 100%; font-size: 8pt;'>{pageNumber} of {totalPages} - {date}</div>",

    # The document bottom margin (in mm)
    "margin_bottom": "0",

    # Set the document to landscape orientation
    "landscape": "false",

    # Execute JavaScript on the website. This parameter accepts JavaScript as either a string containing
    # JavaScript or for sending multiple separate statements a JSON array or POST array can also be
    # used. You can also use the following specially defined user interaction functions: sleep(seconds);
    # Just wait/sleep for the specified number of seconds. click('selector'); Click on the first element
    # matching the given selector. focus('selector'); Focus on the first element matching the given
    # selector. keys('characters'); Send the specified keyboard characters. Use click() or focus() first
    # to send keys to a specific element. enter(); Send the Enter key. tab(); Send the Tab key.
    "exec": "",

    # Override the browsers default user-agent string with this one
    "user_agent": ""
}
response = client.html_render(params, output_file_path)
if response.is_ok():
    output_file = response.file
    print("API Response OK, output saved to: {0}".format(output_file))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

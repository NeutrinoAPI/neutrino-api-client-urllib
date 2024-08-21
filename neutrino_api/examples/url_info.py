"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The URL to probe
    "url": "https://www.neutrinoapi.com/",

    # If this URL responds with html, text, json or xml then return the response. This option is useful
    # if you want to perform further processing on the URL content (e.g. with the HTML Extract or HTML
    # Clean APIs)
    "fetch_content": "false",

    # Ignore any TLS/SSL certificate errors and load the URL anyway
    "ignore_certificate_errors": "false",

    # Timeout in seconds. Give up if still trying to load the URL after this number of seconds
    "timeout": "60",

    # If the request fails for any reason try again this many times
    "retry": "0"
}
response = client.url_info(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The actual content this URL responded with. Only set if the 'fetch-content' option was used
    print("content:", "'{0}'".format(data.get("content")))

    # The encoding format the URL uses
    print("content-encoding:", "'{0}'".format(data.get("content-encoding")))

    # The size of the URL content in bytes
    print("content-size:", data.get("content-size"))

    # The content-type this URL serves
    print("content-type:", "'{0}'".format(data.get("content-type")))

    # True if this URL responded with an HTTP OK (200) status
    print("http-ok:", data.get("http-ok"))

    # True if this URL responded with an HTTP redirect
    print("http-redirect:", data.get("http-redirect"))

    # The HTTP status code this URL responded with. An HTTP status of 0 indicates a network level issue
    print("http-status:", data.get("http-status"))

    # The HTTP status message assoicated with the status code
    print("http-status-message:", "'{0}'".format(data.get("http-status-message")))

    # True if an error occurred while loading the URL. This includes network errors, TLS errors and
    # timeouts
    print("is-error:", data.get("is-error"))

    # True if a timeout occurred while loading the URL. You can set the timeout with the request
    # parameter 'timeout'
    print("is-timeout:", data.get("is-timeout"))

    # The ISO 2-letter language code of the page. Extracted from either the HTML document or via HTTP
    # headers
    print("language-code:", "'{0}'".format(data.get("language-code")))

    # The time taken to load the URL content in seconds
    print("load-time:", data.get("load-time"))

    # A key-value map of the URL query paramaters
    print("query:", data.get("query"))

    # Is this URL actually serving real content
    print("real:", data.get("real"))

    # The servers IP geo-location: full city name (if detectable)
    print("server-city:", "'{0}'".format(data.get("server-city")))

    # The servers IP geo-location: full country name
    print("server-country:", "'{0}'".format(data.get("server-country")))

    # The servers IP geo-location: ISO 2-letter country code
    print("server-country-code:", "'{0}'".format(data.get("server-country-code")))

    # The servers hostname (PTR record)
    print("server-hostname:", "'{0}'".format(data.get("server-hostname")))

    # The IP address of the server hosting this URL
    print("server-ip:", "'{0}'".format(data.get("server-ip")))

    # The name of the server software hosting this URL
    print("server-name:", "'{0}'".format(data.get("server-name")))

    # The servers IP geo-location: full region name (if detectable)
    print("server-region:", "'{0}'".format(data.get("server-region")))

    # The document title
    print("title:", "'{0}'".format(data.get("title")))

    # The fully qualified URL. This may be different to the URL requested if http-redirect is true
    print("url:", "'{0}'".format(data.get("url")))

    # The URL path
    print("url-path:", "'{0}'".format(data.get("url-path")))

    # The URL port
    print("url-port:", data.get("url-port"))

    # The URL protocol, usually http or https
    print("url-protocol:", "'{0}'".format(data.get("url-protocol")))

    # Is this a valid well-formed URL
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

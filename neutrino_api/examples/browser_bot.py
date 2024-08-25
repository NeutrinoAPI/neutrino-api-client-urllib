"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # Delay in seconds to wait before capturing any page data, executing selectors or JavaScript
    "delay": "3",

    # Ignore any TLS/SSL certificate errors and load the page anyway
    "ignore_certificate_errors": "false",

    # Extract content from the page DOM using this selector. Commonly known as a CSS selector, you can
    # find a good reference here
    "selector": ".button",

    # The URL to load
    "url": "https://www.neutrinoapi.com/",

    # Timeout in seconds. Give up if still trying to load the page after this number of seconds
    "timeout": "30",

    # Execute JavaScript on the website. This parameter accepts JavaScript as either a string containing
    # JavaScript or for sending multiple separate statements a JSON array or POST array can also be
    # used. If a statement returns any value it will be returned in the 'exec-results' response. You can
    # also use the following specially defined user interaction functions: sleep(seconds); Just
    # wait/sleep for the specified number of seconds. click('selector'); Click on the first element
    # matching the given selector. focus('selector'); Focus on the first element matching the given
    # selector. keys('characters'); Send the specified keyboard characters. Use click() or focus() first
    # to send keys to a specific element. enter(); Send the Enter key. tab(); Send the Tab key.
    "exec": "[click('#button-id'), sleep(1), click('.class'), keys('1234'), enter()]",

    # Override the browsers default user-agent string with this one
    "user_agent": ""
}
response = client.browser_bot(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The complete raw, decompressed and decoded page content. Usually will be either HTML, JSON or XML
    print("content:", "'{0}'".format(data.get("content")))

    # The size of the returned content in bytes
    print("content-size:", data.get("content-size"))

    # Array containing all the elements matching the supplied selector
    print("elements:", end=None)
    for item in data.get("elements"):

        # The 'class' attribute of the element
        print("    class:", "'{0}'".format(item.get("class")))

        # The 'href' attribute of the element
        print("    href:", "'{0}'".format(item.get("href")))

        # The raw HTML of the element
        print("    html:", "'{0}'".format(item.get("html")))

        # The 'id' attribute of the element
        print("    id:", "'{0}'".format(item.get("id")))

        # The plain-text content of the element with normalized whitespace
        print("    text:", "'{0}'".format(item.get("text")))
        print("")

    # Contains the error message if an error has occurred ('is-error' will be true)
    print("error-message:", "'{0}'".format(data.get("error-message")))

    # If you executed any JavaScript this array holds the results as objects
    print("exec-results:", end=None)
    for item in data.get("exec-results"):

        # The result of the executed JavaScript statement. Will be empty if the statement returned nothing
        print("    result:", "'{0}'".format(item.get("result")))

        # The JavaScript statement that was executed
        print("    statement:", "'{0}'".format(item.get("statement")))
        print("")

    # The redirected URL if the URL responded with an HTTP redirect
    print("http-redirect-url:", "'{0}'".format(data.get("http-redirect-url")))

    # The HTTP status code the URL returned
    print("http-status-code:", data.get("http-status-code"))

    # The HTTP status message the URL returned
    print("http-status-message:", "'{0}'".format(data.get("http-status-message")))

    # True if an error has occurred loading the page. Check the 'error-message' field for details
    print("is-error:", data.get("is-error"))

    # True if the HTTP status is OK (200)
    print("is-http-ok:", data.get("is-http-ok"))

    # True if the URL responded with an HTTP redirect
    print("is-http-redirect:", data.get("is-http-redirect"))

    # True if the page is secured using TLS/SSL
    print("is-secure:", data.get("is-secure"))

    # True if a timeout occurred while loading the page. You can set the timeout with the request
    # parameter 'timeout'
    print("is-timeout:", data.get("is-timeout"))

    # The ISO 2-letter language code of the page. Extracted from either the HTML document or via HTTP
    # headers
    print("language-code:", "'{0}'".format(data.get("language-code")))

    # The number of seconds taken to load the page (from initial request until DOM ready)
    print("load-time:", data.get("load-time"))

    # The document MIME type
    print("mime-type:", "'{0}'".format(data.get("mime-type")))

    # Map containing all the HTTP response headers the URL responded with
    print("response-headers:", data.get("response-headers"))

    # Map containing details of the TLS/SSL setup
    print("security-details:", data.get("security-details"))

    # The HTTP servers hostname (PTR/RDNS record)
    print("server-hostname:", "'{0}'".format(data.get("server-hostname")))

    # The HTTP servers IP address
    print("server-ip:", "'{0}'".format(data.get("server-ip")))

    # The document title
    print("title:", "'{0}'".format(data.get("title")))

    # The requested URL. This may not be the same as the final destination URL, if the URL redirects
    # then it will be set in 'http-redirect-url' and 'is-http-redirect' will also be true
    print("url:", "'{0}'".format(data.get("url")))

    # Structure of a browser-bot -> url-components response
    print("url-components:", data.get("url-components"))

    # True if the URL supplied is valid
    print("url-valid:", data.get("url-valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

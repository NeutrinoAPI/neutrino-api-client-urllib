"""Python client using native urllib HTTP client"""

__version__ = '4.6.13'

from socket import timeout
from ssl import SSLError
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen
import json
import os

from neutrino_api.api_error_code import APIErrorCode
from neutrino_api.api_response import APIResponse

# Servers
MULTICLOUD_ENDPOINT = "https://neutrinoapi.net/"
AWS_ENDPOINT = "https://aws.neutrinoapi.net/"
GCP_ENDPOINT = "https://gcp.neutrinoapi.net/"
MS_AZURE_ENDPOINT = "https://msa.neutrinoapi.net/"


class NeutrinoAPIClient:
    """
    Make a request to the Neutrino API
    """

    def __init__(self, user_id, api_key, base_url=MULTICLOUD_ENDPOINT) -> None:
        self.user_id = user_id
        self.api_key = api_key
        self.base_url = base_url

    def bad_word_filter(self, params) -> APIResponse:
        """
        Detect bad words, swear words and profanity in a given text

        The parameters this API accepts are:
        * censor-character - The character to use to censor out the bad words found
        * catalog - Which catalog of bad words to use
        * content - The content to scan

        Link
        ----
        https://www.neutrinoapi.com/api/bad-word-filter

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "bad-word-filter", params, None, 30)

    def bin_list_download(self, params, output_file_path):
        """
        Download our entire BIN database for direct use on your own systems

        The parameters this API accepts are:
        * include-iso3 - Include ISO 3-letter country codes and ISO 3-letter currency codes in the data
        * include-8digit - Include 8-digit and higher BIN codes
        * include-all - Include all BINs and all available fields in the CSV file (overrides any values set for 'include-iso3' or 'include-8digit')
        * output-encoding - Set this option to 'gzip' to have the output file compressed using gzip

        Link
        ----
        https://www.neutrinoapi.com/api/bin-list-download

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "bin-list-download", params, output_file_path, 30)

    def bin_lookup(self, params) -> APIResponse:
        """
        Perform a BIN (Bank Identification Number) or IIN (Issuer Identification Number) lookup

        The parameters this API accepts are:
        * bin-number - The BIN or IIN number
        * customer-ip - Pass in the customers IP address and we will return some extra information about them

        Link
        ----
        https://www.neutrinoapi.com/api/bin-lookup

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "bin-lookup", params, None, 10)

    def browser_bot(self, params) -> APIResponse:
        """
        Browser bot can extract content, interact with keyboard and mouse events, and execute JavaScript on a website

        The parameters this API accepts are:
        * delay - Delay in seconds to wait before capturing any page data
        * ignore-certificate-errors - Ignore any TLS/SSL certificate errors and load the page anyway
        * selector - Extract content from the page DOM using this selector
        * url - The URL to load
        * timeout - Timeout in seconds
        * exec - Execute JavaScript on the website
        * user-agent - Override the browsers default user-agent string with this one

        Link
        ----
        https://www.neutrinoapi.com/api/browser-bot

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "browser-bot", params, None, 300)

    def convert(self, params) -> APIResponse:
        """
        A currency and unit conversion tool

        The parameters this API accepts are:
        * from-value - The value to convert from (e.g. 10.95)
        * from-type - The type of the value to convert from (e.g. USD)
        * to-type - The type to convert to (e.g. EUR)

        Link
        ----
        https://www.neutrinoapi.com/api/convert

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "convert", params, None, 10)

    def domain_lookup(self, params) -> APIResponse:
        """
        Retrieve domain name details and detect potentially malicious or dangerous domains

        The parameters this API accepts are:
        * host - A domain name
        * live - For domains that we have never seen before then perform various live checks and realtime reconnaissance

        Link
        ----
        https://www.neutrinoapi.com/api/domain-lookup

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "domain-lookup", params, None, 120)

    def email_validate(self, params) -> APIResponse:
        """
        Parse, validate and clean an email address

        The parameters this API accepts are:
        * email - An email address
        * fix-typos - Automatically attempt to fix typos in the address

        Link
        ----
        https://www.neutrinoapi.com/api/email-validate

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "email-validate", params, None, 30)

    def email_verify(self, params) -> APIResponse:
        """
        SMTP based email address verification

        The parameters this API accepts are:
        * email - An email address
        * fix-typos - Automatically attempt to fix typos in the address

        Link
        ----
        https://www.neutrinoapi.com/api/email-verify

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "email-verify", params, None, 120)

    def geocode_address(self, params) -> APIResponse:
        """
        Geocode an address, partial address or just the name of a place

        The parameters this API accepts are:
        * address - The full address
        * house-number - The house/building number to locate
        * street - The street/road name to locate
        * city - The city/town name to locate
        * county - The county/region name to locate
        * state - The state name to locate
        * postal-code - The postal code to locate
        * country-code - Limit result to this country (the default is no country bias)
        * language-code - The language to display results in
        * fuzzy-search - If no matches are found for the given address

        Link
        ----
        https://www.neutrinoapi.com/api/geocode-address

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "geocode-address", params, None, 30)

    def geocode_reverse(self, params) -> APIResponse:
        """
        Convert a geographic coordinate (latitude and longitude) into a real world address

        The parameters this API accepts are:
        * latitude - The location latitude in decimal degrees format
        * longitude - The location longitude in decimal degrees format
        * language-code - The language to display results in
        * zoom - The zoom level to respond with: address - the most precise address available street - the street level city - the city level state - the state level country - the country level 

        Link
        ----
        https://www.neutrinoapi.com/api/geocode-reverse

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "geocode-reverse", params, None, 30)

    def hlr_lookup(self, params) -> APIResponse:
        """
        Connect to the global mobile cellular network and retrieve the status of a mobile device

        The parameters this API accepts are:
        * number - A phone number
        * country-code - ISO 2-letter country code

        Link
        ----
        https://www.neutrinoapi.com/api/hlr-lookup

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "hlr-lookup", params, None, 30)

    def host_reputation(self, params) -> APIResponse:
        """
        Check the reputation of an IP address, domain name or URL against a comprehensive list of blacklists and blocklists

        The parameters this API accepts are:
        * host - An IP address
        * list-rating - Only check lists with this rating or better
        * zones - Only check these DNSBL zones/hosts

        Link
        ----
        https://www.neutrinoapi.com/api/host-reputation

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "host-reputation", params, None, 120)

    def html_clean(self, params, output_file_path):
        """
        Clean and sanitize untrusted HTML

        The parameters this API accepts are:
        * output-type - The level of sanitization
        * content - The HTML content

        Link
        ----
        https://www.neutrinoapi.com/api/html-clean

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "html-clean", params, output_file_path, 30)

    def html_render(self, params, output_file_path):
        """
        Render HTML content to PDF, JPG or PNG

        The parameters this API accepts are:
        * margin - The document margin (in mm)
        * css - Inject custom CSS into the HTML
        * image-width - If rendering to an image format (PNG or JPG) use this image width (in pixels)
        * footer - The footer HTML to insert into each page
        * format - Which format to output
        * zoom - Set the zoom factor when rendering the page (2.0 for double size
        * title - The document title
        * content - The HTML content
        * page-width - Set the PDF page width explicitly (in mm)
        * timeout - Timeout in seconds
        * margin-right - The document right margin (in mm)
        * grayscale - Render the final document in grayscale
        * margin-left - The document left margin (in mm)
        * page-size - Set the document page size
        * delay - Number of seconds to wait before rendering the page (can be useful for pages with animations etc)
        * ignore-certificate-errors - Ignore any TLS/SSL certificate errors
        * page-height - Set the PDF page height explicitly (in mm)
        * image-height - If rendering to an image format (PNG or JPG) use this image height (in pixels)
        * header - The header HTML to insert into each page
        * margin-top - The document top margin (in mm)
        * margin-bottom - The document bottom margin (in mm)
        * bg-color - For image rendering set the background color in hexadecimal notation (e.g. #0000ff)
        * landscape - Set the document to landscape orientation

        Link
        ----
        https://www.neutrinoapi.com/api/html-render

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "html-render", params, output_file_path, 300)

    def image_resize(self, params, output_file_path):
        """
        Resize an image and output as either JPEG or PNG

        The parameters this API accepts are:
        * resize-mode - The resize mode to use
        * width - The width to resize to (in px)
        * format - The output image format
        * image-url - The URL or Base64 encoded Data URL for the source image
        * bg-color - The image background color in hexadecimal notation (e.g. #0000ff)
        * height - The height to resize to (in px)

        Link
        ----
        https://www.neutrinoapi.com/api/image-resize

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "image-resize", params, output_file_path, 20)

    def image_watermark(self, params, output_file_path):
        """
        Watermark one image with another image

        The parameters this API accepts are:
        * resize-mode - The resize mode to use
        * format - The output image format
        * width - If set resize the resulting image to this width (in px)
        * image-url - The URL or Base64 encoded Data URL for the source image
        * position - The position of the watermark image
        * watermark-url - The URL or Base64 encoded Data URL for the watermark image
        * opacity - The opacity of the watermark (0 to 100)
        * bg-color - The image background color in hexadecimal notation (e.g. #0000ff)
        * height - If set resize the resulting image to this height (in px)

        Link
        ----
        https://www.neutrinoapi.com/api/image-watermark

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "image-watermark", params, output_file_path, 20)

    def ip_blocklist(self, params) -> APIResponse:
        """
        The IP Blocklist API will detect potentially malicious or dangerous IP addresses

        The parameters this API accepts are:
        * ip - An IPv4 or IPv6 address
        * vpn-lookup - Include public VPN provider IP addresses

        Link
        ----
        https://www.neutrinoapi.com/api/ip-blocklist

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "ip-blocklist", params, None, 10)

    def ip_blocklist_download(self, params, output_file_path):
        """
        This API is a direct feed to our IP blocklist data

        The parameters this API accepts are:
        * format - The data format
        * cidr - Output IPs using CIDR notation
        * ip6 - Output the IPv6 version of the blocklist
        * category - The category of IP addresses to include in the download file
        * output-encoding - Set this option to 'gzip' to have the output file compressed using gzip
        * checksum - Do not download the file but just return the current files MurmurHash3 checksum

        Link
        ----
        https://www.neutrinoapi.com/api/ip-blocklist-download

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "ip-blocklist-download", params, output_file_path, 30)

    def ip_info(self, params) -> APIResponse:
        """
        Get location information about an IP address and do reverse DNS (PTR) lookups

        The parameters this API accepts are:
        * ip - IPv4 or IPv6 address
        * reverse-lookup - Do a reverse DNS (PTR) lookup

        Link
        ----
        https://www.neutrinoapi.com/api/ip-info

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "ip-info", params, None, 10)

    def ip_probe(self, params) -> APIResponse:
        """
        Execute a realtime network probe against an IPv4 or IPv6 address

        The parameters this API accepts are:
        * ip - IPv4 or IPv6 address

        Link
        ----
        https://www.neutrinoapi.com/api/ip-probe

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "ip-probe", params, None, 120)

    def phone_playback(self, params) -> APIResponse:
        """
        Make an automated call to any valid phone number and playback an audio message

        The parameters this API accepts are:
        * number - The phone number to call
        * limit - Limit the total number of calls allowed to the supplied phone number
        * audio-url - A URL to a valid audio file
        * limit-ttl - Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)

        Link
        ----
        https://www.neutrinoapi.com/api/phone-playback

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "phone-playback", params, None, 30)

    def phone_validate(self, params) -> APIResponse:
        """
        Parse, validate and get location information about a phone number

        The parameters this API accepts are:
        * number - A phone number
        * country-code - ISO 2-letter country code
        * ip - Pass in a users IP address and we will assume numbers are based in the country of the IP address

        Link
        ----
        https://www.neutrinoapi.com/api/phone-validate

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "phone-validate", params, None, 10)

    def phone_verify(self, params) -> APIResponse:
        """
        Make an automated call to any valid phone number and playback a unique security code

        The parameters this API accepts are:
        * number - The phone number to send the verification code to
        * country-code - ISO 2-letter country code
        * security-code - Pass in your own security code
        * language-code - The language to playback the verification code in
        * code-length - The number of digits to use in the security code (between 4 and 12)
        * limit - Limit the total number of calls allowed to the supplied phone number
        * playback-delay - The delay in milliseconds between the playback of each security code
        * limit-ttl - Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)

        Link
        ----
        https://www.neutrinoapi.com/api/phone-verify

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "phone-verify", params, None, 30)

    def qr_code(self, params, output_file_path):
        """
        Generate a QR code as a PNG image

        The parameters this API accepts are:
        * width - The width of the QR code (in px)
        * fg-color - The QR code foreground color
        * bg-color - The QR code background color
        * content - The content to encode into the QR code (e.g. a URL or a phone number)
        * height - The height of the QR code (in px)

        Link
        ----
        https://www.neutrinoapi.com/api/qr-code

        Parameters
        ----------
        params: dict
            String key-value pairs
        output_file_path: str
            Path to store the response data

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "qr-code", params, output_file_path, 20)

    def sms_verify(self, params) -> APIResponse:
        """
        Send a unique security code to any mobile device via SMS

        The parameters this API accepts are:
        * number - The phone number to send a verification code to
        * country-code - ISO 2-letter country code
        * security-code - Pass in your own security code
        * language-code - The language to send the verification code in
        * code-length - The number of digits to use in the security code (must be between 4 and 12)
        * limit - Limit the total number of SMS allowed to the supplied phone number
        * brand-name - Set a custom brand or product name in the verification message
        * limit-ttl - Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)

        Link
        ----
        https://www.neutrinoapi.com/api/sms-verify

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("POST", "sms-verify", params, None, 30)

    def ua_lookup(self, params) -> APIResponse:
        """
        Parse, validate and get detailed user-agent information from a user agent string or from client hints

        The parameters this API accepts are:
        * ua - The user-agent string to lookup
        * ua-version - For client hints this corresponds to the 'UA-Full-Version' header or 'uaFullVersion' from NavigatorUAData
        * ua-platform - For client hints this corresponds to the 'UA-Platform' header or 'platform' from NavigatorUAData
        * ua-platform-version - For client hints this corresponds to the 'UA-Platform-Version' header or 'platformVersion' from NavigatorUAData
        * ua-mobile - For client hints this corresponds to the 'UA-Mobile' header or 'mobile' from NavigatorUAData
        * device-model - For client hints this corresponds to the 'UA-Model' header or 'model' from NavigatorUAData
        * device-brand - This parameter is only used in combination with 'device-model' when doing direct device lookups without any user-agent data

        Link
        ----
        https://www.neutrinoapi.com/api/ua-lookup

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "ua-lookup", params, None, 10)

    def url_info(self, params) -> APIResponse:
        """
        Parse, analyze and retrieve content from the supplied URL

        The parameters this API accepts are:
        * url - The URL to probe
        * fetch-content - If this URL responds with html
        * ignore-certificate-errors - Ignore any TLS/SSL certificate errors and load the URL anyway
        * timeout - Timeout in seconds
        * retry - If the request fails for any reason try again this many times

        Link
        ----
        https://www.neutrinoapi.com/api/url-info

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "url-info", params, None, 30)

    def verify_security_code(self, params) -> APIResponse:
        """
        Check if a security code sent via SMS Verify or Phone Verify is valid

        The parameters this API accepts are:
        * security-code - The security code to verify
        * limit-by - If set then enable additional brute-force protection by limiting the number of attempts by the supplied value

        Link
        ----
        https://www.neutrinoapi.com/api/verify-security-code

        Parameters
        ----------
        params: dict
            String key-value pairs

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        return self.exec_request("GET", "verify-security-code", params, None, 30)

    def exec_request(
            self,
            http_method: str,
            endpoint: str,
            params: dict,
            output_file_path=None,
            timeout_in_seconds: int = 10,
    ) -> APIResponse:
        """
        Make a request to the Neutrino API

        Parameters
        ----------
        http_method : str
            "GET" or "POST"
        endpoint : string
            The endpoint to call
        params : dict
            The API request parameters
        output_file_path : str | None
            The file path to write the response data to
        timeout_in_seconds : integer
            How long to wait before throwing a timeout error, in seconds

        Returns
        -------
        APIResponse
            Neutrino API response object
        """
        url = f'{self.base_url}{endpoint}'
        headers = {
            'User-ID': self.user_id,
            'API-Key': self.api_key
        }
        try:
            if http_method == "GET":
                params = urlencode(params, encoding="utf-8")
                req = Request("%s?%s" % (url, params), headers=headers)
            else:
                headers['Content-Type'] = 'application/json; charset=utf-8'
                params = json.dumps(params).encode('utf-8')
                req = Request(url, params, headers)

            with urlopen(req, timeout=timeout_in_seconds) as response:
                content_type = response.headers.get('content-type')
                status_code = response.status
                if status_code == 200:
                    # 200 OK
                    if "application/json" in content_type:
                        return APIResponse.of_data(status_code, content_type, json.load(response))
                    elif output_file_path is not None:
                        with open(output_file_path, 'wb') as file:
                            while True:
                                buffer = response.read(2048)
                                if not buffer:
                                    break
                                file.write(buffer)
                            return APIResponse.of_output_file_path(status_code, content_type,
                                                                   os.path.abspath(output_file_path))
                    else:
                        return APIResponse.of_http_status(status_code, content_type, APIErrorCode.API_GATEWAY_ERROR,
                                                          response.read().decode('utf-8'))
        except HTTPError as err:
            # Non-200 error received
            content_type = err.headers.get('content-type')
            status_code = err.status
            if "application/json" in content_type:
                err_json = json.load(err)
                api_error = err_json.get("api-error")
                api_error_msg = err_json.get("api-error-msg")
                if api_error and api_error_msg:
                    return APIResponse.of_http_status(
                        status_code,
                        content_type,
                        api_error,
                        api_error_msg
                    )
                else:
                    return APIResponse.of_error_code(
                        status_code, content_type, APIErrorCode.INVALID_JSON_RESPONSE
                    )
            else:
                return APIResponse.of_http_status(
                    status_code, content_type, APIErrorCode.NETWORK_IO_ERROR, err.read().decode("utf-8")
                )
        except timeout as err:
            return APIResponse.of_cause(APIErrorCode.READ_TIMEOUT, err)
        except URLError as err:
            if isinstance(err.args[0], SSLError):
                return APIResponse.of_cause(APIErrorCode.TLS_PROTOCOL_ERROR, err)
            elif isinstance(err.args[0], OSError) and err.args[0].errno == 101:
                return APIResponse.of_cause(APIErrorCode.CONNECT_TIMEOUT, err)
            elif isinstance(err.args[0], timeout):
                return APIResponse.of_cause(APIErrorCode.CONNECT_TIMEOUT, err)
            else:
                return APIResponse.of_cause(APIErrorCode.BAD_URL, err)
        except OSError as err:
            return APIResponse.of_cause(APIErrorCode.NETWORK_IO_ERROR, err)

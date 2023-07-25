"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The user-agent string to lookup. For client hints use the 'UA' header or the JSON data directly
    # from 'navigator.userAgentData.brands' or 'navigator.userAgentData.getHighEntropyValues()'
    "ua": "Mozilla/5.0 (Linux; Android 11; SM-G9980U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",

    # For client hints this corresponds to the 'UA-Full-Version' header or 'uaFullVersion' from
    # NavigatorUAData
    "ua_version": "",

    # For client hints this corresponds to the 'UA-Platform' header or 'platform' from NavigatorUAData
    "ua_platform": "",

    # For client hints this corresponds to the 'UA-Platform-Version' header or 'platformVersion' from
    # NavigatorUAData
    "ua_platform_version": "",

    # For client hints this corresponds to the 'UA-Mobile' header or 'mobile' from NavigatorUAData
    "ua_mobile": "",

    # For client hints this corresponds to the 'UA-Model' header or 'model' from NavigatorUAData. You
    # can also use this parameter to lookup a device directly by its model name, model code or hardware
    # code, on android you can get the model name from:
    # https://developer.android.com/reference/android/os/Build.html#MODEL
    "device_model": "",

    # This parameter is only used in combination with 'device-model' when doing direct device lookups
    # without any user-agent data. Set this to the brand or manufacturer name, this is required for
    # accurate device detection with ambiguous model names. On android you can get the device brand
    # from: https://developer.android.com/reference/android/os/Build#MANUFACTURER
    "device_brand": ""
}
response = client.ua_lookup(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # If the client is a web browser which underlying browser engine does it use
    print("browser-engine:", "'{0}'".format(data.get("browser-engine")))

    # If the client is a web browser which year was this browser version released
    print("browser-release:", "'{0}'".format(data.get("browser-release")))

    # The device brand / manufacturer
    print("device-brand:", "'{0}'".format(data.get("device-brand")))

    # The device display height in CSS 'px'
    print("device-height-px:", data.get("device-height-px"))

    # The device model
    print("device-model:", "'{0}'".format(data.get("device-model")))

    # The device model code
    print("device-model-code:", "'{0}'".format(data.get("device-model-code")))

    # The device display pixel ratio (the ratio of the resolution in physical pixels to the resolution
    # in CSS pixels)
    print("device-pixel-ratio:", data.get("device-pixel-ratio"))

    # The device display PPI (pixels per inch)
    print("device-ppi:", data.get("device-ppi"))

    # The average device price on release in USD
    print("device-price:", data.get("device-price"))

    # The year when this device model was released
    print("device-release:", "'{0}'".format(data.get("device-release")))

    # The device display resolution in physical pixels (e.g. 720x1280)
    print("device-resolution:", "'{0}'".format(data.get("device-resolution")))

    # The device display width in CSS 'px'
    print("device-width-px:", data.get("device-width-px"))

    # Is this a mobile device (e.g. a phone or tablet)
    print("is-mobile:", data.get("is-mobile"))

    # Is this a WebView / embedded software client
    print("is-webview:", data.get("is-webview"))

    # The client software name
    print("name:", "'{0}'".format(data.get("name")))

    # The full operating system name
    print("os:", "'{0}'".format(data.get("os")))

    # The operating system family. The major OS families are: Android, Windows, macOS, iOS, Linux
    print("os-family:", "'{0}'".format(data.get("os-family")))

    # The operating system full version
    print("os-version:", "'{0}'".format(data.get("os-version")))

    # The operating system major version
    print("os-version-major:", "'{0}'".format(data.get("os-version-major")))

    # The user agent type, possible values are:
    # • desktop
    # • phone
    # • tablet
    # • wearable
    # • tv
    # • console
    # • email
    # • library
    # • robot
    # • unknown
    print("type:", "'{0}'".format(data.get("type")))

    # The user agent string
    print("ua:", "'{0}'".format(data.get("ua")))

    # The client software full version
    print("version:", "'{0}'".format(data.get("version")))

    # The client software major version
    print("version-major:", "'{0}'".format(data.get("version-major")))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

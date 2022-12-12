"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The phone number to call. Must be in valid international format
    "number": "+12106100045",

    # Limit the total number of calls allowed to the supplied phone number, if the limit is reached
    # within the TTL then error code 14 will be returned
    "limit": "3",

    # A URL to a valid audio file. Accepted audio formats are:
    # • MP3
    # • WAV
    # • OGG You can use the following MP3 URL for testing:
    #   https://www.neutrinoapi.com/test-files/test1.mp3
    "audio_url": "https://www.neutrinoapi.com/test-files/test1.mp3",

    # Set the TTL in number of days that the 'limit' option will remember a phone number (the default is
    # 1 day and the maximum is 365 days)
    "limit_ttl": "1"
}
response = client.phone_playback(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # True if the call is being made now
    print("calling:", data.get("calling"))

    # True if this a valid phone number
    print("number-valid:", data.get("number-valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

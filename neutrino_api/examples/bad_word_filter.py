"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # The character to use to censor out the bad words found
    "censor_character": "",

    # Which catalog of bad words to use, we currently maintain two bad word catalogs:
    # • strict - the largest database of bad words which includes profanity, obscenity, sexual, rude,
    #   cuss, dirty, swear and objectionable words and phrases. This catalog is suitable for
    #   environments of all ages including educational or children's content
    # • obscene - like the strict catalog but does not include any mild profanities, idiomatic phrases
    #   or words which are considered formal terminology. This catalog is suitable for adult
    #   environments where certain types of bad words are considered OK
    "catalog": "strict",

    # The content to scan. This can be either a URL to load from, a file upload (multipart/form-data) or
    # an HTML content string
    "content": "https://en.wikipedia.org/wiki/Profanity"
}
response = client.bad_word_filter(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # An array of the bad words found
    print("bad-words-list:", data.get("bad-words-list"))

    # Total number of bad words detected
    print("bad-words-total:", data.get("bad-words-total"))

    # The censored content (only set if censor-character has been set)
    print("censored-content:", "'{0}'".format(data.get("censored-content")))

    # Does the text contain bad words
    print("is-bad:", data.get("is-bad"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # An email address
    "email": "tech@neutrinoapi.com",

    # Automatically attempt to fix typos in the address
    "fix_typos": "false"
}
response = client.email_validate(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The email domain
    print("domain:", "'{0}'".format(data.get("domain")))

    # True if this address has a domain error (e.g. no valid mail server records)
    print("domain-error:", data.get("domain-error"))

    # The email address. If you have used the fix-typos option then this will be the fixed address
    print("email:", "'{0}'".format(data.get("email")))

    # True if this address is a disposable, temporary or darknet related email address
    print("is-disposable:", data.get("is-disposable"))

    # True if this address is a free-mail address
    print("is-freemail:", data.get("is-freemail"))

    # True if this address belongs to a person. False if this is a role based address, e.g. admin@,
    # help@, office@, etc.
    print("is-personal:", data.get("is-personal"))

    # The email service provider domain
    print("provider:", "'{0}'".format(data.get("provider")))

    # True if this address has a syntax error
    print("syntax-error:", data.get("syntax-error"))

    # True if typos have been fixed
    print("typos-fixed:", data.get("typos-fixed"))

    # Is this a valid email
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

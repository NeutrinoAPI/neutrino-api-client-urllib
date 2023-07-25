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
response = client.email_verify(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The email domain
    print("domain:", "'{0}'".format(data.get("domain")))

    # True if this address has a domain error (e.g. no valid mail server records)
    print("domain-error:", data.get("domain-error"))

    # The email address. If you have used the fix-typos option then this will be the fixed address
    print("email:", "'{0}'".format(data.get("email")))

    # True if this email domain has a catch-all policy (it will accept mail for any username)
    print("is-catch-all:", data.get("is-catch-all"))

    # True if the mail server responded with a temporary failure (either a 4xx response code or
    # unresponsive server). You can retry this address later, we recommend waiting at least 15 minutes
    # before retrying
    print("is-deferred:", data.get("is-deferred"))

    # True if this address is a disposable, temporary or darknet related email address
    print("is-disposable:", data.get("is-disposable"))

    # True if this address is a free-mail address
    print("is-freemail:", data.get("is-freemail"))

    # True if this address is for a person. False if this is a role based address, e.g. admin@, help@,
    # office@, etc.
    print("is-personal:", data.get("is-personal"))

    # The email service provider domain
    print("provider:", "'{0}'".format(data.get("provider")))

    # The raw SMTP response message received during verification
    print("smtp-response:", "'{0}'".format(data.get("smtp-response")))

    # The SMTP verification status for the address:
    # • ok - SMTP verification was successful, this is a real address that can receive mail
    # • invalid - this is not a valid email address (has either a domain or syntax error)
    # • absent - this address is not registered with the email service provider
    # • unresponsive - the mail server(s) for this address timed-out or refused to open an SMTP
    #   connection
    # • unknown - sorry, we could not reliably determine the real status of this address (this address
    #   may or may not exist)
    print("smtp-status:", "'{0}'".format(data.get("smtp-status")))

    # True if this address has a syntax error
    print("syntax-error:", data.get("syntax-error"))

    # True if typos have been fixed
    print("typos-fixed:", data.get("typos-fixed"))

    # Is this a valid email address (syntax and domain is valid)
    print("valid:", data.get("valid"))

    # True if this address has passed SMTP verification. Check the smtp-status and smtp-response fields
    # for specific verification details
    print("verified:", data.get("verified"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

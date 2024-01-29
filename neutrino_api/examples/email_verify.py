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

    # The domain name of this email address
    print("domain:", "'{0}'".format(data.get("domain")))

    # True if this address has any domain name or DNS related errors. Check the 'domain-status' field
    # for the detailed error reason
    print("domain-error:", data.get("domain-error"))

    # The email domain status, possible values are:
    # • ok - the domain is in working order and can receive email
    # • invalid - the domain is not a conformant hostname. May contain invalid syntax or characters
    # • no-service - the domain owner has indicated there is no mail service on the domain (also known
    #   as the 'Null MX')
    # • no-mail - the domain has no valid MX records so cannot receive email
    # • mx-invalid - MX records contain invalid or non-conformant hostname values
    # • mx-bogon - MX records point to bogon IP addresses
    # • resolv-error - MX records do not resolve to any valid IP addresses
    print("domain-status:", "'{0}'".format(data.get("domain-status")))

    # The complete email address. If you enabled the 'fix-typos' option then this will be the corrected
    # address
    print("email:", "'{0}'".format(data.get("email")))

    # True if this email domain has a catch-all policy. A catch-all domain will accept mail for any
    # username so therefor the 'smtp-status' will always be 'ok'
    print("is-catch-all:", data.get("is-catch-all"))

    # True if the mail server responded with a temporary failure (either a 4xx response code or
    # unresponsive server). You can retry this address later, we recommend waiting at least 15 minutes
    # before retrying
    print("is-deferred:", data.get("is-deferred"))

    # True if this address is a disposable, temporary or darknet related email address
    print("is-disposable:", data.get("is-disposable"))

    # True if this address is from a free email provider
    print("is-freemail:", data.get("is-freemail"))

    # True if this address likely belongs to a person. False if this is a role based address, e.g.
    # admin@, help@, office@, etc.
    print("is-personal:", data.get("is-personal"))

    # The first resolved IP address of the primary MX server, may be empty if there are domain errors
    # present
    print("mx-ip:", "'{0}'".format(data.get("mx-ip")))

    # The domain name of the email hosting provider
    print("provider:", "'{0}'".format(data.get("provider")))

    # The raw SMTP response message received during verification
    print("smtp-response:", "'{0}'".format(data.get("smtp-response")))

    # The SMTP username verification status for this address:
    # • ok - verification was successful, this is a real username that can receive mail
    # • absent - this username or domain is not registered with the email service provider
    # • invalid - not a valid email address, check the 'domain-status' field for specific details
    # • unresponsive - the mail servers for this domain have repeatedly timed-out or refused multiple
    #   connection attempts
    # • unknown - sorry, we could not reliably determine the status of this username
    print("smtp-status:", "'{0}'".format(data.get("smtp-status")))

    # True if this address has any syntax errors or is not in RFC compliant formatting
    print("syntax-error:", data.get("syntax-error"))

    # True if any typos have been fixed. The 'fix-typos' option must be enabled for this to work
    print("typos-fixed:", data.get("typos-fixed"))

    # Is this a valid email address. To be valid an email must have: correct syntax, a registered and
    # active domain name, correct DNS records and operational MX servers
    print("valid:", data.get("valid"))

    # True if this email address has passed SMTP username verification. Check the 'smtp-status' and
    # 'domain-status' fields for specific verification details
    print("verified:", data.get("verified"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

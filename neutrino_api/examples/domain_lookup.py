"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # A domain name, hostname, FQDN, URL, HTML link or email address to lookup. For internationalized
    # domain names (IDNs) this field will accept either punycode or the raw unicode domain name, the API
    # will always automatically return IDNs encoded into punycode
    "host": "neutrinoapi.com",

    # For domains that we have never seen before then perform various live checks and realtime
    # reconnaissance. NOTE: this option may add additional non-deterministic delay to the request, if
    # you require consistently fast API response times or just want to check our domain blocklists then
    # you can disable this option
    "live": "true"
}
response = client.domain_lookup(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # The number of days since the domain was registered. A domain age of under 90 days is generally
    # considered to be potentially risky. A value of 0 indicates no registration date was found for this
    # domain
    print("age:", data.get("age"))

    # An array of strings indicating which blocklist categories this domain is listed on. Current
    # possible values are:
    # • phishing - Domain has recently been hosting phishing links or involved in the sending of
    #   phishing messages
    # • malware - Domain has recently been hosting malware or involved in the distribution of malware
    # • spam - Domain has recently been sending spam either directly or indirectly
    # • anonymizer - Domain is involved in anonymizer activity such as disposable email, hosting
    #   proxies or tor services
    # • nefarious - Domain is involved in nefarious or malicious activity such as hacking, fraud or
    #   other abusive behavior
    print("blocklists:", data.get("blocklists"))

    # The primary domain of the DNS provider for this domain
    print("dns-provider:", "'{0}'".format(data.get("dns-provider")))

    # The primary domain name excluding any subdomains. This is also commonly referred to as the
    # second-level domain (SLD), the registrable domain, the root domain or the eTLD+1
    print("domain:", "'{0}'".format(data.get("domain")))

    # The effective top-level domain (eTLD). Usually the same as the TLD but will differ when a domain
    # is on the public suffix list (PSL) and acts as a TLD for registrable domains (for example
    # github.io is an eTLD)
    print("etld:", "'{0}'".format(data.get("etld")))

    # The ISO date this domain is due to expire. An empty value indicates we could not reliably
    # determine the date
    print("expiry-date:", "'{0}'".format(data.get("expiry-date")))

    # The fully qualified domain name (FQDN)
    print("fqdn:", "'{0}'".format(data.get("fqdn")))

    # This domain is hosting adult content such as porn, webcams, escorts, etc
    print("is-adult:", data.get("is-adult"))

    # Is this domain under a government or military TLD
    print("is-gov:", data.get("is-gov"))

    # Consider this domain malicious as it is currently listed on at least 1 blocklist
    print("is-malicious:", data.get("is-malicious"))

    # Is this domain under an OpenNIC TLD
    print("is-opennic:", data.get("is-opennic"))

    # True if this domain is unseen and is currently being processed in the background. This field only
    # matters when the 'live' lookup setting has been explicitly disabled and indicates that not all
    # domain data my be present yet
    print("is-pending:", data.get("is-pending"))

    # Is the FQDN a subdomain of the primary domain
    print("is-subdomain:", data.get("is-subdomain"))

    # The primary domain of the email provider for this domain. An empty value indicates the domain has
    # no valid MX records
    print("mail-provider:", "'{0}'".format(data.get("mail-provider")))

    # The status of the domains mail configuration, possible values are:
    # • ok - the domain is in working order and can receive email
    # • invalid - the domain is not a conformant hostname. May contain invalid syntax or characters
    # • no-service - the domain owner has indicated there is no mail service on the domain (also known
    #   as the 'Null MX')
    # • no-mail - the domain has no valid MX records so cannot receive email
    # • mx-invalid - MX records contain invalid or non-conformant hostname values
    # • mx-bogon - MX records point to bogon IP addresses
    # • resolv-error - MX records do not resolve to any valid IP addresses
    # • unknown - mail status is currently unknown (the domain may still be pending processing)
    print("mail-status:", "'{0}'".format(data.get("mail-status")))

    # The domains estimated global traffic rank with the highest rank being 1. A value of 0 indicates
    # the domain is currently ranked outside of the top 1M of domains
    print("rank:", data.get("rank"))

    # The ISO date this domain was registered or first seen on the internet. An empty value indicates we
    # could not reliably determine the date
    print("registered-date:", "'{0}'".format(data.get("registered-date")))

    # True if the registrar is an officially IANA accredited registrar
    print("registrar-accredited:", data.get("registrar-accredited"))

    # The ISO 2-letter country code where the registrar is located
    print("registrar-country-code:", "'{0}'".format(data.get("registrar-country-code")))

    # The IANA registrar ID (0 if no official IANA registrar ID exists)
    print("registrar-id:", data.get("registrar-id"))

    # The name of the domain registrar owning this domain
    print("registrar-name:", "'{0}'".format(data.get("registrar-name")))

    # The main website URL for the registrar
    print("registrar-website:", "'{0}'".format(data.get("registrar-website")))

    # An array of objects containing details on which specific blocklist sensors have detected this
    # domain
    print("sensors:", end=None)
    for item in data.get("sensors"):

        # The primary blocklist category this sensor belongs to
        print("    blocklist:", "'{0}'".format(item.get("blocklist")))

        # Contains details about the sensor source and what type of malicious activity was detected
        print("    description:", "'{0}'".format(item.get("description")))

        # The sensor ID. This is a permanent and unique ID for each sensor
        print("    id:", item.get("id"))
        print("")

    # The top-level domain (TLD)
    print("tld:", "'{0}'".format(data.get("tld")))

    # For a country code top-level domain (ccTLD) this will contain the associated ISO 2-letter country
    # code. For non-ccTLD domains this field will always be empty
    print("tld-cc:", "'{0}'".format(data.get("tld-cc")))

    # True if a valid domain was found. For a domain to be considered valid it must be registered and
    # have valid DNS NS records
    print("valid:", data.get("valid"))

    # The primary domain of the website hosting provider for this domain. An empty value indicates the
    # domain has no active website provider
    print("website-provider:", "'{0}'".format(data.get("website-provider")))

    # The status of the domains website configuration, possible values are:
    # • ok - the domain has a valid and working website
    # • no-http - the domain has website records but the HTTP servers are unresponsive or dead
    # • no-ip - the domain has no valid A or AAAA website records
    # • bogon-ip - the domains website records point to bogon or invalid IP addresses
    # • parked - the domain has a working website but indicates it is currently parked or for sale
    # • unknown - website status is currently unknown (the domain may still be pending processing)
    print("website-status:", "'{0}'".format(data.get("website-status")))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

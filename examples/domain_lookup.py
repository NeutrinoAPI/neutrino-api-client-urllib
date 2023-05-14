"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # A domain name, hostname, FQDN, URL, HTML link or email address to lookup
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
    # categories are: phishing, malware, spam, anonymizer, nefarious
    print("blocklists:", data.get("blocklists"))

    # The primary domain of the DNS provider for this domain
    print("dns-provider:", "'{0}'".format(data.get("dns-provider")))

    # The primary domain name excluding any subdomains. This is also referred to as the second-level
    # domain (SLD)
    print("domain:", "'{0}'".format(data.get("domain")))

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

    # The domains estimated global traffic rank with the highest rank being 1. A value of 0 indicates
    # the domain is currently ranked outside of the top 1M of domains
    print("rank:", data.get("rank"))

    # The ISO date this domain was registered or first seen on the internet. An empty value indicates we
    # could not reliably determine the date
    print("registered-date:", "'{0}'".format(data.get("registered-date")))

    # The IANA registrar ID (0 if no registrar ID was found)
    print("registrar-id:", data.get("registrar-id"))

    # The name of the domain registrar owning this domain
    print("registrar-name:", "'{0}'".format(data.get("registrar-name")))

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
    # code
    print("tld-cc:", "'{0}'".format(data.get("tld-cc")))

    # True if a valid domain was found. For a domain to be considered valid it must be registered and
    # have valid DNS NS records
    print("valid:", data.get("valid"))
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

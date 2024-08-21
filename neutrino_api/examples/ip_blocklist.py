"""NeutrinoAPIClient Example"""

import sys
from neutrino_api.neutrino_api_client import *


client = NeutrinoAPIClient("<your-user-id>", "<your-api-key>")
params = {

    # An IPv4 or IPv6 address. Accepts standard IP notation (with or without port number), CIDR notation
    # and IPv6 compressed notation. If multiple IPs are passed using comma-separated values the first
    # non-bogon address on the list will be checked
    "ip": "104.244.72.115",

    # Include public VPN provider IP addresses. NOTE: For more advanced VPN detection including the
    # ability to identify private and stealth VPNs use the IP Probe API
    "vpn_lookup": "false"
}
response = client.ip_blocklist(params)
if response.is_ok():
    data = response.data
    print("API Response OK:")

    # An array of strings indicating which blocklist categories this IP is listed on. Current possible
    # values are:
    # • tor - IP is a Tor node or running a Tor related service
    # • proxy - IP has been detected as an anonymous web proxy or HTTP proxy
    # • vpn - IP belongs to a public VPN provider
    # • bot - IP is hosting a malicious bot or is part of a botnet. This is a broad category which
    #   includes brute-force crackers
    # • spam-bot - IP address is hosting a spam bot, comment spamming or any other spamming type
    #   software
    # • exploit-bot - IP is hosting an exploit finding bot or is running exploit scanning software
    # • hijacked - IP is part of a hijacked netblock or a netblock controlled by a criminal
    #   organization
    # • malware - IP is currently involved in distributing or is running malware
    # • spyware - IP is currently involved in distributing or is running spyware
    # • spider - IP is running a hostile web spider / web crawler
    # • dshield - IP has been flagged as a significant attack source by DShield (dshield.org)
    print("blocklists:", data.get("blocklists"))

    # The CIDR address for this listing (only set if the IP is listed)
    print("cidr:", "'{0}'".format(data.get("cidr")))

    # The IP address
    print("ip:", "'{0}'".format(data.get("ip")))

    # IP is hosting a malicious bot or is part of a botnet. This is a broad category which includes
    # brute-force crackers
    print("is-bot:", data.get("is-bot"))

    # IP has been flagged as a significant attack source by DShield (dshield.org)
    print("is-dshield:", data.get("is-dshield"))

    # IP is hosting an exploit finding bot or is running exploit scanning software
    print("is-exploit-bot:", data.get("is-exploit-bot"))

    # IP is part of a hijacked netblock or a netblock controlled by a criminal organization
    print("is-hijacked:", data.get("is-hijacked"))

    # Is this IP on a blocklist
    print("is-listed:", data.get("is-listed"))

    # IP is involved in distributing or is running malware
    print("is-malware:", data.get("is-malware"))

    # IP has been detected as an anonymous web proxy or anonymous HTTP proxy
    print("is-proxy:", data.get("is-proxy"))

    # IP address is hosting a spam bot, comment spamming or any other spamming type software
    print("is-spam-bot:", data.get("is-spam-bot"))

    # IP is running a hostile web spider / web crawler
    print("is-spider:", data.get("is-spider"))

    # IP is involved in distributing or is running spyware
    print("is-spyware:", data.get("is-spyware"))

    # IP is a Tor node or running a Tor related service
    print("is-tor:", data.get("is-tor"))

    # IP belongs to a public VPN provider (only set if the 'vpn-lookup' option is enabled)
    print("is-vpn:", data.get("is-vpn"))

    # The unix time when this IP was last seen on any blocklist. IPs are automatically removed after 7
    # days therefor this value will never be older than 7 days
    print("last-seen:", data.get("last-seen"))

    # The number of blocklists the IP is listed on
    print("list-count:", data.get("list-count"))

    # An array of objects containing details on which specific sensors detected the IP
    print("sensors:", end=None)
    for item in data.get("sensors"):

        # The primary blocklist category this sensor belongs to
        print("    blocklist:", "'{0}'".format(item.get("blocklist")))

        # Contains details about the sensor source and what type of malicious activity was detected
        print("    description:", "'{0}'".format(item.get("description")))

        # The sensor ID. This is a permanent and unique ID for each sensor
        print("    id:", item.get("id"))
        print("")
else:
    print("API Error: {0}, Error Code: {1}, HTTP Status Code: {2}".format(response.error_message, response.error_code, response.status_code), file=sys.stderr)
    if response.error_cause:
        print("Error Caused By: {0}".format(response.error_cause), file=sys.stderr)

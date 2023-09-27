from scapy.all import ARP, Ether, srp


def scan_network():
    # Create an ARP request packet
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="172.0.0.0/8")

    # Send the ARP request and receive the response
    result = srp(arp_request, timeout=3, verbose=0)[0]

    # Extract the active hosts from the response
    active_hosts = []
    for sent, received in result:
        active_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})

    # Return the list of active hosts
    return active_hosts


if __name__ == '__main__':
    active_hosts = scan_network()
    for host in active_hosts:
        print(f"IP: {host['ip']}, MAC: {host['mac']}")

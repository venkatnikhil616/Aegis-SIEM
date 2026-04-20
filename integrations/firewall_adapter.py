from core.firewall import Firewall

class FirewallAdapter:
    def __init__(self):
        self.firewall = Firewall()

    def block(self, ip):
        return self.firewall.block_ip(ip)

    def unblock(self, ip):
        return self.firewall.unblock_ip(ip)

    def bulk_block(self, ips):
        results = {}
        for ip in ips:
            results[ip] = self.block(ip)
        return results

    def bulk_unblock(self, ips):
        results = {}
        for ip in ips:
            results[ip] = self.unblock(ip)
        return results

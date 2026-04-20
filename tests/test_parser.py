import unittest
from scapy.all import IP, TCP, UDP, ICMP

from core.parser import PacketParser

class TestPacketParser(unittest.TestCase):

    def setUp(self):
        self.parser = PacketParser()

    def test_parse_tcp_packet(self):
        packet = IP(src="192.168.1.1", dst="192.168.1.2") / TCP(sport=1234, dport=80, flags="S")
        result = self.parser.parse(packet)

        self.assertIsNotNone(result)
        self.assertEqual(result["protocol"], "TCP")
        self.assertEqual(result["src_ip"], "192.168.1.1")
        self.assertEqual(result["dst_port"], 80)

    def test_parse_udp_packet(self):
        packet = IP(src="10.0.0.1", dst="10.0.0.2") / UDP(sport=5000, dport=53)
        result = self.parser.parse(packet)

        self.assertIsNotNone(result)
        self.assertEqual(result["protocol"], "UDP")
        self.assertEqual(result["dst_port"], 53)

    def test_parse_icmp_packet(self):
        packet = IP(src="8.8.8.8", dst="1.1.1.1") / ICMP()
        result = self.parser.parse(packet)

        self.assertIsNotNone(result)
        self.assertEqual(result["protocol"], "ICMP")

    def test_invalid_packet(self):
        class DummyPacket:
            pass

        packet = DummyPacket()
        result = self.parser.parse(packet)

        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()

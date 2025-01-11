from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("Raw"):
        print(f"Captured Raw Data: {packet['Raw'].load}")

def start_sniffer(port):
    print(f"Starting sniffer on TCP port {port}...")
    sniff(filter=f"tcp port {port}", prn=packet_callback)

if __name__ == '__main__':
    port = 65432  # Replace with your application's port
    start_sniffer(port)

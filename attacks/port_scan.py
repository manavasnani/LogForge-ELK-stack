import random
from datetime import datetime, timedelta

def generate():
    def generate_random_ip():
        return ".".join(str(random.randint(0, 255)) for _ in range(4))

    def generate_random_port():
        return str(random.randint(1024, 65535))

    protocols = ["ICMP", "UDP", "TCP"]
    directions = ["SEND", "RECEIVE"]
    logs = []
    start_time = datetime(2025, 6, 21, 15, 8, 8)

    for i in range(25):
        timestamp = start_time + timedelta(seconds=i // 2)
        action = "ALLOW"
        protocol = random.choice(protocols)
        src_ip = "10.0.0.95"
        dst_ip = generate_random_ip() if random.random() < 0.5 else src_ip
        src_port = generate_random_port() if protocol != "ICMP" else "-"
        dst_port = generate_random_port() if protocol != "ICMP" else "-"
        send_recv = random.choice(directions)
        byte_size = random.randint(4, 60000)
        log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {action} {protocol} {src_ip} {dst_ip} {src_port} {dst_port} 0 - - - - 0 0 - {send_recv} {byte_size}"
        logs.append(log)

    return logs
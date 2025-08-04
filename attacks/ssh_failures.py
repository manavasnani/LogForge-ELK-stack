from datetime import datetime
import random

def generate():
    logs = []
    for _ in range(random.randint(3, 7)):
        ip = f"192.168.1.{random.randint(2, 254)}"
        logs.append(f"{datetime.now().isoformat()} SSH login failed for user root from {ip}")
    return logs
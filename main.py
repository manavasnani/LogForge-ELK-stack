from attacks import (
    powershell_exec,
    ssh_failures,
    linux_brute_force,
    port_scan,
    cloud_iam_misuse
)
from utils.formatter import format_log
from utils.writer import write_logs
import yaml
import os
from datetime import datetime

mapping_path = os.path.join("config", "mitre_mapping.yaml")
with open(mapping_path, "r") as f:
    mitre_map = yaml.safe_load(f)

attack_to_module = {
    "powershell_execution": powershell_exec,
    "ssh_failures": ssh_failures,
    "brute_force": linux_brute_force,
    "portscan": port_scan,
    "cloudtrail": cloud_iam_misuse,
}

attack_to_folder = {
    "powershell_execution": "Windows",
    "ssh_failures": "Windows",
    "brute_force": "Linux",
    "portscan": "Linux",
    "cloudtrail": "Cloud"
}

attack_to_extension = {
    "powershell_execution": ".json",
    "ssh_failures": ".json",
    "brute_force": ".log",
    "portscan": ".log",
    "cloudtrail": ".json"
}

base_log_path = "D:/LogForge/Logs"

for attack, module in attack_to_module.items():
    logs = module.generate()
    mitre_id = mitre_map.get(attack, "T0000")
    formatted_logs = [format_log(log, attack, mitre_id) for log in logs]

    folder = attack_to_folder[attack]
    ext = attack_to_extension[attack]
    filename = f"{attack}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
    full_path = os.path.join(base_log_path, folder, filename)

    write_logs(formatted_logs, full_path)
    print(f"[+] {len(formatted_logs)} logs written to {full_path}")
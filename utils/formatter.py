import json
from datetime import datetime

def format_log(message, attack_type, mitre_id):
    return json.dumps({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "message": message,
    })
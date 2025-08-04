from datetime import datetime

def generate():
    logs = []
    logs.append(f"{datetime.now().isoformat()} [PowerShell] Creating Scriptblock text: $env:USERNAME; whoami; Get-Process")
    return logs
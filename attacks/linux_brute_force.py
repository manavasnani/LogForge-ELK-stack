import random
from datetime import datetime, timedelta

def generate():
    logs = []
    base_time = datetime(2025, 6, 13, 18, 51, 4)
    pids = [23139, 23747, 23857, 23989]
    ports = [55734, 50556, 49032, 60146]
    time_deltas = [5, 4, 5, 4, 4, 5, 5, 5, 6, 3, 4, 33]

    # Generate SSH failed login attempts
    time = base_time
    for i in range(12):
        pid_index = i // 3
        pid = pids[pid_index]
        port = ports[pid_index]
        log_time = time.isoformat(timespec='microseconds') + "-04:00"
        log = f"{log_time} kali sshd-session[{pid}]: Failed password for invalid user invaliduser from 127.0.0.1 port {port} ssh2"
        logs.append(log)
        time += timedelta(seconds=time_deltas[i])

    # Add the sudo grep command as the last entry
    log_time = time.isoformat(timespec='microseconds') + "-04:00"
    logs.append(f"{log_time} kali sudo:     kali : TTY=pts/0 ; PWD=/home/kali/LogForge ; USER=root ; COMMAND=/usr/bin/grep 'Failed password' /var/log/auth.log")

    return logs
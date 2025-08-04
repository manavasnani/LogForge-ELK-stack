def write_logs(logs, filepath):
    with open(filepath, "a", encoding="utf-8") as f:
        for log in logs:
            f.write(log + "\n")
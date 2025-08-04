from datetime import datetime, timedelta

def generate():
    base_time = datetime(2025, 6, 21, 10, 15, 22)
    events = [
        "CreateAccessKey",
        "AttachUserPolicy",
        "ListUsers",
        "ListRoles",
        "UpdateAssumeRolePolicy",
        "PutUserPolicy",
        "GetAccountAuthorizationDetails"
    ]

    logs = []
    for i, event in enumerate(events):
        event_time = (base_time + timedelta(minutes=2 * i + i // 2)).strftime('%Y-%m-%dT%H:%M:%SZ')
        log = {
            "eventTime": event_time,
            "eventSource": "iam.amazonaws.com",
            "eventName": event,
            "userIdentity": {
                "type": "IAMUser",
                "userName": "iam-test-user"
            },
            "sourceIPAddress": "203.0.113.45",
            "awsRegion": "us-east-1"
        }
        logs.append(log)

    return logs
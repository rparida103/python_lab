from datetime import datetime, timezone

event_time = datetime.now().astimezone(timezone.utc)
print(event_time)
with open("../resources/dummy.log", 'r') as fh:
    for line in fh.readlines():
        if "BEGIN" in line:
            tstamp_str=' '.join(line.split()[:2])
            tstamp = datetime.strptime(tstamp_str, "%Y-%m-%d %H:%M:%S.%f").astimezone(timezone.utc)
            print(tstamp)
if event_time < tstamp:
    print(f"{event_time} is before {tstamp}")
else:
    print(f"{event_time} is after {tstamp}")



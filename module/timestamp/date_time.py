import datetime

print(datetime.datetime.now().astimezone().replace(microsecond=0))
import os

from datetime import datetime

exec_time = datetime.now()
timestamp = exec_time.strftime('%Y%m%d-%H%M%S')
output_dir = "output"
file = "1"

path = os.path.join(output_dir, str(timestamp))
print(path)

if not os.path.isdir(path):
    os.mkdir(path)
import json

from datetime import datetime
from pathlib import Path

url= 'https://eproc.esdm.go.id/eproc4/'

file_time = datetime.now()
file_name = f"{'-'.join(url.split('/')[2].split('.')[:2])}"
# file_name = f"{file_name}-tender-{file_time.strftime('%Y%m%d-%H%M%S')}.json"
file_name = f"{file_name}-tender.json"


print(file_name)

my_file = Path(f"{file_name}")

data = []

if my_file.is_file():
	with open(f'{file_name}') as json_file:
		data = json.load(json_file)

# Dummy data
new_data = {
	'a': 1,
	'b': 2,
	'c': 3
}

data.append(new_data)

with open(f'{file_name}', 'w', encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)

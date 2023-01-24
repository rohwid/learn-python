from datetime import datetime

url= 'https://eproc.esdm.go.id/eproc4/'

time = f'{datetime.now()}'
file_name = f"{'-'.join(url.split('/')[2].split('.')[:2])}"
# file_name = f"{file_name}-tender-{file_time.strftime('%Y%m%d-%H%M%S')}.json"
file_name = f"{file_name}-tender.log"

print(file_name)
err = '123'

with open(f'{file_name}', 'a', encoding='utf-8') as f:
    f.write(f'{time} - [E] Found in {url}\n')
    f.write(f"{''.join([i.replace(i, ' ') for i in list(time)])} - message: {err}\n")
    
import time

def generate_date_timestamp():
    current_time = time.time()
    time_obj = time.localtime(current_time)
    
    for_date = time.strftime("%Y%m%d%H%M", time_obj)

    return f"{for_date}"

print(generate_date_timestamp())


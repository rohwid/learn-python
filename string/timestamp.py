import os
import time

def generate_name_timestamp(name):
    current_time = time.time()
    time_obj = time.localtime(current_time)
    
    timestamp = '%d%d%d%d%d%d' % (
        time_obj.tm_year,
        time_obj.tm_mon,
        time_obj.tm_mday,
        time_obj.tm_hour, 
        time_obj.tm_min, 
        time_obj.tm_sec
    )

    return f"{name}-{timestamp}"

with open('file.txt', 'w') as f:
    f.write('Create a new text file!')



os.rename('file.txt', f"{generate_name_timestamp('sembik')}.txt")
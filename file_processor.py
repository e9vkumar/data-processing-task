import os
import pandas as pd
import datetime
from collections import defaultdict

path = "generated_files/"
output_dir = "file_structure/"
files = os.listdir(path)

start_date = datetime.datetime(2020,1,1,0,0,0)


for file in files:
    read_file_path = os.path.join(path,file)
    
    df = pd.read_csv(read_file_path)
    length = len(df)
    for i in range(0,length,24):
        day_chunk = df.iloc[i:i+24]
        datetime_str = day_chunk.iloc[0]['Date']
        date_key = datetime.datetime.strptime(datetime_str,'%Y-%m-%d %H:%M:%S').date()

        resource_folder_name = day_chunk.iloc[0]['Resource']
        year_folder_name = str(date_key.year)

        month_folder_name = str(date_key.month)
        if date_key.month < 10:
            month_folder_name = "0" + month_folder_name

        month_folder_name = year_folder_name + month_folder_name

        day_file_name = str(date_key.day)

        if date_key.day <10:
            day_file_name = "0" + day_file_name

        day_file_name = month_folder_name + day_file_name + ".csv"

        file_path = os.path.join(output_dir,resource_folder_name)

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        file_path = os.path.join(file_path,year_folder_name)

        if not os.path.exists(file_path):
            os.makedirs(file_path)        

        file_path = os.path.join(file_path,month_folder_name)

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        file_path = os.path.join(file_path,day_file_name)

        day_chunk.to_csv(file_path,index=False)






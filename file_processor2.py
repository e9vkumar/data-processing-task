import os,json,datetime,calendar

output_dir = "file_structure2"
input_dir = "generated_files"
counter = 1

for file in os.scandir(input_dir):
    file_pointer = open(file.path)
    file_data = file_pointer.readlines()
    # print(file_data)
    resource = file_data[1].strip().split(',')[1]
    start_date = datetime.datetime(2020,1,1,0,0,0)
    end_date = datetime.datetime(2024,5,31,23,0,0)
    temp_date = start_date
    summary = []

    for line in range(1,len(file_data),24):
        month_folder_path = os.path.join(output_dir,resource,str(temp_date.year),str(temp_date.year) + str(temp_date.month).zfill(2))
        os.makedirs(month_folder_path,exist_ok=True)

        day_file_name = str(temp_date.year) + str(temp_date.month).zfill(2) + str(temp_date.day).zfill(2) + '.csv'
        with open(os.path.join(month_folder_path,day_file_name),'w') as output_file:
            output_file.write('Date,Resource,Value\n')
            output_file.writelines(file_data[line:line+24])
            sum_val = sum([float(i.strip().split(',')[-1]) for i in file_data[line:line+24]])
            sum_val = round(sum_val,2)
            summary.append({"Date":temp_date.date(),"Value":sum_val})

        if temp_date.day == calendar.monthrange(temp_date.year,temp_date.month)[1]:
            with open(os.path.join(month_folder_path,'totals.json'),'w') as json_file:
                json.dump(summary,json_file,indent=3,default=str)
            summary = []
        temp_date += datetime.timedelta(days=1)
    file_pointer.close()
    print(counter)
    counter += 1
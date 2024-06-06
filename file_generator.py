import os
import datetime
import pandas as pd
import random
import string

def generateVal():
    lower,upper = 20.00, 142.00
    random_num = round(random.uniform(lower,upper),2)
    return random_num

def generateSlug():
    random_upper = random.choice(string.ascii_uppercase)
    random_slug = ''.join(random.choices(string.ascii_lowercase,k=15))
    return random_upper + random_slug

for i in range(6542):
    df = []
    start_date = datetime.datetime(2020,1,1,0,0,0)
    end_date = datetime.datetime(2024,5,31,23,0,0)
    slug = generateSlug()

    while start_date <= end_date:
        price_val = generateVal()
        new_row = {'Date':start_date,'Resource':slug,'Price':price_val}
        df.append(new_row)
        start_date += datetime.timedelta(hours=1)

    df = pd.DataFrame(df)
    df.to_csv(f'generated_files/output_{i}.csv',index=False)
    print(f"File {i} done")




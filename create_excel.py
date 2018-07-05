import xlwt


def generate_time_string():
    import datetime
    temp_my_time = datetime.datetime.now()
    result_date=""
    result_date+= str(temp_my_time.year)
    result_date+=str(temp_my_time.month)
    result_date+=str(temp_my_time.day)
    result_date+=str(temp_my_time.hour)
    result_date+=str(temp_my_time.minute)
    result_date+=str(temp_my_time.second)
    return result_date

wbk = xlwt.Workbook()
sheet = wbk.add_sheet("ljw_first_one")
sheet.write(0,1,'test text')
file_name = generate_time_string()
file_name+='.xls'
print(file_name)
wbk.save(file_name)
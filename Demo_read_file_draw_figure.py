import datetime

axis_x=[]
axis_y=[]

def generate_time_string():
    
    temp_my_time = datetime.datetime.now()
    result_date=""
    result_date+= str(temp_my_time.year)
    result_date+=str(temp_my_time.month)
    result_date+=str(temp_my_time.day)
    result_date+=str(temp_my_time.hour)
    result_date+=str(temp_my_time.minute)
    result_date+=str(temp_my_time.second)
    return result_date

def draw_figure(axis_x,axis_y):
    import matplotlib.pyplot as plt
    plt.plot(axis_x,axis_y,label='First line',linewidth=3,color='r',marker='o', 
    markerfacecolor='blue',markersize=1,) #the 
       
    plt.xlabel('time') 
    plt.ylabel('Value of the smoke') 
    plt.title('the detector data\nauthor:foo') 
    plt.legend() 
    #plt.savefig("examples.png") 
    plt.show() 


def read_draw_figure():
    # for creating a new excel file
    import xlwt
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("ljw_first_one")
    #for reading a file's absolute path
    import tkinter as tk  
    from tkinter import filedialog  
      
    root = tk.Tk()  
    root.withdraw()  
       
    file_path_tuple = filedialog.askopenfilenames() 
    file_path_list=list(file_path_tuple)
    
    #read the file
    f = open(file_path_list[0],'r')
    # s=f.read()#read all the context at a time
    # print (s)
    line = f.readline()#read a line at a time
    line_index = 0
    array_input =[]
    
    while line:
        line_index += 1
        array = line.split()#get the array
        for i in range(1,len(array)):
            sheet.write(line_index,i,array[i])
            
#        sheet.write(line_index,1,'test text')
        if line_index > 7 :#clear the needless data,otherwise it will be wrong when split the data
            data = array[4]#get the smoke data that I want
            array_input.append(data)
            print (data)
            
            time_stamp = array[0]
            temp_length = len(time_stamp)
            time_stamp = time_stamp[:temp_length-3]
            transfer_data = int(time_stamp)
            dateArray = datetime.datetime.utcfromtimestamp(transfer_data)
            otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
            sheet.write(line_index,0,otherStyleTime)
        line = f.readline()
        
    print(array_input) 
    file_name = generate_time_string()
    file_name+='.xls'
    print(file_name)
    wbk.save(file_name)
      
    f.close()  
       
    global  axis_y
    axis_y = array_input
    global axis_x
    axis_x=range(0,line_index-7) 
    
    draw_figure(axis_x,axis_y)  
           
read_draw_figure()
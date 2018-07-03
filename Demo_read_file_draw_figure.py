print ("HelloWorld")
#read the file
f = open(r"device001.txt",'r')

# s=f.read()#read all the context at a time
# print (s)
line = f.readline()#read a line at a time
line_index = 0
array_input =[]
while line:
    line_index += 1
    if line_index > 7 :#clear the needless data,otherwise it will be wrong when split the data
        array = line.split()#get the array
#         print array
        data = array[4]#get the smoke data that I want
        array_input.append(data)
        print (data)
    line = f.readline()
    
print(array_input)   
f.close()
import matplotlib.pyplot as plt
   
y1=[] 
y1 = array_input
x1=range(0,line_index-7) 
   
   
plt.plot(x1,y1,label='First line',linewidth=3,color='r',marker='o', 
markerfacecolor='blue',markersize=1) #the 
   
plt.xlabel('time') 
plt.ylabel('Value of the smoke') 
plt.title('the detector data\nauthor:foo') 
plt.legend() 
#plt.savefig("examples.png") 
plt.show() 
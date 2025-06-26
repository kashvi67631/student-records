import pickle 
#student records
print('Welcome! Thank you for choosing us!')
def write():
    f=open('student.dat','wb')
    rec=[]
    while True:
        roll=int (input('enter the roll number of candidate:'))
        name=input('enter the name of candidate')
        stream_course=input('enter the stream or course of candidate:')
        percent=int (input('enter the percentage obtained:'))
        r=[roll,name,percent,stream_course]
        rec.append(r)
        ch=input('do you want to enter more records?:Yes/No')
        if ch.lower()=='no':
            break
    pickle.dump(rec,f)
    f.close()
write()
def display():
    import pickle 
    f=open('student.dat','rb')
    k=pickle.load(f)
    for i in k:
        print('The details are as below')
        print('rollno ', i[0])
        print('name:', i[1])
        print('stream/course :', i[3])
        print('marks:',i[2])
    f.close()    
def update():
    try:
        with open('student.dat', 'rb') as f:
            k = pickle.load(f)
    except:
        print(" Error reading file.")
        return

    roll_to_update = int(input("Enter Roll No to update: "))
    for i in k:
        if i[0] == roll_to_update:
            print(f"Current Record: {i}")
            field = int(input("What to update? (1=Roll, 2=Name, 3=Marks, 4=Stream): "))
            if field == 1:
                i[0] = int(input("New Roll No: "))
            elif field == 2:
                i[1] = input("New Name: ")
            elif field == 3:
                i[2] = float(input("New Percentage: "))
            elif field == 4:
                i[3] = input("New Stream: ")
            else:
                print(" Invalid option.")
            break
    else:
        print(" Roll number not found.")

    with open('student.dat', 'wb') as f:
        pickle.dump(k, f)
    print(" Record updated.")
            
def search():
    import pickle
    f=open('student.dat','rb')
    k=pickle.load(f)
    r = int(input('enter the roll number to be searched:'))
    try:
        for i in k:
            if i[0]==r:
                 print('The details are as below')
                 print('rollno ', i[0])
                 print('name:', i[1])
                 print('stream/course :', i[3])
                 print('marks:',i[2])   
    except EOFError :
        print('error found')                        
ch=int(input('Do you want to display-1/update-2/search-3/none-4'))
if ch==1:
    display()
elif ch==2 :
    update()
elif ch==3 : 
    search()
else:
    print('Thank You ! for visiting us')

#CSV file on student
print('Welcome Thank You for choosing us')
print("Let's pursue with students records , kindly enter the given details")
import csv
def write():
    f=('student.csv','w')
    k=csv.writer(f)
    while True:
        roll=int(input('Roll NO. of the student-'))
        name=input('Name of the student-')
        per=int(input('Percentage of the student-'))
        course_stream=input('Course/stream of the student-')
        rec=[roll,name,per,course_stream]
        k.writerow(rec)
        ch=input('Do you have more records?-Yes/No')
        if ch.lower()=='no':
            break
    f.close()
    print('Task completed!')
 write()
def search():
     import csv
     f=('student.csv','r')
     k=csv.reader(f)
     n=input('please enter the name of the candidate to be searched-')
     try:
         for i in k:
             if i[1]==n:
                 print('The roll number is:' , i[0])
                 print('The name is:', i[1])
                 print('The course stream:',i[2])
                 print('The percentage is : ' , i[3])
            else:
                print('Sorry,no such name found')
    except EOFError:
        print('Error found')
    f.close()
def update():
    import csv
    f=('student.csv','r')
    k=csv.reader(f)
    n=input('please enter the name of the candidate to be updated-')
    p=int(input('''what do u want to update kindly click following for :)
             roll number - 0
             name-1
             course/stream-2
             percentage-3'''))
    try:
         for i in k:
             if i[1]==n and i==p and p%2==0 :
                 i[1]=int(input('Enter new record-'))
    except EOFError :
        print('Error Found')
    f.close()
def display():
    import csv
    f=('student.csv','r')
    k=csv.reader(f)
    print('These are the codes entered')
    for i in k :
        print(i)
    f.close()
ch=input('Do you want to search/update/display data or none ? -')
if ch=='search':
     search()
elif ch=='update':
    update()
elif ch=='display':
    display()
    

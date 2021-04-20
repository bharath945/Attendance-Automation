import csv,time
from collections import defaultdict
dicti=defaultdict(int)
dictf=defaultdict(int)
f1=None
try:
    f1=open("meetingAttendanceList.csv",'r')
except Exception as e:
    print(e)
    print("Please change today's attendance file name as :- meetingAttendanceList")
    print(" and then run the code again")
    time.sleep(3)
    exit(1)

reader=csv.reader(f1)
j=0
print("Enter time at which session ended in the 24 hour format Eg:- (12:30)")
try:
    hr,mi=[int(i) for i in input().split(":")]
except:
    print("Please enter in 24 hour format with collon Eg:- (12:30) and run the program again.....!")
    time.sleep(3)
    exit(1)
if hr>=24 or mi>=60:
    print("You should enter hours less than 24 and minutes less than 60")
    print("You should enter valid time")
    print("Run the program again")
    time.sleep(3)
    exit(1)
nm=int(input("Enter minimum time of presence requried in minutes: "))
j=0
try:
    for i in reader:
        if j==0:
            j=1
        else:
            if i[0][0]=='1' or i[0][0]=='2':
                if i[1]=="Joined" or i[1]=="Joined before":
                    k=i[2].split()
                    amopm=k[-1].lower()
                    k=k[1]
                    h=0
                    min1=0
                    if k[1]==":":
                        h=int(k[0])
                        min1=int(k[2:4])
                    else:
                        h=int(k[0:2])
                        min1=int(k[3:5])
                    if amopm=="pm" and h!=12:
                        h+=12
                    min1=int(min1)
                    min1=min1+int(h)*60
                    dicti[i[0]]=min1
                elif i[1]=='Left':
                    k=i[2].split()
                    amopm=k[-1].lower()
                    k=k[1]
                    h=0
                    min1=0
                    if k[1]==":":
                        h=int(k[0])
                        min1=int(k[2:4])
                    else:
                        h=int(k[0:2])
                        min1=int(k[3:5])
                    if amopm=="pm" and h!=12:
                        h+=12
                    min1=int(min1)
                    min1=min1+int(h)*60
                    dicti[i[0]]=min1-dicti[i[0]]
                    dictf[i[0].lower()]=dicti[i[0]]
                    del dicti[i[0]]
except Exception as e:
    print(e)
    print("please change file to csv extention")
    print(" and then run the code again")
    time.sleep(3)
    exit(1)
for i in dicti:
    min1=hr*60+mi 
    dicti[i]=min1-dicti[i]
    dictf[i]+=dicti[i]
lst=[]
for i in dictf:
    if dictf[i]>=nm:
        lst.append(i)
lst.sort()
file_name=input("Enter Dailly Attendance sheet's file name : ")
ba=file_name+".csv"
f3=None
try:
    f3=open(ba,"r")
except Exception as e:
    print(e)
    print("please enter valid file name")
    time.sleep(3)
    exit(1)
reader=csv.reader(f3)
j=0
np=0
na=0
lsta=[]
lst_file=[]
for i in reader:
    if j==0:
        lst_file.append(i)
        j+=1
    elif j==1:
        i.append(input("Enter topic name : "))
        lst_file.append(i)
        j+=1
    elif j==2:
        i.append(input("Enter date, when the session was held : "))
        lst_file.append(i)
        j+=1
    else:
        try:
            int(i[0])
            if i[2].lower() in lst:
                i.append("")
                lst_file.append(i)
                np+=1
            else:
                lsta.append(str(i[2]))
                i.append("A")
                lst_file.append(i)
                na+=1
        except:
            if j==3:
                i.append(np)
                lst_file.append(i)
            elif j==4:
                i.append(na)
                lst_file.append(i)
            elif j==5:
                i.append(str((np/(np+na))*100)+"%")
                lst_file.append(i)
            elif j==6:
                i.append(str(lsta))
                lst_file.append(i)
            j+=1

f1.close()
f3.close()
print(file_name)
f2=open(file_name+'.csv',"w",newline='')
writer=csv.writer(f2)
for i in lst_file:
    writer.writerow(i)
f2.close()
print("Data Saved Successfully")
time.sleep(5)

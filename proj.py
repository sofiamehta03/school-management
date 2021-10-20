import mysql.connector
def selection():
    db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
    cursor = db.cursor()
    print('--------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM OF WOODLANDS\n-----------------------------------')
    print("1.STUDENT MANAGEMENT")
    print("2.EMPLOYEE MANAGEMENT")
    print("3.FEE MANAGEMENT")
    print("4.EXAM MANAGEMENT")
    ch=int(input("\nEnter ur choice (1-4)and 5 to EXIT:"))
    if ch==1:
        print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
        print('a.NEW ADMISSION')
        print('b.UPDATE STUDENT DETAILS')
        print('c.ISSUE TC')
        c=input("Enter ur choice (a-c) : ")
        print('\nInitially the details are..\n')
        
        if c=='a':
            display1()
            insert1()
            print('\nModified details are..\n')
            display1()
            selection()
        elif c=='b':
            display1()
            update1()
            print('\nModified details are..\n')
            display1()
            selection()
        elif c=='c':
            delete1()
            print('\nModified details are..\n')
            display1()
            selection()
        else:
            print('Enter correct choice...!!')
            selection()
    elif ch==2:
        print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
        print('a.NEW EMPLOYEE')
        print('b.UPDATE STAFF DETAILS')
        print('c.DELETE EMPLOYEE')
        c=input("Enter ur choice : ")
        if c=='a':
            display2()
            insert2()
            print('\nModified details are..\n')
            display2()
            selection()
        elif c=='b':
            display2()
            update2()
            print('\nModified details are..\n')
            display2()
            selection()
        elif c=='c':
            display2()
            delete2()
            print('\nModified details are..\n')
            display2()
            selection()
        else:
            print('Enter correct choice...!!')
            selection()
    elif ch==3:
        print('WELCOME TO FEE MANAGEMENT SYSTEM')
        print('a.NEW FEE')
        print('b.UPDATE FEE')
        print('c.EXEMPT FEE')
        c=input("Enter ur choice : ")
        if c=='a':
            display3()
            insert3()
            print('\nModified details are..\n')
            display3()
            selection()
        elif c=='b':
            display3()
            update3()
            print('\nModified details are..\n')
            display3()
            selection()
        elif c=='c':
            display3()
            delete3()
            print('\nModified details are..\n')
            display3()
            selection()
        else:
            print('Enter correct choice...!!')
            selection()
    elif ch==4:
        print('WELCOME TO EXAM MANAGEMENT SYSTEM')
        print('a.ENTER EXAM DETAILS')
        print('b.UPDATE DETAILS ')
        print('c.DELETE DETAILS')
        c=input("Enter ur choice : ")
        if c=='a':
            display4()
            insert4()
            print('\nModified details are..\n')
            display4()
            selection()
        elif c=='b':
            display4()
            update4()
            print('\nModified details are..\n')
            display4()
            selection()
        elif c=='c':
            display4()
            delete4()
            print('\nModified details are..\n')
            display4()
            selection()
        else:
            print('Enter correct choice...!!')
            selection()
        db.rollback()
        db.close()
    if ch==5:
        exit()
    else:
        print("Enter valid choice No from 1-4")
        selection()
def insert1():
    sname=input("Enter Student Name : ")
    admno=int(input("Enter Admission No : "))
    dob=input("Enter Date of Birth(yyyy-mm-dd): ")
    cls=input("Enter class for admission: ")
    cty=input("Enter City : ")
    db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
    cursor = db.cursor()
    sql="INSERT INTO student(sname,admno,dob,cls,cty) VALUES ( '%s' ,'%d','%s','%s','%s')"%(sname,admno,dob,cls,cty)
    cursor.execute(sql)
    db.commit()
    db.close()
def display1():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            print ("(sname=%s,admno=%d,dob=%s,cls=%s,cty=%s)" % (sname,admno,dob,cls,cty))
    except:
            print ("Error: unable to fetch data")
            db.close()
    

def update1():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print ("Error: unable to fetch data")
        print()
    tempst=int(input("Enter Admission No : "))
    temp=input("Enter new class if want to change otherwise old only : ")
    temp1=input("Enter new dob if want to change otherwise old only : ")
    temp2=input("Enter new city if want to change otherwise old only : ")
    try:
        sql = "Update student set cls='%s', dob='%s', cty='%s' where admno='%d'" % (temp,temp1,temp2,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
        db.close()


def delete1():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print ("Error: unable to fetch data")
    temp=int(input("\nEnter adm no to be deleted : "))
    try:
        sql = "delete from student where admno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()
def insert2():
    try:
        empno=int(input("Enter Employee No : "))
        ename=input("Enter Employee Name : ")
        job=input("Enter Designation: ")
        hiredate=input("Enter date of joining: ")
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql="INSERT INTO employee VALUES ( '%d' ,'%s','%s','%s')"%(empno,ename,job,hiredate)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
   
def display2():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM employee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            ename = c[1]
            empno= c[0]
            job=c[2]
            hiredate=c[3]
            print ("(empno=%d,ename=%s,job=%s,hiredate=%s)" % (empno,ename,job,hiredate))
    except Exception as e:
        print(e)
    db.close()

def update2():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM employee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            ename = c[0]
            empno= c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print ("Error: unable to fetch data")
        print()
        
    try:
        tempst=int(input("Enter Employee No : "))
        temp=input("Enter new designation : ")
        sql="Update employee set job='%s' where empno ='%d'" % (temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
    db.close()
def delete2():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM employee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            ename = c[0]
            empno= c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print ("Error: unable to fetch data")
        
    try:
        temp=int(input("\nEnter emp no to be deleted : "))
        sql = "delete from employee where empno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
            print("deleted")
    except Exception as e:
        print (e)
        db.close()
def insert3():
    admno=int(input("Enter adm no: "))
    fee=float(input("Enter fee amount : "))
    month=input("Enter Month: ")
    db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
    cursor = db.cursor()
    sql="INSERT INTO fee(admno,fee,month) VALUES ( '%d','%d','%s')"%(admno,fee,month)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        db.close()
def display3():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno= c[0]
            fee=c[1]
            month=c[2]
            print ("(admno=%d,fee=%s,month=%s)" % (admno,fee,month))
    except Exception as e:
        print(e) 
    db.close()
def update3():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno= c[0]
            fee=c[1]
            month=c[2]
    except:
        print ("Error: unable to fetch data")
        print()
        
    try:
        tempst=int(input("Enter Admission No : "))
        temp=input("Enter new month : ")
        temp1=input("Enter new Fee Amount : ")
        sql="Update fee set month='%s', fee='%s' where admno='%d'" % (temp,temp1,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
    db.close()
def delete3():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno= c[0]
            fee=c[1]
            month=c[2]
    except:
        print ("Error: unable to fetch data")
        
    try:
        temp=int(input("\nEnter adm no to be deleted : "))
        sql = "delete from student where admno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
    db.close()
def insert4():
    sname=input("Enter Student Name : ")
    admno=int(input("Enter Admission No : "))
    per=float(input("Enter percentage : "))
    res=input("Enter result: ")
    db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
    cursor = db.cursor()
    sql="INSERT INTO exam(sname,admno,per,res) VALUES ( '%s' ,'%d','%s','%s')"%(sname,admno,per,res)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        
    db.close()
def display4():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            per=c[2]
            res=c[3]
            print ("(sname=%s,admno=%d,per=%d,res=%s)"%(sname,admno,per,res) )
    except Exception as e:
        print (e)
    db.close()
def update4():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            per=c[2]
            res=c[3]
    except:
        print ("Error: unable to fetch data")
        print()
        
    try:
        tempst=int(input("Enter Admission No : "))
        temp=input("Enter new result : ")
        sql = "Update exam set res='%s' where admno='%d'" % (temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
       print (e)
    db.close()
def delete4():
    try:
        db = mysql.connector.connect(user='root', password='admin', host='localhost',database='woodland')
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print ("Error: unable to fetch data")
        
    try:
        temp=int(input("\nEnter adm no to be deleted : "))
        sql = "delete from exam where admno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
    db.close()
selection()

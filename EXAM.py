import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="mysql",passwd="12345",database="students")
myco=sqltor.connect(host="localhost",user="mysql",passwd="12345",database="student")
if mycon.is_connected():
    print("CBSE Board")
if myco.is_connected():
    print("CBSE registration information system") 
cursor=mycon.cursor()
curso=myco.cursor()
def check():
    if n!="" and s!="" and t!="" and ci!="" and d!="" and st!="" and f!="" and m!="" and co!="":
        return True
    else:
        return False
while True:
    print("1.Registration")
    print("2.Time Table")
    print("3.Feed Back")
    print("4.Project Mark")
    print("5.Checking the information(registration)")
    print("6.Deleting the information(registration)")
    print("7.Checking the information(project marks)")
    print("8.Deleting the information(project marks)")
    print("9.Exam Center")
    print("10.Circulars")
    print("11.Results")
    print("12.Sample Question paper") 
    print("13.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("ENTER THE NECESSARY DETAILS")
        n=input("Enter your name(IN CAPITAL LETTERS)                              :")
        su=input("Enter your surname(IN CAPITAL LETTERS)                           :")
        reg=int(input("Enter the number alloted for the school by the CENTRAL GOVERNMENT:"))
        c=int(input("Enter your class(in numbers)                                     :"))
        a=int(input("Enter your age(in numbers)                                       :"))
        s=input("Enter your school name                                           :")
        print("All the below details can be filled based on your school location")
        t=input("Enter your town                                                  :")
        ci=input("Enter your city                                                  :")
        d=input("Enter your district                                              :")
        st=input("Enter your state                                                 :")
        f=input("Enter your father's name                                         :")
        m=input("Enter your mother's name                                         :")
        co=input("Enter your community                                             :")
        ad=int(input("Enter your aadhar number                                         :"))
        if check():
            print("The necessary details is filled")
            if c==10: 
                def roll():
                    curso.execute("select * from student")
                    data=curso.fetchall()
                    x=0
                    for row in data:
                        x=x+1
                    return x
                r=20141500+roll()
                print("**********")
                print("Your roll number is:",r)
                print("**********")
                qw="insert into student(name,class,age,school,town,city,district,state,father,mother,community,aadharno,rollno,surname,schoolno)values('{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}',{})".format(n,c,a,s,t,ci,d,st,f,m,co,ad,r,su,reg)
                curso.execute(qw)
                myco.commit()
            elif c==12:
                def rolls():
                    cursor.execute("select * from students")
                    data=cursor.fetchall()
                    y=0
                    for row in data:
                        y=y+1
                    return y
                g=21141500+rolls()
                print("**********")
                print("Your roll number is:",g)
                print("**********")
                qw="insert into students(name,class,age,school,town,city,district,state,father,mother,community,aadharno,rollno,surname,schoolno)values('{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}',{})".format(n,c,a,s,t,ci,d,st,f,m,co,ad,g,su,reg)
                cursor.execute(qw)
                mycon.commit()
            else:
                print("check the class entered by you")
        else:
            print("The necessary details isn't filled")
    if ch==2:
        c=int(input("Enter your class:"))
        if c==10:
            print("For class 10")
            print("*****-science")
            print("*****-maths")
            print("*****-english")
            print("*****-social science")
            print("*****-language")
        elif c==12:
            print("For class 12")
            print("For Science stream")
            print("20.06.2021       -        physics")
            print(" 25.06.2021       -        chemistry")
            print("01.07.2021       -        english")
            print("05.07.2021       -        computer science")
            print(" 10.07.2021       -        maths")
            print("For commerce stream:")
            print("*******-ACCOUNTANCY")
            print("*******-BUSINESS STUDIES ")
            print("***********-ECONOMICS")
            print("**********-MATHS/CS")
            print("For arts stream:")
            print("*********-HISTORY")
            print("*********-GEOGRAPHY")
            print("********-POLTICAL SCIENCE")
            print("**********-CS/MUSIC")            
        else:
            print("check the class entered by you")
    if ch==3:
            print("1.Parents")
            print("2.Teacher")
            print("3.Students")
            print("4.Exit")
            yu=int(input("Enter your category:"))
            if yu==1:
                abt=input("What is your feedback about")
                feedback_parents=input("Enter your feedback")
                qw="insert into feed_parents(about,feedback)values('{}','{}')".format(abt,feedback_parents)
                
            elif yu==2:
                abt=input("What is your feedback about")
                feedback_teachers=input("Enter your feedback")
                qw="insert into feed_teachers(about,feedback)values('{}','{}')".format(abt,feedback_teachers)
            elif yu==3:
                abt=input("What is your feedback about")
                feedback_students=input("Enter your feedback")
                qw="insert into feed_students(about,feedback)values('{}','{}')".format(abt,feedback_students)
            else:
                break
    if ch==4:
        c=int(input("Enter your class:"))
        my=sqltor.connect(host="localhost",user="mysql",passwd="12345",database="promarks10")
        mys=sqltor.connect(host="localhost",user="mysql",passwd="12345",database="promarks12")
        if my.is_connected:
            print("Enter the project marks:")
        if mys.is_connected:
            print("**********")
        cu=my.cursor()
        cus=mys.cursor()
        if c==10:
            r=int(input("Enter your roll number:"))
            un=int(input("Maths:"))
            pn=int(input("English:"))
            rn=int(input("Socialscience:"))
            dn=int(input("Science:"))
            ln=int(input("Language:"))
            qs="insert into promarks10(maths,english,socialscience,science,language,rollno)values({},{},{},{},{},{})".format(un,pn,rn,dn,ln,r)
            cu.execute(qs)
            my.commit()
            print("Thank you")
        elif c==12:
            g=int(input("Enter your roll number:"))
            print("For science stream:")
            print("Subject1-PHYSICS")
            print("Subject2-CHEMISTRY")
            print("Subject3-MATHS/CS")
            print("Subject4-BIOLOGY/CS")
            print("For commerce stream:")
            print("Subject1-ACCOUNTANCY")
            print("Subject2-BUSINESS STUDIES ")
            print("Subject3-ECONOMICS")
            print("Subject4-MATHS/CS")
            print("For arts stream:")
            print("Subject1-HISTORY")
            print("Subject2-GEOGRAPHY")
            print("Subject3-POLTICAL SCIENCE")
            print("Subject4-CS/MUSIC")
            print("If the student chose other subjects you can enter the project marks under the optional subject")
            un=int(input("Subject1:"))
            pn=int(input("English:"))
            rn=int(input("Subject2:"))
            dn=int(input("Subject3:"))
            ln=int(input("Subject4:"))
            qe="insert into promarks12(sub1,english,sub2,sub3,sub4,rollno)values({},{},{},{},{},{})".format(un,pn,rn,dn,ln,g)
            cus.execute(qe)
            mys.commit()
            print("Thank you")
        else:
            pass
    elif ch==5:
        c=int(input("Enter your class:"))
        if c==10:
            r=int(input("Enter your roll number:"))
            ag="select * from student where rollno={}".format(r)
            curso.execute(ag)
            dat=curso.fetchall()
            for row in dat:
                name=row[0]
                clas=row[1]
                age=row[2]
                school=row[3]
                town=row[4]
                city=row[5]
                district=row[6]
                state=row[7]
                father=row[8]
                mother=row[9]
                community=row[10]
                aadharno=row[11]
                rollno=row[12]
                sur=row[13]
                reg=row[14]
                print("Name          :",name)
                print("Class         :",clas)
                print("Age           :",age)
                print("School        :",school)
                print("Towm          :",town)
                print("City          :",city)
                print("District      :",district)
                print("State         :",state)
                print("Father        :",father)
                print("Mother        :",mother)
                print("Community     :",community)
                print("Aadharno      :",aadharno)
                print("Rollno        :",rollno)
                print("Surname       :",sur)
                print("Schoolno      :",reg)
        elif c==12:
            g=int(input("Enter your roll number:"))
            ak="select * from students where rollno={}".format(g)
            cursor.execute(ak)
            dat=cursor.fetchall()
            for row in dat:
                name=row[0]
                clas=row[1]
                age=row[2]
                school=row[3]
                town=row[4]
                city=row[5]
                district=row[6]
                state=row[7]
                father=row[8]
                mother=row[9]
                community=row[10]
                aadharno=row[11]
                rollno=row[12]
                sur=row[13]
                reg=row[14]
                print("Name          :",name)
                print("Class         :",clas)
                print("Age           :",age)
                print("School        :",school)
                print("Towm          :",town)
                print("City          :",city)
                print("District      :",district)
                print("State         :",state)
                print("Father        :",father)
                print("Mother        :",mother)
                print("Community     :",community)
                print("Aadharno      :",aadharno)
                print("Rollno        :",rollno)
                print("Surname       :",sur)               
                print("Schoolno      :",reg)
        else:
            print("Check the class entered by you")
    elif ch==6:
        c=int(input("Enter your class:"))
        if c==10:
            r=int(input("Enter your roll number:"))
            st="delete from student where rollno={}".format(r)
            curso.execute(st)
            myco.commit()
            print("The information entered by you is deleted")
        elif c==12:
            g=int(input("Enter your roll number:"))
            st="delete from students where rollno={}".format(g)
            cursor.execute(st)
            mycon.commit()
            print("The information entered by you is deleted")
        else:
            pass
    elif ch==7:
        c=int(input("Enter your class:"))
        if c==10:
            r=int(input("Enter your roll number:"))
            ag="select * from promarks10 where rollno={}".format(r)
            curso.execute(ag)
            dat=curso.fetchall()
            for row in dat:
                math=row[0]
                eng=row[1]
                soci=row[2]
                sci=row[3]
                lang=row[4]
                print("Maths                 :",math)
                print("English               :",eng)
                print("Social Science        :",soci)
                print("Science               :",sci)
                print("Language              :",lang)
        elif ch==12:
            g=int(input("Enter your roll number:"))
            ag="select * from promarks12 where rollno={}".format(g)
            curso.execute(ag)
            dat=curso.fetchall()
            for row in dat:
                math=row[0]
                eng=row[1]
                soci=row[2]
                sci=row[3]
                lang=row[4]
                print("Subject1                 :",math)
                print("English                  :",eng)
                print("Subject2                 :",soci)
                print("Subject3                 :",sci)
                print("Subject4                 :",lang)
        else:
            pass
    elif ch==8:
        rt=input("Is the project marks entered by you correct(yes\no):")
        if rt=="yes":
            print("No changes will be added to the data")
        elif rt=="no":
            c=int(input("Enter your class:"))
            if c==10:
                r=int(input("Enter your roll number:"))
                st="delete from promarks10 where rollno={}".format(r)
                cu.execute(st)
                my.commit()
                print("The information entered by you is deleted")
            elif c==12:
                r=int(input("Enter your roll number:"))
                st="delete from promarks12 where rollno={}".format(g)
                cus.execute(st)
                mys.commit()
                print("The information entered by you is deleted")
        else:
            pass
    elif ch==9:
        ij=sqltor.connect(host="localhost",user="mysql",passwd="12345",database="examcenter")
        if ij.is_connected():
            print("EXAMS CENTER")
        cur=ij.cursor()
        print("NOTE THE NUMBER BASED ON YOUR STATE:")
        print("Tamil nadu:1")
        print("Andhra pradesh:2")
        print("Arunachal pradesh:3")
        print("Assam:4")
        print("Bihar:5")
        print("Chhattisgarh:6")
        print("Goa:7")
        print("Gujarat:8")
        print("Haryana:9")
        print("Himachal pradesh:10")
        print("Jammu and kashmir:11")
        print("Jharkhand:12")
        print("Karnataka:13")
        print("Kerala:14")
        print("Madhya pradesh:15")
        print("Maharashtra:16")
        print("Manipur:17")
        print("Meghalaya:18")
        print("Mizoram:19")
        print("Nagaland:20")
        print("Odisha:21")
        print("Punjab:22")
        print("Rajasthan:23")
        print("Sikkim:24")
        print("Telangana:25")
        print("Tripura:26")
        print("Uttarkhand:28")
        print("Andaman and nicobar island:30")
        print("Chandigarh:31")
        print("Daman and diu:33")
        print("Delhi:35")
        print("Dadra and nagar haveli:32")
        lm=int(input("Enter the number of your state:"))
        st=lm
        if lm==st and lm<37:
            st="select * from examcenter where number='{}'".format(lm)
            cur.execute(st)
            data=cur.fetchall() 
            for row in data:
                state=row[0]
                centercity=row[1]
                centerno=row[2]
            print("**********")
            print("State:",state)
            print("Capital city:",centercity)
            print("The center number is:",centerno)
            print("**********")
        else:
            print("The state filled by you is incorrect")
        ij.close()
    elif ch==10:
       print("No recent circulars")
    elif ch==11:
        print("The results are yet to be released")
    elif ch==12:
        c=int(input("Enter your class:"))
        if c==10:
            print("1.Maths")
            print("2.science")
            print("3.Social studies")
            print("4.English")
            print("5.Language")
            subjecct=int(input("Enter the number:"))
            if subjecct==1:
                print("For class 10")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\10 sub1.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subjecct==2:
                print("For class 10")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\10 sub2.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subjecct==3:
                print("For class 10")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\10 sub3.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subjecct==4:
                print("For class 10")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\10 sub4.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subjecct==5:
                print("For class 10")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\10 sub5.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            else:
                print("Check the number entered by you")
        elif c==12:
            print("For science stream:")
            print("Subject1-PHYSICS")
            print("Subject2-CHEMISTRY")
            print("Subject3-MATHS/CS")
            print("Subject4-BIOLOGY/CS")
            print("For commerce stream:")
            print("Subject5-ACCOUNTANCY")
            print("Subject6-BUSINESS STUDIES ")
            print("Subject7-ECONOMICS")
            print("Subject8-MATHS/CS")
            print("For arts stream:")
            print("Subject9-HISTORY")
            print("Subject10-GEOGRAPHY")
            print("Subject12-POLTICAL SCIENCE")
            print("Subject13-CS/MUSIC")
            subje=int(input("Enter your subject number:"))
            if subje==1:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub1.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==2:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub2.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==3:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub3.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==4:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub4.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==5:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub5.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==6:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub6.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==7:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub7.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==8:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub8.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==9:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub9.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==10:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub10.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==11:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub11.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==12:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub12.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            elif subje==13:
                print("For class 12")
                myfile=open(r'C:\Users\sowmy\Desktop\indhuja\sample paper\11 sub13.txt','r')
                str=myfile.read()
                print(str)
                myfile.close()
            
            else:
                print("Check the number entered by you")
    elif ch==13:
        break
    else:
        print("***************************STARTS*************************************")
       

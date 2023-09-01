import streamlit as st;
import mysql.connector
import pandas as pd
import datetime
import json
import yfinance as yf
import numpy as np
from matplotlib import pyplot as plt 
from streamlit_lottie import st_lottie
x=np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])
st.set_page_config(page_title='Employee Management System',page_icon='random')
with open("animation_lkfz9kt5.json") as source:
    animation=json.load(source)
st_lottie(animation)
choice=st.sidebar.selectbox("My Menu", ("Home", "employee", "admin", "Tech Articles And Information"))
if(choice == "Home"):
    st.markdown("<h1 style= 'text-align:center;color:brown;'>EMPLOYEE MANAGEMENT SYSTEM</h1>",unsafe_allow_html=True)
    with open("animation_lkilepd9.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    
    st.markdown("<h1 style= 'text-align:center;color:green;'>WELCOME TO OUR PAGE</h1>",unsafe_allow_html=True)
    with open("animation_lkilckhx.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    st.markdown("<h4 style= 'color:green;'>Hello this is an application, developed by Khushboo kumari as a training project.There is requirement in the industries for skills such as Database Management skills, Programming skills, Web Development skills and these skills get improved by working on these kinds of projects.It is database application which store data of employee such as name, Id of employee, address, salary of employee, number. </h4>",unsafe_allow_html=True)  
    with open("animation_lkilv2e2.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    st.markdown("<h3 style='color:yellow;'>Employee management is the process by which employers ensure workers perform their jobs to the best of their abilities so as to achieve business goals. It typically entails building and maintaining healthy relationships with employees, as well as monitoring their daily labor and measuring progress. In this way, employers can identify opportunities for improvement and recognize achievements.</h3>", unsafe_allow_html=True )
    with open("animation_lkilw8zf.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    
    st.markdown("<h3 style='color:red;'>Employee management systems are important because a business’s workforce is its greatest asset. Yet, despite this intrinsic value, employee engagement is sometimes overlooked because HR professionals are either too busy with administrative work or lack the integrations necessary to use their people data effectively. Technology can alleviate such burdens and afford employers more time to connect with workers and create strategic initiatives that will attract and retain talent.</h3>", unsafe_allow_html=True )
    
    with open("animation_lkilx13e.json") as source:
        animation=json.load(source)
    st_lottie(animation)

    st.markdown("<h3 style='color:blue;'>Employee management refers to the processes used to ensure employees perform their best. It consists of keeping track of employees’ achievements and progress, fostering healthy professional relationships and giving them the tools they need to succeed. Done right, employees will be motivated to fulfill the organization’s objectives. It can also lead to a boost in employee productivity, satisfaction, retention and engagement.</h3>", unsafe_allow_html=True )
   
 
    st.image("https://i1.wp.com/juntrax.com/blog/wp-content/uploads/2021/01/Employee-Management-System.jpg?w=1600&ssl=1")
   
    st.markdown("<h3 style='text-align:center;color:purple;'>As an employee management system, (EMS) makes it easy to onboard new hires and oversee teams and projects. The intuitive system has many features for onboarding processes, recruitment pipelines, employee well-being, as well as development and learning.Managers and HR personnel can get a complete overview of their team’s daily performance. Thanks to this feature, you can centralize planning and coordination with hiring managers and get a high-level overview of employee performance to make data-backed decisions.</h3>", unsafe_allow_html=True )
    with open("animation_lkilw2uo.json") as source:
        animation=json.load(source)
    st_lottie(animation)

    
   

elif(choice=='employee'):
    st.markdown("<h1 style= 'text-align:center;color:brown;'>WELCOME TO EMPLOYEE BLOCK</h1>",unsafe_allow_html=True)
    with open("animation_lki5fser.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    if 'login' not in st.session_state:
        st.session_state['login']=False
    id=st.text_input("ENTERS EMPLOYEE ID") 
    password=st.text_input("ENTER PASSWORD")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
        c=mydb.cursor();
        c.execute("select * from emp_login")
        for row in c:
            if(row[0]==id and row[2]==password):
                st.session_state['login']= True;
                break;
        if(st.session_state['login']==False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.subheader("login Succesful")
        with open("animation_lkgqgomw.json") as source:
            animation=json.load(source)
        st_lottie(animation)
        choice2=st.selectbox("Features",("None", "view all employee detail", "employee entry timing", "employee work record", "Apply for leave", "Contact Form"))
        
        if(choice2=="view all employee detail"):
            with open("animation_lkgptqjk.json") as source:
                animation=json.load(source)
            st_lottie(animation)
            mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
            c=mydb.cursor();
            c.execute("select * from emp")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l, columns=['emp_id', 'emp_name', 'emp_gender', 'emp_age', 'emp_email', 'address', 'emp_pss'])
            st.dataframe(df)
        if(choice2=="employee entry timing"):

            eid=st.text_input("Enter emp id")
            day=st.text_input("Enter day")
            btn2=st.button("Submit Attendence")
            if(btn2):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("insert into entry_time values(%s, %s, %s)",(doi,eid,day))
                mydb.commit()
                st.header("submittted successfully")
            btn3= st.button("Show details")
            with open("animation_lkgqxt7w.json") as source:
                animation=json.load(source)
            st_lottie(animation)
            if(btn3):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("select * from entry_time")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['emp_id', 'emp_day', 'emp_time'])
                st.dataframe(df) 
        if(choice2=="employee work record"): 
            with open("animation_lkgq12pz.json") as source:
                animation=json.load(source)
            st_lottie(animation)
            name=st.text_input("Enter Name")
            tsk=st.text_input("Enter Today's Task")
            btn4=st.button("submit task")
            if(btn4):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("insert into task values(%s, %s, %s)",(name,tsk,doi))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("select * from task")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['emp_name', 'emp_task', 'emp_time'])
                st.dataframe(df)
        if(choice2=="Apply for leave"):
            with open("animation_lkgqk5c0.json") as source:
                animation=json.load(source)
            st_lottie(animation)
            eid=st.text_input("Enter emp id")
            with st.form("form 1"):
                st.write("From")
                day,month,year=st.columns(3)
                fd=day.text_input("Day")
                fm=month.text_input("Month")
                fy=year.text_input("Year")
                st.form_submit_button("submit")
            with st.form("form 2"):
                st.write("To")
                day,month,year=st.columns(3)
                td=day.text_input("Day")
                tm=month.text_input("Month")
                ty=year.text_input("Year")
                st.form_submit_button("submit")
            btn8=st.button("Apply for leave")
            if(btn8):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("insert into apply_leave values(%s, %s, %s, %s, %s, %s, %s, %s)",(eid,fd,fm,fy,td,tm,ty,doi))
                mydb.commit()
                st.header("submittted successfully") 
            btn9= st.button("Show details")
            if(btn9):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("select * from apply_leave")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['emp_name', 'fd','fm','fy','td','tm','ty', 'emp_time'])
                st.dataframe(df)
        if(choice2=="Contact Form"):
            st.header(":mailbox: Get In Touch With US!")
            contact_form = """
            <form action="https://formsubmit.co/khushisinha011@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your Email" required>
                <textarea name="message" placeholder="Details of you problem"></textarea>
                <button type="submit">Send</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
            local_css("C:\myproject\employee\Scripts\style\style.css")
       
            
elif(choice=='admin'):
    st.markdown("<h1 style= 'text-align:center;color:brown;'>WELCOME TO ADMIN BLOCK</h1>",unsafe_allow_html=True)
    with open("animation_lkild0rd.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    if 'login2' not in st.session_state:
        st.session_state['login2']=False
    id=st.text_input("Enter admin ID") 
    password=st.text_input("Enter password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
        c=mydb.cursor();
        c.execute("select * from admin_login")
        for row in c:
            if(row[0]==id and row[2]==password):
                st.session_state['login2']= True;
                break;
        if(st.session_state['login2']==False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state['login2']==True):
        st.subheader("login Succesful")
        with open("animation_lkgteqzg.json") as source:
            animation=json.load(source)
        st_lottie(animation)
        choice2=st.selectbox("Features",("None", "ADD EMPLOYEE DETAILS", "JOB DESCRIPTION", "COMPANY PRODUCTION"))
        if(choice2=="ADD EMPLOYEE DETAILS"):
            
            st.markdown("<h1 style= 'text-align:center;color:brown;'>Add Employee</h1>",unsafe_allow_html=True)
            with open("animation_lkgptqjk.json") as source:
                animation=json.load(source)
            st_lottie(animation)
            
            with st.form("form 2"):
                col1,col2=st.columns(2)
                emp_name=col1.text_input("Name")
                emp_id=col2.text_input("id")
                emp_gender=st.radio("gender", options=("MALE", "FEMALE"))
      
                emp_age=st.text_input("age", key="emp_age")
                emp_email=st.text_input("email", key="emp_email")
                address=st.text_input("address", key="address")
                emp_pss=st.text_input("password", key="emp_pss")
                s_state=st.form_submit_button("submit")
                if(s_state):
                    mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                    c=mydb.cursor();
                    c.execute("insert into emp values(%s, %s, %s,%s, %s,  %s,  %s)",(emp_id, emp_name, emp_gender, emp_age, emp_email, address, emp_pss))
                    mydb.commit()
                    st.header("submittted successfully")
            btn9= st.button("Show details")
            if(btn9):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("select * from emp")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['emp_id', 'emp_name', 'emp_gender', 'emp_age', 'emp_email', 'address', 'emp_pss'])
                st.dataframe(df)   

        if(choice2=="COMPANY PRODUCTION"):
            with open("animation_lkim2912.json") as source:
                animation=json.load(source)
            st_lottie(animation)
            st.write("Chart Of GME Stoke Price")
            tickerSymbol = 'GME'
            tickerData = yf.Ticker(tickerSymbol)
            tickerDf = tickerData.history(
                        period='1d',
                        start='2005-5-1',
                        end='2023-5-1')
            st.line_chart(tickerDf.Open)

            st.write("Company gowth in chart form")
            opt=st.radio("Select any graph", options=("Line", "Bar", "H-Bar"))
            if(opt == "Line"):
                st.markdown("<h1 style='text-align: center;'> Line Chart</h1>", unsafe_allow_html=True)
                fig=plt.figure()
                
                plt.plot(x, np.sin(x))
                plt.plot(x, np.cos(x), '--')
                st.write(fig)
            elif(opt=="Bar"):
                st.markdown("<h1 style='text-align: center;'> Bar Chart</h1>", unsafe_allow_html=True)
                fig=plt.figure()
                plt.bar(bar_x,bar_x*10)
                st.write(fig)
            else:
                st.markdown("<h1 style='text-align: center;'> H-Bar Chart</h1>", unsafe_allow_html=True)
                fig=plt.figure()
                plt.barh(bar_x*10, bar_x)
                st.write(fig)
        if(choice2=="JOB DESCRIPTION"):
            with st.form("form 2"):
                col1,col2=st.columns(2)
                job_id=col1.text_input("Enter Job ID")
                dep_name=col2.text_input("Enter Department name")
                descrip=st.text_input("Job Description", key="descrip")
                sal_range=st.text_input("Enter Salary", key="sal_range")
                s_state=st.form_submit_button("submit")
                if(s_state):
                    mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                    c=mydb.cursor();
                    c.execute("insert into job_dep values(%s, %s, %s,%s)",(job_id, dep_name, descrip, sal_range))
                    mydb.commit()
                    st.header("submittted successfully")
            btn9= st.button("Show details")
            if(btn9):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
                c=mydb.cursor();
                c.execute("select * from job_dep")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['job_id', 'dep_name', 'descrip', 'sal_range'])
                st.dataframe(df)            
            
            
elif(choice=='Tech Articles And Information'):
    st.markdown("<h1>Latest Articles and Information</h1>", unsafe_allow_html=True)
    with open("animation_lkgtgih5.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    st.header(":mailbox: Python")
    st.markdown('<iframe src="http://tdc-www.harvard.edu/Python.pdf" width="100%" height="1200px"></iframe>', unsafe_allow_html=True)
    with open("animation_lkgteqzg.json") as source:
        animation=json.load(source)
    st_lottie(animation)
    st.header(":mailbox: Java")
    st.markdown('<iframe src="http://blog.ezyang.com" width="100%" height="1200px"></iframe>', unsafe_allow_html=True)
    st.markdown('<iframe src="http://www.cs.trincoll.edu/~ram/jjj/jjj-os-20170625.pdf" width="100%" height="900px"></iframe>', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=69lvI4tdqss")
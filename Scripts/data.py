import streamlit as st
import mysql.connector
st.title("Application")
emp_id=st.text_input("Enter employee id")
emp_salary=st.text_input("Enter employee salary")
emp_loan=st.selectbox("Do we haave a loan",("No", "yes"))
btn=st.button("submit")
if btn:
    mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo", database="employee2")
    c=mydb.cursor()
    c.execute("insert into info values(%s ,%s, %s)",(emp_id,emp_salary, emp_loan))
    mydb.commit()
    st.header("Data submitted successfully.")
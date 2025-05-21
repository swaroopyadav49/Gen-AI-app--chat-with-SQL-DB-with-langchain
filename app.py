# Here I will create Streamlit app
# Here entire llm application will be created and these llm application should interact with the database.

from dotenv import load_dotenv
load_dotenv()    ## load all the environment varaibles

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## configure our API KEY
genai.configure(api_key=os.getenv("Google_API_KEY"))


# Function to Load Google Gemini Model and provide sql query as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content([prompt[0],question])
    return response.text

## Another Function to retrive the sql from sql_database

def read_sql_query(sql,db):
    print(f"Executing SQL: {sql}")  # Print the SQL for debugging
    conn = sqlite3.connect(db)
    cur=conn.cursor()
    # Only execute the first line, strip whitespace
    sql_line = sql.strip().splitlines()[0]
    try:
        cur.execute(sql_line)
        rows = cur.fetchall()
        conn.commit()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"SQL execution error: {e}")
        return [f"SQL execution error: {e}"]
    finally:
        conn.close()


## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)


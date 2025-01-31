#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install lxml_html_clean')


# In[9]:


get_ipython().system('jupyter nbconvert --to script query_handler.ipynb')


# In[ ]:


def get_sql_query(user_input):
    """Converts user query into an SQL query."""
    doc = nlp(user_input.lower())

    # Identify department names
    department_names = ["sales", "engineering", "marketing"]
    department = next((token.text.capitalize() for token in doc if token.text.lower() in department_names), None)

    # Identify date
    date = next((token.text for token in doc if token.ent_type_ == "DATE"), None)

    # Identify query type
    if "employees" in user_input and department:
        return f"SELECT * FROM Employees WHERE Department = '{department}';"
    
    if "manager" in user_input and department:
        return f"SELECT Manager FROM Departments WHERE Name = '{department}';"
    
    if "hired after" in user_input and date:
        return f"SELECT * FROM Employees WHERE Hire_Date > '{date}';"
    
    if "total salary expense" in user_input and department:
        return f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}';"

    return None

def execute_query(sql):
    """Executes SQL query and fetches results."""
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result


# In[ ]:





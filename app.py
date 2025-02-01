#!/usr/bin/env python
# coding: utf-8

# In[22]:


from flask import Flask, request, jsonify
from query_handler import get_sql_query, execute_query

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Chatbot API! Use the /chat endpoint to send queries."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "No query provided!"}), 400

    sql_query = get_sql_query(user_query)
    
    if sql_query is None:
        return jsonify({"response": "Sorry, I didn't understand the query."})

    result = execute_query(sql_query)
    
    return jsonify({"response": result})

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


# In[ ]:





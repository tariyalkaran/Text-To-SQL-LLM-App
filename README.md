# Text-To-SQL-LLM-App


**Gemini SQL Query Bot**
This project is a Streamlit application that integrates Google Gemini AI (Generative AI) to convert natural language questions into SQL queries and retrieves data from an SQLite database. The application is designed to assist users in querying a STUDENT database with columns such as NAME, CLASS, SECTION, and MARKS.

**Features**
Convert natural language queries into SQL queries using Google Gemini AI.
Retrieve data from an SQLite database based on the generated SQL query.
Real-time responses displayed on the Streamlit interface.

**Technologies Used**
Streamlit: For building the web application interface.
Google Gemini AI: To convert English questions to SQL queries.
SQLite: The database used for storing the student records.
dotenv: For environment variable management, including API keys.
PyPI packages: google.generativeai, dotenv, sqlite3.

**Project Setup**
**Prerequisites**
1. Python 3.x
2 .Google Gemini AI API Key
3. Streamlit
4. SQLite database (student.db)
   
**Installation**

Clone the repository:
```Python
git clone https://github.com/yourusername/Gemini-SQL-Query-Bot.git
```
Install required packages:
```Python
pip install -r requirements.txt
```

Set up environment variables. Create a .env file in the project root and add your Google Gemini API key:
```python
GOOGLE_API_KEY=your_google_gemini_api_key
```

Prepare your SQLite database (student.db) with the following schema:
sql
```sql
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT,
    Date_of_Admission DATE,
    Gender VARCHAR(25)
);
```
Start the Streamlit app:
```Python
streamlit run app.py
```
Input any natural language query related to the STUDENT database. For example:

"How many students are in the Data Science class?"
"What are the names of all the students in section A?"
The app will use Google Gemini AI to convert the question into an SQL query and fetch the relevant data from the student.db SQLite database.

**Example Queries**
How many records are present?
SQL query: SELECT COUNT(*) FROM STUDENT;
Tell me all students studying in the Data Science class.
SQL query: SELECT * FROM STUDENT WHERE CLASS="Data Science";

**Code Structure**
app.py: The main application file which contains the Streamlit code and functions for interacting with Google Gemini AI and the SQLite database.
.env: A file to securely store the API keys (not to be pushed to GitHub).
requirements.txt: Contains all the required dependencies for the project.
License
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
Google Gemini AI: For providing the natural language to SQL conversion capability.
Streamlit: For providing the easy-to-use interface for the application.

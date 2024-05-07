import os
from dotenv import load_dotenv
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv("chekin.env")

# Database connection parameters
username = "root"
password = ""
host = '127.0.0.1'
port = '3306'
mydatabase = "eventinfo"

# MySQL connection string
mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{mydatabase}"

# Initialize the database object
db = SQLDatabase.from_uri(mysql_uri)

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
)

question = "what is the first event name in the table called information in a database eventinfo?"

# Run the agent with the question
agent_executor.run(question)

import os 
from crewai import Crew, Process
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpoint
from utils import *
from agents import agents
from tasks import tasks
load_dotenv(find_dotenv())

# Configuration
os.environ["SERPER_API_KEY"] = "serper_api_key"  # Replace with your Serper API key
os.environ["GROQ_API_KEY"] = "groq_api_key"  # Replace with your Groq API key


# Step 1: Setup LLM (Mistral with HuggingFace)
HF_TOKEN = "HF_token"  # Replace with your Hugging Face token
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

def load_llm(huggingface_repo_id):
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repo_id,
        temperature=0.5,
        task="text-generation",  # Updated task
        model_kwargs={
            "token": HF_TOKEN,
            "max_length": 1024
        }
    )
    return llm

llm=load_llm(HUGGINGFACE_REPO_ID)

#load the llm
#llm = ChatGroq(model="mixtral-8x7b-32768", temperature= 0)

#Provide the innputs

resume = read_all_pdf_pages("CV.pdf")
job_desire = input("Enter Desiring Job: ")

#Creating agents and tasks

job_requirements_researcher, resume_swot_analyser = agents(llm)

research, resume_swot_analysis = tasks(llm, job_desire, resume)

#Building crew and kicking it off
crew = Crew(
    agents = [job_requirements_researcher, resume_swot_analyser],
    tasks=[research, resume_swot_analysis],
    verbose=1,
    process = Process.sequential
)

result = crew.kickoff()
print(result)
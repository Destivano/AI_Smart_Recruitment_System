from crewai import Task
from agents import agents

def tasks(llm, job_desire, resume_content):
    '''
    jpb_requirements_research - find the relevent skills, projects and experience
    resume_swot_analysis- understand the report and the resume based on this make a swot analysis
    '''

    job_requirements_researcher, resume_swot_analyser= agents(llm)

    research = Task(description=f'For Job Position of Desire: {job_desire} research to identify the current market requirements for a person at the job including the relevant skills, some unique research projects or common projects alonf with what experience would be required. For searching query use ACTION INPUT KEY as "search_query"',expected_output = 'A report on what are the skills required and some unique required and some unique real time projectts that can be there which enhaces the chance of a ^person to get a job',agent = job_requirements_researcher)

    resume_swot_analysis = Task(description = f'Resume Content: {resume_content} \n Analyse the resume provided and the report of job_requirements_researcher to provide a detailed SWOT analysis report on the resume along with the Resume Match Percentage and Suggestions to improve',expected_output='A JSON formatted report as follows: "candidate": candidate, "strengths":[strengths], "weaknesses":[weaknesses], "opportunities":[opportunities], "threats":[threats], "resume_match_percentage": resume_match_percentage, "suggestions": "suggestions"',agents = resume_swot_analyser,output_file='resume-report/resume_review.json')
    
    return research, resume_swot_analysis

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()

# Uncomment the following line to use an example of a custom tool
# from ai_latest_development.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class AiLatestDevelopment():
	"""AiLatestDevelopment crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	ollama_llm = LLM(
		model='ollama/mistral',
		base_url='http://localhost:11434',
	)

	@agent
	def body_language_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['body_language_analyst'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=self.ollama_llm
		)

	@agent
	def cheating_detector(self) -> Agent:
		return Agent(
			config=self.agents_config['cheating_detector'],
			verbose=True,
			llm=self.ollama_llm
		)

	@task
	def body_language_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['body_language_analysis_task'],
		)

	@task
	def cheating_detection_task(self) -> Task:
		return Task(
			config=self.tasks_config['cheating_detection_task'],
			output_file='report.txt'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AiLatestDevelopment crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
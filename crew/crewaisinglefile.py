
from crewai import Agent, Task, Crew
from crewai.process import Process
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ServerBuildAgent = Agent(
                    role = "Builing cloud server end to end",
                    goal = "create a server from AWS  and deploying the application on top of that and integrate with load balancer",
                    backstory = "As an AI assistant I need to build and validate step by step in my system",
                    tools =[],
                    llm = "openai/gpt-4o-mini",
                    verbose = True
                    )

Serverreq_validation = Task (
                            description ="provide step by step validation for building a cloud server on AWS and deploying an application with load balancer integration",
                            expected_output = "A step by step validated procedure to build the server and deploy the application",
                            agent = ServerBuildAgent
   )

Crew = Crew(
    agents = [ServerBuildAgent],
    tasks = [Serverreq_validation],
    process = Process.sequential,
)

result = Crew.kickoff()
print("\n=== FINAL RESULT ===")
print(result)


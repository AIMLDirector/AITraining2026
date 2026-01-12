from crewai import Crew
from tasks.stock_tasks import create_tasks
import os
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file.")

stock = input("Enter the name of the Indian stock to analyze: ")

tasks = create_tasks(stock)

crew = Crew(
    agents=[task.agent for task in tasks],
    tasks=tasks,
    verbose=True
)

result = crew.kickoff()

print("\n===== STOCK ANALYSIS REPORT =====\n")
print(result)

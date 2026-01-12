import os
from dotenv import load_dotenv
from crewai import Crew
from tasks.top10_tasks import create_top10_tasks
from datetime import datetime

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env")

current_year = datetime.now().year

# Create AI tasks (no stock list needed)
tasks = create_top10_tasks()

crew = Crew(
    agents=[task.agent for task in tasks],
    tasks=tasks,
    verbose=True
)

result = crew.kickoff()

print(f"\n===== TOP 10 INDIAN STOCKS FOR {current_year} =====\n")
print(result)
print("\n⚠️ This is educational, not financial advice.")

from crewai import Agent

from dotenv import load_dotenv
load_dotenv()

fundamental_analyst = Agent(
    role="Fundamental Analyst",
    goal="Analyze financial health, revenue, profit, and valuation metrics",
    backstory="Chartered analyst focused on Indian company fundamentals.",
    verbose=True
)

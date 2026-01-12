from crewai import Agent

from dotenv import load_dotenv
load_dotenv()
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide Buy/Sell/Hold recommendation with risk analysis",
    backstory="SEBI-aware advisor focusing on long-term Indian investors.",
    verbose=True
)

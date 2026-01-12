from crewai import Agent

from dotenv import load_dotenv
load_dotenv()

technical_analyst = Agent(
    role="Technical Analyst",
    goal="Analyze price trends, RSI, MACD, support and resistance levels",
    backstory="Trading expert using Indian market technical indicators.",
    verbose=True
)

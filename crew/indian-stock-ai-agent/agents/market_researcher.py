from crewai import Agent

from dotenv import load_dotenv
load_dotenv()
market_researcher = Agent(
    role="Indian Stock Market Researcher",
    goal="Collect recent performance, news, and trends for Indian stocks",
    backstory="Expert in NSE/BSE markets and Indian equities.",
    verbose=True
)

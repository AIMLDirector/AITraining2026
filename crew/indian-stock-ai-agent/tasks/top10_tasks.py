from datetime import datetime
from crewai import Task
from agents.market_researcher import market_researcher
from agents.fundamental_analyst import fundamental_analyst
from agents.technical_analyst import technical_analyst
from agents.investment_advisor import investment_advisor

current_year = datetime.now().year

def create_top10_tasks():
    research = Task(
        description=f"Analyze the Indian stock market trends, sectors, and macro factors for the year {current_year}.",
        expected_output="Market outlook and strong-performing sectors for the current year.",
        agent=market_researcher
    )

    fundamentals = Task(
        description=f"Identify Indian companies with strong fundamentals, earnings growth, and balance sheets for {current_year}.",
        expected_output="List of fundamentally strong Indian companies.",
        agent=fundamental_analyst
    )

    technicals = Task(
        description=f"Analyze technical trends of top Indian stocks to confirm momentum and trend direction for {current_year}.",
        expected_output="Technical trend confirmation of leading stocks.",
        agent=technical_analyst
    )

    recommendation = Task(
        description=f"Based on market trends, fundamentals, and technicals, provide the Top 10 Indian stocks to buy for {current_year} with reasons, expected outlook, and risks.",
        expected_output="Final Top 10 stock list with explanations and risks.",
        agent=investment_advisor
    )

    return [research, fundamentals, technicals, recommendation]

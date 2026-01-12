from crewai import Task
from agents.market_researcher import market_researcher
from agents.fundamental_analyst import fundamental_analyst
from agents.technical_analyst import technical_analyst
from agents.investment_advisor import investment_advisor

def create_tasks(stock_name):
    research = Task(
        description=f"Research recent performance and news for {stock_name} (India).",
        expected_output="A summary of recent news, trends, and market sentiment.",
        agent=market_researcher
    )

    fundamentals = Task(
        description=f"Analyze financials of {stock_name}: revenue, profit, PE, debt, growth.",
        expected_output="Key financial metrics and fundamental health assessment.",
        agent=fundamental_analyst
    )

    technicals = Task(
        description=f"Analyze price chart of {stock_name}: RSI, MACD, trend, support/resistance.",
        expected_output="Technical indicator analysis with trend direction.",
        agent=technical_analyst
    )

    recommendation = Task(
        description=f"Give Buy/Sell/Hold recommendation for {stock_name} with risks.",
        expected_output="Final investment recommendation with risk factors and smart summary with table.",
        agent=investment_advisor
    )

    return [research, fundamentals, technicals, recommendation]

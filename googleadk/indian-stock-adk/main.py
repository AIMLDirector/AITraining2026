import os
from dotenv import load_dotenv
from agents import create_stock_agent
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

current_year = datetime.now().year

model, SYSTEM_PROMPT = create_stock_agent(API_KEY)

prompt = f"""
{SYSTEM_PROMPT}

Now provide the Top 10 Indian stocks to buy for {current_year}.
Include:
- Sector
- Reason
- Expected outlook
- Key risks
"""

response = model.generate_content(prompt)

print(f"\n===== TOP 10 INDIAN STOCKS FOR {current_year} =====\n")
print(response.text)
print("\n⚠️ This is educational, not financial advice.")

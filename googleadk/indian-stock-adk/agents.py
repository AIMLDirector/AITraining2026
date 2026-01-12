from google import genai
from datetime import datetime

current_year = datetime.now().year

SYSTEM_PROMPT = f"""
You are an expert Indian stock market analyst.

Your task:
1. Analyze Indian market trends for {current_year}
2. Identify strong sectors
3. Select the Top 10 Indian stocks for a 1-year investment horizon
4. Provide reasons, expected outlook, and risks

Rules:
- No predefined stock list
- Use general market knowledge
- Focus on fundamentals + trends + momentum
- Add a disclaimer
"""

def create_stock_agent(api_key):
    client = genai.Client(api_key=api_key)
    model = client.models.get(model="gemini-1.5-pro")
    return model, SYSTEM_PROMPT

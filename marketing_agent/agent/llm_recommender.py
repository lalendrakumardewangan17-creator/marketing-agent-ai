import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_recommendation(campaign, insights):
    prompt = f"""
You are a Google Ads expert.
Campaign: {campaign}
Issues: {insights}

Generate clear optimization recommendations.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

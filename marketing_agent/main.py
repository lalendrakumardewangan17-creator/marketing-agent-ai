import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent.data_loader import load_data
from agent.kpi_analyzer import calculate_kpis
from agent.decision_engine import analyze_campaign
from agent.llm_recommender import generate_recommendation





df = load_data("data/google_ads_sample.csv")
df = calculate_kpis(df)

for _, row in df.iterrows():
    insights = analyze_campaign(row)
    if insights:
        recommendation = generate_recommendation(row["Campaign"], insights)
        print(f"\n📌 Campaign: {row['Campaign']}")
        print(recommendation)
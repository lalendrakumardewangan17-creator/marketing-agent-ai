import streamlit as st
import pandas as pd
from data_loader import load_data
from decision_engine import analyze_campaign
from kpi_analyzer import calculate_kpis
from llm_recommender import generate_recommendation


st.set_page_config(
    page_title="Google Ads Agentic AI",
    layout="wide"
)

st.title("🤖 Google Ads Agentic AI Dashboard")
st.write("Upload Google Ads data and get AI-powered optimization recommendations.")

# File upload
uploaded_file = st.file_uploader("Upload Google Ads CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = calculate_kpis(df)

    st.subheader("📊 Campaign Performance Data")
    st.dataframe(df)

    if st.button("🔍 Analyze Campaigns"):
        st.subheader("🧠 AI Optimization Recommendations")

        for _, row in df.iterrows():
            insights = analyze_campaign(row)
            if insights:
                recommendation = generate_recommendation(
                    row["Campaign"], insights
                )

                with st.expander(f"📌 {row['Campaign']}"):
                    st.markdown(recommendation)
            else:
                with st.expander(f"📌 {row['Campaign']}"):
                    st.write("✅ Campaign is performing well. No action needed.")

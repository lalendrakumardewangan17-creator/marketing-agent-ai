def calculate_kpis(df):
    df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100
    df["CPC"] = df["Cost"] / df["Clicks"]
    df["CPA"] = df["Cost"] / df["Conversions"]
    return df
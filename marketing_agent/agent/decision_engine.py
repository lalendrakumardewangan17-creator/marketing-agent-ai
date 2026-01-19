def analyze_campaign(row):
    insights = []

    if row["CTR"] < 2:
        insights.append("Low CTR – improve ad copy or keywords")

    if row["CPC"] > 100:
        insights.append("High CPC – optimize bids")

    if row["CPA"] > 1500:
        insights.append("High CPA – pause or refine targeting")

    if row["Conversions"] > 20:
        insights.append("High performer – consider increasing budget")

    return insights
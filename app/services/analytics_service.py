import pandas as pd

def perform_analysis(historical_data):
    df = pd.DataFrame(historical_data)
    insights = {
        "mean_close": df['Close'].mean(),
        "max_close": df['Close'].max(),
        "min_close": df['Close'].min(),
        "volatility": df['Close'].std()
    }
    return insights

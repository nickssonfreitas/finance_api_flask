import yfinance as yf

def get_company_info(symbol):
    ticker = yf.Ticker(symbol)
    return ticker.info

def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return data.iloc[-1].to_dict()

def get_historical_data(symbol, start_date, end_date):
    ticker = yf.Ticker(symbol)
    data = ticker.history(start=start_date, end=end_date)
    return data.reset_index().to_dict(orient='records')

from app import app
from flask import jsonify, request
from app.services.yahoo_finance_service import get_company_info, get_stock_data, get_historical_data
from app.services.analytics_service import perform_analysis

@app.route('/company_information/<symbol>', methods=['GET'])
def company_information(symbol):
    data = get_company_info(symbol)
    return jsonify(data)

@app.route('/stock_market_data/<symbol>', methods=['GET'])
def stock_market_data(symbol):
    data = get_stock_data(symbol)
    return jsonify(data)

@app.route('/data_historial_market', methods=['POST'])
def data_historial_market():
    request_data = request.get_json()
    symbol = request_data.get('symbol')
    start_date = request_data.get('start_date')
    end_date = request_data.get('end_date')
    data = get_historical_data(symbol, start_date, end_date)
    return jsonify(data)

@app.route('/analytical_insights', methods=['POST'])
def analytical_insights():
    request_data = request.get_json()
    symbol = request_data.get('symbol')
    start_date = request_data.get('start_date')
    end_date = request_data.get('end_date')
    historical_data = get_historical_data(symbol, start_date, end_date)
    insights = perform_analysis(historical_data)
    return jsonify(insights)

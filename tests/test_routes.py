import pytest
from app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_company_information(client):
    response = client.get('/company_information/AAPL')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'address1' in data

def test_stock_market_data(client):
    response = client.get('/stock_market_data/GOOG')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'Close' in data

def test_data_historial_market(client):
    payload = {
        'symbol': 'MSFT',
        'start_date': '2023-01-01',
        'end_date': '2023-01-31'
    }
    response = client.post('/data_historial_market', json=payload)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_analytical_insights(client):
    payload = {
        'symbol': 'AMZN',
        'start_date': '2023-01-01',
        'end_date': '2023-01-31'
    }
    response = client.post('/analytical_insights', json=payload)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'max_close' in data
    assert 'mean_close' in data
    assert 'min_close' in data
    assert 'volatility' in data

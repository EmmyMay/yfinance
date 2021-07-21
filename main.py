from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import pandas as pd
from datetime import datetime
app = Flask(__name__)
CORS(app)
api = Api(app)
import yfinance as yf

aapl = yf.Ticker('aapl')

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]



class StockPrice(Resource):
    def get(self):
        return {"data": get_current_price('AAPL')}

api.add_resource(StockPrice, "/stockprice")



if __name__ == "__main__":
    app.run(debug=True)
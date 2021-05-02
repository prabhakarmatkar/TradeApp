# TradeApp

This is the server side socket io based inplementation to get stock price data from nse.

It provide continous updates on the stock prices with the interval of 1sec.

To consume the data at client, socket.io-client is recommended for the use.


## Set up guide

Inorder to make the backend server up and running please install the below packages:

pip install nsetools
pip install nsetools --upgrade
pip install python-socketio
pip install gunicorn

### To run the project

gunicorn --reload --thread 50 main:app


#### Thank You.

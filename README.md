# interactive_crypto_portfolio_analyzer
crypto_currency_portfolio_analyzer

Interactive Crypto Portfolio Analyzer and Arbitrage Dectection


User Stories:

- This project will analyze the risk indicators  of several crypto currencies traded on several crypto exchanges to uncover patterns in the crypto market. To do so the following tasks are performed: 
	- Calculate the daily returns of a stock traded on seevral exchanges
	- Analyze the volatility of each of the stocks listed on in the desired ETF
	- Evaluate the risk profile of each stock by using the standard deviation and the beta
	- Calculate the Sharpe ratios for each portfolio to determine the risk-retun profile.
	
- It offers an interactive menu to allow the user to select:
	- The choice of risk indicator (standard deviation, beta, daily returns and sharpe ratio) based on an 180 days rolling window
	- The choice of one ten crypto currency to analyse
		BTC - Bitcoin
		XRP - XRP Ledger
		ETH - Ether
		BCH - Bitcoin Cash
		LTC - Litecoin
		EOS - EOS
		XMR - Monero
		XLM - Stellar Lumens 
		ADA - Cardano
		XTZ - Tezos
		
	- The crypto currency closing value are compared on five crypto exchanges: Coinbase,Bittrex,Bitstamp,Kraken,Gemini

Data Collection and Preparation
	- Historical crypto data is collected from a CSV file
	- The data contains an hourly market data for ten crypto currencies on five different exchanges from 2014-2019.
	- A limited set of data is cleaned and prepared for the application using panadas

- Installation
	The following packages are required:
		dash
		plotly
		pandas
		plotly.express
		numpy
		python3
	To install clone the repo and install the required packages
	- To run type the following formt eh comand line: 'python app.py'
		
Usage:
	To run the app:
	- Open a command line and type: python app.py
	- The result on the command line:
		$ python app.py
			Dash is running on http://127.0.0.1:8050/

			* Serving Flask app 'app'
			* Debug mode: on
	Open a browser and connect to http://127.0.0.1:8050/

	Menu navigation:
		- Select a risk indicator
		- Select a crypto currency
		- The grapgh will be updated with the selected options


# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import numpy as np
from utils.daily_returns import daily_returns
from utils.sharpe_ratio import sharpe_ratio
from utils.standard_deviation import standard_deviation
from utils.beta import beta

# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
   
    html.Div(className='row', children='Interactive Crypto Portfolio Analyzer and Arbitrage Dectection',
             style={'border':'3px solid Coral','background':'blue','color':'white','textAlign': 'center', 'background-color': 'black', 'fontSize': 20}),
   
    html.Div(className='row',children=['Select a Risk Indicator:', 
        
        dcc.RadioItems(options=['daily_returns', 'standard_deviation', 'beta', 'sharpe_ratio'],
                       value='daily_returns',
                       inline=True,
                       id='my_radio_buttons_risk_indicator'),
        
        
    ],style={'border':'2px solid Coral','color':'white','textAlign': 'left', 'background-color': 'black','fontSize': 14}),
    
    html.Div(className='row',children=['Select a Crypto Currency:', 
        html.Br(),
        dcc.RadioItems(options=[
                    {'label':'BTC - Bitcoin', 'value':'BTC'},
                    {'label':'XRP - XRP Ledger', 'value':'XRP'},
                    {'label':'ETH - Ether', 'value':'ETH'},
                    {'label':'BCH - Bitcoin Cash','value':'BCH'},
                    {'label':'LTC - Litecoin','value':'LTC'},
                    {'label': 'EOS - EOS','value':'EOS'},
                    {'label': 'XMR - Monero', 'value':'XMR'},
                    {'label':'XLM - Stellar Lumens','value':'XLM'},
                    {'label':'ADA - Cardano','value':'ADA'},
                    {'label':'XTZ - Tezos', 'value':'XTZ'}

                    ],
                       value='BTC',
                       inline=True,
                       id='crypto_selector'),
        
        
    ],style={'border':'2px solid Coral','color':'white','textAlign': 'left', 'background-color': 'black','fontSize': 14}),

    html.Div(className='row', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
            
    ]),
    
])

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    [Input(component_id='my_radio_buttons_risk_indicator', component_property='value'),
    Input(component_id='crypto_selector', component_property='value')]
	
)
def update_graph(value1, value2):
        if value1== 'daily_returns':
           df = daily_returns(180)
           figure=px.line(df,title='Daily Returns - 180 Days Rolling Window')
           figure.update_layout(
               yaxis_title=value2+' Crypto Currency Daily Returns',
               legend_title_text='Crypto Exchanges'    
               )
           return figure       
        if value1== 'sharpe_ratio':
          
           df = sharpe_ratio(value2)
           figure=px.bar(df,title=value2+' Sharpe Ratio - 180 Days Rolling Window')
           figure.update_layout(
               yaxis_title=value2+' Crypto Currency Sharpe Ratio',
               legend_title_text='Crypto Exchanges'    
            )
           return figure
        if value1== 'standard_deviation':
           df = standard_deviation(value2)
           figure=px.bar(df,title='Standard Deviation - 180 Days Rolling Window')
           figure.update_layout(
               yaxis_title=value2+' Crypto Currency Standard Devation',
               legend_title_text='Crypto Exchanges'    
            )
           return figure       
        if value1== 'beta':
           df = beta(value2)
           figure=px.bar(df,title='Beta - 180 Days Rolling Window')
           figure.update_layout(
               yaxis_title='Crypto Currency Beta Value',
               legend_title_text='Crypto Exchanges'    
            )
           return figure
          
           
    
    
        

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
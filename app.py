"""
This is the main executable app
- Build an interactive web GUI with dropdown menu
- Call the processing modules and plot the resulting graph
- Allow user to  interact with the graph
- Provides tooltips for additional description of the axes and data of the graph
"""
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

import numpy as np
from utils.daily_returns import daily_returns
from utils.sharpe_ratio import sharpe_ratio
from utils.standard_deviation import standard_deviation
from utils.arbitrage import arbitrage

# Initialize the app - incorporate css

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Preapre dropdown html layout
risk_dropdown = html.Div(
    [
        html.Label("Select a Risk Indicator", style={"font-weight": "bold"}, htmlFor="risk-dropdown"),
                dbc.Select(options=[
                  {'label':'Arbitrage', 'value':'beta'},
                    {'label':'Daily Returns', 'value':'daily_returns'},
                    {'label':'Standard Deviation', 'value':'standard_deviation'},
                    #{'label':'Beta', 'value':'beta'},
                    {'label':'Sharpe Ratio','value':'sharpe_ratio'}
                    ],
                      value='beta',
  
                       id='risk_indicator'),
    ],                        style=dict(
                    display='inline-block',
                    verticalAlign="middle",
                    horizontalAlign="middle"
            
)),

crypto_dropdown = html.Div(
    [
        html.Label("Select a Crypto Currency", style={"font-weight": "bold"},htmlFor="crypto-dropdown"),
        dbc.Select(options=[
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

                       id='crypto_selector'),
    ],                       style=dict(
                    display='inline-block',
                    verticalAlign="middle",
                    horizontalAlign="middle"
                ),
),

rolling_dropdown = html.Div(
    [
        html.Label("Select a Rolling Window", style={"font-weight": "bold"},htmlFor="rolling-dropdown"),
        dbc.Select(options=[
                    {'label':'1 Day', 'value':'1'},
                    {'label':'7 Days', 'value':'7'},
                    {'label':'30 Days', 'value':'30'},
                    {'label':'180 Days', 'value':'180'}

                    ],
                    value=1,

                       
                       id='rolling_window')
    ],                        style=dict(
                    display='inline-block',
                    verticalAlign="middle",
                    horizontalAlign="middle",
                    
                ),
)



#Prepare title and dropdown seelctors layout
app.layout = dbc.Container(
    [
        html.H2("Interactive Crypto Portfolio Analyzer and Arbitrage Dectection", className="text-center",
             style={'border':'3px solid Coral','background':'blue','color':'white','textAlign': 'center', 'background-color': 'black', 'fontSize': 20}),
        dbc.Row([dbc.Col(risk_dropdown), dbc.Col(crypto_dropdown),dbc.Col(rolling_dropdown)]),
                dbc.Row(dbc.Col(dbc.Card(dcc.Graph(figure={}, id='histo-chart-final'))),style={'border':'6px solid coral','background':'blue','color':'white','textAlign': 'center', 'background-color': 'black', 'fontSize': 20}),
       
    ],
   
       
)

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    [Input(component_id='risk_indicator', component_property='value'), 
    Input(component_id='crypto_selector', component_property='value'),
    Input(component_id='rolling_window', component_property='value')]
	
)
# use callback function to process user input
# value1 = risk indicator
# value2 = crypto seelctor
# value 3 = rolling window selector
def update_graph(value1, value2, value3):
        if value1== 'daily_returns':
           df = daily_returns(value2, value3)
           figure=px.line(df)
           figure.update_layout(
               yaxis_title='<b>'+value2+' Crypto Currency Daily Returns</b>',
               legend_title_text='<b>Crypto Exchanges</b>', 
               title= '<b>'+value2+f' Daily Returns - {value3} Days Rolling Window</b>',
               title_x=0.5,
               font=dict(
                  family="Courier New, monospace",
                  color="RebeccaPurple")    
            )
           return figure       
        if value1== 'sharpe_ratio':
          
           df = sharpe_ratio(value2, value3)
           figure=px.bar(df)
           figure.update_layout(
               yaxis_title='<b>'+value2+' Crypto Currency Sharpe Ratio</b>',
               legend_title_text='<b>Crypto Exchanges</b>', 
               title= '<b>'+value2+f' Sharpe Ratio - {value3} Days Rolling Window</b>',
               title_x=0.5,
               font=dict(
                  family="Courier New, monospace",
                  color="RebeccaPurple")    
            )
           return figure
        if value1== 'standard_deviation':
           df = standard_deviation(value2, value3)
           figure=px.bar(df)
           figure.update_layout(
               yaxis_title='<b>'+value2+' Crypto Currency Standard Deviation</b>',
               legend_title_text='<b>Crypto Exchanges</b>', 
               title= '<b>'+value2+f' Standard Deviation {value3} Days Rolling Window</b>',
               title_x=0.5,
               font=dict(
                  family="Courier New, monospace",
                  color="RebeccaPurple")    
            )
           return figure       
        if value1== 'beta':
           df = arbitrage(value2, value3)
           figure=px.bar(df)
           figure.update_layout(
               yaxis_title='<b>'+value2+' Crypto Currency </b>',
               legend_title_text='<b>Crypto Exchanges</b>', 
               title= '<b>'+value2+f' Arbitrage - Price difference on Exchanges</b>',
               title_x=0.5,
               font=dict(
                  family="Courier New, monospace",
                  color="RebeccaPurple")    
            )
           return figure
          
   
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


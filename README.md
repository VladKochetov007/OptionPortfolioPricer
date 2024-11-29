# OptionPortfolioPricer
Pricer for weighed sum of european vanilla options

## Overview
A web application for pricing and analyzing portfolios of European vanilla options. The tool allows users to:

- Construct option portfolios by combining calls and puts with different strikes and quantities
- Visualize the total portfolio payoff at expiration
- Explore the price surface across different spot prices and times to maturity
- Adjust market parameters like spot price, interest rate, and volatility

<p align="center">
    <img src="image.png" width="400" />
</p>


## Features
- Interactive GUI built with Streamlit
- Real-time portfolio payoff visualization using Plotly
- Price surface heatmaps showing portfolio value sensitivity
- Black-Scholes pricing model for vanilla options
- Ability to add multiple options and clear portfolio

## Usage
The application provides an intuitive interface where you can:
1. Set market parameters in the sidebar
2. Add options to your portfolio using the option constructor
3. View current portfolio composition 
4. Analyze payoff diagram and price surface visualizations

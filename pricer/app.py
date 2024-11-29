import streamlit as st
import numpy as np
from ui.option_constructor import OptionConstructor
from ui.charts import ChartManager
from services.pricing_service import PricingService
from services.payoff_service import PayoffService


def main():
    st.title("Exotic Option Pricer")
    
    # Get market parameters
    S0, r, sigma, T = OptionConstructor.render_market_params()
    
    # Initialize session state
    if 'options' not in st.session_state:
        st.session_state.options = []
    
    # Render option constructor
    new_option = OptionConstructor.render_option_inputs()
    if st.button("Add Option"):
        st.session_state.options.append(new_option)
    
    # Display portfolio
    OptionConstructor.render_portfolio(st.session_state.options)
    
    # Calculate and display visualizations
    if st.session_state.options:
        # Calculate payoff
        S_range = np.linspace(max(0.5*S0, 1), 1.5*S0, 100)
        payoff = PayoffService.calculate_payoff(S_range, st.session_state.options)
        ChartManager.plot_payoff(S_range, payoff)
        
        # Calculate and display price surface
        S_grid = np.linspace(max(0.5*S0, 1), 1.5*S0, 50)
        T_grid = np.linspace(0.1, T, 50)
        price_surface = PricingService.calculate_price_surface(
            st.session_state.options,
            S_grid,
            T_grid,
            r,
            sigma
        )
        ChartManager.plot_heatmap(price_surface, S_grid, T_grid)

if __name__ == "__main__":
    main() 
import streamlit as st
import numpy as np
from ui.option_constructor import OptionConstructor
from ui.charts import ChartManager
from services.pricing_service import PricingService
from services.payoff_service import PayoffService


def main():
    # Set wider layout
    st.set_page_config(layout="wide")
    
    # Custom CSS to increase content width
    st.markdown("""
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Option Portfolio Pricer")
    
    # Create two columns for layout
    left_col, right_col = st.columns([1, 1])
    
    with left_col:
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
        
        # Heatmap resolution slider
        resolution = st.slider(
            "Heatmap Resolution",
            min_value=5,
            max_value=500,
            value=100,
            help="Higher values give more detailed heatmap but may slow down rendering"
        )
        
        # Calculate and display payoff in left column
        if st.session_state.options:
            # Get min and max strikes from portfolio
            strikes = [option['strike'] for option in st.session_state.options]
            min_strike = min(strikes)
            max_strike = max(strikes)
            
            # Calculate price range based on strikes and volatility
            price_range = 1.5 * sigma * max_strike  # 1.5 standard deviations
            S_min = max(min_strike - price_range, 1)  # Ensure positive price
            S_max = max_strike + price_range
            
            # Calculate and display payoff
            S_range = np.linspace(S_min, S_max, 100)
            payoff = PayoffService.calculate_payoff(S_range, st.session_state.options)
            ChartManager.plot_payoff(S_range, payoff)
    
    with right_col:
        # Calculate and display heatmap
        if st.session_state.options:
            # Calculate and display price surface with same price range
            S_grid = np.linspace(S_min, S_max, resolution)
            T_grid = np.linspace(0.1, T, resolution)
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
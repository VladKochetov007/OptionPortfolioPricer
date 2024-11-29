import streamlit as st
import pandas as pd


class OptionConstructor:
    @staticmethod
    def render_market_params() -> tuple[float, float, float, float]:
        st.sidebar.header("Market Parameters")
        S0 = st.sidebar.number_input("Spot Price", min_value=0.1, value=100.0)
        r = st.sidebar.number_input("Risk-free Rate (%)", min_value=-10.0, max_value=100.0, value=5.0) / 100
        sigma = st.sidebar.number_input("Volatility (%)", min_value=0.1, max_value=200.0, value=20.0) / 100
        T = st.sidebar.number_input("Time to Maturity (years)", min_value=0.01, max_value=30.0, value=1.0)
        return S0, r, sigma, T
    
    @staticmethod
    def render_option_inputs() -> dict[str, float]:
        st.header("Option Constructor")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            option_type = st.selectbox("Option Type", ['call', 'put'])
        with col2:
            strike = st.number_input("Strike Price", value=100.0)
        with col3:
            quantity = st.number_input("Quantity", value=1.0, step=0.1)
            
        return {"type": option_type, "strike": strike, "quantity": quantity}
    
    @staticmethod
    def render_portfolio(options: list[dict[str, float]]) -> None:
        if options:
            st.subheader("Current Portfolio")
            df = pd.DataFrame(options)
            st.dataframe(df)
            
            if st.button("Clear Portfolio"):
                st.session_state.options = []
                st.rerun() 
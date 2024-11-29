import streamlit as st


class OptionConstructor:
    """Handles option portfolio construction UI"""
    @staticmethod
    def render_market_params() -> tuple[float, float, float, float]:
        """Render market parameters input widgets"""
        with st.sidebar:
            st.header("Market Parameters")
            S0 = st.number_input("Spot Price", value=100.0, step=1.0)
            r = st.number_input("Risk-free Rate", value=0.05, step=0.01)
            sigma = st.number_input("Volatility", value=0.2, step=0.01)
            T = st.number_input("Time to Maturity", value=1.0, step=0.1)
        return S0, r, sigma, T
    
    @staticmethod
    def render_option_inputs() -> dict[str, any]:
        """Render option parameters input widgets"""
        st.subheader("Add New Option")
        
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
        
        with col1:
            option_type = st.selectbox(
                "Option Type",
                options=['call', 'put'],
                key='option_type',
                label_visibility="collapsed",
                placeholder="Type"
            )
        
        with col2:
            strike = st.number_input(
                "Strike Price",
                value=100.0,
                step=1.0,
                label_visibility="collapsed",
                placeholder="Strike"
            )
        
        with col3:
            quantity = st.number_input(
                "Quantity",
                value=1.0,
                step=1.0,
                label_visibility="collapsed",
                placeholder="Qty"
            )
        
        with col4:
            add_button = st.button("Add", use_container_width=True)
        
        if add_button:
            return {
                'type': option_type,
                'strike': strike,
                'quantity': quantity
            }
        return None
    
    @staticmethod
    def render_portfolio(options: list[dict[str, any]]) -> None:
        """Display current portfolio composition"""
        if options:
            st.subheader("Current Portfolio")
            
            # Create portfolio table
            data = [
                {
                    'Type': opt['type'].capitalize(),
                    'Strike': f"{opt['strike']:.2f}",
                    'Quantity': f"{opt['quantity']:.2f}"
                }
                for opt in options
            ]
            
            st.table(data)
            
            if st.button("Clear Portfolio"):
                st.session_state.options = []
                st.rerun() 
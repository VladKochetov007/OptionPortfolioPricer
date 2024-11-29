import streamlit as st


class OptionConstructor:
    """Handles option portfolio construction UI"""
    @staticmethod
    def render_market_params() -> tuple[float, float, float, float]:
        """Render market parameters input widgets"""
        with st.sidebar:
            st.header("Market Parameters")
            S0 = st.number_input("Spot Price", value=100.0, step=1.0)
            
            # Convert percentages to decimals
            r_percent = st.number_input(
                "Risk-free Rate (%)", 
                value=5.0,
                step=1.0,
                min_value=-10.0,
                max_value=100.0,
                help="Annual risk-free interest rate in percent"
            )
            r = r_percent / 100.0
            
            sigma_percent = st.number_input(
                "Volatility (%)", 
                value=20.0,
                step=1.0,
                min_value=1.0,
                max_value=200.0,
                help="Annual volatility in percent"
            )
            sigma = sigma_percent / 100.0
            
            T = st.number_input(
                "Time to Maturity (years)", 
                value=1.0,
                step=0.1,
                min_value=0.01,
                max_value=30.0,
                help="Time to expiration in years"
            )
            
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
            
            # Create portfolio table with delete buttons
            for idx, opt in enumerate(options):
                col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
                
                with col1:
                    st.text(opt['type'].capitalize())
                with col2:
                    st.text(f"{opt['strike']:.2f}")
                with col3:
                    st.text(f"{opt['quantity']:.2f}")
                with col4:
                    if st.button("🗑️", key=f"delete_{idx}", use_container_width=True):
                        st.session_state.options.pop(idx)
                        st.rerun()
            
            # Add clear all button below the table
            if st.button("Clear Portfolio", use_container_width=True):
                st.session_state.options = []
                st.rerun() 
import streamlit as st
from ui.layout_manager import LayoutManager
from ui.option_constructor import OptionConstructor
from ui.charts import ChartManager
from services.pricing_service import PricingService
from services.payoff_service import PayoffService
from services.calculation_service import CalculationService
from state.app_state import AppState


class OptionPricerApp:
    """Main application class"""
    def __init__(self):
        self.layout = LayoutManager()
        self.calc_service = CalculationService()
    
    def render_left_column(self, left_col: st.delta_generator.DeltaGenerator) -> tuple:
        with left_col:
            # Market parameters
            S0, r, sigma, T = OptionConstructor.render_market_params()
            
            # Option constructor
            new_option = OptionConstructor.render_option_inputs()
            if new_option:
                AppState.add_option(new_option)
            
            # Portfolio display
            OptionConstructor.render_portfolio(AppState.get_options())
            
            # Resolution control
            resolution = st.slider(
                "Heatmap Resolution",
                min_value=5,
                max_value=1000,
                value=100,
                help="Higher values give more detailed heatmap but may slow down rendering"
            )
            
            # Initialize price bounds
            S_min, S_max = S0 * 0.5, S0 * 1.5  # Default bounds if no options
            
            # Payoff visualization
            if AppState.get_options():
                # Update bounds based on portfolio
                S_min, S_max = self.calc_service.calculate_price_bounds(
                    AppState.get_options(), 
                    sigma
                )
                S_range = self.calc_service.create_grids(S_min, S_max, T, 100)[0]
                payoff = PayoffService.calculate_payoff(S_range, AppState.get_options())
                ChartManager.plot_payoff(S_range, payoff)
            
            return resolution, S_min, S_max, r, sigma, T
    
    def render_right_column(
        self,
        right_col: st.delta_generator.DeltaGenerator,
        params: tuple
    ) -> None:
        resolution, S_min, S_max, r, sigma, T = params
        
        with right_col:
            if AppState.get_options():
                S_grid, T_grid = self.calc_service.create_grids(
                    S_min, S_max, T, resolution
                )
                price_surface = PricingService.calculate_price_surface(
                    AppState.get_options(),
                    S_grid,
                    T_grid,
                    r,
                    sigma
                )
                ChartManager.plot_heatmap(price_surface, S_grid, T_grid)
    
    def run(self) -> None:
        """Main application entry point"""
        # Initialize application state
        AppState.initialize()
        
        # Setup page layout
        self.layout.setup_page()
        
        # Create main columns
        left_col, right_col = self.layout.create_columns()
        
        # Render columns
        params = self.render_left_column(left_col)
        self.render_right_column(right_col, params)


if __name__ == "__main__":
    app = OptionPricerApp()
    app.run()

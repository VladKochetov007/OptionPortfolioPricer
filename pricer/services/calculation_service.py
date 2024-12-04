import numpy as np

class CalculationService:
    """Handles all numerical calculations"""
    @staticmethod
    def calculate_price_bounds(
        options: list[dict[str, any]], 
        sigma: float
    ) -> tuple[float, float]:
        strikes = [option['strike'] for option in options]
        min_strike = min(strikes)
        max_strike = max(strikes)
        
        price_range = 1.5 * sigma * max_strike  # 1.5 standard deviations
        S_min = max(min_strike - price_range, 1)  # Ensure positive price
        S_max = max_strike + price_range
        
        return S_min, S_max
    
    @staticmethod
    def create_grids(
        S_min: float,
        S_max: float,
        T: float,
        resolution: int
    ) -> tuple[np.ndarray, np.ndarray]:
        S_grid = np.linspace(S_min, S_max, resolution)
        T_grid = np.linspace(0, T, resolution)
        return S_grid, T_grid
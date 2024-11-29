import numpy as np
from typing import List, Dict
from models.vanilla_option import VanillaOption


class PricingService:
    @staticmethod
    def calculate_price_surface(
        options: List[Dict],
        S_grid: np.ndarray,
        T_grid: np.ndarray,
        r: float,
        sigma: float
    ) -> np.ndarray:
        """Calculate price surface for multiple options"""
        S_mesh, T_mesh = np.meshgrid(S_grid, T_grid)
        price_surface = np.zeros_like(S_mesh)
        
        for i in range(len(T_grid)):
            for j in range(len(S_grid)):
                total_price = 0
                for opt in options:
                    vanilla = VanillaOption(
                        S=S_grid[j],
                        K=opt['strike'],
                        T=T_grid[i],
                        r=r,
                        sigma=sigma,
                        option_type=opt['type']
                    )
                    total_price += vanilla.price() * opt['quantity']
                price_surface[i,j] = total_price
                
        return price_surface 
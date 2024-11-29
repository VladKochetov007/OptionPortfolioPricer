import torch
from torch.distributions import Normal
import numpy as np

normal = Normal(0, 1)

class PricingService:
    @staticmethod
    def calculate_price_surface(
        options: list[dict[str, float]],
        S_grid: np.ndarray,
        T_grid: np.ndarray,
        r: float,
        sigma: float
    ) -> np.ndarray:
        """Calculate price surface for multiple options using PyTorch"""
        # Convert numpy arrays to torch tensors
        S_grid_t = torch.from_numpy(S_grid).float()
        T_grid_t = torch.from_numpy(T_grid).float()
        
        # Create meshgrid with torch
        S_mesh, T_mesh = torch.meshgrid(S_grid_t, T_grid_t, indexing='xy')
        price_surface = torch.zeros_like(S_mesh)
        
        # Vectorized computation for each option
        for opt in options:
            K = torch.tensor(opt['strike']).float()
            quantity = opt['quantity']
            
            # Calculate d1 and d2 for entire mesh
            d1 = (torch.log(S_mesh/K) + (r + 0.5*sigma**2)*T_mesh) / (sigma*torch.sqrt(T_mesh))
            d2 = d1 - sigma*torch.sqrt(T_mesh)
            
            if opt['type'] == 'call':
                option_price = (S_mesh * normal.cdf(d1) - 
                              K * torch.exp(-r*T_mesh) * normal.cdf(d2))
            else:  # put
                option_price = (K * torch.exp(-r*T_mesh) * normal.cdf(-d2) - 
                              S_mesh * normal.cdf(-d1))
            
            price_surface += option_price * quantity
        
        # Convert back to numpy for plotting
        return price_surface.numpy()
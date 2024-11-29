from dataclasses import dataclass
import torch
from torch.distributions import Normal

normal = Normal(0, 1)

@dataclass
class VanillaOption:
    """Class for vanilla option pricing using Black-Scholes model"""
    S: float      # Spot price
    K: float      # Strike price
    T: float      # Time to maturity
    r: float      # Risk-free rate
    sigma: float  # Volatility
    option_type: str = 'call'
    
    def d1(self) -> torch.Tensor:
        return (torch.log(self.S/self.K) + (self.r + 0.5*self.sigma**2)*self.T) / (self.sigma*torch.sqrt(torch.tensor(self.T)))
    
    def d2(self) -> torch.Tensor:
        return self.d1() - self.sigma*torch.sqrt(torch.tensor(self.T))
    
    def price(self) -> float:
        if self.option_type == 'call':
            return (self.S * normal.cdf(self.d1()) - 
                   self.K * torch.exp(-self.r*self.T) * normal.cdf(self.d2())).item()
        else:  # put
            return (self.K * torch.exp(-self.r*self.T) * normal.cdf(-self.d2()) - 
                   self.S * normal.cdf(-self.d1())).item() 
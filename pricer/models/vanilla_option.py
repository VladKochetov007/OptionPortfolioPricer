from dataclasses import dataclass
from scipy.stats import norm
import numpy as np


@dataclass
class VanillaOption:
    """Class for vanilla option pricing using Black-Scholes model"""
    S: float  # Spot price
    K: float  # Strike price
    T: float  # Time to maturity
    r: float  # Risk-free rate
    sigma: float  # Volatility
    option_type: str = 'call'
    
    def d1(self) -> float:
        return (np.log(self.S/self.K) + (self.r + 0.5*self.sigma**2)*self.T) / (self.sigma*np.sqrt(self.T))
    
    def d2(self) -> float:
        return self.d1() - self.sigma*np.sqrt(self.T)
    
    def price(self) -> float:
        if self.option_type == 'call':
            return self.S*norm.cdf(self.d1()) - self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2())
        else:  # put
            return self.K*np.exp(-self.r*self.T)*norm.cdf(-self.d2()) - self.S*norm.cdf(-self.d1()) 
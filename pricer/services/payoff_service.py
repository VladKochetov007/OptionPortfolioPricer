import numpy as np


class PayoffService:
    @staticmethod
    def calculate_payoff(S: np.ndarray, options: list[dict[str, float]]) -> np.ndarray:
        """Calculate total payoff for a combination of options"""
        total_payoff = np.zeros_like(S)
        for opt in options:
            if opt['type'] == 'call':
                payoff = np.maximum(S - opt['strike'], 0)
            else:  # put
                payoff = np.maximum(opt['strike'] - S, 0)
            total_payoff += payoff * opt['quantity']
        return total_payoff 
"""FinRL-Trading: Reinforcement Learning for Stock Trading.

A fork of AI4Finance-Foundation/FinRL-Trading with enhancements
for production-grade algorithmic trading using deep RL agents.

Personal fork notes:
- Using this to experiment with PPO/SAC agents on crypto data
- See notebooks/ for my custom backtesting experiments
"""

__version__ = "0.1.0"
__author__ = "FinRL-Trading Contributors"
__license__ = "MIT"

from finrl_trading.config import settings

__all__ = ["settings"]

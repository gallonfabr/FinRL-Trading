
<div align="center">

# FinRL-X

### An AI-Native Modular Infrastructure for Quantitative Trading

<img src="https://github.com/user-attachments/assets/80fe89bb-fb09-4267-b29a-76030512f8cf" width="420">

[![Paper](https://img.shields.io/badge/Paper-arXiv_2603.21330-b31b1b?style=for-the-badge)](https://arxiv.org/abs/2603.21330)
&nbsp;
[![PyPI](https://img.shields.io/badge/PyPI-finrl--trading-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/finrl-trading/)

[![Python 3.11](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
![License](https://img.shields.io/github/license/AI4Finance-Foundation/FinRL-Trading.svg?color=brightgreen)
[![Downloads](https://static.pepy.tech/badge/finrl-trading)](https://pepy.tech/project/finrl-trading)
[![Downloads](https://static.pepy.tech/badge/finrl-trading/week)](https://pepy.tech/project/finrl-trading)
[![Join Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/trsr8SXpW5)

![](https://img.shields.io/github/issues-raw/AI4Finance-Foundation/FinRL-Trading?label=Issues)
![](https://img.shields.io/github/issues-pr-raw/AI4Finance-Foundation/FinRL-Trading?label=PRs)
![Visitors](https://api.visitorbadge.io/api/VisitorHit?user=AI4Finance-Foundation&repo=FinRL-Trading&countColor=%23B17A)

*A deployment-consistent trading system that unifies data processing, strategy composition, backtesting, and broker execution through a weight-centric interface.*

[Paper](https://arxiv.org/abs/2603.21330) | [Quick Start](#quick-start) | [Strategies](#strategies) | [Results](#results) | [Discord](https://discord.gg/trsr8SXpW5)

</div>

---

> **Personal fork note:** I'm using this for learning purposes — mainly exploring the backtesting pipeline and the weight-centric architecture. Upstream repo: [AI4Finance-Foundation/FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading).
>
> **My focus areas:**
> - Understanding how portfolio weight vectors flow through the execution pipeline
> - Experimenting with custom data sources (Yahoo Finance + Alpaca)
> - Notes/findings tracked in [`NOTES.md`](./NOTES.md)
>
> **Local setup reminder:** activate venv with `source .venv/bin/activate` before running any scripts; `.env` holds Alpaca paper-trading keys (not committed).
>
> **Useful commands I keep forgetting:**
> - Sync with upstream: `git fetch upstream && git merge upstream/main`
> - Run backtest on sample data: `python examples/backtest_demo.py --config configs/sample.yaml`

## About

**FinRL-X** is a next-generation, **AI-native** quantitative trading infrastructure that redefines how researchers and practitioners build, test, and deploy algorithmic trading strategies. 

Introduced in our paper *"FinRL-X: An AI-Native Modular Infrastructure for Quantitative Trading"* ([arXiv:2603.21330](https://arxiv.org/abs/2603.21330)), FinRL-X succeeds the original [FinRL](https://github.com/AI4Finance-Foundation/FinRL) framework with a fully modernized architecture designed for the LLM and agentic AI era.

> FinRL-X is **not just a library** — it is a full-stack trading platform engineered around modularity, reproducibility, and pr

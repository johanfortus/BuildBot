# BuildBot: Fortnite Reinforcement Learning Agent

BuildBot is a group project for CAP4621: Artificial Intelligence that trains an AI to play Fortnite using reinforcement learning, computer vision, and behavior cloning.

The system captures the game screen in real time, sends actions to the player character, and learns from reward signals extracted from gameplay.

## Setup

Before starting:

- Install **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)**

Clone the repository
```bash
git clone https://github.com/johanfortus/BuildBot
cd BuildBot
```

Create the conda environment
```bash
conda create -n buildbot python=3.11
conda activate buildbot
```

Install dependencies
```bash
pip install -r requirements.txt
```

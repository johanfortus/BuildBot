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

## Training

### PPO (Proximal Policy Optimization)

Train the agent using PPO reinforcement learning:

```bash
python -m agent.train.train_ppo
```

The training will:
- Run for 1,000,000 timesteps by default
- Save the model to `models/buildbot_ppo` on completion or interruption (Ctrl+C)
- Log training metrics to `./logs` for TensorBoard visualization

To view training progress with TensorBoard:
```bash
tensorboard --logdir ./logs
```

### Behavior Cloning

*Currently in development.*

---

**Training Tips:**
- Press `CTRL + C` during training to safely stop and save the current model
- Models are automatically saved to the `models/` directory

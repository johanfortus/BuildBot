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

To use the RL agent within our provided environments, follow the environment setup instructions here:

➡️ **[uefn/README.md](uefn/README.md)**  

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

## Fortnite Settings

To ensure consistent computer-vision detection and reward tracking,
Fortnite must run using the following graphics settings:

**Resolution:** 1920 x 1080  
**Rendering Mode:** DirectX12  
**Brightness:** 100%  
**User Interface Contrast:** 1x  
**Color Blind Mode:** Off  
**Color Blind Strength:** 5  
**Anti-Aliasing & Super Resolution:** NVIDIA DLSS  
**Global Illumination:** Ambient Occlusion  
**Reflections:** Screen Space  
**Shadows:** High  
**View Distance:** Epic  
**Textures:** High  
**Effects:** High  
**Post Processing:** Medium  
**HUD Scale:** 100%  

If your Fortnite colors differ or detection seems off,
you can tune HSV thresholds using the tools inside:

➡️ **[vision/README.md](vision/README.md)**  
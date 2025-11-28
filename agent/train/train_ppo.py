from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from agent.env.fortnite_env import FortniteEnv


def main():
    env = make_vec_env(FortniteEnv, n_envs=1)

    model = PPO(
        "CnnPolicy",
        env,
        verbose=1,
        tensorboard_log="./logs",
        n_steps=2048,
        batch_size=64,
        learning_rate=2.5e-4
    )

    try:
        model.learn(total_timesteps=1_000_000)
    except KeyboardInterrupt:
        print("Training interrupted, saving model...")
    
    model.save("models/buildbot_ppo")


if __name__ == "__main__":
    main()

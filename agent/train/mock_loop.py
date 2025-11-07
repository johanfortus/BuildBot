import time
from agent.env.fortnite_env import BuildBotEnv

def run_mock_training(episodes=5):
    env = BuildBotEnv()

    for episode in range(episodes):
        obs, _ = env.reset()
        done = False
        total_reward = 0.0
        step = 0

        print(f"\n[Episode {episode + 1}] starting...")

        while not done:
            action = env.action_space.sample()
            obs, reward, terminated, truncated, _ = env.step(action)
            total_reward+=reward
            step+=1

            print(
                f"step = {step:02d} | action={action}"
                f"reward={reward:.1f} | total={total_reward:.1f}"
            )

            done = terminated or truncated
            time.sleep(0.05)

        print(f"Episode {episode + 1} finished with reward {total_reward:.2f}")

if __name__ == "__main__":
    run_mock_training()
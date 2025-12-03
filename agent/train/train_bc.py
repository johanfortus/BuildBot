from imitation.algorithms.bc import BC
import numpy as np
import os



def train_bc_agent():

    log_folder = './logs_bc'


    for subdir in os.listdir(log_folder):
        subdir_path = os.path.join(log_folder, subdir)

        if os.path.isdir(subdir_path):
            try:
                states = np.load(os.path.join(subdir_path, 'states.npy'))
                actions = np.load(os.path.join(subdir_path, 'actions.npy'))

                min_len = min(len(states), len(actions))
                states = states[:min_len]
                actions = actions[:min_len]

                print(f"Loaded {subdir} with {len(states)} states and {len(actions)} actions.")

                model = BC(
                    "CnnPolicy",
                    None,
                    dataset=(states, actions),
                    verbose=1,
                    tensorboard_log="./logs_bc",
                )


                try:
                    model.learn(total_timesteps=1_000_000)
                except KeyboardInterrupt:
                    print("Exiting BC learning early")

                model.save("models/buildbot_bc")


            except Exception as e:
                print(f"Error loading data from {subdir_path}")





if __name__ == "__main__":
    train_bc_agent()
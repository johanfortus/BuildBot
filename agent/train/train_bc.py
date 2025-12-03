from imitation.algorithms.bc import BC
from gymnasium import spaces
import numpy as np
import os



def train_bc_agent():

    log_folder = './logs_bc'    

    all_states = []
    all_actions = []

    for subdir in os.listdir(log_folder):
        subdir_path = os.path.join(log_folder, subdir)

        if os.path.isdir(subdir_path):
            try:
                states = np.load(os.path.join(subdir_path, 'states.npy'))
                actions = np.load(os.path.join(subdir_path, 'actions.npy'))

                print(f"Loaded {subdir} with {len(states)} states and {len(actions)} actions.")

                all_states.append(states)
                all_actions.append(actions)

            except Exception as e:
                print(f"Error loading data from {subdir_path}")

    all_states = np.concatenate(all_states, axis=0)
    all_actions = np.concatenate(all_actions, axis=0)


    print(f"Shape of all_states: {all_states.shape}")
    print(f"Shape of all_actions: {all_actions.shape}")


    observation_space = spaces.Box(
        low=0, high=255, shape=(all_states.shape[1], 84, 84), 
        dtype=np.uint8
    )

    action_space = spaces.Discrete(3)

    demonstrations = (all_states, all_actions)

    rng = np.random.default_rng()
    

    model = BC(
        observation_space= observation_space,
        action_space= action_space,
        demonstrations= demonstrations,
        rng=rng,
        batch_size = 64,
    )

    print("Starting BC training...")
    try:
        model.train(
            n_batches=10,
            log_interval=10,
            )
    except KeyboardInterrupt:
        print("Exiting BC learning early")

    model.save("models/buildbot_bc")


if __name__ == "__main__":
    train_bc_agent()
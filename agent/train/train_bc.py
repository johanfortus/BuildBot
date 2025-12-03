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

    transitions =   []
    for state, action in zip(all_states, all_actions):
        transition ={
            "obs" : all_states,
            "acts" : all_actions,
            }
        transitions.append(transition)


    observation_space = spaces.Box(
        low=0, high=255, shape=(4, 84, 84), dtype=np.uint8
    )

    action_space = spaces.Discrete(3)

    rng = np.random.default_rng(0)
    

    model = BC(
        observation_space= observation_space,
        action_space= action_space,
        demonstrations= transitions,
        rng=rng,
        batch_size = all_states.shape[0],
    )

    print("Starting BC training...")
    try:
        model.train(
            n_epochs=1
            )
    except Exception as e:
        print("Failed to train", e)

    model.policy.save("models/buildbot_bc_policy")

if __name__ == "__main__":
    train_bc_agent()
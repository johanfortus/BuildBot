from pathlib import Path
import sys

import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator


def find_latest_event_file(log_root: Path) -> Path:
    event_files = sorted(log_root.glob("**/events.out.tfevents.*"))
    if not event_files:
        raise FileNotFoundError(f"No TensorBoard event files found under {log_root}")
    return event_files[-1]


def load_scalar(event_file: Path, tag: str):
    ea = event_accumulator.EventAccumulator(
        str(event_file),
        size_guidance={event_accumulator.SCALARS: 0},
    )
    ea.Reload()

    if tag not in ea.Tags().get("scalars", []):
        raise KeyError(f"Tag '{tag}' not found. Available scalar tags: {ea.Tags().get('scalars', [])}")

    scalars = ea.Scalars(tag)
    if not scalars:
        raise ValueError(f"No scalar data found for tag '{tag}' in {event_file}")

    steps = [s.step for s in scalars]
    values = [s.value for s in scalars]

    start_time = scalars[0].wall_time
    end_time = scalars[-1].wall_time
    duration_seconds = end_time - start_time

    return steps, values, duration_seconds


def main():
    project_root = Path(__file__).resolve().parents[1]
    log_root_base = project_root / "logs"

    # if a run name is provided
    if len(sys.argv) > 1:
        run_name = sys.argv[1]
        log_root = log_root_base / run_name
        print(f"Using run: {run_name} (log root: {log_root})")
    else:
        log_root = log_root_base
        print(f"No run name provided; searching latest event file under {log_root}")

    # For SB3 PPO, episodic reward is usually logged as "rollout/ep_rew_mean"
    tag = "rollout/ep_rew_mean"
    event_file = find_latest_event_file(log_root)
    print(f"Using event file: {event_file}")

    steps, rewards, duration_seconds = load_scalar(event_file, tag)

    # convert duration into hours and minutes
    hours = int(duration_seconds // 3600)
    minutes = int((duration_seconds % 3600) // 60)
    duration_str = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"

    plt.figure(figsize=(8, 4))
    plt.plot(steps, rewards, label=tag)
    plt.xlabel("Training step")
    plt.ylabel("Reward")
    plt.title(f"Episode reward over training\nRun duration: {duration_str}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
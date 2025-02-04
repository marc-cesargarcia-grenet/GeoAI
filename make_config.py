from pathlib import Path

import yaml


def load_yml(filepath):
    """Load data from a YAML file.

    Args:
        filepath (str | Path): The path to the YAML file.

    Returns:
        Dict: The loaded data, or None if the file does not exist.
    """
    filepath = Path(filepath)
    with filepath.open() as f:
        return yaml.safe_load(f)


def save_yml(data, filepath):
    """Save data to a YAML file.

    Args:
        data (Dict): The data to save.
        filepath (str | Path): The file path to save the YAML to.
    """
    filepath = Path(filepath)
    with filepath.open("w") as f:
        yaml.dump(data, f)
    print(f"Data saved to {filepath}.")


# Updat locust file
# Load the Locust model configuration file
locust_cfg_path = "instageo/model/configs/locust.yaml"
# Load the YAML configuration into a dictionary
locust_cfg = load_yml(locust_cfg_path)
# Update the mean and standard deviation values in the configuration
locust_cfg["dataloader"]["mean"] = [
    670.5441284179688,
    1267.7974853515625,
    1772.599365234375,
    2415.69091796875,
    2879.2431640625,
    2337.822509765625,
]
locust_cfg["dataloader"]["std"] = [
    2146.305419921875,
    2203.416259765625,
    2247.03515625,
    2310.74755859375,
    2322.708984375,
    2211.968505859375,
]
# Save the updated configuration back to the YAML file
save_yml(locust_cfg, locust_cfg_path)

"""Configuration loader — loads common.yaml and resolves environment-specific values."""

from pathlib import Path
import yaml


_ROOT_DIR = Path(__file__).resolve().parent.parent
_CONFIG_DIR = _ROOT_DIR / "config"


def load_yaml(path: str | Path) -> dict:
    """Load a single YAML file and return its contents as a dict."""
    filepath = Path(path)
    if not filepath.exists():
        raise FileNotFoundError(f"YAML file not found: {filepath}")
    with open(filepath, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_config(env: str) -> dict:
    """Load ``common.yaml`` and resolve the environment-specific section. """
    config = load_yaml(_CONFIG_DIR / "common.yaml")

    env_section = config.pop("env", {})
    if env not in env_section:
        raise ValueError(
            f"Environment '{env}' not found in common.yaml. "
            f"Available environments: {list(env_section.keys())}"
        )

    config["base_url"] = env_section[env]["base_url"]

    return config


def resolve_env(pytest_config=None) -> str:
    """Fetches the environment from the ``--env`` pytest CLI option."""
    if pytest_config is not None:
        return pytest_config.getoption("--env", default="dev")
    return "dev"

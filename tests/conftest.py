
import os

import pytest

from utils.config_loader import load_config, resolve_env


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Target environment: dev | uat | prod",
    )

@pytest.fixture(scope="session")
def env_config(request):
    """Read --env CLI option and load merged config for the target environment."""
    env = resolve_env(request.config)
    return load_config(env)



@pytest.fixture(scope="function")
def browser_context(env_config, playwright):
    """Launch browser and create a context with stored auth state."""
    auth_file = env_config["auth"]["state_file"]
    browser = playwright.chromium.launch(headless=False)

    context_args = {}
    if os.path.exists(auth_file):
        context_args["storage_state"] = auth_file

    context = browser.new_context(**context_args)
    yield context
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    """Create a new page from the browser context."""
    pg = browser_context.new_page()
    yield pg
    pg.close()
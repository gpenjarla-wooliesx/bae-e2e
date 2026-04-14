import pytest

@pytest.mark.sanity
@pytest.mark.dev
def test_open_dev_url(page, env_config):
    page.goto(env_config["base_url"])
    assert "BAE - An AI Powered QA Bot" in page.title()
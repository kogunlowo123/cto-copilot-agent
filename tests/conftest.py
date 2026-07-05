"""Test configuration for CTO Copilot Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cto-copilot-agent", "category": "Executive"}

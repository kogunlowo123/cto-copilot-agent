"""CTO Copilot Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_evaluate_tech_trends():
    """Test Evaluate emerging technology trends for relevance and readiness."""
    tools = AgentTools()
    result = await tools.evaluate_tech_trends(technologies="test", evaluation_framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_assess_architecture():
    """Test Assess system architecture against quality attributes."""
    tools = AgentTools()
    result = await tools.assess_architecture(system="test", quality_attributes="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_monitor_engineering_metrics():
    """Test Monitor engineering productivity and quality metrics."""
    tools = AgentTools()
    result = await tools.monitor_engineering_metrics(teams="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_tech_debt():
    """Test Track and prioritize technical debt across systems."""
    tools = AgentTools()
    result = await tools.track_tech_debt(systems="test", severity_filter="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.cto_copilot_agent_agent import CtoCopilotAgentAgent
    agent = CtoCopilotAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0

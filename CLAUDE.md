# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Curestry is an advanced, open-source **Agentic AI Application Observability, Monitoring, and Evaluation Framework** written in Python. It provides tracing, visualization, and evaluation capabilities for AI agents, LLM calls, and tool interactions.

## Development Commands

### Installation
```bash
pip install -e .
```

### Testing
```bash
python -m pytest tests/
```

### Code Quality
```bash
# Format code
black agentneo/ --line-length 88

# Sort imports
isort agentneo/ --profile black --line-length 88

# Run linting (if configured)
ruff check agentneo/
```

### Running the Dashboard
```bash
# From Python code
python -c "from curestry import launch_dashboard; launch_dashboard(port=3000)"
```

## Architecture Overview

Curestry follows a modular architecture with these key components:

### Core Modules
- **`curestry/curestry.py`**: Main Curestry class for session and project management
- **`curestry/tracing/tracer.py`**: Central Tracer class that inherits from multiple mixin classes
- **`curestry/evaluation/evaluation.py`**: Evaluation framework for AI agent performance
- **`curestry/server/`**: Flask-based dashboard server
- **`curestry/data/`**: Data models and classes using SQLAlchemy

### Tracing System
The tracing system uses a mixin-based design:
- **`BaseTracer`**: Core tracing functionality
- **`LLMTracerMixin`**: Traces LLM calls (OpenAI, LiteLLM)
- **`ToolTracerMixin`**: Traces tool usage
- **`AgentTracerMixin`**: Traces agent interactions
- **`NetworkTracer`**: Traces network calls
- **`UserInteractionTracer`**: Traces user interactions

### Storage
- Uses SQLite for structured data storage
- JSON logs for detailed trace information
- Data models defined in `curestry/data/data_models.py`

### Evaluation Metrics
Located in `curestry/evaluation/metrics/`:
- Goal Decomposition Efficiency
- Goal Fulfillment Rate
- Tool Call Correctness/Success Rate
- Tool Selection Accuracy
- Tool Usage Efficiency

## Key Patterns

### Decorator-Based Instrumentation
```python
@tracer.trace_llm("my_llm_call")
async def my_llm_function():
    pass

@tracer.trace_tool("my_tool")
def my_tool_function():
    pass

@tracer.trace_agent("my_agent")
def my_agent_function():
    pass
```

### Session and Project Management
```python
neo_session = Curestry(session_name="my_session")
neo_session.create_project(project_name="my_project")
tracer = Tracer(session=neo_session)
```

### Auto-Instrumentation
The tracer can automatically instrument LLM calls from popular libraries when `auto_instrument_llm=True` (default).

## Configuration

### Dependencies
- Core dependencies defined in `pyproject.toml`
- Python 3.9+ required
- Key deps: SQLAlchemy, Flask, OpenAI, LiteLLM, LangChain

### Code Style
- Black formatter with line length 88
- isort for import sorting with black profile
- Uses setuptools for package management

## Important Implementation Notes

1. **Mixin Architecture**: The Tracer class inherits from multiple mixins for different tracing capabilities
2. **Context Variables**: Uses `contextvars` for managing call depth and state
3. **Automatic Patching**: LLM calls are automatically patched when tracer starts
4. **Database Migrations**: SQLAlchemy models auto-create tables on initialization
5. **Dashboard**: Flask-based web interface with CORS support for visualization
6. **Evaluation**: Separate evaluation framework that works with trace data

## Testing Structure

Tests are located in `tests/` directory:
- Unit tests for core functionality
- Data model tests
- Utility function tests

## Documentation

Comprehensive documentation available in `docs/` directory using markdown format, covering:
- Getting started guides
- Core features and architecture
- API reference
- Troubleshooting guides
# Curestry

![GitHub release (latest by date)](https://img.shields.io/github/v/release/rldyourmnd/curestry) ![GitHub stars](https://img.shields.io/github/stars/rldyourmnd/curestry?style=social) ![Issues](https://img.shields.io/github/issues/rldyourmnd/curestry) ![GitHub license](https://img.shields.io/github/license/rldyourmnd/curestry) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/curestry)

**Advanced AI Application Observability, Monitoring, and Evaluation Framework**

Curestry is an open-source framework designed to provide deep insights into your AI agents, Large Language Model (LLM) calls, and tool interactions. Build more efficient, cost-effective, and high-quality AI-driven solutions with comprehensive monitoring and evaluation capabilities.

## ⚡ Why Curestry?

Whether you're a seasoned AI developer or just starting out, Curestry offers robust logging, visualization, and evaluation capabilities to help you debug and optimize your applications with ease.

## 🚀 Key Features

- **Trace LLM Calls**: Monitor and analyze LLM calls from various providers like OpenAI and LiteLLM
- **Trace Agents and Tools**: Instrument and monitor your agents and tools to gain deeper insights
- **Monitor Interactions**: Keep track of tool and agent interactions to understand system behavior
- **Detailed Metrics**: Collect comprehensive metrics on token usage, costs, and execution time
- **Flexible Data Storage**: Store trace data in SQLite databases and JSON log files
- **Simple Instrumentation**: Utilize easy-to-use decorators to instrument your code
- **Interactive Dashboard**: Visualize trace data and execution graphs in a user-friendly dashboard
- **Project Management**: Manage multiple projects seamlessly within the framework
- **Evaluation Tools**: Assess and improve your AI agent's performance with built-in evaluation tools

## 🛠 Requirements

- **Python**: Version 3.9 or higher

## 📦 Installation

Install Curestry effortlessly using pip:

```bash
pip install curestry
```

## 🌟 Quick Start Guide

### 1. Import the Necessary Components

```python
from curestry import Curestry, Tracer, Evaluation, launch_dashboard
```

### 2. Create a Session and Project

```python
neo_session = Curestry(session_name="my_session")
neo_session.create_project(project_name="my_project")
```

### 3. Initialize the Tracer

```python
tracer = Tracer(session=neo_session)
tracer.start()
```

### 4. Instrument Your Code

Wrap your functions with Curestry's decorators to start tracing:

```python
@tracer.trace_llm("my_llm_call")
async def my_llm_function():
    # Your LLM call here
    pass

@tracer.trace_tool("my_tool")
def my_tool_function():
    # Your tool logic here
    pass

@tracer.trace_agent("my_agent")
def my_agent_function():
    # Your agent logic here
    pass
```

### 5. Evaluate your AI Agent's performance

```python
exe = Evaluation(session=neo_session, trace_id=tracer.trace_id)

# Run evaluation metrics
exe.evaluate(metric_list=['goal_fulfillment_rate', 'tool_call_success_rate'])

# Get results
metric_results = exe.get_results()
print(metric_results)
```

### 6. Stop Tracing and Launch the Dashboard

```python
tracer.stop()

launch_dashboard(port=3000)
```

Access the interactive dashboard by visiting `http://localhost:3000` in your web browser.

## 🔧 Advanced Usage

### Project Management

Manage multiple projects with ease:

```python
# List all projects
projects = neo_session.list_projects()

# Connect to an existing project
neo_session.connect_project(project_name="existing_project")
```

### Metrics Evaluation

#### Supported Metrics
1. **Goal Decomposition Efficiency** - Measures how well goals are broken down into actionable steps
2. **Goal Fulfillment Rate** - Evaluates how successfully goals are achieved
3. **Tool Call Correctness Rate** - Assesses accuracy of tool usage
4. **Tool Call Success Rate** - Measures successful tool executions

**Run multiple metrics:**
```python
exe.evaluate(metric_list=['goal_fulfillment_rate', 'tool_call_success_rate'])
```

**Use custom configuration:**
```python
config = {"model": "gpt-4o-mini"}
metadata = {
    "tools": [
        {"name": "flight_price_estimator_tool", "description": "Estimates flight prices"},
        {"name": "currency_converter_tool", "description": "Converts currencies"}
    ]
}
exe.evaluate(metric_list=['tool_call_correctness_rate'], config=config, metadata=metadata)
```

## 📊 Dashboard Features

The Curestry dashboard provides comprehensive insights:

- **Project Overview** - High-level project statistics
- **System Information** - Resource usage and performance data
- **LLM Call Statistics** - Token usage, costs, and response times
- **Tool and Agent Metrics** - Interaction patterns and success rates
- **Execution Graph Visualization** - Visual flow of your application
- **Timeline of Events** - Chronological view of all activities

Launch the dashboard:
```python
neo_session.launch_dashboard(port=3000)
```

## 🛣️ Development Roadmap

| Feature | Status |
|---------|---------|
| **Local Data Storage Improvements** | ✅ Completed |
| **Support for Additional LLMs** | ✅ Completed |
| **Integration with AutoGen** | ✅ Completed |
| **Integration with CrewAI** | ✅ Completed |
| **Integration with Langraph** | ✅ Completed |
| **Tracing User Interactions** | ✅ Completed |
| **Tracing Network Calls** | ✅ Completed |
| **Comprehensive Logging** | ✅ Completed |
| **Custom Agent Orchestration** | ✅ Completed |
| **Multi-Agent Visualization** | ✅ Completed |
| **Performance Bottleneck Detection** | ✅ Completed |
| **Evaluation Metrics** | ✅ Completed |
| **Advanced Error Detection** | 🔄 In Progress |
| **Code Execution Sandbox** | 🔜 Coming Soon |
| **Prompt Caching** | 📝 Planned |
| **Real-Time Guardrails** | 📝 Planned |
| **Security & Jailbreak Detection** | 📝 Planned |
| **VLM Evaluation** | 📝 Planned |

**Legend:** ✅ Completed | 🔄 In Progress | 🔜 Coming Soon | 📝 Planned

## 📚 Documentation

For detailed documentation, visit: [Curestry Documentation](https://curestry.rldyourmnd.dev)

## 🤝 Contributing

We welcome contributions from the community! Whether it's reporting bugs, suggesting new features, or improving documentation, your input is valuable.

- **GitHub Repository**: [rldyourmnd/curestry](https://github.com/rldyourmnd/curestry)
- **Contribution Guidelines**: Check out our [Contribution Guidelines](https://github.com/rldyourmnd/curestry/blob/main/CONTRIBUTING.md)

Join us in making Curestry even better!

## 📄 License

Curestry is released under the GNU General Public License v3.0 (GPLv3). See the [LICENSE](https://github.com/rldyourmnd/curestry/blob/main/LICENSE) file for details.

## 👤 Author

**Danil Silantyev** ([@rldyourmnd](https://github.com/rldyourmnd))
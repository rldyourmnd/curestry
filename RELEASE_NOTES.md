# Curestry v1.2.2 - Initial Release

## 🚀 Welcome to Curestry!

Curestry is a powerful, open-source **Advanced AI Application Observability, Monitoring, and Evaluation Framework**. This initial release provides comprehensive tools for monitoring, evaluating, and optimizing your AI applications.

## ✨ Key Features

### 🔍 Comprehensive Tracing
- **LLM Call Monitoring**: Track calls from OpenAI, LiteLLM, and other providers
- **Agent Tracing**: Monitor agent behaviors and decision-making processes
- **Tool Usage Tracking**: Observe tool interactions and performance
- **Network Call Tracing**: Monitor external API calls and responses

### 📊 Interactive Dashboard
- **Real-time Visualization**: See your AI application flow in real-time
- **Execution Graphs**: Visual representation of agent workflows
- **Performance Metrics**: Comprehensive analytics and insights
- **Timeline Views**: Track events chronologically

### 📏 Built-in Evaluation Metrics
- **Goal Decomposition Efficiency**: Measure how well goals are broken down
- **Goal Fulfillment Rate**: Evaluate success in achieving objectives
- **Tool Call Correctness Rate**: Assess accuracy of tool usage
- **Tool Call Success Rate**: Monitor successful tool executions
- **Tool Selection Accuracy**: Evaluate tool choice effectiveness
- **Tool Usage Efficiency**: Measure optimal tool utilization

### 💾 Flexible Data Storage
- **SQLite Integration**: Local database storage for trace data
- **JSON Export**: Human-readable data export format
- **Project Management**: Organize work across multiple projects
- **Session Tracking**: Maintain context across different runs

### 🔧 Easy Integration
- **Simple Decorators**: `@tracer.trace_llm()`, `@tracer.trace_agent()`, `@tracer.trace_tool()`
- **Auto-Instrumentation**: Automatic LLM call detection
- **Framework Support**: Works with popular AI frameworks

## 🌐 Supported Frameworks

- **AutoGen**: Multi-agent conversation framework
- **CrewAI**: Collaborative AI agent platform  
- **LangGraph**: Graph-based language model workflows
- **OpenAI Swarm**: Multi-agent orchestration
- **Custom Frameworks**: Flexible integration for any AI system

## 🛠 System Requirements

- **Python**: 3.9 or higher
- **Operating Systems**: Windows, macOS, Linux
- **Dependencies**: All included in installation

## 📦 Installation

### From Source (Current)
```bash
git clone https://github.com/rldyourmnd/curestry.git
cd curestry
pip install -e .
```

### Quick Start Example
```python
from curestry import Curestry, Tracer, launch_dashboard

# Initialize session
session = Curestry(session_name="my_session")
session.create_project(project_name="my_project")

# Start tracing
tracer = Tracer(session=session)
tracer.start()

# Your AI code with tracing
@tracer.trace_llm("openai_call")
async def my_llm_function():
    # Your LLM calls here
    pass

@tracer.trace_tool("data_processor")  
def process_data(data):
    # Your tool logic here
    return processed_data

# Stop tracing and launch dashboard
tracer.stop()
launch_dashboard(port=3000)  # Visit http://localhost:3000
```

## 🎯 Use Cases

- **AI Application Development**: Monitor and debug AI workflows
- **Performance Optimization**: Identify bottlenecks and inefficiencies
- **Cost Analysis**: Track LLM usage and associated costs
- **Quality Assurance**: Evaluate AI agent performance systematically
- **Research & Development**: Analyze AI behavior patterns
- **Production Monitoring**: Observe AI systems in live environments

## 📚 What's Included

- **Complete Python Package**: Full framework implementation
- **Interactive Web Dashboard**: React-based visualization interface
- **Comprehensive Documentation**: Guides, examples, and API reference
- **Example Notebooks**: Jupyter notebooks for major frameworks
- **Test Suite**: Unit tests for core functionality
- **Development Tools**: Linting, formatting, and build configurations

## 🔮 Future Roadmap

- **PyPI Package**: Official package distribution
- **Advanced Metrics**: Additional evaluation capabilities
- **Enhanced Visualizations**: More dashboard features
- **API Integrations**: Cloud platform support
- **Performance Optimizations**: Faster tracing and storage
- **Extended Framework Support**: More AI framework integrations

## 🤝 Contributing

We welcome contributions from the community! Whether you're:
- Reporting bugs
- Suggesting features  
- Improving documentation
- Adding framework support
- Optimizing performance

Check out our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## 👤 Author

**Danil Silantyev** ([@rldyourmnd](https://github.com/rldyourmnd))

## 📄 License

GNU General Public License v3.0 (GPLv3) - See [LICENSE](LICENSE) for details.

---

🎉 **Thank you for trying Curestry!** We're excited to see what you build with it.
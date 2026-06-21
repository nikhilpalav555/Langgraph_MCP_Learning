# Agentic LangGraph - MCP Learning

A learning project exploring **LangGraph**, **LLM agents**, and **Model Context Protocol (MCP)** integration. This repository contains examples of building intelligent chatbots with tool-calling capabilities and agentic workflows.

## 📋 Project Overview

This project demonstrates:
- Building agentic AI systems using **LangGraph**
- Integration with **LangChain** and local LLMs via **Ollama**
- **Model Context Protocol (MCP)** servers for tool integration
- Stateful conversation management with memory
- Tool-calling and conditional routing in agent workflows
- Weather service and math computation examples

## 🏗️ Project Structure

```
AgenticLanggraph/
├── main.py                    # Entry point
├── requirements.txt           # Project dependencies
├── pyproject.toml            # Project configuration
├── .gitignore                # Git ignore rules
├── README.md                 # This file
├── BasicChatBot/
│   ├── basic_chatbot.py      # Basic LangGraph chatbot with Tavily search
│   ├── chat_bot_2.py         # Advanced chatbot implementation
│   ├── client.py             # Client for interacting with services
│   ├── mathserver.py         # MCP server for math operations
│   └── weather.py            # MCP server for weather information
└── .venv/                    # Virtual environment
```

## 🛠️ Tech Stack

- **LangGraph** (≥1.2.5) - Agentic graph framework
- **LangChain** (≥1.3.9) - LLM orchestration
- **Ollama** - Local LLM runtime
- **MCP** (≥1.28.0) - Model Context Protocol for tool integration
- **LangChain MCP Adapters** (≥0.3.0) - Bridge between LangChain and MCP
- **Tavily Search** - Search tool integration
- **LangSmith** - Tracing and monitoring
- **Python** ≥3.13

## 📦 Installation

### Prerequisites
- Python 3.13+
- Ollama installed and running locally
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nikhilpalav555/Langgraph_MCP_Learning.git
   cd AgenticLanggraph
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   # Create a .env file in the root directory
   echo "OLLAMA_MODEL=qwen3.5:0.8b" > .env
   echo "TAVILY_API_KEY=your_api_key_here" >> .env
   ```

5. **Ensure Ollama is running:**
   ```bash
   ollama serve
   # In another terminal, pull the model if needed:
   ollama pull qwen3.5:0.8b
   ```

## 🚀 Usage

### Run the main application:
```bash
python main.py
```

### Run the basic chatbot:
```bash
cd BasicChatBot
python basic_chatbot.py
```

### Start MCP servers:

**Weather Server:**
```bash
python weather.py
```

**Math Server:**
```bash
python mathserver.py
```

### Using the client:
```bash
python BasicChatBot/client.py
```

## 📚 Key Components

### LangGraph Agent (basic_chatbot.py)
- Uses **StateGraph** for workflow management
- **State** with message history using `add_messages`
- **ChatOllama** LLM with Tavily search tool
- **ToolNode** for tool execution
- **MemorySaver** for conversation state management

### MCP Servers
- **weather.py**: Weather information tool
- **mathserver.py**: Mathematical operations tool

Both servers use FastMCP for rapid server development.

## 🔧 Configuration

Create a `.env` file in the root directory:
```
OLLAMA_MODEL=qwen3.5:0.8b
TAVILY_API_KEY=your_api_key
```

## 🎯 Learning Resources

This project explores:
- **Agent Patterns**: Tool-calling, routing, memory
- **LangGraph**: State management, workflow graphs
- **MCP Protocol**: Building tool servers
- **Ollama Integration**: Running local LLMs
- **Conversation Management**: Stateful interactions

## ⚠️ Important Notes

- The `.env` file should NOT be committed (already in `.gitignore`)
- Ensure Ollama is running before starting agents
- Some features may require API keys (Tavily)
- Python 3.13+ is required

## 📝 Future Enhancements

- [ ] Advanced multi-tool workflows
- [ ] Integration with more MCP servers
- [ ] Persistent conversation storage
- [ ] Web interface for chatbot
- [ ] Performance optimizations
- [ ] Additional LLM integrations

## 🤝 Contributing

Feel free to fork, modify, and enhance this learning project!

## 📄 License

This project is for educational purposes.

## 👤 Author

Created as part of LangGraph and MCP learning journey.

---

**Happy Learning! 🚀**

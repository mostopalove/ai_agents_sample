# AI Agents Sample Project

A FastAPI-based demonstration project showcasing the implementation of AI agents using OpenAI's agent framework. This project demonstrates how to create, coordinate, and orchestrate multiple AI agents for different tasks.

## 🎯 Main Idea

This project serves as a practical example of building AI agent systems with the following key concepts:

- **Multi-Agent Architecture**: Demonstrates how to create specialized agents for specific tasks
- **Agent Coordination**: Shows how a manager agent can orchestrate multiple specialized agents
- **Tool Integration**: Illustrates how agents can use tools and functions to accomplish tasks
- **API Integration**: Provides RESTful endpoints to interact with AI agents

## 🏗️ Project Structure

```
ai_agents_sample/
├── ai_agents/                 # Translation agents module
│   ├── __init__.py
│   ├── manager_agent.py       # Coordinates translation agents
│   ├── translator_agents.py   # Language-specific translation agents
│   └── routes.py              # Translation API endpoints
├── greeting_agent/            # Greeting agents module
│   ├── __init__.py
│   ├── goodbye_agent.py       # Farewell message agent
│   ├── greeting_agent.py      # Greeting message agent
│   ├── main_agent.py          # Coordinates greeting/goodbye agents
│   └── routes.py              # Greeting API endpoints
├── main.py                    # FastAPI application entry point
├── routes.py                  # Main application routes
└── requirements.txt           # Python dependencies
```

## 🚀 Features

### 1. Translation Agents (`/ai` endpoints)
- **Manager Agent**: Coordinates between different language translation agents
- **Russian Translator**: Specialized agent for English to Russian translation
- **Ukrainian Translator**: Specialized agent for English to Ukrainian translation
- **Endpoint**: `POST /ai/translate` - Translates messages to multiple languages

### 2. Greeting Agents (`/greeting` endpoints)
- **Main Agent**: Coordinates between greeting and goodbye agents
- **Greeting Agent**: Generates friendly greeting messages with cultural variety
- **Goodbye Agent**: Creates appropriate farewell messages
- **Endpoint**: `POST /greeting/say-hi` - Generates context-appropriate greetings

### 3. Core Features
- **FastAPI Integration**: Modern, fast web framework with automatic API documentation
- **Environment Configuration**: Uses dotenv for environment variable management
- **Pydantic Models**: Type-safe request/response handling
- **Modular Design**: Clean separation of concerns with dedicated modules

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **OpenAI Agents**: Framework for creating and managing AI agents
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running FastAPI applications
- **Python 3.8+**: Modern Python features and syntax

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mostopalove/ai_agents_sample
   cd ai_agents_sample
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 Running the Application

1. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application**
   - Main API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

## 📡 API Endpoints

### Main Routes
- `GET /` - Welcome message

### AI Translation Agents
- `POST /ai/translate` - Translate messages using coordinated agents
  ```json
  {
    "message": "Hello, how are you?"
  }
  ```

### Greeting Agents
- `POST /greeting/say-hi` - Generate context-appropriate greetings
  ```json
  {
    "message": "I want to say hello"
  }
  ```

## 🔧 How It Works

### Agent Architecture
1. **Specialized Agents**: Each agent has a specific role (translation, greeting, etc.)
2. **Manager Agents**: Coordinate multiple specialized agents for complex tasks
3. **Tool Integration**: Agents can use custom functions and tools
4. **Context Awareness**: Agents understand user intent and delegate appropriately

### Request Flow
1. User sends request to API endpoint
2. Request is processed by the appropriate router
3. Manager agent analyzes the request and determines which specialized agents to use
4. Specialized agents process the request using their tools
5. Results are coordinated and returned to the user

## 🎨 Customization

### Adding New Agents
1. Create a new agent module following the existing pattern
2. Define agent instructions and tools
3. Create a manager agent to coordinate if needed
4. Add API routes for the new functionality

### Extending Existing Agents
- Modify agent instructions in the respective agent files
- Add new tools using the `@function_tool` decorator
- Update the manager agent's tool list

## 🔍 Key Benefits

- **Educational**: Perfect for learning AI agent concepts
- **Modular**: Easy to extend and modify
- **Production Ready**: Built with FastAPI for scalability
- **Well Documented**: Clear code structure and comments
- **API First**: RESTful endpoints for easy integration

## 🤝 Contributing

This project serves as a learning resource and can be extended with:
- Additional agent types
- More sophisticated coordination patterns
- Enhanced error handling
- Testing and validation
- Performance optimizations

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI Agents Framework](https://github.com/openai/openai-agents-python)

## 📄 License

This project is provided as a sample for educational purposes. Feel free to use, modify, and extend it according to your needs.

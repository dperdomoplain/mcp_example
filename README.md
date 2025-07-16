# mcp_example

This project uses `uv` as a Python package and virtual environment manager. The following commands explain how to set up the project:

## Project Setup

### 1. Initialize the project
```bash
uv init --name mcp_example .
```
This command initializes a new Python project in the current directory (`.`) with the name `mcp_example` and specifies that Python 3.13 should be used.

### 2. Create virtual environment on mac
```bash
uv venv --python /opt/homebrew/bin/python3
```
Creates a virtual environment using `uv`. The virtual environment is stored in the `.venv` directory.

### 3. Activate virtual environment
```bash
source .venv/bin/activate
```
Activates the virtual environment so that dependencies are installed in the project's isolated environment.

### 4. Install dependencies
```bash
uv add "mcp[cli]"
uv add pyodbc
uv add pydantic
uv add pydantic-settings
```
Installs the required packages:
- `mcp` with CLI extras for Model Context Protocol
- `pyodbc` for SQL Server connectivity
- `pydantic` for data validation and configuration management

## Features

This MCP server includes the following tools:

### 1. Basic Math Tool
- `add(a, b)` - Adds two numbers

### 2. SQL Server Tools
- `sql_server_query()` - Connect to SQL Server and execute queries
- `sql_server_list_tables()` - List all tables in a database
- `sql_server_table_info()` - Get detailed information about a specific table
- `sql_server_test_connection()` - Test connection to SQL Server database
- `sql_server_database_info()` - Get basic database information
- `sql_server_list_schemas()` - List all schemas in the database

### 3. Environment-based SQL Server Tools
- `sql_server_query_env()` - Execute queries using environment variables
- `sql_server_test_connection_env()` - Test connection using environment variables

### 4. Greeting Resources
- Dynamic greeting resources for personalized messages

### 5. Prompt Templates
- `greet_user()` - Generate greeting prompts with different styles

## Architecture

The project uses a clean, modern architecture with Pydantic for data validation:

- **`sql_server.py`**: Contains the `SQLServerConnection` class and Pydantic models
- **`main.py`**: Contains the MCP server and tool definitions
- **Pydantic Models**: Strong typing and validation for all data structures
- **Environment Variables**: Support for loading configuration from environment
- **Context Management**: Automatic connection cleanup using Python context managers
- **Error Handling**: Comprehensive error handling with detailed error messages

## Configuration

### Environment Variables
Create a `.env` file (copy from `.env.example`) with your SQL Server configuration:

```bash
# SQL Server connection details
SQL_SERVER=localhost
SQL_DATABASE=TestDB
SQL_USERNAME=your_username
SQL_PASSWORD=your_password
SQL_PORT=1433
SQL_TRUSTED_CONNECTION=false
```

### Pydantic Models
The project uses Pydantic models for data validation:

- **`SQLServerConfig`**: Configuration with validation
- **`QueryRequest`**: SQL query requests with validation
- **`QueryResponse`**: Structured query responses
- **`TableInfoRequest`**: Table information requests
- **`ConnectionTestResponse`**: Connection test results

## SQL Server Setup

### Prerequisites
You need to install the ODBC Driver 18 for SQL Server:

### Usage Examples

See `SQL_SERVER_CONFIG.md` for detailed configuration examples and usage instructions.

## Running the Server

```bash
uv run main.py
```

The server will start and listen for MCP client connections.


uv add pyodbc
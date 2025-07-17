# Stack Overflow MCP Server

This is a Model Context Protocol (MCP) server that provides tools to query Stack Overflow data from a SQL Server database. The project uses `uv` as a Python package and virtual environment manager.

## Project Setup

The following commands explain how to set up the project:

### 1. Initialize the project
```bash
uv init --name mcp_example --python 3.13 . 
```
This command initializes a new Python project in the current directory (`.`) with the name `mcp_example` and specifies that Python 3.13 should be used.

### 2. Create virtual environment

#### 2.1 Create virtual environment specifying path
```bash
uv venv --python /opt/homebrew/bin/python3
```

#### 2.2 Create virtual environment on windows, linux and mac

```bash
uv venv --python 3.13
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
- `pydantic` for data validation
- `pydantic-settings` for configuration management

## Features

This MCP server includes the following tools:

- **`get_most_viewed_posts`**: Retrieves the most viewed posts from the Stack Overflow database
- **`get_last_post_with_activity`**: Gets the most recent posts with activity from the Stack Overflow database



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
Create a `.env` file with your SQL Server configuration:

```bash
SERVER=localhost
DATABASE=TestDB
USERNAME=your_username
PASSWORD=your_password
PORT=1433
TRUSTED_CONNECTION=false
```

### Pydantic Models
The project uses Pydantic models for data validation:

- **`SQLServerConfig`**: Configuration with validation
- **`QueryRequest`**: SQL query requests with validation
- **`QueryResponse`**: Structured query responses

## SQL Server Setup

### Prerequisites
You need to install the ODBC Driver 17 for SQL Server:

#### On macOS:
Download and install from the [Microsoft SQL Server ODBC Driver download page](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver17)

#### On Windows:
Download and install from the [Microsoft SQL Server ODBC Driver download page](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

#### On Linux:
Download and install from the [Microsoft SQL Server ODBC Driver download page](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver17)


### Database Schema
This MCP server expects a SQL Server database with Stack Overflow data. The database should contain at least a `Posts` table with the following relevant columns:
- `ViewCount`: Number of times the post has been viewed
- `LastActivityDate`: The date of the last activity on the post
- Other standard Stack Overflow post fields

You can obtain Stack Overflow data dumps from the [Stack Exchange Data Dump](https://archive.org/details/stackexchange) and import them into your SQL Server database.

## Running the Server

```bash
uv run main.py
```

The server will start and listen for MCP client connections.
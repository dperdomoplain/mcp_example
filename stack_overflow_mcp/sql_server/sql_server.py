import pyodbc
from typing import Any, List
from contextlib import contextmanager
from pydantic import BaseModel, Field

from stack_overflow_mcp.config import SQLServerConfigProvider


class QueryRequest(BaseModel):
    """Pydantic model for query requests"""

    query: str = Field(..., description="SQL query to execute")
    params: List[Any] = Field(
        default_factory=list, description="Parameters for the SQL query"
    )


class QueryResponse(BaseModel):
    """Pydantic model for query responses"""

    results: List[Any] = Field(..., description="Query results")
    row_count: int = Field(..., description="Number of rows affected/returned")


class SQLServerConnection:
    """SQL Server connection manager class"""

    def __init__(self, config: SQLServerConfigProvider):
        """
        Initialize SQL Server connection with Pydantic configuration.

        Args:
            config: SQLServerConfig instance with connection parameters
        """
        self.config = config
        self._connection = None
        self._cursor = None

    def _build_connection_string(self) -> str:
        """Build connection string based on authentication method"""
        if self.config.trusted_connection:
            return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config.server},{self.config.port};DATABASE={self.config.database};Trusted_Connection=yes;"
        else:
            return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config.server},{self.config.port};DATABASE={self.config.database};UID={self.config.username};PWD={self.config.password};"

    def connect(self) -> bool:
        """
        Establish connection to SQL Server.

        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            conn_str = self._build_connection_string()
            self._connection = pyodbc.connect(conn_str)
            return True
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        try:
            if not self.connect():
                raise Exception("Failed to connect to database")
            yield self._connection
        finally:
            self.disconnect()

    def execute_query(self, request: QueryRequest) -> QueryResponse:
        """
        Execute a SQL query and return results.

        Args:
            request: QueryRequest instance with query to execute

        Returns:
            QueryResponse instance with query results, row count, and status
        """

        with self.get_connection() as conn:
            cursor = conn.execute(request.query, request.params)
            rows = cursor.fetchall()
            if not rows:
                return QueryResponse(results=[], row_count=0)
            return QueryResponse(results=rows, row_count=len(rows))

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SQLServerConfigProvider(BaseSettings):
    """Pydantic model for SQL Server configuration"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )

    server: str = Field(alias="SERVER", description="SQL Server hostname or IP address")
    database: str = Field(alias="DATABASE", description="Database name to connect to")
    username: Optional[str] = Field(
        alias="USERNAME", default=None, description="SQL Server username"
    )
    password: Optional[str] = Field(
        alias="PASSWORD", default=None, description="SQL Server password"
    )
    port: int = Field(alias="PORT", default=1433, description="SQL Server port")
    trusted_connection: bool = Field(
        alias="TRUSTED_CONNECTION",
        default=False,
        description="Use Windows Authentication",
    )

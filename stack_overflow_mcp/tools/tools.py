from stack_overflow_mcp.sql_server.sql_server import (
    SQLServerConnection,
    QueryRequest,
    QueryResponse,
    SQLServerConfigProvider,
)


def get_most_viewed_posts(numbers_of_posts: int) -> QueryResponse:
    query = f"""
        SELECT TOP {numbers_of_posts} *
        FROM [dbo].[Posts]
        ORDER BY [ViewCount] DESC
    """
    config = SQLServerConfigProvider()
    sql_conn = SQLServerConnection(config)
    query_request = QueryRequest(query=query)
    result = sql_conn.execute_query(query_request)
    return result


def get_last_post_with_activity(numbers_of_posts: int) -> QueryResponse:

    query = f"""
        SELECT TOP {numbers_of_posts} *
        FROM [dbo].[Posts]    
        ORDER BY [LastActivityDate] DESC
    """
    config = SQLServerConfigProvider()
    sql_conn = SQLServerConnection(config)
    query_request = QueryRequest(query=query)
    result = sql_conn.execute_query(query_request)
    return result

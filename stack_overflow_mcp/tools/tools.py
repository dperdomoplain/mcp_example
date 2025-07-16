from stack_overflow_mcp.sql_server.sql_server import (
    SQLServerConnection,
    QueryRequest,
    QueryResponse,
    SQLServerConfigProvider,
)


def get_most_viewed_posts(numbers_of_posts: int) -> QueryResponse:

    if not isinstance(numbers_of_posts, int) or numbers_of_posts <= 0:
        raise ValueError("numbers_of_posts must be a positive integer")

    query = f"""
        SELECT TOP {numbers_of_posts} *
        FROM [dbo].[Posts]
        ORDER BY [ViewCount] DESC
    """
    config = SQLServerConfigProvider()
    sql_conn = SQLServerConnection(config)
    query_request = QueryRequest(query=query, params=[])
    result = sql_conn.execute_query(query_request)
    return result


def get_last_post_with_activity(numbers_of_posts: int) -> QueryResponse:

    if not isinstance(numbers_of_posts, int) or numbers_of_posts <= 0:
        raise ValueError("numbers_of_posts must be a positive integer")

    query = f"""
        SELECT TOP {numbers_of_posts} *
        FROM [dbo].[Posts]    
        ORDER BY [LastActivityDate] DESC
    """
    config = SQLServerConfigProvider()
    sql_conn = SQLServerConnection(config)
    query_request = QueryRequest(query=query, params=[])
    result = sql_conn.execute_query(query_request)
    return result

from mcp.server.fastmcp import FastMCP


mcp=FastMCP("Weather")

@mcp.tool()
async def get_weater(location:str)->str:
    """Get the Weather location"""
    return "Its always raining in India"


if __name__=="__main__":
    mcp.run(transport="streamable-http")
    
    
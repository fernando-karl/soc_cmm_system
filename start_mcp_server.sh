#!/bin/bash

# SOC CMM Assessment MCP Server Startup Script

echo "🚀 Starting SOC CMM Assessment MCP Server..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed. Please install Python 3 first.${NC}"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}❌ pip3 is not installed. Please install pip3 first.${NC}"
    exit 1
fi

# Install dependencies
echo -e "${YELLOW}📦 Installing dependencies...${NC}"
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
fi

# Check if API is already running
echo -e "${YELLOW}🔍 Checking if API is already running...${NC}"
if curl -f http://localhost:8400/api/domains &> /dev/null; then
    echo -e "${GREEN}✅ API is already running on port 8400${NC}"
else
    echo -e "${YELLOW}🔄 Starting API server...${NC}"
    python3 main.py &
    API_PID=$!
    
    # Wait for API to start
    sleep 3
    
    # Check if API started successfully
    if curl -f http://localhost:8400/api/domains &> /dev/null; then
        echo -e "${GREEN}✅ API server started successfully (PID: $API_PID)${NC}"
    else
        echo -e "${RED}❌ Failed to start API server${NC}"
        exit 1
    fi
fi

# Run tests
echo -e "${YELLOW}🧪 Running tests...${NC}"
python3 test_mcp_server.py

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed!${NC}"
else
    echo -e "${RED}❌ Some tests failed${NC}"
    exit 1
fi

# Start MCP server
echo -e "${YELLOW}🔧 Starting MCP server...${NC}"
echo -e "${GREEN}✅ MCP server is ready for connections${NC}"
echo -e "${YELLOW}📝 Use mcp_config.json to configure your MCP client${NC}"
echo -e "${YELLOW}📚 See MCP_README.md for detailed usage instructions${NC}"

python3 mcp_server.py
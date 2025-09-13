# BeeAI Threat Hunter Test Agent

🛡️ **Test Agent for BeeAI Platform Integration**

A comprehensive test agent built on the BeeAI framework to verify platform integration and provide system health checks for SOC & Threat Hunting operations.

## Features

✅ **System Health Monitoring** - Real-time status checks for all components
✅ **BeeAI Integration Testing** - Validates platform connectivity and functionality  
✅ **Configuration Validation** - Tests MindsDB and external service configurations
✅ **Interactive Help System** - Provides guidance on available commands
✅ **Multi-turn Conversations** - Maintains context across interactions

## Quick Start

### Using BeeAI Platform

1. **Import via GitHub**:
   ```
   https://github.com/weqodeai/beeai-threat-hunter.git
   ```

2. **Or build locally**:
   ```bash
   docker build -t threat-hunter-test .
   docker run -p 8000:8000 threat-hunter-test
   ```

### Available Commands

- `test connection` - Verify BeeAI platform integration
- `status` / `health` - Complete system health check
- `mindsdb` - Test MindsDB service configuration  
- `help` - Show available commands

## Agent Details

- **Name**: Threat Hunter Test Agent
- **Version**: 1.0.0
- **Framework**: BeeAI
- **Language**: Python 3.13
- **License**: Apache 2.0

## API Endpoints

The agent exposes standard BeeAI endpoints:
- `/.well-known/agent-card.json` - Agent metadata
- `/v1/message:send` - Send messages
- `/v1/message:stream` - Streaming responses
- `/docs` - OpenAPI documentation

## Development

### Project Structure
```
├── Dockerfile              # Container configuration
├── pyproject.toml          # Python project metadata
├── src/beeai_threat_hunter/
│   └── agents/
│       └── test_agent.py   # Main agent implementation
└── beeai-agent.yaml        # BeeAI agent configuration
```

### Local Development

```bash
# Install dependencies
pip install beeai-sdk pydantic httpx python-dotenv

# Run the agent
python src/beeai_threat_hunter/agents/test_agent.py
```

## Integration

This test agent serves as a foundation for building production SOC and Threat Hunting agents:

- **Analyst Agent** - Threat analysis and IOC detection
- **Integration Agent** - External system connectivity  
- **Case Management Agent** - Incident response workflows

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Apache 2.0 - see [LICENSE](LICENSE) file for details.

---

**Built with BeeAI Framework** 🐝

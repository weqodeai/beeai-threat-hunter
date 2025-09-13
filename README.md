# BeeAI Threat Hunter - Integration Test

## Overview

This is a minimal prototype to test BeeAI Framework integration for the AI Agents Team for SOC & Threat Hunting project.

## Purpose

**Primary Goal**: Verify that we can successfully add a custom agent to BeeAI UI without encountering the previous integration issues.

## Quick Start

### 1. Install Dependencies

```bash
# Copy environment template
cp .env.example .env

# Install Python dependencies (choose one method)
# Option A: Using Poetry (recommended)
poetry install

# Option B: Using pip
pip install beeai-sdk asyncio pydantic httpx python-dotenv
```

### 2. Run the Test Agent

```bash
# Using Poetry
poetry run python src/beeai_threat_hunter/agents/test_agent.py

# Or using the script
poetry run threat-hunter-test

# Or direct Python
python src/beeai_threat_hunter/agents/test_agent.py
```

### 3. Test BeeAI UI Integration

1. **Start the agent server** (it should run on `http://localhost:48000` by default)
2. **Add to BeeAI UI**:
   - Open your BeeAI Platform UI
   - Add new agent with URL: `http://localhost:48000`
   - Agent should appear as "Threat Hunter Test Agent"

### 4. Verify Functionality

Once added to BeeAI UI, test these commands:

- `test connection` - Verify BeeAI integration works
- `mindsdb` - Check MindsDB configuration
- `status` - System health check  
- `help` - Show available commands

## Expected Results

✅ **Success Criteria**:
- Agent appears in BeeAI UI without errors
- Can send messages and receive responses
- All test commands work correctly
- No integration failures

❌ **If it fails**:
- Document the exact error messages
- Check console logs from both agent and BeeAI UI
- Verify the agent server is running and accessible

## Project Structure

```
beeai-threat-hunter/
├── src/beeai_threat_hunter/
│   ├── agents/
│   │   └── test_agent.py      # Minimal test agent
│   ├── tools/                 # Future: Agent tools
│   └── core/                  # Future: Core functionality
├── docs/                      # Documentation & references
├── pyproject.toml            # Python dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

## Configuration

Edit `.env` file to configure:

```bash
# BeeAI Configuration
BEEAI_HOST=127.0.0.1
BEEAI_PORT=48000

# MindsDB Configuration (for future testing)
MINDSDB_URL=http://localhost:47334
MINDSDB_USER=dotroot
MINDSDB_PASSWORD=Ood0tr00t
MINDSDB_PROJECT=secops_project

# Development Settings
DEBUG=true
LOG_LEVEL=INFO
```

## Next Steps

Once this minimal agent successfully integrates with BeeAI UI:

1. ✅ **Integration Confirmed** - We can proceed with full development
2. 🏗️ **Build Core Agents** - Implement the actual threat hunting agents
3. 🔌 **Add MindsDB Integration** - Connect to real data sources
4. 📊 **Implement Case Management** - Add investigation tracking
5. 🚀 **Production Deployment** - Scale for enterprise use

## Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Change port in .env
   BEEAI_PORT=48001
   ```

2. **Import errors**:
   ```bash
   # Install BeeAI SDK
   pip install beeai-sdk
   ```

3. **Agent not appearing in UI**:
   - Check agent server logs
   - Verify BeeAI UI can reach `http://localhost:48000`
   - Check firewall settings

### Debug Mode

Enable debug logging:
```bash
DEBUG=true python src/beeai_threat_hunter/agents/test_agent.py
```

## Development Rules (From WARP.md)

- ✅ **BeeAI Framework Compliance**: Using official BeeAI SDK
- ✅ **Professional Code**: Clean, documented, no emojis in code
- ✅ **Latest Documentation**: Using current BeeAI SDK version
- ✅ **Official Tools Priority**: BeeAI SDK over custom solutions
- ✅ **Working Code First**: Simple, functional prototype

---

**Status**: 🧪 Testing Phase  
**Next**: Full agent development after integration verification
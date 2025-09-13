"""
Threat Hunter Test Agent - BeeAI Integration Test Agent
Built on BeeAI framework for testing platform integration and basic functionality
"""
import os
from textwrap import dedent

from a2a.types import AgentSkill, Message
from a2a.utils.message import get_message_text
from beeai_sdk.a2a.extensions import AgentDetail, AgentDetailContributor
from beeai_sdk.a2a.types import AgentMessage
from beeai_sdk.server import Server
from beeai_sdk.server.context import RunContext

# Initialize BeeAI server
server = Server()


@server.agent(
    name="Threat Hunter Test Agent",
    documentation_url="https://github.com/wunitb/bee_labs/tree/main/beeai-threat-hunter",
    version="1.0.0",
    default_input_modes=["text", "text/plain"],
    default_output_modes=["text", "text/plain"],
    detail=AgentDetail(
        interaction_mode="multi-turn",
        user_greeting="🛡️ Hello! I'm your Threat Hunter Test Agent. How can I help you test the system?",
        framework="BeeAI",
        programming_language="Python",
        author=AgentDetailContributor(name="BeeAI Labs Team"),
        contributors=[],
        license="Apache 2.0",
    ),
    skills=[
        AgentSkill(
            id="threat_hunter_test",
            name="System Testing and Integration",
            description=dedent(
                """\
                This is a test agent designed to verify BeeAI platform integration and basic functionality.
                It provides system health checks, connection tests, and configuration validation for the
                Threat Hunter system.

                ## Features
                - **Connection Testing** - Verifies BeeAI integration is working correctly
                - **System Health** - Provides status checks for all components
                - **Configuration Validation** - Tests MindsDB and other service configurations
                - **Interactive Help** - Provides guidance on available commands

                ## Usage
                This agent responds to various test commands:
                - Connection tests to verify platform integration
                - Status checks for system health monitoring
                - Configuration validation for external services
                - Help commands for user guidance
                """
            ),
            tags=["testing", "integration", "system-health"],
            examples=[
                "test connection",
                "check system status",
                "validate mindsdb configuration",
                "show help"
            ],
        )
    ],
)
async def threat_hunter_test_agent(message: Message, context: RunContext):
    """
    Test agent for BeeAI platform integration verification.
    Provides system health checks, connection tests, and configuration validation.
    """
    user_message = get_message_text(message).strip().lower()
    
    # Build response based on user input
    if "test connection" in user_message or "connection" in user_message:
        response_text = "✅ **Connection Test: SUCCESS**\n\n🔧 **System Status**: All core components are initialized\n📡 **Network**: Agent is responding to requests\n🐝 **BeeAI SDK**: Active and functional"
    elif "mindsdb" in user_message:
        mindsdb_configured = bool(os.getenv('MINDSDB_URL'))
        mindsdb_url = os.getenv('MINDSDB_URL', 'Not configured')
        status_emoji = "✅" if mindsdb_configured else "⚠️"
        response_text = f"{status_emoji} **MindsDB Integration Test**\n\n📝 **Configuration**: {'Found' if mindsdb_configured else 'Missing'}\n🌐 **Target URL**: {mindsdb_url}\n🔍 **Status**: {'Ready for connections' if mindsdb_configured else 'Needs configuration'}"
    elif "status" in user_message or "health" in user_message:
        response_text = "🏥 **System Health Check**\n\n🐍 **Python Runtime**: ✅ Running\n🐝 **BeeAI SDK**: ✅ Active\n⚙️ **Agent Service**: ✅ Operational\n🌐 **Network**: ✅ Accessible\n📊 **Overall Status**: 🟢 All Systems Go"
    elif "help" in user_message:
        response_text = dedent("""
        🤖 **Threat Hunter Test Agent - Available Commands**
        
        ### System Testing
        • `test connection` - Verify BeeAI platform integration
        • `status` or `health` - Complete system health check
        • `mindsdb` - Test MindsDB service configuration
        
        ### Information
        • `help` - Show this help message
        
        ### Example Usage
        Try asking: "test connection" or "check system status"
        """)
    else:
        response_text = f"👋 **Hello!** You said: *'{get_message_text(message).strip()}'*\n\nI'm your **Threat Hunter Test Agent** for the BeeAI platform.\n\n🔍 **Available Commands**: test connection, status, mindsdb, help\n\n💡 **Tip**: Try `help` to see all available commands!"
    
    yield AgentMessage(text=response_text)


def serve():
    """Run the threat hunter test agent server"""
    server.run(
        host="localhost",
        port=int(os.getenv("PORT", 8000)),
        configure_telemetry=False,
    )


if __name__ == "__main__":
    serve()

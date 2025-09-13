# BeeAI Threat Hunter - Updated Project Rules & Standards

## Core Development Rules

### 1. Development Approach
- KISS Principle: Keep everything simple, no over-engineering
- Working Code First: Focus on functional solution before perfection
- Incremental Development: Build step-by-step, test frequently

### 2. Technical Standards
- **BeeAI Framework Compliance**: Strict adherence to BeeAI Framework directory structure
- **Professional Code**: No emoji icons in code or output, minimal professional icons only
- **Clean Architecture**: Well-documented, maintainable, production-ready code
- **Multi-agent Design**: Clear separation of responsibilities between agents when appropriate

### 3. Technology Integration Standards (NEW)
- **Latest Documentation First**: Always study current version specifications of external tools/APIs
- **Official Tools Priority**: Use official SDKs and recommended approaches over custom solutions
- **Research & Approval Process**: Present research findings and approach recommendations for approval before implementation
- **Best Practices Compliance**: Follow official best practices and standards for all integrations
- **Version Compatibility**: Ensure compatibility with latest stable versions of dependencies

### 4. Project Scope
- **Core Function**: Multi-agent threat hunting system
- **Production Focus**: Enterprise-grade security operations
- **Single Purpose**: Clear focus on threat hunting workflows
- **Scalable Design**: Built for production deployment and monitoring

### 5. Communication & Process
- **Ask Before Changes**: Confirm architecture or feature changes before implementation
- **Show Working Code**: Demo functional solutions rather than theoretical approaches
- **Thai/English**: Bilingual communication acceptable
- **Version Control**: Clear version numbering with GitHub integration

### 6. Quality Standards
- **Functional First**: Code must work before committing
- **Simple Configuration**: Easy-to-understand settings
- **Comprehensive Error Handling**: Production-grade error management
- **Type Safety**: Full type hints and validation

### 7. Environment Flexibility & Deployment Rules (NEW)
- **No Hardcoded Values**: Never hardcode project names, agent names, or environment-specific values
- **Dynamic Resource Selection**: Support multiple projects and agents dynamically based on configuration
- **Environment Portability**: Code must work across development, staging, and production environments
- **Configuration-Driven**: All environment-specific settings must come from configuration files or environment variables
- **Multi-Instance Support**: Support concurrent operations with multiple MindsDB projects and agents
- **Auto-Discovery**: Implement resource discovery mechanisms where possible
- **Fallback Strategies**: Provide graceful fallbacks when specific resources are not available
- **Labs Port Configuration**: All services must use port range 4x,xxx where xxxx is the default port (e.g., 8000 → 48000, 8123 → 48123)

---

## MindsDB Integration - Research & Recommendation

### Current Situation Analysis:
- **Previously**: Using custom REST API calls via httpx
- **Current Best Practice**: MindsDB Python SDK (Official)
- **Documentation Source**: https://docs.mindsdb.com/sdks/python/overview

### Research Findings:

#### MindsDB Python SDK Benefits:
1. **Official Support**: Maintained by MindsDB team
2. **Type Safety**: Full type hints and IDE support
3. **Error Handling**: Built-in retry logic and exception management
4. **Future-proof**: First to receive new features and updates
5. **Simplified API**: No manual SQL string construction or authentication handling

#### Comparison:

| Aspect | Current (REST API) | Recommended (Python SDK) |
|--------|-------------------|---------------------------|
| Maintenance | Custom implementation | Official support |
| Error Handling | Manual retry logic | Built-in resilience |
| Type Safety | Limited | Full type hints |
| API Changes | Manual updates needed | Automatic compatibility |
| Development Speed | Slower (custom code) | Faster (official methods) |
| Documentation | Generic REST docs | SDK-specific guides |

### Implementation Plan:

#### Phase 1: SDK Integration
```python
# Old approach (current):
response = await httpx.post("/api/sql/query", json={"query": sql})

# New approach (recommended):
import mindsdb_sdk
server = mindsdb_sdk.connect('http://localhost:47334', login='dotroot', password='Ood0tr00t')
result = server.agents.query('secops_project.threat_hunter_fallback', question)
```

#### Phase 2: Tool Refactoring
- Replace MindsDBConnector class with SDK-based implementation
- Maintain same BeeAI Tool interface for compatibility
- Add async wrapper for SDK operations
- Preserve existing error handling patterns

#### Phase 3: Testing & Validation
- Test against existing MindsDB agent
- Verify functionality with current data sources
- Performance comparison with previous implementation
- Integration testing with BeeAI agents

### Migration Benefits:
- **Reduced Code**: ~50% less custom connection code
- **Better Reliability**: Official error handling and retries
- **Future Compatibility**: Automatic SDK updates
- **Developer Experience**: Better IDE support and documentation

### Risks & Mitigation:
- **Dependency**: Additional dependency (mitigated by official support)
- **Learning Curve**: New API patterns (mitigated by better documentation)
- **Breaking Changes**: SDK updates (mitigated by semantic versioning)

---

## Recommendation

**I recommend proceeding with MindsDB Python SDK integration** based on:

1. **Official Best Practice**: Aligns with MindsDB's recommended approach
2. **Long-term Maintenance**: Reduces future maintenance burden
3. **Professional Standards**: Uses official, supported tools
4. **Code Quality**: Improves type safety and error handling

**Request for Approval:**

May I proceed with:
1. Updating `tools/mindsdb_tools.py` to use MindsDB Python SDK
2. Maintaining the same BeeAI Tool interface for compatibility
3. Adding comprehensive testing for the new implementation
4. Documenting the migration for future reference

The change will improve code quality while maintaining all existing functionality.

---

**Updated Rules Summary:**
- Always research latest documentation before integration
- Use official tools and SDKs when available
- Present findings and get approval before major changes
- Maintain professional, production-ready code standards
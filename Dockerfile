FROM python:3.13-bookworm

ADD . /app
WORKDIR /app

# Install dependencies directly with pip
RUN pip install beeai-sdk pydantic httpx python-dotenv fastapi

CMD ["python", "src/beeai_threat_hunter/agents/test_agent.py"]

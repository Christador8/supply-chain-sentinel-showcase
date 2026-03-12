# Supply Chain Sentinel - Showcase Version
# SHOWCASE NOTE: Dockerfile structure shown for reference.
# This demonstrates containerization patterns but execution is limited.

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (including dashboard)
COPY schema.py tools.py utils.py main.py dashboard.py ./

# Create logs and results directories
RUN mkdir -p logs results

# Set environment variables for LangSmith
ENV LANGCHAIN_TRACING_V2=true
ENV LANGCHAIN_ENDPOINT=https://api.smith.langchain.com

# Expose port (Render will set PORT env var)
EXPOSE 8501

# Run Streamlit dashboard
# SHOWCASE: Dashboard will run but execution functionality is disabled
CMD streamlit run dashboard.py --server.port=$PORT --server.address=0.0.0.0

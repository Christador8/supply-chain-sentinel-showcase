# 🚢 Supply Chain Sentinel - Showcase Version

<div align="center">

**⚠️ SHOWCASE VERSION ⚠️**

*This repository demonstrates the architecture and design of the Supply Chain Sentinel project.*

**The full working version is available upon request.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28+-green.svg)](https://www.crewai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.55+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Showcase](https://img.shields.io/badge/Version-Showcase-orange.svg)](SHOWCASE.md)

[📖 Showcase Details](SHOWCASE.md) • [💻 Full Version Request](#contact)

</div>

---

## ⚠️ Important Notice

**This is a SHOWCASE VERSION** of the Supply Chain Sentinel project. This repository demonstrates:

- ✅ **Architecture & Design**: Complete code structure and organization
- ✅ **UI/UX Design**: Full Streamlit dashboard with premium styling
- ✅ **Code Patterns**: Best practices, error handling, validation
- ✅ **Documentation**: Comprehensive setup and deployment guides

**The following are removed/stubbed in this showcase:**
- ❌ **Full Implementations**: Critical execution logic is stubbed
- ❌ **API Integrations**: Actual API calls are placeholders
- ❌ **Working Tools**: Tool implementations are demonstration stubs
- ❌ **Agent Execution**: Crew execution is disabled

**For the full working version**, please see the [Contact](#contact) section below.

---

## ✨ Project Showcase

### 🎯 The Challenge
Supply chain disruptions cost businesses **billions annually**. Manual monitoring of logistics news is time-consuming, error-prone, and misses critical events. Traditional solutions lack real-time intelligence and structured data extraction.

### 💡 The Solution
A **production-grade multi-agent AI system** that autonomously monitors global supply chain news, extracts structured intelligence, and delivers actionable insights through a real-time dashboard. Built with CrewAI, this system processes RSS feeds from major logistics publications, uses specialized LLM agents to extract validated data, and surfaces critical disruptions with severity-based alerts.

### 🏆 Key Achievements

| Metric | Achievement |
|--------|------------|
| **Automation** | Eliminated hours of daily manual monitoring |
| **Real-Time** | Instant detection of supply chain disruptions |
| **Data Quality** | 100% validated output with Pydantic schemas |
| **Production** | Live deployment serving stakeholders |
| **Scalability** | Multi-feed architecture with extensible design |

---

## 🚀 Technical Excellence

### 🧠 Multi-Agent Architecture
- **Two Specialized AI Agents**: The Scout (data collection) and The Analyst (intelligence extraction)
- **CrewAI Orchestration**: Seamless task management and agent coordination
- **Lean Architecture**: Direct tool integration without middleware overhead

### 🛡️ Production-Ready Engineering
- ✅ **Type-Safe Validation**: Pydantic schemas ensure data integrity
- ✅ **Resilient Error Handling**: Exponential backoff for HTTP errors
- ✅ **Comprehensive Observability**: Loguru + LangSmith tracing
- ✅ **Rate Limit Management**: Intelligent backoff strategies
- ✅ **Containerized Deployment**: Docker for consistent environments
- ✅ **Cloud-Native**: Automated CI/CD on Render

### 🎨 Premium Web Dashboard
- 🎯 **Interactive UI**: Gradient hero sections with modern design
- 🔍 **Real-Time Search**: Filter disruptions by severity, location, carrier
- 📊 **Geographic Insights**: Visual breakdown of affected regions
- 🚢 **Carrier Analysis**: Impact metrics and statistics
- 🎨 **Modern Styling**: Custom CSS with hover effects and animations

### 📊 Data Quality & Validation
- **Pydantic Models**: Type-safe data structures
- **Automatic Alerts**: CRITICAL warnings for severity > 8
- **Structured Output**: JSON with metadata (timestamp, count)
- **Error Recovery**: Graceful degradation and retry logic

---

## 🛠️ Technology Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **🤖 AI/ML** | CrewAI, LangChain, OpenAI GPT-4 |
| **🐍 Backend** | Python 3.11+, Pydantic, Loguru |
| **🎨 Frontend** | Streamlit, Custom CSS |
| **☁️ DevOps** | Docker, Render, Git |
| **📊 Observability** | LangSmith, Structured Logging |
| **📡 Data Sources** | RSS Feeds (Supply Chain Dive, FreightWaves) |

</div>

---

## 🌟 What Makes This Special

### 🎯 End-to-End Automation
From RSS monitoring → AI extraction → Structured JSON → Real-time dashboard. Complete pipeline automation.

### 🏗️ Production-Grade Quality
Not just a prototype. Full error handling, logging, monitoring, and deployment configurations included.

### 🧩 Intelligent Agent Design
Specialized roles for optimal performance. The Scout gathers, The Analyst extracts—each agent optimized for its task.

### 📱 Real-Time Intelligence
Live dashboard with search, filtering, and analytics. See disruptions as they happen.

### 🔒 Type-Safe Architecture
Pydantic validation ensures data quality at every step. No surprises, just validated intelligence.

### ☁️ Cloud-Native
Dockerized, containerized, and deployed. Ready for production from day one.

---

## 📈 Impact & Results

- ⚡ **Automated** a manual process requiring hours of daily monitoring
- 🎯 **Real-Time Detection** of supply chain disruptions with structured data
- 🚀 **Production Deployment** serving live intelligence to stakeholders
- 📊 **Scalable Architecture** supporting multiple feeds and custom sources
- ✅ **100% Validated Output** ensuring data quality and reliability

---

## 🎓 Skills Demonstrated

This project showcases expertise in:

- 🤖 **Multi-Agent AI Systems** - CrewAI orchestration and agent design
- 🐍 **Production Python** - Type safety, error handling, logging
- 📊 **Real-Time Data Processing** - RSS parsing, validation, transformation
- 🎨 **Modern Web Development** - Streamlit dashboards with custom styling
- ☁️ **Cloud Deployment** - Docker, CI/CD, infrastructure as code
- 📈 **Observability** - Logging, tracing, monitoring systems

---

## 📋 What's Included in This Showcase

### ✅ Visible (Architecture & Design)
- **Code Structure**: Complete file organization and architecture
- **Design Patterns**: Multi-agent system design with CrewAI
- **UI/UX Design**: Full Streamlit dashboard structure and styling
- **Data Models**: Pydantic schemas and validation patterns
- **Error Handling**: Retry logic and error handling patterns
- **Documentation**: Complete README, setup guides, and architecture docs
- **Deployment Configs**: Docker and Render configurations

### ❌ Removed/Stubbed (Executable Functionality)
- **API Integrations**: Actual OpenAI API calls are stubbed
- **RSS Feed Fetching**: Real feed fetching implementation removed
- **Agent Execution**: Crew execution logic is stubbed
- **Subprocess Execution**: Dashboard execution functionality disabled
- **Working Tools**: Tool implementations are placeholder stubs

---

## 🏗️ Architecture Overview

### Standalone Design
This is a **lean, standalone CrewAI project** with no external tool frameworks. All tools are implemented as local Python functions wrapped with CrewAI's `@tool` decorator, allowing agents to call them directly without any middleware.

### Schema (`schema.py`)
- `LogisticsDisruption` Pydantic model with validation
- Severity validator that logs CRITICAL warnings for high-severity events
- Fields: event_name, location_iso, carriers_affected, severity, summary, source_url

### Agents (`main.py`)
- **The Scout**: Uses RSS/URL fetching tools to collect news
- **The Analyst**: Extracts structured data using the Pydantic schema
- Tools are assigned directly to agents via `tools=[fetch_rss_feed, fetch_url_content]`

### Tools (`tools.py`)
- `fetch_rss_feed`: Parses RSS feeds with retry logic (stubbed in showcase)
- `fetch_url_content`: Fetches direct URL content with retry logic (stubbed in showcase)
- Both tools use CrewAI's `@tool` decorator for direct agent integration
- Both tools include exponential backoff for HTTP errors

### Logging (`utils.py`)
- Loguru configuration with 10MB rotation
- LangSmith environment variable integration
- Structured logging to console and files

### Dashboard (`dashboard.py`)
- Premium Streamlit UI with custom CSS
- Real-time disruption visualization
- Search and filter capabilities
- Geographic and carrier analytics
- **SHOWCASE**: Execution functionality disabled

---

## 📁 Project Structure

```
supply-chain-sentinel-showcase/
├── schema.py          # Pydantic models (fully visible)
├── main.py            # CrewAI agents and crew (stubbed execution)
├── tools.py           # RSS/URL fetching tools (stubbed)
├── utils.py           # Logging configuration (visible)
├── dashboard.py       # Streamlit web dashboard (UI visible, execution disabled)
├── requirements.txt   # Python dependencies (showcase note)
├── Dockerfile         # Docker configuration (visible)
├── render.yaml        # Render deployment config (visible)
├── SHOWCASE.md        # Showcase documentation
├── README.md          # This file
└── LICENSE            # MIT License
```

---

## 🚀 Setup (Showcase Version)

### Prerequisites
- Python 3.11+
- (Optional) OpenAI API key (for understanding structure, not execution)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd supply-chain-sentinel-showcase
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. View the dashboard (UI only, execution disabled):
```bash
streamlit run dashboard.py
```

**Note**: The dashboard will display the UI structure but execution is disabled in the showcase version.

---

## 📖 Documentation

- **[SHOWCASE.md](SHOWCASE.md)**: Detailed information about what's included/removed in this showcase
- **Code Comments**: All files include `SHOWCASE` comments explaining modifications

---

## 📧 Contact

For access to the **full working version** or licensing inquiries:

- **GitHub**: [@Christador8](https://github.com/Christador8)
- **Repository**: [supply-chain-sentinel](https://github.com/Christador8/supply-chain-sentinel)

---

## ⚖️ License

This showcase version is provided under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2026 Christa Dor**

All rights reserved. This software and associated documentation files are the proprietary 
and confidential information of Christa Dor. Unauthorized copying, modification, distribution, 
or use of this Software, via any medium, is strictly prohibited without express written 
permission from the copyright owner.

For licensing inquiries, please contact the repository owner.

---

<div align="center">

**Built with ❤️ by [Christa Dor](https://github.com/Christador8)**

[📖 Showcase Details](SHOWCASE.md) • [💻 Full Version Request](#contact)

</div>

"""
Supply Chain Sentinel - AI-Powered Logistics Intelligence Platform
SHOWCASE VERSION

Copyright (c) 2026 Christa Dor
All rights reserved.

⚠️ SHOWCASE NOTICE: This is a showcase version. Critical implementation details
have been removed. The full working version is available upon request.

This software and associated documentation files (the "Software") are the 
proprietary and confidential information of Christa Dor. Unauthorized copying, 
modification, distribution, or use of this Software, via any medium, is strictly 
prohibited without express written permission from the copyright owner.

For licensing information, see the LICENSE file in the root directory of this repository.
"""

# SHOWCASE: Imports kept to show dependencies and structure
import os
import time
import re
import json
from pathlib import Path
from datetime import datetime
# SHOWCASE: CrewAI imports shown but execution is stubbed
from crewai import Agent, Crew, Task
from langchain_openai import ChatOpenAI
from loguru import logger
from dotenv import load_dotenv
from openai import RateLimitError

from schema import LogisticsDisruption
from tools import fetch_rss_feed, fetch_url_content
from utils import setup_logging

# Load environment variables from .env file
load_dotenv()

# Setup logging
setup_logging()

# Disable CrewAI interactive tracing prompt (for Docker/Render compatibility)
os.environ.setdefault("CREWAI_TRACING_ENABLED", "false")

# Configure LangSmith (if environment variables are set)
os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
os.environ.setdefault("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
os.environ.setdefault("LANGCHAIN_API_KEY", os.getenv("LANGSMITH_API_KEY", ""))
os.environ.setdefault("LANGCHAIN_PROJECT", os.getenv("LANGSMITH_PROJECT", "supply-chain-sentinel"))


def create_agents(llm):
    """
    Create the Scout and Analyst agents.
    
    SHOWCASE: Agent definitions are shown to demonstrate the architecture.
    In the full version, these agents execute with real LLM calls.
    """
    
    # The Scout - Fetches news from RSS feeds
    scout = Agent(
        role="Supply Chain News Scout",
        goal="Monitor and collect logistics and supply chain news from RSS feeds and URLs",
        backstory="""You are an expert news scout specializing in logistics and supply chain disruptions. 
        You have access to RSS feeds from major logistics publications and can fetch content from URLs.
        Your job is to gather raw news articles about port closures, carrier disruptions, strikes, 
        natural disasters, and other events affecting global supply chains.""",
        tools=[fetch_rss_feed, fetch_url_content],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    # The Analyst - Extracts structured data using Pydantic schema
    analyst = Agent(
        role="Supply Chain Disruption Analyst",
        goal="Extract structured logistics disruption data from news articles using the LogisticsDisruption schema",
        backstory="""You are a logistics analyst expert at identifying and categorizing supply chain disruptions.
        You analyze news articles and extract key information: event names, locations (ISO codes), 
        affected carriers, severity ratings (1-10), summaries, and source URLs.
        You are meticulous about data quality and always validate severity levels.""",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    return scout, analyst


def create_tasks(scout, analyst, rss_urls=None):
    """
    Create tasks for the crew.
    
    SHOWCASE: Task definitions shown. RSS URLs are placeholders in showcase version.
    """
    if rss_urls is None:
        # SHOWCASE: Placeholder URLs - actual feeds removed
        rss_urls = [
            "https://example.com/feed1",  # Placeholder
            "https://example.com/feed2",  # Placeholder
        ]
    
    # Task 1: Scout fetches news
    scout_task = Task(
        description=f"""
        Fetch the latest logistics and supply chain news from the following RSS feeds:
        {', '.join(rss_urls)}
        
        Use the fetch_rss_feed tool for each URL. Collect all recent articles about:
        - Port closures or disruptions
        - Carrier strikes or labor issues
        - Natural disasters affecting logistics
        - Trade route disruptions
        - Carrier service changes or delays
        - Shipping delays and capacity issues
        - Trade policy changes affecting supply chains
        - Maritime and air freight disruptions
        
        Return the raw article content with titles, summaries, and links.
        """,
        expected_output="A comprehensive collection of recent logistics news articles with titles, summaries, and source URLs",
        agent=scout
    )
    
    # Task 2: Analyst extracts structured data
    analyst_task = Task(
        description="""
        Analyze the news articles collected by the Scout and extract structured disruption data.
        
        For each significant logistics disruption found, create a LogisticsDisruption entry with:
        - event_name: Clear, descriptive name of the event
        - location_iso: ISO country/region code (e.g., "US-CA", "CN-SH", "DE-HH")
        - carriers_affected: List of carrier/shipping company names mentioned
        - severity: Integer 1-10 (1=minor, 5=moderate, 8+=critical)
        - summary: 2-3 sentence summary of the disruption
        - source_url: Original article URL
        
        Return a JSON array of LogisticsDisruption objects. Only include events that are:
        - Currently active or recent (within last 30 days)
        - Actually affecting logistics operations
        - Have identifiable locations and carriers
        
        If no disruptions are found, return an empty array.
        """,
        expected_output="A JSON array of LogisticsDisruption objects, each validated against the Pydantic schema",
        agent=analyst,
        context=[scout_task]
    )
    
    return scout_task, analyst_task


def create_llm_with_retry(api_key: str, model_name: str, max_retries: int = 5):
    """
    Create ChatOpenAI LLM with retry logic for rate limits.
    
    SHOWCASE: Function signature shown, but actual LLM creation is stubbed.
    """
    # SHOWCASE: Implementation removed - returns None in showcase version
    logger.info(f"SHOWCASE: LLM creation stubbed (would use {model_name})")
    return None


def extract_retry_after(error_message: str) -> float:
    """Extract retry-after time from OpenAI error message."""
    # Look for patterns like "Please try again in 99ms" or "Please try again in 2.5s"
    patterns = [
        r"Please try again in (\d+(?:\.\d+)?)\s*ms",
        r"Please try again in (\d+(?:\.\d+)?)\s*s",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, error_message, re.IGNORECASE)
        if match:
            value = float(match.group(1))
            # Convert ms to seconds
            if "ms" in match.group(0).lower():
                return value / 1000.0
            return value
    
    # Default backoff if we can't parse the time
    return 2.0


def save_results_to_file(result):
    """
    Save crew execution results to JSON file for dashboard.
    
    SHOWCASE: Function structure shown, but file saving is disabled.
    """
    # SHOWCASE: Implementation removed for showcase
    logger.info("SHOWCASE: Results saving disabled")
    logger.info(f"SHOWCASE: Would save {len(result) if isinstance(result, list) else 'results'} disruptions")


def main():
    """
    Main execution function.
    
    SHOWCASE: Execution is stubbed. Shows the structure but doesn't actually run agents.
    """
    logger.info("SHOWCASE: Starting Supply Chain Sentinel Agent (Showcase Mode)")
    logger.warning("⚠️  This is a SHOWCASE VERSION - execution is disabled")
    
    # SHOWCASE: Check for API key but don't actually use it
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("SHOWCASE: OPENAI_API_KEY not set (expected in showcase)")
    
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    logger.info(f"SHOWCASE: Would use LLM: {model_name}")
    
    # SHOWCASE: Agent creation shown but execution stubbed
    logger.info("SHOWCASE: Creating agents (structure only)...")
    # llm = create_llm_with_retry(api_key, model_name, max_retries=5)  # Stubbed
    # scout, analyst = create_agents(llm)  # Would create agents
    # scout_task, analyst_task = create_tasks(scout, analyst)  # Would create tasks
    
    # SHOWCASE: Crew creation and execution removed
    logger.info("SHOWCASE: Crew execution disabled in showcase version")
    logger.info("SHOWCASE: In full version, this would execute the multi-agent workflow")
    
    # Return example data structure
    example_result = [
        {
            "event_name": "Example Disruption",
            "location_iso": "US-CA",
            "carriers_affected": ["Example Carrier"],
            "severity": 5,
            "summary": "This is example data from the showcase version",
            "source_url": "https://example.com"
        }
    ]
    
    logger.info("SHOWCASE: Returning example data structure")
    return example_result


if __name__ == "__main__":
    # SHOWCASE: Show that main would be called, but execution is limited
    logger.info("=" * 60)
    logger.info("SHOWCASE VERSION - Execution Limited")
    logger.info("=" * 60)
    result = main()
    logger.info(f"SHOWCASE: Example result structure: {len(result)} items")

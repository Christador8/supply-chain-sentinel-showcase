"""
Supply Chain Sentinel - Utilities
SHOWCASE VERSION

Copyright (c) 2026 Christa Dor
All rights reserved.

⚠️ SHOWCASE NOTICE: This is a showcase version. Logging configuration is shown
to demonstrate observability patterns.

This software and associated documentation files (the "Software") are the 
proprietary and confidential information of Christa Dor. Unauthorized copying, 
modification, distribution, or use of this Software, via any medium, is strictly 
prohibited without express written permission from the copyright owner.

For licensing information, see the LICENSE file in the root directory of this repository.
"""

import os
import sys
from loguru import logger


def setup_logging():
    """
    Configure Loguru logging with rotation and LangSmith integration.
    
    SHOWCASE: Logging configuration shown to demonstrate observability setup.
    In the full version, this provides comprehensive logging and tracing.
    """
    # Remove default handler
    logger.remove()
    
    # Add console handler with formatting
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )
    
    # SHOWCASE: File logging shown but may be limited in showcase
    # Add file handler with rotation
    try:
        logger.add(
            "logs/supply_chain_sentinel_{time:YYYY-MM-DD}.log",
            rotation="10 MB",
            retention="30 days",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            level="DEBUG",
            compression="zip"
        )
    except Exception:
        # SHOWCASE: Graceful fallback if logs directory doesn't exist
        logger.warning("SHOWCASE: File logging disabled (logs directory not available)")
    
    # Log LangSmith environment variables if set
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
    langsmith_project = os.getenv("LANGSMITH_PROJECT")
    langsmith_tracing = os.getenv("LANGSMITH_TRACING", "true")
    
    if langsmith_api_key:
        logger.info("SHOWCASE: LangSmith tracing would be enabled in full version")
        logger.debug(f"SHOWCASE: LangSmith Project: {langsmith_project or 'default'}")
    else:
        logger.warning("SHOWCASE: LANGSMITH_API_KEY not set - tracing disabled")
    
    return logger

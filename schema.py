"""
Supply Chain Sentinel - Data Schema
SHOWCASE VERSION

Copyright (c) 2026 Christa Dor
All rights reserved.

⚠️ SHOWCASE NOTICE: This is a showcase version. The schema is fully visible
as it demonstrates data modeling patterns.

This software and associated documentation files (the "Software") are the 
proprietary and confidential information of Christa Dor. Unauthorized copying, 
modification, distribution, or use of this Software, via any medium, is strictly 
prohibited without express written permission from the copyright owner.

For licensing information, see the LICENSE file in the root directory of this repository.
"""

from pydantic import BaseModel, field_validator
from typing import List
from loguru import logger


class LogisticsDisruption(BaseModel):
    """
    Model for representing logistics disruptions in the supply chain.
    
    SHOWCASE: This schema is fully visible as it demonstrates:
    - Pydantic data modeling
    - Field validation patterns
    - Type safety and data structure design
    """
    
    event_name: str
    location_iso: str  # ISO country/region code
    carriers_affected: List[str]
    severity: int  # 1-10 scale
    summary: str
    source_url: str
    
    @field_validator('severity')
    @classmethod
    def validate_severity(cls, v: int) -> int:
        """
        Validate severity and log CRITICAL warning if > 8.
        
        SHOWCASE: Validation logic shown - demonstrates Pydantic validators.
        """
        if not 1 <= v <= 10:
            raise ValueError('Severity must be between 1 and 10')
        
        if v > 8:
            logger.critical(
                f"CRITICAL SEVERITY ALERT: Severity level {v} detected. "
                f"This disruption requires immediate attention."
            )
        
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_name": "Port Strike in Los Angeles",
                "location_iso": "US-CA",
                "carriers_affected": ["Maersk", "CMA CGM", "Evergreen"],
                "severity": 9,
                "summary": "Major port workers strike affecting container operations",
                "source_url": "https://example.com/news/article"
            }
        }

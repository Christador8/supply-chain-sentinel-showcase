"""
Supply Chain Sentinel - Dashboard
SHOWCASE VERSION

Copyright (c) 2026 Christa Dor
All rights reserved.

⚠️ SHOWCASE NOTICE: This is a showcase version. The dashboard UI structure is
fully visible, but execution functionality is disabled. The full working version
is available upon request.

This software and associated documentation files (the "Software") are the 
proprietary and confidential information of Christa Dor. Unauthorized copying, 
modification, distribution, or use of this Software, via any medium, is strictly 
prohibited without express written permission from the copyright owner.

For licensing information, see the LICENSE file in the root directory of this repository.
"""

import streamlit as st
import json
# SHOWCASE: subprocess import kept but execution disabled
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict
import time
from collections import Counter

st.set_page_config(
    page_title="Supply Chain Sentinel - AI-Powered Logistics Monitoring (Showcase)",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# SHOWCASE BANNER
st.markdown("""
    <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); 
                padding: 1rem; border-radius: 10px; margin-bottom: 1rem; 
                color: white; text-align: center; font-weight: bold;">
        ⚠️ SHOWCASE VERSION - Execution Disabled ⚠️
        <br>
        <small>This demonstrates the UI/UX design. Full version available upon request.</small>
    </div>
""", unsafe_allow_html=True)

# Browser metadata (title, author, description, etc.)
st.markdown("""
    <head>
        <meta name="author" content="Christa Dor">
        <meta name="description" content="AI-powered logistics disruption monitoring system that tracks supply chain events, carrier impacts, and regional disruptions in real-time.">
        <meta name="keywords" content="supply chain, logistics, disruption monitoring, AI, freight, shipping">
        <meta property="og:title" content="Supply Chain Sentinel - AI-Powered Logistics Monitoring">
        <meta property="og:description" content="Real-time supply chain disruption monitoring with AI agents">
        <meta property="og:type" content="website">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="Supply Chain Sentinel">
        <meta name="twitter:description" content="AI-powered logistics disruption monitoring">
    </head>
""", unsafe_allow_html=True)

# Premium CSS Styling
st.markdown("""
    <style>
    /* Main styling */
    .main {
        padding: 2rem 1rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border-left: 4px solid;
        transition: transform 0.2s;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .metric-critical { border-left-color: #d32f2f; }
    .metric-high { border-left-color: #f57c00; }
    .metric-medium { border-left-color: #fbc02d; }
    .metric-low { border-left-color: #388e3c; }
    
    /* Disruption Cards */
    .disruption-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .disruption-card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    .severity-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-left: 0.5rem;
    }
    
    .badge-critical { background: #ffebee; color: #d32f2f; }
    .badge-high { background: #fff3e0; color: #f57c00; }
    .badge-medium { background: #fffde7; color: #fbc02d; }
    .badge-low { background: #e8f5e9; color: #388e3c; }
    
    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        color: #1a1a1a;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Status Indicator */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 0.5rem;
    }
    
    .status-active { background: #4caf50; }
    .status-inactive { background: #9e9e9e; }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

def load_latest_results() -> Dict:
    """Load the latest results from JSON file."""
    latest_file = Path("results/latest.json")
    if latest_file.exists():
        try:
            with open(latest_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading results: {e}")
            return {"disruptions": [], "count": 0, "timestamp": None}
    return {"disruptions": [], "count": 0, "timestamp": None}

def get_severity_class(severity: int) -> str:
    """Get CSS class based on severity level."""
    if severity >= 8:
        return "severity-critical"
    elif severity >= 5:
        return "severity-high"
    elif severity >= 3:
        return "severity-medium"
    else:
        return "severity-low"

def get_severity_emoji(severity: int) -> str:
    """Get emoji based on severity level."""
    if severity >= 8:
        return "🔴"
    elif severity >= 5:
        return "🟠"
    elif severity >= 3:
        return "🟡"
    else:
        return "🟢"

def run_sentinel():
    """
    Run the Supply Chain Sentinel agent.
    
    SHOWCASE: Execution is disabled. Shows the UI flow but doesn't actually run.
    """
    # SHOWCASE: Execution disabled
    st.warning("⚠️ **SHOWCASE VERSION**: Agent execution is disabled in this showcase.")
    st.info("💡 In the full version, this would execute the multi-agent workflow to fetch and analyze supply chain disruptions.")
    return False, "SHOWCASE: Execution disabled - this is a demonstration version"

# Load data
results = load_latest_results()
disruptions = results.get("disruptions", [])

# ========== HERO SECTION ==========
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🚢 Supply Chain Sentinel</div>
        <div class="hero-subtitle">AI-Powered Logistics Disruption Monitoring & Analysis</div>
    </div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("### ⚙️ Control Center")
    
    if st.button("🔄 Run Sentinel Analysis", type="primary", use_container_width=True):
        success, message = run_sentinel()
        if success:
            st.success(message)
            time.sleep(1)
            st.rerun()
        else:
            st.error(message)
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    
    if disruptions:
        st.metric("Total Disruptions", len(disruptions), delta=None)
        critical = sum(1 for d in disruptions if d.get("severity", 0) >= 8)
        if critical > 0:
            st.error(f"🔴 {critical} Critical")
    else:
        st.info("No data available (Showcase Mode)")
    
    st.markdown("---")
    st.markdown("### ℹ️ System Info")
    
    if results.get("timestamp"):
        try:
            timestamp = datetime.fromisoformat(results["timestamp"])
            st.caption(f"**Last Run:** {timestamp.strftime('%Y-%m-%d %H:%M')}")
            st.caption(f"**Status:** <span class='status-indicator status-active'></span>Active", unsafe_allow_html=True)
        except:
            st.caption(f"Last run: {results['timestamp']}")
    else:
        st.caption("**Status:** <span class='status-indicator status-inactive'></span>Showcase Mode", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📡 Data Sources")
    st.caption("• Supply Chain Dive (Placeholder)")
    st.caption("• FreightWaves (Placeholder)")
    
    st.markdown("---")
    st.markdown("### ⚠️ Showcase Notice")
    st.caption("This is a showcase version. Full implementation available upon request.")
    
    st.markdown("---")
    auto_refresh = st.checkbox("🔄 Auto-refresh (30s)", value=False)

# ========== OVERVIEW METRICS SECTION ==========
if disruptions:
    st.markdown('<div class="section-header">📈 Overview Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        critical = [d for d in disruptions if d.get("severity", 0) >= 8]
        st.markdown(f"""
            <div class="metric-card metric-critical">
                <div style="font-size: 2rem; font-weight: 700; color: #d32f2f;">{len(critical)}</div>
                <div style="color: #666; margin-top: 0.5rem;">🔴 Critical Disruptions</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        high = [d for d in disruptions if 5 <= d.get("severity", 0) < 8]
        st.markdown(f"""
            <div class="metric-card metric-high">
                <div style="font-size: 2rem; font-weight: 700; color: #f57c00;">{len(high)}</div>
                <div style="color: #666; margin-top: 0.5rem;">🟠 High Priority</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        medium = [d for d in disruptions if 3 <= d.get("severity", 0) < 5]
        st.markdown(f"""
            <div class="metric-card metric-medium">
                <div style="font-size: 2rem; font-weight: 700; color: #fbc02d;">{len(medium)}</div>
                <div style="color: #666; margin-top: 0.5rem;">🟡 Medium Impact</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        low = [d for d in disruptions if d.get("severity", 0) < 3]
        st.markdown(f"""
            <div class="metric-card metric-low">
                <div style="font-size: 2rem; font-weight: 700; color: #388e3c;">{len(low)}</div>
                <div style="color: #666; margin-top: 0.5rem;">🟢 Low Impact</div>
            </div>
        """, unsafe_allow_html=True)
    
    # ========== ACTIVE DISRUPTIONS SECTION ==========
    st.markdown('<div class="section-header">⚠️ Active Disruptions</div>', unsafe_allow_html=True)
    
    # Filter options
    col_filter1, col_filter2 = st.columns([3, 1])
    with col_filter1:
        search_term = st.text_input("🔍 Search disruptions...", placeholder="Search by name, location, or carrier", key="search")
    with col_filter2:
        severity_filter = st.selectbox("Filter by Severity", ["All", "Critical (8-10)", "High (5-7)", "Medium (3-4)", "Low (1-2)"], key="severity_filter")
    
    # Filter disruptions
    filtered_disruptions = disruptions
    if search_term:
        filtered_disruptions = [d for d in filtered_disruptions if 
                              search_term.lower() in d.get("event_name", "").lower() or
                              search_term.lower() in d.get("location_iso", "").lower() or
                              any(search_term.lower() in c.lower() for c in d.get("carriers_affected", []))]
    
    if severity_filter != "All":
        if "Critical" in severity_filter:
            filtered_disruptions = [d for d in filtered_disruptions if d.get("severity", 0) >= 8]
        elif "High" in severity_filter:
            filtered_disruptions = [d for d in filtered_disruptions if 5 <= d.get("severity", 0) < 8]
        elif "Medium" in severity_filter:
            filtered_disruptions = [d for d in filtered_disruptions if 3 <= d.get("severity", 0) < 5]
        elif "Low" in severity_filter:
            filtered_disruptions = [d for d in filtered_disruptions if d.get("severity", 0) < 3]
    
    # Sort by severity
    filtered_disruptions = sorted(filtered_disruptions, key=lambda x: x.get("severity", 0), reverse=True)
    
    # Display filtered disruptions
    if filtered_disruptions:
        for disruption in filtered_disruptions:
            severity = disruption.get("severity", 0)
            badge_class = "badge-critical" if severity >= 8 else "badge-high" if severity >= 5 else "badge-medium" if severity >= 3 else "badge-low"
            severity_label = "CRITICAL" if severity >= 8 else "HIGH" if severity >= 5 else "MEDIUM" if severity >= 3 else "LOW"
            
            st.markdown(f"""
                <div class="disruption-card">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                        <div>
                            <h3 style="margin: 0; font-size: 1.3rem; color: #1a1a1a;">
                                {get_severity_emoji(severity)} {disruption.get('event_name', 'Unknown Event')}
                            </h3>
                            <span class="severity-badge {badge_class}">{severity_label} - {severity}/10</span>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                        <div>
                            <strong>📍 Location:</strong> <code>{disruption.get('location_iso', 'N/A')}</code>
                        </div>
                        <div>
                            <strong>🚢 Carriers:</strong> {', '.join(disruption.get('carriers_affected', ['N/A']))}
                        </div>
                    </div>
                    <div style="margin-bottom: 1rem;">
                        <strong>📝 Summary:</strong>
                        <p style="color: #666; margin-top: 0.5rem;">{disruption.get('summary', 'No summary available')}</p>
                    </div>
                    <div>
                        <a href="{disruption.get('source_url', '#')}" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 600;">
                            📰 Read Full Article →
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No disruptions match your search criteria.")
    
    # ========== GEOGRAPHIC INSIGHTS SECTION ==========
    st.markdown('<div class="section-header">🌍 Geographic Insights</div>', unsafe_allow_html=True)
    
    locations = [d.get("location_iso", "Unknown") for d in disruptions]
    location_counts = Counter(locations)
    
    col_geo1, col_geo2 = st.columns([2, 1])
    
    with col_geo1:
        st.markdown("**Most Affected Regions:**")
        for loc, count in location_counts.most_common(10):
            st.markdown(f"• **{loc}**: {count} disruption(s)")
    
    with col_geo2:
        st.markdown("**Regional Breakdown:**")
        st.json(dict(location_counts))
    
    # ========== CARRIER ANALYSIS SECTION ==========
    st.markdown('<div class="section-header">🚢 Carrier Impact Analysis</div>', unsafe_allow_html=True)
    
    all_carriers = []
    for d in disruptions:
        all_carriers.extend(d.get("carriers_affected", []))
    
    if all_carriers:
        carrier_counts = Counter(all_carriers)
        col_carrier1, col_carrier2 = st.columns(2)
        
        with col_carrier1:
            st.markdown("**Most Affected Carriers:**")
            for carrier, count in carrier_counts.most_common(5):
                st.markdown(f"• **{carrier}**: {count} disruption(s)")
        
        with col_carrier2:
            st.markdown("**Carrier Statistics:**")
            st.metric("Unique Carriers Affected", len(carrier_counts))
            st.metric("Total Carrier Mentions", len(all_carriers))
    else:
        st.info("No carrier data available")

else:
    # ========== EMPTY STATE ==========
    st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📭</div>
            <h2 style="color: #666; margin-bottom: 1rem;">No Disruptions Detected</h2>
            <p style="color: #999; margin-bottom: 2rem;">This is a showcase version - execution is disabled</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📖 What does the system monitor?"):
        st.markdown("""
        The Supply Chain Sentinel monitors RSS feeds for:
        - 🚢 Port closures or disruptions
        - ⚠️ Carrier strikes or labor issues
        - 🌊 Natural disasters affecting logistics
        - 🗺️ Trade route disruptions
        - 📦 Carrier service changes or delays
        - ⏱️ Shipping delays and capacity issues
        - 📋 Trade policy changes affecting supply chains
        
        **SHOWCASE NOTE**: In the full version, this system actively monitors and extracts
        real-time disruptions from logistics news sources.
        """)
    
    with st.expander("ℹ️ About This Showcase"):
        st.markdown("""
        This showcase version demonstrates:
        - **UI/UX Design**: Modern Streamlit dashboard with premium styling
        - **Architecture**: Multi-agent AI system structure
        - **Code Organization**: Clean, maintainable codebase
        - **Data Models**: Pydantic validation patterns
        
        The full working version includes:
        - Active RSS feed monitoring
        - Real-time AI agent execution
        - Complete data extraction pipeline
        - Production deployment configurations
        
        For access to the full version, please contact the repository owner.
        """)

# Auto-refresh
if auto_refresh:
    time.sleep(30)
    st.rerun()

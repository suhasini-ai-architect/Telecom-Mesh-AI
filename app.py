import streamlit as st
import time
from src.engine import executor

# 1. Page Configuration
st.set_page_config(page_title="Telecom-Mesh AI", layout="wide", page_icon="🌐")

# 2. Cache the Graph Executor to prevent reload lag
@st.cache_resource
def get_executor():
    return executor

# 3. Custom CSS for Enterprise Aesthetic and Colored Buttons
st.markdown("""
    <style>
    /* Global Styles */
    .main { background-color: #0e1117; }
    
    /* Button Base Styles */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    /* Test A - CRM (Blue) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        border: 2px solid #0078D4 !important;
        color: #0078D4 !important;
        background-color: rgba(0, 120, 212, 0.1) !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:hover {
        background-color: #0078D4 !important;
        color: white !important;
    }

    /* Test B - RAG (Green) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        border: 2px solid #28a745 !important;
        color: #28a745 !important;
        background-color: rgba(40, 167, 69, 0.1) !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:hover {
        background-color: #28a745 !important;
        color: white !important;
    }

    /* Test C - Audit (Orange) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {
        border: 2px solid #ff8c00 !important;
        color: #ff8c00 !important;
        background-color: rgba(255, 140, 0, 0.1) !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) button:hover {
        background-color: #ff8c00 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Sidebar - Governance & FinOps
with st.sidebar:
    st.title("🛡️ Governance Portal")
    st.status("System: Operational", state="complete")
    st.info("**Engine:** Phi-4-Mini")
    st.write("**Environment:** Global Telecom (Local)")
    st.divider()
    st.metric("Inference Cost", "$0.00", delta="Local Compute")
    st.caption("Zero-Trust Architecture: Data remains on-prem.")

# 5. Main UI Header
st.title("🌐 Telecom-Mesh: Enterprise AI Controller")
st.markdown("#### Intelligent Integration for ERP, CRM, and SCM Landscapes")
st.divider()

# 6. Auto-Test Scenarios
st.subheader("🚀 One-Click Scenario Testing")
test_cases = {
    "A": "What is the SLA tier for Global-IX?",
    "B": "What are the ISO27001 data encryption requirements for telecom?",
    "C": "Audit: Does INC-99 (4h downtime) violate Global-IX's Gold SLA?"
}

# Logic to handle button clicks and "Auto-fill"
if 'query_input' not in st.session_state:
    st.session_state.query_input = ""

c1, c2, c3 = st.columns(3)

if c1.button("Test A: CRM Lookup"):
    st.session_state.query_input = test_cases["A"]
if c2.button("Test B: RAG Specs"):
    st.session_state.query_input = test_cases["B"]
if c3.button("Test C: Hybrid Audit"):
    st.session_state.query_input = test_cases["C"]

# 7. Input and Execution
user_input = st.text_input("System Query:", value=st.session_state.query_input)

if user_input:
    start_time = time.time()
    with st.spinner("🤖 Agentic Mesh Reasoning..."):
        # Use the cached executor
        agent = get_executor()
        result = agent.invoke({"query": user_input})
        
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        
        st.markdown("### 📋 AI Architect Response")
        st.write(result["response"])
        
        # 8. Architect's Logic Trace
        with st.expander("🔍 View Execution Path & Telemetry"):
            col_a, col_b, col_c = st.columns(3)
            col_a.info(f"**Route:** {result['route']}")
            col_b.success(f"**Latency:** {duration}s")
            col_c.warning("**Status:** Local-Only")
            
            st.markdown("**Context Injected from Source:**")
            st.json(result["context"])
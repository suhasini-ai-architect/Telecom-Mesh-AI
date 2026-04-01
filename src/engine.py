import json
import os
from typing import TypedDict, Literal
from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, END

# Initialize the model (using the 'phi4' alias we created)
llm = OllamaLLM(model="phi4", temperature=0)

# 1. Define the State
class AgentState(TypedDict):
    query: str
    context: str
    response: str
    route: str

# 2. Define the Nodes (The Processing Steps)
def router_node(state: AgentState):
    """Analyze query and route to CRM (Structured) or RAG (Unstructured)"""
    prompt = (
        f"Analyze this telecom query: '{state['query']}'\n"
        "If it asks for specific customer data, ID, or incident status, reply 'CRM'.\n"
        "If it asks for technical specs, ISO standards, or general SLA rules, reply 'RAG'.\n"
        "Reply with ONLY the word CRM or RAG."
    )
    decision = llm.invoke(prompt).strip().upper()
    # Fallback if model gets chatty
    route = "CRM" if "CRM" in decision else "RAG"
    return {"route": route}

def crm_node(state: AgentState):
    """Simulate a database call to the ERP/CRM system"""
    with open(os.path.join("data", "erp_crm_mock.json"), "r") as f:
        data = json.load(f)
    # Fix: Return ONLY the data string or the dict, no prefix text
    return {"context": json.dumps(data, indent=2)}

def rag_node(state: AgentState):
    """Simulate a RAG lookup from technical manuals"""
    knowledge_base = {
        "source": "SLA_Policy_v2.pdf",
        "content": "Gold Tier: 99.9% uptime (max 2h downtime). Silver Tier: 6h downtime. AES-256 required."
    }
    return {"context": json.dumps(knowledge_base, indent=2)}
    
def generator_node(state: AgentState):
    """Final Synthesis: Answering as a Senior AI Architect"""
    prompt = (
        f"You are a Senior Telecom AI Architect.\n"
        f"Data Context: {state['context']}\n"
        f"User Inquiry: {state['query']}\n"
        "Provide a professional audit response. If a violation is found, highlight it."
    )
    response = llm.invoke(prompt)
    return {"response": response}

# 3. Build the Graph
workflow = StateGraph(AgentState)

workflow.add_node("router", router_node)
workflow.add_node("fetch_crm", crm_node)
workflow.add_node("fetch_rag", rag_node)
workflow.add_node("generate", generator_node)

workflow.set_entry_point("router")

# Conditional Logic for Routing
workflow.add_conditional_edges(
    "router",
    lambda x: x["route"],
    {
        "CRM": "fetch_crm",
        "RAG": "fetch_rag"
    }
)

workflow.add_edge("fetch_crm", "generate")
workflow.add_edge("fetch_rag", "generate")
workflow.add_edge("generate", END)

executor = workflow.compile()
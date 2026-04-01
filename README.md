Telecom-Mesh: Zero-Trust Enterprise AI Controller

Telecom-Mesh is a high-seniority AI architecture prototype designed for global Telecommunications and enterprise IT ecosystems.

It demonstrates how Generative AI, Agentic Workflows, and Retrieval-Augmented Generation (RAG) can be integrated into enterprise systems such as CRM, ERP, and SCM while maintaining Zero-Trust, compliance, and data sovereignty.

Business Problem

In telecom enterprises, incident auditing against SLAs and regulatory policies is:

Manual
Time-consuming
Distributed across multiple systems
Example

A network outage must be validated against:

Customer SLA (e.g., Gold Tier → 2h max downtime)
Regulatory policies
Internal incident logs
Solution: Telecom-Mesh

Telecom-Mesh introduces a Federated AI Mesh Architecture that automates:

Semantic Routing

Determines whether a query requires:

Structured data (CRM/ERP)
Unstructured data (RAG)
Compliance Auditing
Correlates incident data with SLA contracts
Generates audit-ready responses
Zero-Trust and Data Sovereignty
Uses local Small Language Models (SLMs)
Ensures sensitive data remains within enterprise boundaries
Tech Stack
Layer	Technology
LLM Engine	Ollama (Phi-4 Mini)
Orchestration	LangGraph
Frontend	Streamlit
Data Layer	JSON-based CRM/ERP + Simulated RAG
Governance	FinOps Telemetry
Architecture Overview

Telecom-Mesh operates as a multi-node AI decision graph.

Flow
User Query
Router Node (Intent Detection)
Data Source Selection
Context Aggregation
Generator Node (LLM)
Audit Response
Architecture Diagram
                  ┌────────────────────┐
                  │    User Query      │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │   Router Node      │
                  │ (Intent Analysis)  │
                  └─────────┬──────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ CRM / ERP     │   │ RAG Knowledge │   │ Policy Engine │
│ (Structured)  │   │ (Unstructured)│   │ (SLA Rules)   │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        └──────────┬────────┴────────┬──────────┘
                   ▼                 ▼
             ┌────────────────────────────┐
             │   Context Aggregator       │
             └──────────┬─────────────────┘
                        ▼
             ┌────────────────────────────┐
             │   Generator Node (LLM)     │
             └──────────┬─────────────────┘
                        ▼
             ┌────────────────────────────┐
             │ Audit Response + Insights  │
             └────────────────────────────┘
Project Structure
telecom-mesh/
├── data/
│   └── erp_crm_mock.json
├── src/
│   ├── __init__.py
│   └── engine.py
├── app.py
├── requirements.txt
└── README.md
Getting Started
Prerequisites
Python 3.10+
Ollama installed
ollama pull phi4-mini
ollama cp phi4-mini:latest phi4
Installation
git clone https://github.com/your-username/telecom-mesh.git
cd telecom-mesh
pip install -r requirements.txt
Run the Application
streamlit run app.py
Key Features
Agentic AI (LangGraph)
Stateful workflow orchestration
Multi-step reasoning across systems
FinOps and Observability
Tracks latency
Tracks token usage
Tracks cost
Zero-Trust AI Design
Local inference using Ollama
No external API dependency
Enterprise Integration
Structured data (CRM/ERP)
Unstructured data (documents, policies)
Roadmap
Vector database integration (Qdrant / Pinecone)
Multi-model routing (LiteLLM)
Kubernetes deployment (Docker)
Real-time telemetry (OpenTelemetry)
Author

Suhasini Kshirsagar
Azure Solution Architect transitioning to AI Architect
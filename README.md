# Hello-NeMo-Guardrails

## Introduction

This project provides a practical, modular framework for adding **Defense-in-Depth** to Large Language Model (LLM) agents. It demonstrates how to wrap an AI agent with programmable guardrails to enforce safety, security, and policy compliance at every stage of the interaction.

The repository is structured around a **4-Layer Defense Pipeline**, allowing you to run each layer individually for testing or combined into a single **Unified Agent**.

![demo gif](./topical_demo.gif)

## The 4-Layer Defense Architecture

This repository implements a complete security pipeline consisting of four distinct layers:

| Layer | Type | Description | File in Repo |
| :--- | :--- | :--- | :--- |
| **Layer 1** | **Input Rails** | **Prompt Injection & Safety:** Detects and blocks jailbreak attempts (e.g., "Ignore previous instructions") before they reach the LLM. | `jailbreak.py` |
| **Layer 2** | **Dialog Rails** | **Planning & Topic Enforcement:** strictly defines the "Policy Allowlist." It prevents goal hijacking by ensuring the conversation stays within approved scopes (e.g., preventing political debates). | `topical.py` |
| **Layer 3** | **Execution Rails** | **Tool-Use & Permissions:** Intercepts tool calls (actions) to enforce permissions and validate arguments before execution. | `actions.py` |
| **Layer 4** | **Output Rails** | **Hallucination & Fact Checking:** Verifies the agent's response against a Knowledge Base or ground truth to prevent hallucinations before the user sees the answer. | `fact_checking.py` |

## Getting Started

### Prerequisites

* Python 3.9+
* An OpenAI API Key

### Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/chirag-7/Hello-NeMo-Guardrails.git](https://github.com/chirag-7/Hello-NeMo-Guardrails.git)
    cd Hello-NeMo-Guardrails
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up your OpenAI API key:
    ```bash
    export OPENAI_API_KEY=sk-...
    ```

---

## Run the Unified Agent (All 4 Layers)

The **Unified Agent** combines all four security layers into a single application. It enforces jailbreak detection, topic boundaries, tool permissions, and fact-checking simultaneously.

**Run the command:**
```bash
python unified_agent.py

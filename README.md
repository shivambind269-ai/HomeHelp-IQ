# HomeHelp IQ

## Overview

HomeHelp IQ is a multi-agent home maintenance assistant that helps users diagnose household issues, assess urgency, receive safety recommendations, estimate repair costs, and generate technician-ready work orders.

The project demonstrates a reasoning-based agent workflow with a knowledge retrieval layer inspired by Microsoft Foundry IQ concepts.

---

## Problem Statement

Homeowners often struggle to:

* Identify the type of issue
* Understand the urgency level
* Follow proper safety procedures
* Estimate repair costs
* Communicate clearly with technicians

HomeHelp IQ provides a single interface that coordinates multiple AI-inspired agents to solve these problems.

---

## Multi-Agent Architecture

1. Issue Detection Agent
2. Urgency Assessment Agent
3. Safety Recommendation Agent
4. Cost Estimation Agent
5. Knowledge Retrieval Agent
6. Work Order Generation Agent

---

## Features

* Home issue classification
* Urgency detection
* Safety recommendations
* Repair cost estimation
* Knowledge retrieval
* Technician work order generation
* Streamlit web interface

---

## Knowledge Retrieval Layer

The system includes a retrieval component that accesses a structured knowledge base containing appliance, plumbing, and electrical maintenance information.

This retrieval-first approach is inspired by Microsoft Foundry IQ principles for grounded responses.

---

## Example Workflow

Input:

My AC is not cooling properly.

Output:

* Issue Category: Air Conditioner
* Urgency Level: Medium
* Safety Advice: Switch off power before inspection
* Estimated Cost: ₹1000 - ₹5000
* Technician Work Order Generated

---

## Tech Stack

* Python
* Streamlit
* Knowledge Retrieval Layer
* Modular Multi-Agent Architecture

---

## Project Structure

HomeHelp-IQ/

* app.py
* agents/

  * issue_agent.py
  * urgency_agent.py
  * safety_agent.py
  * cost_agent.py
  * retrieval_agent.py
  * workorder_agent.py
* data/

  * knowledge_base.txt
* requirements.txt
* README.md

---

## Installation

pip install -r requirements.txt

streamlit run app.py

---

## Future Enhancements

* Azure AI Foundry integration
* Foundry IQ integration
* Image-based issue detection
* Voice-based reporting
* Technician recommendation engine
* PDF report generation

---

## Author

Shivam Kumar Bind

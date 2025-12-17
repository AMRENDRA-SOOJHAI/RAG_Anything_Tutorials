# Overview

GoogleAgentDevelopmentKit ADK)isaflexible,modularframework for developing, deploying, and

orchestrating AI agents. While optimized for Gemini and the Google ecosystem, ADK is deploymentagnostic, and built for compatibility with other frameworks .

# What Makes ADK Different

ADK was designed to make agent development feel more like software development, enabling developers to create, deploy, and orchestrate agentic architectures ranging from simple tasks to complex workflows .

# Key Features

<table><tr><td colspan="1" rowspan="1">Feature</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Benefits</td></tr><tr><td colspan="1" rowspan="1">FlexibleOrchestration</td><td colspan="1" rowspan="1">Define workflows using Sequential, Parallel, Loop agents or LLM- Predictable pipelines + adaptivedriven dynamic routing</td><td colspan="1" rowspan="1">behavior</td></tr><tr><td colspan="1" rowspan="1">Multi-Agent Architecture</td><td colspan="1" rowspan="1">Build modular, scalable applications by composing specializedagents in hierarchies</td><td colspan="1" rowspan="1">Complex coordination and delegation</td></tr><tr><td colspan="1" rowspan="1">Rich Tool Ecosystem</td><td colspan="1" rowspan="1">Pre-buit tools, custom functions, 3rd-party libraries, agents-as-tools</td><td colspan="1" rowspan="1">Diverse capabilities and extensibility</td></tr><tr><td colspan="1" rowspan="1">Deployment Ready</td><td colspan="1" rowspan="1">Containerize and deploy anywhere - local, Vertex Al, Cloud Run,Docker</td><td colspan="1" rowspan="1">Production-grade scalability</td></tr><tr><td colspan="1" rowspan="1">Built-in Evaluation</td><td colspan="1" rowspan="1">Assess agent performance on final responses and executiontrajectories</td><td colspan="1" rowspan="1">Systematic testing and validation</td></tr><tr><td colspan="1" rowspan="1">Safe &amp; Secure</td><td colspan="1" rowspan="1">Implement security patterns and best practices in agent design</td><td colspan="1" rowspan="1">Trustworthy, reliableworkflows</td></tr></table>

# Agent Types

ADK provides three core agent categories built on the BaseAgent

1. LLM Agents (Agent)

<table><tr><td rowspan=1 colspan=1>Primary Function</td><td rowspan=1 colspan=1>Reasoning, Generation, Tool Use</td></tr><tr><td rowspan=1 colspan=1>Core Engine</td><td rowspan=1 colspan=1>Large Language Model LLM</td></tr><tr><td rowspan=1 colspan=1>Determinism</td><td rowspan=1 colspan=1>Non-deterministic Flexible)</td></tr><tr><td rowspan=1 colspan=1>Primary Use</td><td rowspan=1 colspan=1>Language tasks, Dynamic decisions</td></tr><tr><td rowspan=1 colspan=1>Best For</td><td rowspan=1 colspan=1>Natural language interfaces, complex logic, flexible decision-making</td></tr></table>

# 1. Workfl ow Agents

Sequential Agent ParallelAgent LoopAgent

<table><tr><td rowspan=1 colspan=1>Primary Function</td><td rowspan=1 colspan=1>Controlling Agent Execution Flow</td></tr><tr><td rowspan=1 colspan=1>Core Engine</td><td rowspan=1 colspan=1>Predefined Logic Sequence, Parallel, Loop)</td></tr><tr><td rowspan=1 colspan=1>Determinism</td><td rowspan=1 colspan=1>Deterministic Predictable)</td></tr><tr><td rowspan=1 colspan=1>Primary Use</td><td rowspan=1 colspan=1>Structured processes, Orchestration</td></tr><tr><td rowspan=1 colspan=1>Best For</td><td rowspan=1 colspan=1>Predictable execution patterns, process control</td></tr></table>

# LangGraph Agent Integration Challenge with Google ADK

The Google ADK agent serves as the main orchestrator.   
A LangGraph agent is integrated into ADK as a tool.
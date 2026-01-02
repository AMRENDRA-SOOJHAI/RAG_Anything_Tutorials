# 🚀 RAG_ANYTHING

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![CI](https://img.shields.io/badge/CI-Passing-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange)

A **production-ready Retrieval-Augmented Generation (RAG) framework** for building intelligent document understanding systems with **multimodal support**.

**Features • Installation • Quick Start • Documentation • Examples • Contributing**

---

## 📋 Overview

**RAG_ANYTHING** is a comprehensive, modular RAG framework that simplifies building retrieval-augmented generation pipelines for **diverse document types**, including:

* 📄 PDFs & DOCX
* 🖼️ Images
* 📊 Tables
* 📐 Mathematical equations
* 🧾 Structured & semi-structured data

It is built with **production deployment** in mind and integrates seamlessly with popular **vector databases** and **LLM providers**.

Users can query documents containing **interleaved text, visual diagrams, structured tables, and formulas** through one cohesive interface — making it ideal for:

* 📚 Academic research
* 📘 Technical documentation
* 💼 Enterprise knowledge bases
* 📈 Financial & analytical reports

---

## 🎯 Key Features

### 📄 Document Processing

* **Multimodal Document Processing** – Unified APIs for PDFs, DOCX, images, tables, and more
* **Universal Document Support** – Seamless handling of heterogeneous formats
* **Specialized Content Analysis** – Dedicated processors for images, tables, and equations

### 🔍 Intelligence & Retrieval

* **Advanced Retrieval** – Hybrid search, semantic chunking, context-aware retrieval
* **Knowledge Graphs** – Automatic entity extraction & graph-based reasoning
* **Adaptive Processing Modes** – MinerU-based parsing or direct content injection

### 🏗️ Architecture

* **Flexible Vector Stores** – Milvus, Pinecone, ChromaDB, FAISS
* **LLM Integration** – OpenAI, Google ADK, Anthropic, local models
* **Plug-and-Play Architecture** – Swap components without rewriting code

### ⚡ Production Ready

* **FastAPI Server** – Async processing, monitoring, error handling
* **End-to-End Pipeline** – From ingestion to intelligent Q&A
* **Direct Content Insertion** – Skip parsing with pre-processed content lists

---

## 🏗️ Algorithm & Architecture

RAG-Anything implements a **multi-stage multimodal pipeline** extending traditional RAG architectures to handle **cross-modal understanding**.

```mermaid
graph LR
A[📄 Document Parsing] --> B[🧠 Content Analysis]
B --> C[🔍 Knowledge Graph]
C --> D[🎯 Intelligent Retrieval]
```

---

## 🔄 Pipeline Stages

### 1️⃣ 📄 Document Parsing Stage

High-fidelity document extraction with adaptive content decomposition.

**Key Components:**

* ⚙️ MinerU integration for structure-aware parsing
* 🧩 Automatic segmentation into text, images, tables, equations
* 📁 Universal format support

---

### 2️⃣ 🧠 Multi‑Modal Content Understanding

Autonomous categorization with parallel execution pipelines.

**Key Components:**

* 🎯 Content-type routing
* ⚡ Concurrent multi-pipeline execution
* 🏗️ Hierarchy & layout preservation

---

### 3️⃣ 🔍 Multimodal Analysis Engine

Specialized processors for heterogeneous data:

* 🔍 Visual Content Analyzer
* 📊 Structured Data Interpreter
* 📐 Mathematical Expression Parser
* 🔧 Extensible modality handlers

---

### 4️⃣ 🔗 Multimodal Knowledge Graph Index

Transforms content into structured semantic graphs.

**Core Functions:**

* 🔍 Multi-modal entity extraction
* 🔗 Cross-modal relationship mapping
* 🏗️ Hierarchical structure preservation
* ⚖️ Weighted semantic relevance scoring

---

### 5️⃣ 🎯 Modality‑Aware Retrieval

Hybrid retrieval combining vector similarity and graph traversal.

**Retrieval Mechanisms:**

* 🔀 Vector–Graph fusion
* 📊 Modality-aware ranking
* 🔗 Relational coherence preservation

---

## 🚀 Quick Start

### 🔧 Installation

#### Option 1: Install from PyPI (Recommended)

```bash
pip install raganything
```

With optional dependencies:

```bash
pip install "raganything[all]"
pip install "raganything[image]"
pip install "raganything[text]"
pip install "raganything[image,text]"
```

---

#### Option 2: Install from Source

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone https://github.com/HKUDS/RAG-Anything.git
cd RAG-Anything
uv sync
```

If network timeout occurs:

```bash
UV_HTTP_TIMEOUT=120 uv sync
```

---

## 📦 Optional Dependencies

| Extra | Description                     |
| ----- | ------------------------------- |
| image | Image formats (Pillow required) |
| text  | TXT / MD support                |
| all   | All optional dependencies       |

---

## ⚠️ Office Document Support

Office formats require **LibreOffice**:

* **Windows**: Official installer
* **macOS**: `brew install --cask libreoffice`
* **Ubuntu/Debian**: `sudo apt install libreoffice`

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

PRs are welcome! Please follow standard contribution guidelines.

---

## ⭐ Acknowledgements

Built using:

* LangChain
* Milvus
* FastAPI
* Google ADK

---

## ❤️ Author

**Amrendra Singh**
Made with passion for AI & systems engineering.

⭐ Star this repo if you find it useful!

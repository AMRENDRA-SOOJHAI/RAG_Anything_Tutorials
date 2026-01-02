🚀 RAG_ANYTHING
Python License CI PRs Welcome

A production-ready Retrieval-Augmented Generation framework for building intelligent document understanding systems with multimodal support

Features • Installation • Quick Start • Documentation • Examples • Contributing

📋 Overview
RAG_ANYTHING is a comprehensive, modular RAG framework that simplifies building retrieval-augmented generation pipelines for diverse document types including PDFs, images, tables, and structured data. Built with production deployment in mind, it integrates seamlessly with popular vector databases and LLM providers.

🎯 Key Features
Multimodal Document Processing: Handle PDFs, DOCX, images, tables, and more with unified APIs
Flexible Vector Stores: Support for Milvus, Pinecone, ChromaDB, and FAISS
Advanced Retrieval: Hybrid search, semantic chunking, and context-aware retrieval
LLM Integration: Compatible with OpenAI, Google ADK, Anthropic, and local models
Production Ready: FastAPI server, async processing, monitoring, and error handling
Knowledge Graphs: Automatic entity extraction and graph-based reasoning
Plug-and-Play Architecture: Swap components without rewriting code
text

🚀 RAG_ANYTHING
Python License CI PRs Welcome

A production-ready Retrieval-Augmented Generation framework for building intelligent document understanding systems with multimodal support

Features • Installation • Quick Start • Documentation • Examples • Contributing

📋 Overview
RAG_ANYTHING is a comprehensive, modular RAG framework that simplifies building retrieval-augmented generation pipelines for diverse document types including PDFs, images, tables, and structured data. Built with production deployment in mind, it integrates seamlessly with popular vector databases and LLM providers.

Users can query documents containing interleaved text, visual diagrams, structured tables, and mathematical formulations through one cohesive interface. This consolidated approach makes RAG-Anything particularly valuable for academic research, technical documentation, financial reports, and enterprise knowledge management where rich, mixed-content documents demand a unified processing framework.

🎯 Key Features
📄 Document Processing
Multimodal Document Processing: Handle PDFs, DOCX, images, tables, and more with unified APIs
Universal Document Support: Seamless processing of diverse file formats
Specialized Content Analysis: Dedicated processors for images, tables, and mathematical equations
🔍 Intelligence & Retrieval
Advanced Retrieval: Hybrid search, semantic chunking, and context-aware retrieval
Knowledge Graphs: Automatic entity extraction and graph-based reasoning
Adaptive Processing Modes: Flexible MinerU-based parsing or direct content injection
🏗️ Architecture
Flexible Vector Stores: Support for Milvus, Pinecone, ChromaDB, and FAISS
LLM Integration: Compatible with OpenAI, Google ADK, Anthropic, and local models
Plug-and-Play Architecture: Swap components without rewriting code
⚡ Production Ready
FastAPI Server: Async processing, monitoring, and error handling
End-to-End Pipeline: Complete workflow from ingestion to query answering
Direct Content Insertion: Bypass parsing with pre-processed content lists
🏗️ Algorithm & Architecture
RAG-Anything implements an effective multi-stage multimodal pipeline that fundamentally extends traditional RAG architectures to seamlessly handle diverse content modalities through intelligent orchestration and cross-modal understanding.

graph LR A[📄 Document Parsing] --> B[🧠 Content Analysis] B --> C[🔍 Knowledge Graph] C --> D[🎯 Intelligent Retrieval]

text

Pipeline Stages
1. 📄 Document Parsing Stage
The system provides high-fidelity document extraction through adaptive content decomposition. It intelligently segments heterogeneous elements while preserving contextual relationships.

Key Components:

⚙️ MinerU Integration: High-fidelity document structure extraction and semantic preservation
🧩 Adaptive Content Decomposition: Automatic segmentation into text, visuals, tables, and equations
📁 Universal Format Support: Comprehensive handling of PDFs, Office documents, images, and more
2. 🧠 Multi-Modal Content Understanding & Processing
Autonomous content categorization and routing through optimized execution channels with concurrent processing pipelines.

Key Components:

🎯 Autonomous Content Categorization: Automatic identification and routing of different content types
⚡ Concurrent Multi-Pipeline Architecture: Parallel execution for maximum throughput
🏗️ Document Hierarchy Extraction: Preserves original document structure and relationships
3. 🔍 Multimodal Analysis Engine
Specialized processing units for heterogeneous data modalities:

🔍 Visual Content Analyzer
📊 Structured Data Interpreter
📐 Mathematical Expression Parser
🔧 Extensible Modality Handler
4. 🔗 Multimodal Knowledge Graph Index
Transforms document content into structured semantic representations with multi-modal entity extraction and cross-modal relationship mapping.

Core Functions:

🔍 Multi-Modal Entity Extraction: Structured knowledge graph entities with semantic annotations
🔗 Cross-Modal Relationship Mapping: Semantic connections between textual and multimodal components
🏗️ Hierarchical Structure Preservation: Maintains original document organization
⚖️ Weighted Relationship Scoring: Quantitative relevance scores based on semantic proximity
5. 🎯 Modality-Aware Retrieval
Hybrid retrieval system combining vector similarity search with graph traversal algorithms.

Retrieval Mechanisms:

🔀 Vector-Graph Fusion: Integrates semantic embeddings with structural relationships
📊 Modality-Aware Ranking: Adaptive scoring based on content type relevance
🔗 Relational Coherence Maintenance: Preserves semantic and structural relationships
🚀 Quick Start
Installation
Option 1: Install from PyPI (Recommended)
Basic installation pip install raganything

With optional dependencies for extended format support pip install 'raganything[all]' # All optional features pip install 'raganything[image]' # Image format conversion pip install 'raganything[text]' # Text file processing pip install 'raganything[image,text]' # Multiple features

text

Option 2: Install from Source
Install uv (if not already installed) curl -LsSf https://astral.sh/uv/install.sh | sh

Clone and setup the project git clone https://github.com/HKUDS/RAG-Anything.git cd RAG-Anything

Install the package and dependencies uv sync

If you encounter network timeouts UV_HTTP_TIMEOUT=120 uv sync

Run commands directly with uv uv run python examples/raganything_example.py --help

Install with optional dependencies uv sync --extra image --extra text # Specific extras uv sync --all-extras # All optional features

text

Optional Dependencies
Extra	Description
[image]	Enables BMP, TIFF, GIF, WebP processing (requires Pillow)
[text]	Enables TXT and MD files (requires ReportLab)
[all]	Includes all Python optional dependencies
⚠️ Office Document Processing Requirements
Office documents (.doc, .docx, .ppt, .pptx, .xls, .xlsx) require LibreOffice installation:

Windows: Download from official website macOS brew install --cask libreoffice

Ubuntu/Debian sudo apt-get install libreoffice

CentOS/RHEL sudo yum install libreoffice

text

Verify MinerU installation:

Check version mineru --version

Verify configuration python -c "from raganything import RAGAnything; rag = RAGAnything(); print('✅ MinerU installed properly' if rag.check_parser_installation() else '❌ MinerU installation issue')"

text

📚 Usage Examples
1️⃣ End-to-End Document Processing
import asyncio from raganything import RAGAnything, RAGAnythingConfig from lightrag.llm.openai import openai_complete_if_cache, openai_embed from lightrag.utils import EmbeddingFunc

async def main():

Set up API configuration
api_key = "your-api-key" base_url = "your-base-url" # Optional

text

Create RAGAnything configuration
config = RAGAnythingConfig( working_dir="./rag_storage", parser="mineru", # Parser selection: mineru or docling parse_method="auto", # Parse method: auto, ocr, or txt enable_image_processing=True, enable_table_processing=True, enable_equation_processing=True, )

Define LLM model function
def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs): return openai_complete_if_cache( "gpt-4o-mini", prompt, system_prompt=system_prompt, history_messages=history_messages, api_key=api_key, base_url=base_url, **kwargs, )

Define vision model function for image processing
def vision_model_func( prompt, system_prompt=None, history_messages=[], image_data=None, messages=None, **kwargs ): # If messages format is provided (multimodal VLM enhanced query) if messages: return openai_complete_if_cache( "gpt-4o", "", system_prompt=None, history_messages=[], messages=messages, api_key=api_key, base_url=base_url, **kwargs ) # Traditional single image format elif image_data: return openai_complete_if_cache( "gpt-4o", "", system_prompt=None, history_messages=[], messages=[ {"role": "system", "content": system_prompt} if system_prompt else None, { "role": "user", "content": [ {"type": "text", "text": prompt}, { "type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"} }, ], } if image_data else {"role": "user", "content": prompt}, ], api_key=api_key, base_url=base_url, **kwargs ) # Pure text format else: return llm_model_func(prompt, system_prompt, history_messages, **kwargs)

Define embedding function
embedding_func = EmbeddingFunc( embedding_dim=3072, max_token_size=8192, func=lambda texts: openai_embed( texts, model="text-embedding-3-large", api_key=api_key, base_url=base_url, ), )

Initialize RAGAnything
rag = RAGAnything( config=config, llm_model_func=llm_model_func, vision_model_func=vision_model_func, embedding_func=embedding_func, )

Process a document
await rag.process_document_complete( file_path="path/to/your/document.pdf", output_dir="./output", parse_method="auto" )

Query the processed content
Pure text query - for basic knowledge base search
text_result = await rag.aquery( "What are the main findings shown in the figures and tables?", mode="hybrid" ) print("Text query result:", text_result)

Multimodal query with specific multimodal content
multimodal_result = await rag.aquery_with_multimodal( "Explain this formula and its relevance to the document content", multimodal_content=[{ "type": "equation", "latex": "P(d|q) = \frac{P(q|d) \cdot P(d)}{P(q)}", "equation_caption": "Document relevance probability" }], mode="hybrid" ) print("Multimodal query result:", multimodal_result) if name == "main": asyncio.run(main())

text

2️⃣ Direct Multimodal Content Processing
import asyncio from lightrag import LightRAG from lightrag.llm.openai import openai_complete_if_cache, openai_embed from lightrag.utils import EmbeddingFunc from raganything.modalprocessors import ImageModalProcessor, TableModalProcessor

async def process_multimodal_content():

Set up API configuration
api_key = "your-api-key" base_url = "your-base-url" # Optional

text

Initialize LightRAG
rag = LightRAG( working_dir="./rag_storage", llm_model_func=lambda prompt, system_prompt=None, history_messages=[], **kwargs: openai_complete_if_cache( "gpt-4o-mini", prompt, system_prompt=system_prompt, history_messages=history_messages, api_key=api_key, base_url=base_url, **kwargs ), embedding_func=EmbeddingFunc( embedding_dim=3072, max_token_size=8192, func=lambda texts: openai_embed( texts, model="text-embedding-3-large", api_key=api_key, base_url=base_url ), ) ) await rag.initialize_storages()

Process an image
image_processor = ImageModalProcessor(lightrag=rag, modal_caption_func=...)

image_content = { "img_path": "path/to/image.jpg", "image_caption": ["Figure 1: Experimental results"], "image_footnote": ["Data collected in 2024"] }

description, entity_info = await image_processor.process_multimodal_content( modal_content=image_content, content_type="image", file_path="research_paper.pdf", entity_name="Experimental Results Figure" )

Process a table
table_processor = TableModalProcessor(lightrag=rag, modal_caption_func=...)

table_content = { "table_body": """ | Method | Accuracy | F1-Score | |--------|----------|----------| | RAGAnything | 95.2% | 0.94 | | Baseline | 87.3% | 0.85 | """, "table_caption": ["Performance Comparison"], "table_footnote": ["Results on test dataset"] }

description, entity_info = await table_processor.process_multimodal_content( modal_content=table_content, content_type="table", file_path="research_paper.pdf", entity_name="Performance Results Table" ) if name == "main": asyncio.run(process_multimodal_content())

text

3️⃣ Batch Processing
Process multiple documents await rag.process_folder_complete( folder_path="./documents", output_dir="./output", file_extensions=[".pdf", ".docx", ".pptx"], recursive=True, max_workers=4 )

text

4️⃣ Custom Modal Processors
from raganything.modalprocessors import GenericModalProcessor

class CustomModalProcessor(GenericModalProcessor): async def process_multimodal_content( self, modal_content, content_type, file_path, entity_name ):

Your custom processing logic
enhanced_description = await self.analyze_custom_content(modal_content) entity_info = self.create_custom_entity(enhanced_description, entity_name) return await self._create_entity_and_chunk( enhanced_description, entity_info, file_path )

text

5️⃣ Query Options
RAG-Anything provides three types of query methods:

📝 Pure Text Queries
Direct knowledge base search using LightRAG:

Different query modes for text queries text_result_hybrid = await rag.aquery("Your question", mode="hybrid") text_result_local = await rag.aquery("Your question", mode="local") text_result_global = await rag.aquery("Your question", mode="global") text_result_naive = await rag.aquery("Your question", mode="naive")

Synchronous version sync_text_result = rag.query("Your question", mode="hybrid")

text

👁️ VLM Enhanced Queries
Automatically analyze images in retrieved context using Vision Language Model:

VLM enhanced query (automatically enabled when vision_model_func is provided) vlm_result = await rag.aquery( "Analyze the charts and figures in the document", mode="hybrid"

vlm_enhanced=True is automatically set when vision_model_func is available
)

Manually control VLM enhancement vlm_enabled = await rag.aquery( "What do the images show in this document?", mode="hybrid", vlm_enhanced=True # Force enable VLM enhancement )

vlm_disabled = await rag.aquery( "What do the images show in this document?", mode="hybrid", vlm_enhanced=False # Force disable VLM enhancement )

text

Note: When documents contain images, VLM can see and analyze them directly. The system will automatically:

Retrieve relevant context containing image paths
Load and encode images as base64
Send both text context and images to VLM for comprehensive analysis
🎨 Multimodal Queries
Enhanced queries with specific multimodal content analysis:

Query with table data table_result = await rag.aquery_with_multimodal( "Compare these performance metrics with the document content", multimodal_content=[{ "type": "table", "table_data": """Method,Accuracy,Speed RAGAnything,95.2%,120ms Traditional,87.3%,180ms""", "table_caption": "Performance comparison" }], mode="hybrid" )

Query with equation content equation_result = await rag.aquery_with_multimodal( "Explain this formula and its relevance to the document content", multimodal_content=[{ "type": "equation", "latex": "P(d|q) = \frac{P(q|d) \cdot P(d)}{P(q)}", "equation_caption": "Document relevance probability" }], mode="hybrid" )

text

6️⃣ Loading Existing LightRAG Instance
import asyncio from raganything import RAGAnything, RAGAnythingConfig from lightrag import LightRAG from lightrag.llm.openai import openai_complete_if_cache, openai_embed from lightrag.kg.shared_storage import initialize_pipeline_status from lightrag.utils import EmbeddingFunc import os

async def load_existing_lightrag():

Set up API configuration
api_key = "your-api-key" base_url = "your-base-url" # Optional

text

First, create or load existing LightRAG instance
lightrag_working_dir = "./existing_lightrag_storage"

Check if previous LightRAG instance exists
if os.path.exists(lightrag_working_dir) and os.listdir(lightrag_working_dir): print("✅ Found existing LightRAG instance, loading...") else: print("❌ No existing LightRAG instance found, will create new one")

Create/load LightRAG instance with your configuration
lightrag_instance = LightRAG( working_dir=lightrag_working_dir, llm_model_func=lambda prompt, system_prompt=None, history_messages=[], **kwargs: openai_complete_if_cache( "gpt-4o-mini", prompt, system_prompt=system_prompt, history_messages=history_messages, api_key=api_key, base_url=base_url, **kwargs ), embedding_func=EmbeddingFunc( embedding_dim=3072, max_token_size=8192, func=lambda texts: openai_embed( texts, model="text-embedding-3-large", api_key=api_key, base_url=base_url ), ) )

Initialize storage (this will load existing data if available)
await lightrag_instance.initialize_storages() await initialize_pipeline_status()

Define vision model function
def vision_model_func(prompt, system_prompt=None, history_messages=[], image_data=None, messages=None, **kwargs): # Implementation here... pass

Now use existing LightRAG instance to initialize RAGAnything
rag = RAGAnything( lightrag=lightrag_instance, # Pass existing LightRAG instance vision_model_func=vision_model_func, )

Query existing knowledge base
result = await rag.aquery( "What data has been processed in this LightRAG instance?", mode="hybrid" ) print("Query result:", result)

Add new multimodal document to existing LightRAG instance
await rag.process_document_complete( file_path="path/to/new/multimodal_document.pdf", output_dir="./output" ) if name == "main": asyncio.run(load_existing_lightrag())

text

7️⃣ Direct Content List Insertion
For scenarios where you already have a pre-parsed content list (e.g., from external parsers or previous processing), you can directly insert it into RAGAnything without document parsing:

import asyncio from raganything import RAGAnything, RAGAnythingConfig from lightrag.llm.openai import openai_complete_if_cache, openai_embed from lightrag.utils import EmbeddingFunc

async def insert_content_list_example():

Initialize RAGAnything (setup code omitted for brevity)
rag = RAGAnything(config=config, ...)

text

Example: Pre-parsed content list from external source
content_list = [ { "type": "text", "text": "This is the introduction section of our research paper.", "page_idx": 0 }, { "type": "image", "img_path": "/absolute/path/to/figure1.jpg", # IMPORTANT: Use absolute path "image_caption": ["Figure 1: System Architecture"], "image_footnote": ["Source: Authors' original design"], "page_idx": 1 }, { "type": "table", "table_body": "| Method | Accuracy | F1-Score |\n|--------|----------|----------|\n| Ours | 95.2% | 0.94 |\n| Baseline | 87.3% | 0.85 |", "table_caption": ["Table 1: Performance Comparison"], "table_footnote": ["Results on test dataset"], "page_idx": 2 }, { "type": "equation", "latex": "P(d|q) = \frac{P(q|d) \cdot P(d)}{P(q)}", "text": "Document relevance probability formula", "page_idx": 3 }, { "type": "text", "text": "In conclusion, our method demonstrates superior performance.", "page_idx": 4 } ]

Insert the content list directly
await rag.insert_content_list( content_list=content_list, file_path="research_paper.pdf", split_by_character=None, split_by_character_only=False, doc_id=None, display_stats=True )

Query the inserted content
result = await rag.aquery( "What are the key findings and performance metrics?", mode="hybrid" ) print("Query result:", result) if name == "main": asyncio.run(insert_content_list_example())

text

Content List Format
The content_list should follow the standard format:

Content Type	Format
Text	{"type": "text", "text": "content text", "page_idx": 0}
Image	{"type": "image", "img_path": "/absolute/path/to/image.jpg", "image_caption": ["caption"], "image_footnote": ["note"], "page_idx": 1}
Table	{"type": "table", "table_body": "markdown table", "table_caption": ["caption"], "table_footnote": ["note"], "page_idx": 2}
Equation	{"type": "equation", "latex": "LaTeX formula", "text": "description", "page_idx": 3}
Generic	{"type": "custom_type", "content": "any content", "page_idx": 4}
Important Notes
⚠️ img_path: Must be an absolute path to the image file
📄 page_idx: Represents the page number where content appears (0-based indexing)
📋 Content ordering: Items are processed in the order they appear in the list

This method is particularly useful when:

You have content from external parsers (non-MinerU/Docling)
You want to process programmatically generated content
You need to insert content from multiple sources into a single knowledge base
You have cached parsing results that you want to reuse
🤝 Contributing
We welcome contributions! Please see CONTRIBUTING.md for guidelines.

📄 License
This project is licensed under the MIT License - see LICENSE file.

🙏 Acknowledgments
Built with:

LangChain for orchestration
Milvus for vector storage
FastAPI for serving
Google ADK for agent frameworks
⭐ Star this repo if you find it helpful!

Made with ❤️ by Amrendra Singh

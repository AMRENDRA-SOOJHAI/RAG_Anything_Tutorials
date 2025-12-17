import asyncio
from raganything import RAGAnything, RAGAnythingConfig
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc
import os

API_KEY="YOUR_OPENAI_API_KEY"

## MILVUS LITE---------

MILVUS_URI = "uri"
MILVUS_TOKEN = "my_token"
MILVUS_DB_NAME= "db_name"


###- NEO4J---------
NEO4J_URI = "uri"
NEO4J_USERNAME = "username"
NEO4J_PASSWORD = "password"


def build_rag():
    # # Make LightRAG (inside raganything) use Milvus Server
    os.environ["MILVUS_URI"] = MILVUS_URI
    os.environ["MILVUS_TOKEN"] = MILVUS_TOKEN
    os.environ["MILVUS_DB_NAME"] = MILVUS_DB_NAME
    os.environ["NEO4J_URI"] = NEO4J_URI
    os.environ["NEO4J_USERNAME"] = NEO4J_USERNAME
    os.environ["NEO4J_PASSWORD"] = NEO4J_PASSWORD

    lightrag_kwargs = {
        # Force Milvus backend (avoid default NanoVectorDB)
        "graph_storage": "Neo4JStorage",
        "vector_storage": "MilvusVectorDBStorage",
        "vector_db_storage_cls_kwargs": {
            "uri": MILVUS_URI,
            "token": MILVUS_TOKEN,
            "db_name": MILVUS_DB_NAME,
        }
    }

## Config fro raganything in this it uses working directory and enabeled features.
    config = RAGAnythingConfig(
        working_dir="./rag_storage_milvus_graph",
        parser="generic",
        parse_method="auto",
        enable_image_processing=True,
        enable_table_processing=True,
        enable_equation_processing=True,
    )

    def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs):
        return openai_complete_if_cache(
            "gpt-4o",
            prompt,
            system_prompt=system_prompt,
            history_messages=history_messages,
            api_key=API_KEY,
        )

    #from official docs VISION FUNCTION
    def vision_model_func(prompt, system_prompt=None, history_messages=[], image_data=None, messages=None, **kwargs):
        if messages:
            return openai_complete_if_cache("gpt-4o", "", messages=messages, api_key=API_KEY, **kwargs)
        
        elif image_data:
            return openai_complete_if_cache(
                "gpt-4o",
                "",
                messages=[
                    {"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                    ]}
                ],
                api_key=API_KEY,
                **kwargs,
            )
        else:
            return llm_model_func(prompt, system_prompt, history_messages, **kwargs)


    embedding_func = EmbeddingFunc(
        embedding_dim=3072,
        max_token_size=8192,
        func=lambda texts: openai_embed(
            texts,
            model="text-embedding-3-large",
            api_key=API_KEY,
        ))

    return RAGAnything(
        config=config,
        llm_model_func=llm_model_func,
        vision_model_func=vision_model_func,
        embedding_func=embedding_func,
        lightrag_kwargs=lightrag_kwargs,

    )


async def main():

    rag = build_rag()

    ### Ingest---
    # After first ingestion comment it out.

    # await rag.process_document_complete(
    # file_path="data/input.txt",
    # output_dir="./output",
    # parse_method="auto"
    # )

    ##  Query Milvus Vector DB
    # result = await rag.aquery_with_multimodal("WHAT IS AI", mode="hybrid")
    # print("\n Query Result:\n", result)

if __name__ == "__main__":
    asyncio.run(main())
# ---------------------------------------------------

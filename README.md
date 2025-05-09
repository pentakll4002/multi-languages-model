# 🤖 Multi-Language Model Serving API
A unified interface to serve and interact with multiple powerful Large Language Models (LLMs) such as Qwen, LLaMA2, LLaMA3, Mixtral, Gemma, and DeepSeek – all via LangChain, FastAPI, and LangServe. Supports custom chaining, vector search, and multi-model routing.

## 🚀 Supported Models
```markdown
| Alias     | Model Name               |
|-----------|--------------------------|
| qwen      | Qwen-Qwen-32B            |
| llama3    | LLaMA3-70B                |
| llama2    | LLaMA2-70B                |
| mixtral   | Mixtral-8x7B             |
| gemma     | Gemma-7B                 |
| deepseek  | DeepSeek-Coder-33B       |
```

All models are connected via langchain, langchain-openai, or huggingface_hub interfaces and can be dynamically selected per request.

## 📦 Requirements
Make sure you have Python 3.10+ and install dependencies via:

```bash
pip install -r requirements.txt
```

## 🔧 Key Packages
- LangChain ecosystem: langchain, langchain_core, langchain_community, langchain_openai, langchain_huggingface, langchain_chroma, langchain_groq

- Model management: huggingface_hub, faiss-cpu, hf_xet

- Web backend: fastapi, langserve, sse_starlette, uvicorn[standard]

- Others: dotenv, python-dotenv, ipykernel, setuptools

## ⚙️ How It Works
## 🧠 Multi-LLM Routing
Each incoming request can specify a model_id, like so:

```json
{
  "model_id": "llama3",
  "prompt": "Explain quantum computing in simple terms."
}
```

The backend dynamically routes to the appropriate LLM based on this alias.

## 🗂️ Vector Store Integration
- FAISS is used for fast and efficient similarity search.

- ChromaDB and HuggingFace Hub models are also supported for embedding/vector DB use cases.

## 🔌 API Server
Start the server with:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

You can access:

- Interactive docs: http://localhost:8000/docs

- LangServe UI: http://localhost:8000/langchain/

## 📁 Project Structure (gợi ý)
```bash
multi-language-model/
├── app/
│   ├── main.py              # FastAPI + LangServe entry
│   ├── routers/
│   └── chains/
├── models/
│   └── llm_selector.py      # Handles dynamic model routing
├── vectorstores/
│   └── faiss_store.py
├── .env
├── requirements.txt
└── README.md
```

## 🧪 Example .env File
```env
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
GROQ_API_KEY=your_groq_key
```

## 📌 Todo / Roadmap
 - ✅ Multi-model switching via API

 - ✅ HuggingFace & OpenAI integration

 - ❎ Add streaming response support

 - ❎ Add fine-tuning hooks

 - ❎ Deploy with Docker + HTTPS

## 🤝 Contributing
Feel free to open issues or pull requests to improve routing logic, add new model adapters, or optimize chain performance.

## 🧠 Credits
- Powered by LangChain

- Hosted with FastAPI

- Models from HuggingFace Hub & OpenAI


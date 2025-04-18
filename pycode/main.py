from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.translate_route import router as translate_router

app = FastAPI(title="Multi-LLM API", version="1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add route
app.include_router(translate_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5300)

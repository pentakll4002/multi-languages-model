from fastapi import APIRouter, HTTPException
from request_schema import TranslationRequest
from model_selector import get_model
from translation_chain import get_translation_chain

router = APIRouter()

@router.post("/chain")
async def translate(req: TranslationRequest):
    try:
        model = get_model(req.model)
        chain = get_translation_chain(model)
        output = chain.invoke({"text": req.text, "language": req.language})
        return {"result": output}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@router.get("/models")
def list_models():
    return {
        "available_models": [
            "qwen",
            "llama3",
            "llama2",
            "mixtral",
            "gemma",
            "deepseek"
        ]
    }

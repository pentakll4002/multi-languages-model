from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    language: str
    model: str

from pydantic import BaseModel

class DesignInputs(BaseModel):
    land_size: float # in acres
    water_source: str # e.g., 'well', 'river', 'canal'
    crop_type: str

class ChatMessage(BaseModel):
    text: str
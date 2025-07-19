from pydantic import BaseModel, Field

class ItemSim(BaseModel):
    item_id: str = Field(..., example="B00008XDF3")
    score:   float

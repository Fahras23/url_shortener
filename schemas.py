from pydantic import BaseModel

class CreateUrl(BaseModel):
    inputUrl : str
    outputUrl : str
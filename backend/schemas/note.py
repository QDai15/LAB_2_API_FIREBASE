from pydantic import BaseModel

class NoteItem(BaseModel):
    user_email: str
    content: str
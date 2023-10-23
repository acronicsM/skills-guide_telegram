from pydantic import BaseModel, Field


class FromF(BaseModel):
    chat_id: int = Field(alias='id')
    is_bot: bool
    first_name: str
    last_name: str = None
    username: str
    language_code: str


class Message(BaseModel):
    message_id: int
    from_f: FromF = Field(alias='from')
    chat: dict
    date: int
    text: str


class Answer(BaseModel):
    update_id: int
    message: Message

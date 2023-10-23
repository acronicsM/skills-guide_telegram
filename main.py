from fastapi import FastAPI, Request
import uvicorn

from schemas import Answer
from message_processing import new_vacancies


# ssh -R 80:127.0.0.1:8000 nokey@localhost.run
app = FastAPI()


@app.post("/")
async def read_root(request: Request):
    result = await request.json()
    obj = Answer.model_validate(result)
    chat_id = obj.message.from_f.chat_id

    print(result)

    await new_vacancies(chat_id=chat_id)
    return 'ok'



if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)

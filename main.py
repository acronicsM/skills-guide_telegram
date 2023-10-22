from fastapi import FastAPI, Request
import uvicorn

from schemas import Answer

# ssh -R 80:localhost:8080 nokey@localhost.run
app = FastAPI()


@app.post("/")
async def read_root(request: Request):
    result = await request.json()
    print(result)
    obj = Answer.model_validate(result)
    print(obj.message.text)
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run('main.app', port=6000, host='0.0.0.0', reload=True)

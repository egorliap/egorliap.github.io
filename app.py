from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/",response_model=str)
async def hello(name:str = "noname", message:str = "nomessage"):
    return Response(content=f"Hello {name}! {message}", media_type="text/plain")
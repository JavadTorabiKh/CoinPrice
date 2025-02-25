from fastapi import FastAPI

app = FastAPI()


def my_function(name: str) -> str:
    return f"Hello, {name}!"


@app.get("/execute/{name}")
async def execute_function(name: str):
    result = my_function(name)
    return {"result": result}

# uvicorn network_api:app --reload

import uvicorn
from fastapi import FastAPI
from todoapp_backend.routes.todo import todo_router

app = FastAPI()
app.include_router(todo_router)

@app.get("/")
def main():
    return {"message": "Hellooo World!!!"}

if __name__ == "__main__":
    uvicorn.run("todoapp_backend.main:app", reload=True)
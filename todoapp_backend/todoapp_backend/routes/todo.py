from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, text, delete, update, func

from fastapi import APIRouter, Depends, HTTPException, status
from ..models.todo import Todo
from ..schemas.todo import GetTodo, PostTodo, PutTodo
from ..utils.database import get_db

todo_router = APIRouter(prefix="/api", tags=["Todo"])


@todo_router.get("/check-db-connection")
async def check_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT tablename FROM pg_tables WHERE tablename = 'test_table'"))
        table_exists = result.scalar() is not None
        if table_exists:
            return {"status": "Connection successful", "detail": "Table 'users' exists"}
        else:
            return {"status": "Connection successful", "detail": "Table 'users' does not exist"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Connection failed: {str(e)}")
    
@todo_router.get("/get-max-id")
async def get_max_id(db: AsyncSession = Depends(get_db)):
    query = select(func.max(Todo.id))
    result = await db.execute(query)
    max_id = result.scalar()
    return {"max_id": max_id}

@todo_router.get("/get-all-notes")
async def all_todos(db: AsyncSession = Depends(get_db)):
    query = select(Todo)
    result = await db.execute(query)
    todos = result.scalars().all()
    #return [GetTodo.from_orm(todo) for todo in todos]
    return [GetTodo(**todo.__dict__) for todo in todos]

@todo_router.post("/", status_code=201)
async def post_todo(body: PostTodo, db: AsyncSession = Depends(get_db)):
    todo = Todo(**body.model_dump(exclude_unset=True))
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return GetTodo(**todo.__dict__)

@todo_router.put("/{key}")
async def update_todo(key: int, body: PutTodo, db: AsyncSession = Depends(get_db)):
    #data = body.dict(exclude_unset=True)
    data = body.model_dump(exclude_unset=True)

    result = await db.execute(select(Todo).filter(Todo.id == key))
    exists = result.scalar_one_or_none()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await db.execute(update(Todo).where(Todo.id == key).values(**data))
    await db.commit()
    result = await db.execute(select(Todo).filter(Todo.id == key))
    exists = result.scalar_one_or_none()
    return exists

@todo_router.delete("/{key}", status_code=204)
async def delete_todo(key: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).filter(Todo.id == key))
    exists = result.scalar_one_or_none()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await db.execute(delete(Todo).where(Todo.id == key))
    await db.commit()
    return "Todo is deleted successfully."
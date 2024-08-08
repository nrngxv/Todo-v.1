from fastapi import FastAPI, HTTPException
from models import Todo
from data import todos
from models import Todo, Category

app = FastAPI()


#main routing
@app.get("/")
def index() -> dict[str, dict[int, Todo]]:
    return {"todos": todos}

#routing to a specific todo
@app.get("/todo/{todo_id}")
def get_todo_id(todo_id: int) -> Todo:

    #checking if todo_id exists
    if todo_id not in todos:
        raise HTTPException(status_code= 404, details = f"ID {todo_id} does not exist")
    else:
        return todos[todo_id]


#loading todos that are complete   
@app.get('/todos/')
def todo_completed(completed: bool | None=None) -> dict[str, list[Todo]]:
	complete_todo = [todo for todo in todos.values() if todo.completed is completed]
	return {'todos': complete_todo}

#creating a todo
@app.post("/")
def create_todo(todo: Todo) -> dict[str, Todo]:
     
    #checking if the todo item already exists in todos data structure
    if todo.id in todos:
         raise HTTPException(status_code = 400, details = f"ID{todo.id} already exists")
    
    todos[todo.id] = todo
    return {'todo': todo}

#creating a update request for the todo
@app.put("/todos/{todo.id}")
def update_todo(todo_id, todo: Todo ) -> dict[str, Todo]:
     todos[todo_id] = todo #take in the data from the new todo, and pass it the old id
     return {"todo": todo}

#creating a delete request
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int) -> dict[str, Todo]:
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail=f"ID {todo_id} does not exist")
    
    # pop: deletes the todo_id
    todo = todos.pop(todo_id)
    return {"todo": todo}
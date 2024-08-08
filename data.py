from models import Todo, Category

#organising the todo list
todos = {
    0: Todo(title = "Clean the dishes", completed =True, id=0, category = Category.PERSONAL),
    1: Todo(title = "Improve UI", completed =False, id=1, category = Category.WORK),
}

#0 is the key, TODO is the value there
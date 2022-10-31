class Todo:
    """
    Todo represents a task with a name, description, point value, and completed.

    A new Todo should have a `completed` field that defaults to `False`.
    All other attributes must be provided.

    >>> todo = Todo(name='Get Lunch', description='Need to eat.', points=0)
    >>> print(todo)
    Get Lunch (Incomplete - 0 points): Need to eat.
    >>> todo.completed = True
    >>> print(todo)
    Get Lunch (Complete - 0 points): Need to eat.
    >>> todo2 = Todo(name='Test', description='Another todo', points=1, completed=True)
    """
    def __init__(self, name, description, points, completed=False ) -> None:
        self.name=name
        self.description=description
        self.points=points
        self.completed=completed
        pass

    def __repr__(self):
        corredera = self.description
        if self.completed==True:
            corredera = self.name + " (Completed - "+str(self.points) +" points): "+ self.description
        else:
            corredera = self.name + " (Inmpleted - " +str(self.points) +" points): "+ self.description
        return str(corredera)

class TodoList:
    """
    TodoList wraps a list of Todo objects and implements some functionality that
    utilize the information from the entire collection.

    >>> todo = Todo(name='Get Lunch', description='Need to eat', points=0, completed=True)
    >>> todo2 = Todo(name='Submit Talk Proposal', description='Write and submit talk for PyCon', points=3)
    >>> todo_list = TodoList([todo, todo2])
    >>> todo_list.average_points()
    1.5
    >>> todo_list.completed()
    [Get Lunch (Complete - 0 points): Need to eat]
    >>> todo_list.incomplete()
    [Submit Talk Proposal (Incomplete - 3 points): Write and submit talk for PyCon]
    """
    def __init__(self,lista):
        self.lista=lista
    def average_points(self):
        corredera=0
        suma=0
        cantidad=0
        for todo in self.lista:
            suma=suma + todo.points
            cantidad=cantidad+1
        corredera = suma / cantidad
        return corredera
    def completed(self):
        for todo in self.lista:
            if todo.completed == True:
                print(todo.name + " (Completed - "+str(todo.points) +" points): "+ todo.description)
                # print(todo)

    def incomplete(self):
        for todo in self.lista:
            if todo.completed == False:
                print(todo.name + " (Incompleted - "+str(todo.points) +" points): "+ todo.description)
                # print(todo)
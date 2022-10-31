def take_first(todos):
    """
    take_first receives a list of todos and removes the first todo
    and returns that todo and the remaining todos in a touple

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}
    >>> todos
    [{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todos = []
    >>> take_first(todos)
    (None, [])
    """
    if not todos:
        todo = None
    else:
        todo = todo.pop(0)
    return (todo, todos)

    # todos=[{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    # {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]

    # take_first(todos)
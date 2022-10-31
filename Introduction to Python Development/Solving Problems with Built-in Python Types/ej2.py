todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]

def take_first(todos):
    task=todos[0]
    # print(task)
    todos.pop(0)
    halt=(task,todos)

    return halt

print(take_first(todos))
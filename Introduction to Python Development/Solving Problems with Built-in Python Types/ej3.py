todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]

def sum_points(todo1, todo2):
    corredera= int(todo1['points']) + int(todo2['points'])
    return corredera

print(sum_points(todos[0], todos[1]))
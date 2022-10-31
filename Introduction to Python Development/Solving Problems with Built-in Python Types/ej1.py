todo={'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}

def print_todo(todo):
    for item in todo:
        # print(todo[item],":",end='')
        print(item,": ",todo[item])
    pass

print_todo(todo)
# print("hola")

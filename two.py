def is_comment(item):
    return isinstance(item,str) and item.startswith('#')

def execute(program):
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
        else:
            print("empty Program")
            return
        pending =[]
        while program:
            item = program.pop()
            if callable(item):
                result = item(*pending)
                program.append(result)
                pending.clear()
            else:
                pending.append(item)


def fix(string):
    s = set()
    list = []
    for ch in string:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)        

string = "ashirvada"
print(fix(string))

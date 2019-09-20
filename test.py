debug_ls = ["pass","pass","error","error"]
counter = 0

signal = []
for i in debug_ls:
    counter += 1
    if i == "error":
        counter = counter-1
        signal += [counter]
        
q = ['a', 'b', 'c', 'd']
for i in signal:
    q.pop(i)


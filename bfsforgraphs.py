d={0:[1,4],1:[0,2,3],2:[1,3],3:[1,2,4],4:[0,3]}
q=[0]
vis={0}
while q:
    a=q.pop(0)
    print(a)
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i)
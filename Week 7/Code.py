#############################
#     Highest Mountains     #
#############################

def Sequence(lst): 
    res = [[(lst[0], 0)]]
    res1 = [[(lst[0], 0)]]
  
    for i in range(1, len(lst)): 
        if lst[i - 1] + 1 == lst[i]: 
            res[-1].append((lst[i], i)) 
        else:
            res.append([(lst[i], i)])
        
        if lst[i - 1] - 1 == lst[i]: 
            res1[-1].append((lst[i], i)) 
        else: 
            res1.append([(lst[i], i)])
    
    best_res, best_res1 = [], []
    for x in res:
        if x[0][0] == 1 and len(x) > len(best_res):
            best_res = x
    for x in res1:
        if x[-1][0] == 1 and len(x) > len(best_res):
            best_res1 = x 
    return best_res, best_res1

for z in range(int(input())):
    space = input()
    n, nums = int(input()), list(map(int, input().split()))
    if len(nums) == 1:
        try:
            satu = 1
            index = nums.index(1)
        except:
            satu = -1
            index = -1
        print('Case #{0}: {1} {2}'.format(z + 1, satu, index))
    else:
        raise_seq, down_seq = Sequence(nums)
        if raise_seq == [] and down_seq != []:
            print('Case #{0}: {1} {2}'.format(z + 1, down_seq[0][0], down_seq[0][1]))
        elif down_seq == [] and raise_seq != []:
            print('Case #{0}: {1} {2}'.format(z + 1, raise_seq[-1][0], raise_seq[-1][1]))
        elif down_seq == [] and raise_seq == []:
            try:
                satu = 1
                index = nums.index(1)
            except:
                satu = -1
                index = -1
            print('Case #{0}: {1} {2}'.format(z + 1, satu, index))
        elif raise_seq[-1][0] > down_seq[0][0]:
            print('Case #{0}: {1} {2}'.format(z + 1, raise_seq[-1][0], raise_seq[-1][1]))
        else:
            print('Case #{0}: {1} {2}'.format(z + 1, down_seq[0][0], down_seq[0][1]))


#############################
#        Conectivity        #
#############################

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
                return newpath
    return None

q, n = list(map(int, input().split()))
net = []
graph = {}
for _ in range(q):
    inp = input().lower().split()
    if inp[0] == 'push':
        if find_path(graph, inp[1], inp[2]) == None:
            if inp[1] not in graph:
                graph[inp[1]] = [inp[2]]
            else:
                graph[inp[1]].append(inp[2])
            if inp[2] not in graph:
                graph[inp[2]] = [inp[1]]
            else:
                graph[inp[2]].append(inp[1])
            net.append((inp[1], inp[2]))
        else:
            net.append(None)
        
    if inp[0] == 'pop':
        if net != []:
            if net[-1] != None:
                key, value = net.pop()
                graph[key].remove(value)
                graph[value].remove(key)
            else:
                net.pop()
    print(n - sum(map(lambda x : x != None, net)))
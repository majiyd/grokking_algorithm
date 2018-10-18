from collections import deque

graph = {}

graph["you"] = ['claire', 'alice', 'bob']
graph["claire"] = ['thom', 'johnny']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['thom'] = []
graph['johnny'] = []
graph['peggy'] = []



def person_is_seller(name):
    return name[-1] == 'j'

def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    checked = []
    while search_queue:
        print search_queue
        person = search_queue.popleft()
        if person_is_seller(person) and person  not in checked:
            print person + 'is a seller'
            return True
        else:
            search_queue += graph[person]
            checked.append(person)
    return False

bfs('you')
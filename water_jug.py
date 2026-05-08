from collections import deque

# İki sürahi problemi: Belirli hedef hacimler oluştur ve sırayla çöz

def get_neighbors(state, max_A, max_B):
    a, b = state
    opts = []
    if a < max_A: opts.append((max_A, b))           # A kabını doldur.
    if b < max_B: opts.append((a, max_B))           # B kabını doldur.
    if a > 0: opts.append((0, b))                   # A kabını boşalt.
    if b > 0: opts.append((a, 0))                   # B kabını boşalt.
    t = min(a, max_B - b)
    if t > 0: opts.append((a - t, b + t))           # A’dan B’ye su döker.
    t = min(b, max_A - a)
    if t > 0: opts.append((a + t, b - t))           # B’den A’ye su döker.
    return opts


def build_path(parents, start, end):
    path, node = [], end
    while node is not None:
        path.append(node)
        node = parents.get(node)
    return list(reversed(path))

            #BFS Algoritması
def breadth_first(start, end, max_A, max_B):
    q, parents = deque([start]), {start: None}
    while q:
        cur = q.popleft()
        if cur == end:
            return build_path(parents, start, end)
        for next in get_neighbors(cur, max_A, max_B):
            if next not in parents:
                parents[next] = cur
                q.append(next)
    return []

            #DFS Algoritması
def depth_first(start, end, max_A, max_B):
    stack, parents = [start], {start: None}
    while stack:
        cur = stack.pop()
        if cur == end:
            return build_path(parents, start, end)
        for next in get_neighbors(cur, max_A, max_B):
            if next not in parents:
                parents[next] = cur
                stack.append(next)
    return []


if __name__ == '__main__':
    cap_A, cap_B = 5, 3                     #Kapların hacimleri
    start = (0, 0)                          #Kapların başlangıç durumu
    goals = [(2, 0), (4, 3), (0, 1)]        #Senaryoların Hedefleri

    for goal in goals:
        print(f"Hedef: Sürahi A = {goal[0]}L, Sürahi B = {goal[1]}L")

        path_bfs = breadth_first(start, goal, cap_A, cap_B)
        if path_bfs:
            print(' BFS yolu:')
            for s in path_bfs:
                print(f'  --> A={s[0]}L, B={s[1]}L')

        path_dfs = depth_first(start, goal, cap_A, cap_B)
        if path_dfs:
            print(' DFS yolu:')
            for s in path_dfs:
                print(f'  --> A={s[0]}L, B={s[1]}L')
        print()
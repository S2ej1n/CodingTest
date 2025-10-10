import heapq

def daikstra(graph, gates, summits):
    distance = {node:float('inf') for node in graph}
    heap = []
    gates = set(gates)
    summits = set(summits)
    
    for g in gates:
        distance[g] = 0 #각 게이트들을 시작점으로
        heapq.heappush(heap, (0,g))
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if dist > distance[now]:
            continue
        
        # 산봉우리 도착시 더 이상 이동 금지
        if now in summits:
            continue
        
        for ne, w in graph[now]:
            if ne in gates:
                continue
                
            itensity = max(distance[now], w)
            if itensity < distance[ne]:
                distance[ne] = itensity 
                heapq.heappush(heap, (itensity, ne))
    
    return distance

def solution(n, paths, gates, summits):
    intensity = float('inf')
    summit = 0
    
    graph = {i:[] for i in range(1, n+1)}
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    distance = daikstra(graph, gates, summits)
    
    for s in sorted(summits):
        if (distance[s] < intensity) or (distance[s] == intensity and summit == s) :
            intensity = distance[s]
            summit = s
                
    
    answer = [summit, intensity]
    return answer
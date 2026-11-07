import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []
        for i in range(len(servers)):
            heapq.heappush(available,(servers[i],i))
        ans = []
        time = 0
        for i in range(len(tasks)):
            time = max(time,i)
            while busy and busy [0][0]<=time:
                finish,weight,index = heapq.heappop(busy)
                heapq.heappush(available,(weight,index))
            if not available:
                time = busy[0][0]
                while busy and busy [0][0]<=time:
                    finish,weight,index = heapq.heappop(busy)
                    heapq.heappush(available,(weight,index))
            weight,index = heapq.heappop(available)
            ans.append(index)
            heapq.heappush(busy,(time+tasks[i],weight,index))
        return ans
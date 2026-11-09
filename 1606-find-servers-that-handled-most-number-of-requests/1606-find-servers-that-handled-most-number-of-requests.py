import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = [] #finish time or server id store hoga
        count = [0]*k
        size = 1
        while size <k:
            size*=2
        tree = [0]*(2*size)#segment tree form hoga
        for i in range(k):
             tree[size + i] = 1
        for i in range(size - 1, 0, -1):
             tree[i] = tree[2 * i] + tree[2 * i + 1]

         # Find first available server from start
        def find_first(node, left, right, start):
            if right <= start or tree[node] == 0:
                return -1

            if right - left == 1:
                return left

            mid = (left + right) // 2

            result = find_first(2 * node, left, mid, start)

            if result != -1:
                return result

            return find_first(2 * node + 1, mid, right, start)

        # Update server availability
        def update(pos, value):
            pos += size
            tree[pos] = value

            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        for i in range(len(arrival)):

            t = arrival[i]

            # Free completed servers
            while busy and busy [0][0]<=t:
              finish,server = heapq.heappop(busy)
              update(server,1)  # it will make server available again after it completed its work
            server = find_first(1,0,size,i%k)#it will find the available server
            if server == -1:
              server = find_first(1,0,size,0)#if no server is available it will start searching from0 index.
            if server == -1:
              continue # if no available then drop the request.
            count[server]+=1
            update(server,0)#assign the request.

            finish = t+load[i]
            heapq.heappush(busy,(finish,server))#calculate finishing time

        maximum = max(count)

        return[i for i in range(k)if count[i]==maximum]#Return the busiest servers Find the maximum request count and return every server having that count.


        
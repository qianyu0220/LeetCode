class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        if max(count.values()) > (n+1) // 2:
            return ""
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)
        result = []
        prev_freq, prev_ch = 0, ""
        while heap:
            freq, ch = heapq.heappop(heap)
            result.append(ch)

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_ch))
            
            freq +=1
            prev_freq, prev_ch = freq, ch
        return "".join(result)
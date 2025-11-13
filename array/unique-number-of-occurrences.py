class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        arr.sort()
        hashmap[arr[0]] = 1
        for i in range(1, len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                hashmap[arr[i]] += 1
            else:
                hashmap[arr[i]] = 1
        occu = set()
        for cnt in hashmap.values():
            if cnt in occu:
                return False
            occu.add(cnt)
        return True
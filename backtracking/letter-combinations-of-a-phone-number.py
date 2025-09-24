class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # output = []
        # if not digits:
        #     return output
        # phone = {
        #     "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        #     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        # }
        # def backtrack(index, path):
        #     if index == len(digits):
        #         output.append("".join(path))
        #         return 
        #     for char in phone[digits[index]]:
        #         path.append(char)
        #         backtrack(index+1, path)
        #         path.pop()
        # backtrack(0, [])
        # return output
        output = []
        n = len(digits)
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        if not digits:
            return []
        def backtrack(index, path):
            if len(path) == n:
                output.append("".join(path[:]))
                return
            for char in phone[digits[index]]:
                path.append(char)
                backtrack(index+1, path)
                path.pop()
        backtrack(0, [])
        return output

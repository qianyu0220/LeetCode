class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        for char in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix)
            suggestions = []
            for j in range(i, min(i+3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[i])
            result.append(suggestions)
        return result
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ""
        output = []
        for char in searchWord:
            prefix += char
            suggestions = []
            i = bisect.bisect_left(products, prefix)
            for j in range(i, min(i+3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
            output.append(suggestions)
        return output
from collections import defaultdict
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        def helper(products, substring):
            output = []

            for product in products:
                if len(output) == 3:
                    break

                if product.startswith(substring):
                    output.append(product)

            return output

        res = []
        order = sorted(products)
        for i in range(len(searchWord)):
            substring = searchWord[:i+1]
            res.append(helper(order, substring))

        return res
                
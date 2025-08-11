class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.product = 1

        

    def add(self, num: int) -> None:
        if num:
            self.product *= num
            self.products.append(self.product)
        else:
            self.product = 1
            self.products = []
        

        

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        elif k == len(self.products):
            return self.product
        else:
            return (self.products[-1] // self.products[-k-1]  )

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
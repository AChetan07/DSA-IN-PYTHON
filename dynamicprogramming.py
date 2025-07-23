class dynamicprogramming:
    def __init__(self):
        self.memo={}
    def fibonacci(self,n):
        if n in self.memo:
            return self.memo[n]
        if n<=1:
            return n
        self.memo[n]=self.fibonacci(n-1)+self.fibonacci(n-2)
        return self.memo[n]
    def factorial(self,n):
        if n in self.memo:
            return self.memo[n]
        if n==0 and n==1:
            return 1
        self.memo[n]= n* self.factorial(n-1)
        return self.memo[n]
    
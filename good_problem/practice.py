class EX():
    def __init__(self, a) -> None:
        self.a = a
        
    def __eq__(self, __o) -> bool:
        return self.a == __o.a
    
    def __hash__(self) -> int:
        return self.a

a = EX(1)
b = EX(1)
c = {a : 1}

print(c[b])
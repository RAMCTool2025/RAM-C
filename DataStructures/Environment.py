from Types.CommonTypes import *

class Environment:
    def __init__(self):
        self.stack = []
        self.graph = {}
        self.nmap = {}
        
    def copy(self):
        env = Environment()
        env.nmap = self.nmap.copy()
        env.stack, env.graph = self.stack, self.graph
        return env
    
    def __str__(self):
        return f"Environment:\n- stack: {self.stack}\n- graph: {self.graph}\n- nmap: {self.nmap}"

    def alternationDepths(self) -> dict["Var", int]:
        def helper(X, memo):
            x = 0
            for Y in self.graph[X][2]:
                if Y not in memo: memo[Y] = helper(Y, memo)
                if memo[Y] >= x: x = memo[Y]+1
            memo[X] = x
            return x
            
        memo = {}
        for X in self.graph:
            if X not in memo: memo[X] = helper(X, memo)
        return memo
    

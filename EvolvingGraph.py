

class EvolvingGraphPageRank():
    
    def __init__(self):
        self.initial_graph = {}
        self.current_graph = {}
        self.updated_graph = {}
        self.initial_pagerank = {}
        self.current_pagerank = {}
        self.updated_pagerank = {}
        self.num_changes = 0
        
        
    def construct_initial_graph(self, filepath):
        with open("filepath") as file:
            df = file.readlines()[4:]
        for line in df:
            f, t = line.split()
            f, t = int(f), int(t) 
            if f not in self.initial_graph:
                self.initial_graph[f] = []
                self.updated_graph[f] = []
            self.initial_graph[f].append(t)
            self.updated_graph[f].append(t)
            
            
        
        
    def construct_new_graph(self, filepath):
        with open("filepath") as file:
            df = file.readlines()[4:]
        for line in df:
            f, t = line.split()
            f, t = int(f), int(t) 
        if f not in self.current_graph:
                self.current_graph[f] = []
        self.current_graph[f].append(t)
        
        
        
    def update_graph(self, method = 'Random'):
        for node in self.current_graph:
            if node in self.initial_graph:
                if sorted(self.current_graph[node]) == sorted(self.updated_graph[node]):
                    pass
            else:
                self.num_changes += 1
                if method == 'Random':
                    self.random_probing()
                    
                elif method == 'RoundRobin':
                    self.roundrobin_probing()
                    
                elif method == 'Proportional':
                    self.proportional_probing()
                
                elif method == 'Priority':
                    self.priority_probing()
                
        for node in self.initial_graph:
            if node not in self.current_graph:
                self.current_graph[node] = []
                self.num_changes += 1
                
            
            
        
        
    def PowerIteration(self, alpha, graph):
        pi_1 = {node:1/len(graph) for node in graph}
        pi_2 = {node:0 for node in graph}
        abs_diff = max([abs(pi_1[node] - pi_2[node]) for node in graph])
        while abs_diff >= 1e-9:
            for node,neigh in graph.items():
                if len(neigh) > 0:
                    for neigh_node in neigh:
                        pi_2[neigh_node] += pi_1[node]/len(neigh)
            pi_2 = {node:(1-alpha)*pi_2[node]+alpha/len(graph) for node in graph}
            abs_diff = max([abs(pi_1[node] - pi_2[node]) for node in graph])
            pi_1 = pi_2
            pi_2 = {node:0 for node in graph}
        return pi_1
        
    def random_probing(self):
        
        
        
        
        
    def roundrobin_probing(self):
        
        
        
        
    def proportional_probing(self):
        
        
        
        
    def priority_probing(self):
        
        
        
        
        
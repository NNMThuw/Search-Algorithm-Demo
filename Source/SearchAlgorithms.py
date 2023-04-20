from Space import *
from Constants import *
from queue import PriorityQueue
import math

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    father[g.start.value] = g.start.value

    while len(open_set) != 0:
        current = open_set.pop()
        closed_set.append(current)
        g.grid_cells[current].set_color(yellow)
        g.grid_cells[current].draw(sc)
        pygame.time.delay(40)

        if current == g.goal.value:
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            while father[current] != g.start.value:
                pygame.draw.line(sc,green,(g.grid_cells[current].x,g.grid_cells[current].y,),(g.grid_cells[father[current]].x,g.grid_cells[father[current]].y),3)
                current = father[current]
                g.grid_cells[current].set_color(grey)
                g.grid_cells[current].draw(sc)
                pygame.time.delay(40)
            pygame.draw.line(sc,green,(g.grid_cells[current].x,g.grid_cells[current].y,),(g.start.x,g.start.y),3)
            g.draw(sc)

            return

        for node in g.get_neighbors(g.grid_cells[current]):
            if node.value not in closed_set:
                open_set.append(node.value)
                father[node.value] = current
                node.set_color(red)
                node.draw(sc)
                pygame.time.delay(40)

        g.grid_cells[current].set_color(blue)
        g.grid_cells[current].draw(sc)
    print("Not found Solution")

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    father[g.start.value] = g.start.value

    while len(open_set) != 0:
        current = open_set[0]
        open_set.remove(current)
        closed_set.append(current)
        g.grid_cells[current].set_color(yellow)
        g.grid_cells[current].draw(sc)
        pygame.time.delay(40)

        if current == g.goal.value:
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            while father[current] != g.start.value:
                pygame.draw.line(sc,green,(g.grid_cells[current].x,g.grid_cells[current].y,),(g.grid_cells[father[current]].x,g.grid_cells[father[current]].y),3)
                current = father[current]
                g.grid_cells[current].set_color(grey)
                g.grid_cells[current].draw(sc)
                pygame.time.delay(40)
            pygame.draw.line(sc,green,(g.grid_cells[current].x,g.grid_cells[current].y,),(g.start.x,g.start.y),3)
            g.draw(sc)
            return

        for node in g.get_neighbors(g.grid_cells[current]):
            if node.value not in closed_set and node.value not in open_set:
                open_set.append(node.value)
                father[node.value] = current
                node.set_color(red)
                node.draw(sc)
                pygame.time.delay(40)

        g.grid_cells[current].set_color(blue)
        g.grid_cells[current].draw(sc)
    print("Not found Solution")

def get_distance(start:Node, goal:Node): # euclide distance
    return round(math.sqrt((start.x-goal.x)**2+(start.y-goal.y)**2),9)

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')
    open_set = {} # Item = (key = node.value, cost) 
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()

    open_set[g.start.value] = 0
    cost[g.start.value] = 0 
    father[g.start.value] = g.start.value

    while len(open_set) != 0:
        # Choose items with min cost
        key = next(iter(open_set))
        min_cost = open_set.get(key)
        for x, y in open_set.items():
            if y < min_cost:
                min_cost = y
                key = x 
        current = (key, min_cost)
        open_set.pop(key) 
        g.grid_cells[current[0]].set_color(yellow)
        g.grid_cells[current[0]].draw(sc)
        pygame.time.delay(40)
        
        if current[0] == g.goal.value:
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            temp = current[0]
            while father[temp] != g.start.value:
                pygame.draw.line(sc,green,(g.grid_cells[temp].x,g.grid_cells[temp].y,),(g.grid_cells[father[temp]].x,g.grid_cells[father[temp]].y),3)
                temp = father[temp]
                g.grid_cells[temp].set_color(grey)
                g.grid_cells[temp].draw(sc)
                pygame.time.delay(40)
            pygame.draw.line(sc,green,(g.grid_cells[temp].x,g.grid_cells[temp].y,),(g.grid_cells[father[temp]].x,g.grid_cells[father[temp]].y),3)
            g.draw(sc)
            return
        
        closed_set.append(current[0])

        for node in g.get_neighbors(g.grid_cells[current[0]]):
            if node.value not in closed_set:
                total_cost = cost[current[0]] + get_distance(g.grid_cells[current[0]], node) 
                if total_cost < cost[node.value]:
                    cost[node.value] = total_cost
                    open_set[node.value] = total_cost
                    father[node.value] = current[0]
                    node.set_color(red)
                    node.draw(sc)
                    pygame.time.delay(40)
        g.grid_cells[current[0]].set_color(blue)
        g.grid_cells[current[0]].draw(sc)
    print("Not found Solution")

def heuristic_value(g:Graph, start:Node): # Diagonal distance
    dx = abs(start.x - g.goal.x)
    dy = abs(start.y - g.goal.y)
    return dx + dy 

def Greedy(g:Graph, sc:pygame.Surface):
    print('Implement Greedy Search algorithm')
    open_set = {} # Item = (key = node.value, hcost = heuristic_value) 
    closed_set:list[int] = []
    father = [-1]*g.get_len()

    open_set[g.start.value] = heuristic_value(g, g.start) 
    father[g.start.value] = g.start.value

    while len(open_set) != 0:
        # Choose items with min cost
        key = next(iter(open_set))
        min_hcost = open_set.get(key)
        for x, y in open_set.items():
            if y < min_hcost:
                min_hcost = y
                key = x 
        current = (key, min_hcost)
        open_set.pop(key) 
        g.grid_cells[current[0]].set_color(yellow)
        g.grid_cells[current[0]].draw(sc)
        pygame.time.delay(40)
        
        if current[0] == g.goal.value:
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            temp = current[0]
            while father[temp] != g.start.value:
                pygame.draw.line(sc,green,(g.grid_cells[temp].x,g.grid_cells[temp].y,),(g.grid_cells[father[temp]].x,g.grid_cells[father[temp]].y),3)
                temp = father[temp]
                g.grid_cells[temp].set_color(grey)
                g.grid_cells[temp].draw(sc)
                pygame.time.delay(40)
            pygame.draw.line(sc,green,(g.grid_cells[temp].x,g.grid_cells[temp].y,),(g.grid_cells[father[temp]].x,g.grid_cells[father[temp]].y),3)
            g.draw(sc)
            return
        
        closed_set.append(current[0])

        for node in g.get_neighbors(g.grid_cells[current[0]]):
            if node.value not in closed_set:
                open_set[node.value] = heuristic_value(g, node) 
                father[node.value] = current[0]
                node.set_color(red)
                node.draw(sc)
                pygame.time.delay(40)

        g.grid_cells[current[0]].set_color(blue)
        g.grid_cells[current[0]].draw(sc)
    print("Not found Solution")



def AStar(g:Graph, sc:pygame.Surface):
    # UCS order by path cost g(n)
    # Greedy order by goal cost h(n)
    # A* => Order by f(n)=g(n)+h(n)
    print('Implement A* algorithm')
    open_set = {} # Item = (key = node.value, fcost) 
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    gcost = [100_000]*g.get_len() # g(n)

    open_set[g.start.value] = heuristic_value(g, g.start)
    gcost[g.start.value] = 0 
    father[g.start.value] = g.start.value

    while len(open_set) != 0:
        # Choose items with min fcost = g(n) + h(n)
        key = next(iter(open_set))
        min_fcost = open_set.get(key)
        for x, y in open_set.items():
            if y < min_fcost:
                min_fcost = y
                key = x 
        current = (key, min_fcost)
        open_set.pop(key) 
        g.grid_cells[current[0]].set_color(yellow)
        g.grid_cells[current[0]].draw(sc)
        pygame.time.delay(80)

        if current[0] == g.goal.value:
            g.start.set_color(orange)
            g.goal.set_color(purple)
            g.draw(sc)
            temp = current[0]
            while father[temp] != g.start.value:
                pygame.draw.line(sc,green,(g.grid_cells[temp].x,g.grid_cells[temp].y,),(g.grid_cells[father[temp]].x,g.grid_cells[father[temp]].y),3)
                temp = father[temp]
                g.grid_cells[temp].set_color(grey)
                g.grid_cells[temp].draw(sc)
                pygame.time.delay(80)
            pygame.draw.line(sc,green,(g.grid_cells[temp].x,g.grid_cells[temp].y,),(g.grid_cells[father[temp]].x,g.grid_cells[father[temp]].y),3)
            g.draw(sc)
            return
        
        closed_set.append(current[0])

        for node in g.get_neighbors(g.grid_cells[current[0]]):
            if node.value not in closed_set:

                total_gcost = gcost[current[0]] + get_distance(g.grid_cells[current[0]], node) # g(n)
                if total_gcost < gcost[node.value]:
                    gcost[node.value] = total_gcost
                    open_set[node.value] = total_gcost + heuristic_value(g, node)
                    father[node.value] = current[0]
                    node.set_color(red)
                    node.draw(sc)
                    pygame.time.delay(80)
        g.grid_cells[current[0]].set_color(blue)
        g.grid_cells[current[0]].draw(sc)
    print("Not found Solution")

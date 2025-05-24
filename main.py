import tkinter as tk
import itemData as ID
from PIL import ImageTk, Image
from collections import deque

# Breadht First-Search
def bfs(graph, start, target):
    visited = set()
    parent = {}
    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        if current_node in target:
            allRoute(parent, start, current_node)
            target.remove(current_node)
            if target:
                return bfs(graph, current_node, target)
            else:
                return current_node

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    parent[neighbor] = current_node

# Mengisi list allRoute dengan semua rute yang telah dicari
# Jadi hasilnya "allRoute[0]" akan memiliki Value path step ke 1 dan seterusnya
def allRoute(parent, start, target):
    eachRoute = list()
    path = [target]
    eachRoute.append(target)
    while path[-1] != start:
        eachRoute.append(parent[path[-1]])
        path.append(parent[path[-1]])
    totalRoute.append(eachRoute)

# Main
root = tk.Tk()
root.title("Super Speed Shopping Solution")
root.resizable(width=False, height=False)
root.iconbitmap("images/icon.ico")

# Variable Instanciation
searchResult = list()
groceriesCode = set()
groceriesNames = list()
placeholder = list()
mapping = list()
totalRoute = list()
taken = list()
checkboxList = list()
mapping = [[0]*13]*13
itemPlace = ID.item_place

# Pages Instanciation
intro = tk.Frame(root, width=1200, height=640, bg="#05204a")
home = tk.Frame(root, width=1200, height=640, bg="#fffdd0")
maps = tk.Frame(root, width=1200, height=640, bg="#ffffff") # panel denah

# Widget instanciation
leftHome = tk.Canvas(home,width=400, bg="#022546", borderwidth=0, highlightthickness=0)
rightHome = tk.Canvas(home,width=800, bg="#f5f3d9", borderwidth=0, highlightthickness=0)


# Page assignment
intro.grid(row=0, column=0)
home.grid(row=0, column=0)
maps.grid(row=0, column=0)

# TODO: Load the intro Panel


# Start main root frame loop
root.mainloop()
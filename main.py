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

# select all frame widgets and delete them
def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()

# Load Frame Intro awal awal dan memasukkan gambar logo dan button "SHOP!" 
def loadIntro():
    intro.pack_propagate(False)
    intro.tkraise()
    
    logoWidget = tk.Label(intro, image=logo, border=0, bg="#05204a")
    logoWidget.image = logo
    logoWidget.pack()
    logoWidget.place(relx=0.5, rely=0.45, anchor="center")
    
    shopButton = tk.Button (intro, 
                            width=25, 
                            height=3,
                            text="SHOP!",
                            fg="#000000",
                            bg="#fffdd0",
                            borderwidth=0,
                            command=loadHome)
    shopButton.pack()
    shopButton.place(relx=0.5, rely=0.92, anchor=tk.CENTER)

# Untuk menampilkan Panel Home yang isinya merupakan search bar untuk mencari barang
# dan Grocery List yang merupakan llist belanja yang akan dicari jalur terbaiknya
def loadHome():    
    clear_widgets(intro)
    home.tkraise()
    home.pack_propagate(False)
    leftHome.pack_propagate(False)
    rightHome.pack_propagate(False)
    
    logoHome.pack()
    leftHome.pack(side='left', fill='y')
    rightHome.pack(side='right', fill='y')

    searchBar.pack(fill='x')
    searchBar.place(anchor='center', rely=0.5, relx=0.5)

    searchButton.pack()
    searchButton.place(anchor=tk.CENTER, rely=0.5, relx=0.88)
    searchAdd.pack()
    searchAdd.place(rely=0.9, relwidth=0.2, relx=0.5, anchor=tk.CENTER)
    
    groceryLabel.pack()
    groceryLabel.place(anchor=tk.CENTER, relx=0.5, rely=0.05)
    groceryFrame.pack()
    groceryFrame.place(anchor='n', relx=0.5, relwidth=0.8, rely=0.08)

    # Generate Route
    homeButton = tk.Button (leftHome, 
                            width=20, 
                            height=2,
                            text="Generate Route!",
                            fg="#ffffff",
                            bg="#028140",
                            borderwidth=0,
                            command=loadMaps,
                            font=("Helvetica", 16))
    homeButton.pack()
    homeButton.place(anchor=tk.CENTER, relx= 0.5, rely=0.9)

# TODO: create loadMaps, searchItem, addItem
def addItem():
     print('hello')

def loadMaps():
     print('hello')

def searchItem():
     print('hello')


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

# Image instanciation
logo = ImageTk.PhotoImage (Image.open("images/logoSSSS.png"))
homeLogo = ImageTk.PhotoImage (Image.open("images/homeLogo.png"))

# Widget instanciation
leftHome = tk.Canvas(home,width=400, bg="#022546", borderwidth=0, highlightthickness=0)
rightHome = tk.Canvas(home,width=800, bg="#f5f3d9", borderwidth=0, highlightthickness=0)
logoHome = tk.Label(rightHome, image=homeLogo, bg="#f5f3d9")

searchBar = tk.Entry (rightHome, width=105)
searchButton = tk.Button(rightHome, command=searchItem, text="Search")
searchAdd= tk.Button(rightHome, text="ADD", command=addItem)

groceryLabel = tk.Label (leftHome, text=" Your Grocery List", fg="#ffffff", bg="#022546")
groceryFrame = tk.Frame(leftHome, bg="#f5f3d9")

# Page assignment
intro.grid(row=0, column=0)
home.grid(row=0, column=0)
maps.grid(row=0, column=0)

# Load the intro Panel
loadIntro()

# Start main root frame loop
root.mainloop()
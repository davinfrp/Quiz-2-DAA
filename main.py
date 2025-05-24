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

# Mencari item yang sudah di input dan memasukkannya ke dalam searchList, 
# Yang merupakan List yang berisi hasil search
# Lalu display hasil searchnya dengan style Dropdown
def searchItem():
    searchResult.clear()
    searchList.delete(first=0, last=searchList.size())
    searchFrame.pack()
    searchFrame.place(rely=0.55, relx=0.5, anchor=tk.N)
    searchScroll.pack(side="right", fill="y")
    sItem = searchBar.get()
    # Pencarian item
    for i in itemPlace:
        if  i[0].find(sItem)!= -1:
            searchResult.append(i)
            searchList.insert(tk.END, i[0].title())

    searchList.pack(fill="both", side='left')
    searchScroll.config(command=searchList.yview)

# Memasukkan item-item yang sudah di select di Dropdown List searchList ke grocery list
# Lalu display grocery list di kiri
def addItem():
    for i in searchList.curselection():
        if searchResult[i][0] not in groceriesNames :
            groceriesCode.add(searchResult[i][1])
            groceriesNames.append(searchResult[i][0])
            groceryList.insert(tk.END, searchResult[i][0].title())
        
    groceryScroll.pack(side=tk.RIGHT, fill='y')
    groceryList.pack(fill="x", side='left')

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

# Untuk meng-Load asset-asset yang akan dipakai di Frame Denah
def loadmapAssets():
    mapsNext.pack()
    mapsNext.place(anchor=tk.CENTER, rely=0.9, relx=0.7)
    mapsPrev.pack()
    mapsPrev.place(anchor=tk.CENTER, rely=0.9, relx=0.3)
    containerLegend.pack()
    containerLegend.place(anchor=tk.N, relx=0.5, rely=0.05, relwidth=0.85)
    containerCheck.pack()
    containerCheck.place(anchor=tk.CENTER, relx=0.5, rely= 0.5, relwidth=0.85, relheight=0.5)
    containerCheckScroll.pack(side=tk.RIGHT, fill=tk.Y)
    io = tk.Label(denah, text="A", font=("Helvetica", 18))
    io.pack(anchor=tk.CENTER)
    io.place(rely=0.4, relx=0.1)

# Untuk mengassign grid dengan gambar yang seharusnya
# Lalu display gambarnya sesuai dengan posisi di grid
def gridAssignment(imgs, columnz, rowz):
    mapping[rowz][columnz] = tk.Label(denah, width=53, height=53, bd=0, image=imgs)
    mapping[rowz][columnz].image = imgs
    mapping[rowz][columnz].grid(row=rowz,column=columnz, padx=0, pady=0)

# Untuk load asset check list di panel denah
# Check List digunakan untuk memberitahu barang apa yang sudah diambil
def loadCheckLists():
    for val in groceriesNames:
        curCheck = tk.Checkbutton(frameInside, text=f"{val.title()}", bg="#f5f3d9")
        curCheck.pack(anchor=tk.W)
        if val in taken:
            curCheck.select()

# untuk menampilkan gambar denah per kotak
# menujukkan step atau iterasi yang sedang ditelusuri
# step ke berapa adalah di ID.numStep
def Step (numStep, columnz, rowz):
    clear_widgets(denah)
    for i in ID.nodes:
        if i in ID.horizontal :
            if i in totalRoute[numStep] :
                if i == totalRoute[numStep][-1]:
                    gridAssignment(horS, columnz, rowz)
                elif i == totalRoute [numStep][0]:    
                    gridAssignment(horD, columnz, rowz)
                else:
                    gridAssignment(horOn, columnz, rowz)
            else:
                gridAssignment(horOff, columnz, rowz)
        elif i in ID.vertical :
            if i in totalRoute[numStep] :
                if i == totalRoute[numStep][-1]:
                    gridAssignment(verS, columnz, rowz)
                elif i == totalRoute [numStep][0]:    
                    gridAssignment(verD, columnz, rowz)
                else:
                    gridAssignment(vertOn, columnz, rowz)
            else:
                gridAssignment(vertOff, columnz, rowz)
        elif i in ID.empat :
            if i in totalRoute[numStep] :
                gridAssignment(empatOn, columnz, rowz)
            else:
                gridAssignment(empatOff, columnz, rowz)
        elif i in ID.rack :
            if i == 'F0':
                gridAssignment(Arack, columnz, rowz)
            elif i == 'C2':
                gridAssignment(Brack, columnz, rowz)
            elif i == 'H2':
                gridAssignment(Crack, columnz, rowz)
            elif i == 'C4':
                gridAssignment(Drack, columnz, rowz)
            elif i == 'H4':
                gridAssignment(Erack, columnz, rowz)
            elif i == 'C6':
                gridAssignment(Frack, columnz, rowz)
            elif i == 'H6':
                gridAssignment(Grack, columnz, rowz)
            elif i == 'B8':
                gridAssignment(Hrack, columnz, rowz)
            elif i == 'B10':
                gridAssignment(Irack, columnz, rowz)
            elif i == 'E8':
                gridAssignment(Jrack, columnz, rowz)
            elif i == 'E10':
                gridAssignment(Krack, columnz, rowz)
            elif i == 'I9':
                gridAssignment(Lrack, columnz, rowz)
            else:                
                gridAssignment(rack, columnz, rowz)
        elif i in ID.tiga_up :
            if i in totalRoute[numStep] :
                gridAssignment(tigaupOn, columnz, rowz)
            else:
                gridAssignment(tigaupOff, columnz, rowz)
        elif i in ID.tiga_down :
            if i in totalRoute[numStep] :
                gridAssignment(tigadownOn, columnz, rowz)
            else:
                gridAssignment(tigadownOff, columnz, rowz)
        elif i in ID.tiga_right :
            if i in totalRoute[numStep] :
                gridAssignment(tigarightOn, columnz, rowz)
            else:
                gridAssignment(tigarightOff, columnz, rowz)
        elif i in ID.tiga_left :
            if i in totalRoute[numStep] :
                gridAssignment(tigaleftOn, columnz, rowz)
            else:
                gridAssignment(tigaleftOff, columnz, rowz)
        elif i in ID.tiga_up :
            if i in totalRoute[numStep] :
                gridAssignment(tigaupOn, columnz, rowz)
            else:
                gridAssignment(tigaupOff, columnz, rowz)
        elif i in ID.right_corner:
            if i in totalRoute[numStep] :
                gridAssignment(rightcornerOn, columnz, rowz)
            else:
                gridAssignment(rightcornerOff, columnz, rowz)
        elif i in ID.left_corner :
            if i in totalRoute[numStep] :
                gridAssignment(leftcornerOn, columnz, rowz)
            else:
                gridAssignment(leftcornerOff, columnz, rowz)
        elif i == 'L1':
            gridAssignment(cashier1, columnz, rowz)
        elif i == 'L2':
            gridAssignment(cashier2, columnz, rowz)
        else :
            gridAssignment(blank, columnz, rowz)
        columnz+=1
        if columnz == 12 :
                rowz += 1
                columnz = 0
    stepLabel.configure(text=f"Step {ID.numStep + 1} / {len(totalRoute)}")
    stepLabel.pack()
    stepLabel.place(anchor=tk.CENTER, relx=0.5, rely=0.92)
    
    # Untuk menentukan string yang akan di display di kiri atas panel maps
    # String ini berisi informasi sedang ingin mengambil barang yang mana
    currentString = ""
    if totalRoute[numStep][0] != 'L1':
        for i in itemPlace :
            if totalRoute[numStep][0] == i[1] :
                if i[0] in groceriesNames :
                    taken.append(i[0])
                    currentString = currentString + f", {i[0].title()}"
        currentLabel.configure(text=f"The Next Item To Get is:\n {currentString[1:]}")
    else:
        currentLabel.configure(text="Please Pay For Your Groceries at the Cashier!")
    currentLabel.pack(padx=10)
    currentLabel.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
    clear_widgets(frameInside)
    loadCheckLists()

# Fungsi untuk Show Panel Maps yang berisi denah dengan rute yang sudah dicari, cek box, dan beberapa asset pembantu lainnya 
def loadMaps():
    #Menjalankan Algoritma Search
    last = bfs(ID.route, 'L11', groceriesCode)
    groceriesCode.add('L1')
    bfs(ID.route, last , groceriesCode)
    
    rowz = 0
    columnz = 0

    # Fungsi untuk mengganti denah rute menjadi step selanjutnya (Next = selanjutnya; prev = sebelumnya)
    def next():
        if ID.numStep + 1 != len(totalRoute) :
            ID.numStep += 1
            Step(ID.numStep, columnz, rowz)
        
    def prev():
        if ID.numStep != 0:
            ID.numStep -= 1
            Step(ID.numStep, columnz, rowz)

    def on_frame_configure(event):
        containerCheck.configure(scrollregion=containerCheck.bbox("all"))
    
    clear_widgets(home)
    maps.tkraise()
    maps.pack_propagate(False)
    
    guide.grid(row=0,column=0)
    denah.grid(row=0,column=1)
    nav.grid(row=0,column=2)
    
    mapsNext.configure(command=next)
    mapsPrev.configure(command=prev)
    
    containerCheck.create_window((0,0), window=frameInside, anchor=tk.NW)
    frameInside.bind("<Configure>", on_frame_configure)
    loadmapAssets()
    
    # Display legend di panel Maps
    tk.Label (containerLegend, text="A : Vegetables and Fruits", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=0, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="B : Cleaning Product", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=1, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="C : Toiletries", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=2, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="D : Instant Noodles", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=3, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="E : Snacks", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=4, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="F : Canned Products", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=5, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="G : Condiment", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=6, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="H : Beverages", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=7, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="I : Ice Cream", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=8, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="J : Frozen Food", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=9, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="K : Meat Station", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=10, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="L : Bread Section", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=11, column=0, sticky=tk.W)
    canvasBlueC.grid(row=12, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="Current Location/Start", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=13, column=0, sticky=tk.W)
    canvasRedC.grid(row=14, column=0, sticky=tk.W)
    tk.Label (containerLegend, text="Destination", font=("Helvetiva", 13), bg="#f5f3d9").grid(row=15, column=0, sticky=tk.W)
    
    # Menvisualisasi Step pertama
    Step(0, columnz, rowz)
    
    # Debugging
    print(len(totalRoute))
    for i in totalRoute:
        print(i)

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
cashier1 = ImageTk.PhotoImage (Image.open("images/cashier_01.png"))
cashier2 = ImageTk.PhotoImage (Image.open("images/cashier_02.png"))
empatOff = ImageTk.PhotoImage (Image.open("images/empatOff.png"))
empatOn = ImageTk.PhotoImage (Image.open("images/empatOn.png"))
horOff = ImageTk.PhotoImage (Image.open("images/horOff.png"))
horOn = ImageTk.PhotoImage (Image.open("images/horOn.png"))
vertOff = ImageTk.PhotoImage (Image.open("images/vertOff.png"))
vertOn = ImageTk.PhotoImage(Image.open("images/vertOn.png"))
leftcornerOff = ImageTk.PhotoImage (Image.open("images/leftcornerOff.png"))
leftcornerOn = ImageTk.PhotoImage (Image.open("images/leftcornerOn.png"))
rack = ImageTk.PhotoImage (Image.open("images/rack.png"))
rightcornerOff = ImageTk.PhotoImage (Image.open("images/rightcornerOff.png"))
rightcornerOn = ImageTk.PhotoImage (Image.open("images/rightcornerOn.png"))
tigadownOff = ImageTk.PhotoImage (Image.open("images/tigaDownOff.png"))
tigaleftOff = ImageTk.PhotoImage (Image.open("images/tigaLeftOff.png"))
tigarightOff = ImageTk.PhotoImage (Image.open("images/tigaRightOff.png"))
tigaupOff = ImageTk.PhotoImage (Image.open("images/tigaUpOff.png"))
tigadownOn = ImageTk.PhotoImage (Image.open("images/tigaDownOn.png"))
tigaleftOn = ImageTk.PhotoImage (Image.open("images/tigaLeftOn.png"))
tigarightOn = ImageTk.PhotoImage (Image.open("images/tigaRightOn.png"))
tigaupOn = ImageTk.PhotoImage (Image.open("images/tigaUpOn.png"))
blank = ImageTk.PhotoImage (Image.open("images/blank.png"))
verD = ImageTk.PhotoImage (Image.open("images/vertD.png"))
verS = ImageTk.PhotoImage (Image.open("images/vertS.png"))
horD = ImageTk.PhotoImage (Image.open("images/horD.png"))
horS = ImageTk.PhotoImage (Image.open("images/horS.png"))
Arack = ImageTk.PhotoImage (Image.open("images/A.png"))
Brack = ImageTk.PhotoImage (Image.open("images/B.png"))
Crack = ImageTk.PhotoImage (Image.open("images/C.png"))
Drack = ImageTk.PhotoImage (Image.open("images/D.png"))
Erack = ImageTk.PhotoImage (Image.open("images/E.png"))
Frack = ImageTk.PhotoImage (Image.open("images/F.png"))
Grack = ImageTk.PhotoImage (Image.open("images/G.png"))
Hrack = ImageTk.PhotoImage (Image.open("images/H.png"))
Irack = ImageTk.PhotoImage (Image.open("images/I.png"))
Jrack = ImageTk.PhotoImage (Image.open("images/J.png"))
Krack = ImageTk.PhotoImage (Image.open("images/K.png"))
Lrack = ImageTk.PhotoImage (Image.open("images/L.png"))

# Widget instanciation
leftHome = tk.Canvas(home,width=400, bg="#022546", borderwidth=0, highlightthickness=0)
rightHome = tk.Canvas(home,width=800, bg="#f5f3d9", borderwidth=0, highlightthickness=0)
logoHome = tk.Label(rightHome, image=homeLogo, bg="#f5f3d9")
logoHome.image = homeLogo

searchBar = tk.Entry (rightHome, width=105)
searchButton = tk.Button(rightHome, command=searchItem, text="Search")
searchFrame = tk.Frame(rightHome)
searchScroll = tk.Scrollbar(searchFrame)
searchList = tk.Listbox(searchFrame, width=100, yscrollcommand=searchScroll.set, selectmode=tk.MULTIPLE)
searchAdd= tk.Button(rightHome, text="ADD", command=addItem)

groceryFrame = tk.Frame(leftHome, bg="#f5f3d9")
groceryScroll = tk.Scrollbar(groceryFrame)
groceryList= tk.Listbox(groceryFrame, width=105, height=20, bg="#f5f3d9", yscrollcommand=groceryScroll.set)
groceryLabel = tk.Label (leftHome, text=" Your Grocery List", fg="#ffffff", bg="#022546")

guide   = tk.Canvas(maps,width=300,height=640, bg="#022546", borderwidth=0, highlightthickness=0)
denah = tk.Canvas(maps,width=640,height=640, bg="#324c44", borderwidth=0, highlightthickness=0)
nav = tk.Canvas(maps,width=260,height=640, bg="#f5f3d9", borderwidth=0, highlightthickness=0)

mapsNext = tk.Button (nav, text="Next Step ->")
mapsPrev = tk.Button (nav, text="<- Previous Step")
stepLabel = tk.Label (guide, font=("Helvetica", 16), bg="#022546", fg="#ffffff")
currentLabel = tk.Label (guide, font=("Helvetica", 16), bg="#022546", fg="#ffffff", wraplength=250)

containerCheck = tk.Canvas (guide, bg="#f5f3d9", borderwidth=0, highlightthickness=0,)
containerLegend = tk.Canvas (nav, bg="#f5f3d9",borderwidth=0, highlightthickness=0)
containerCheckScroll = tk.Scrollbar (containerCheck, width=20, borderwidth=0, highlightthickness=0, command=containerCheck.yview)
containerCheck.configure(yscrollcommand=containerCheckScroll)
frameInside = tk.Frame(containerCheck, bg="#f5f3d9")
canvasRedC = tk.Canvas (containerLegend, bg='#f5f3d9', borderwidth=0, highlightthickness=0, height=30)
canvasBlueC = tk.Canvas (containerLegend, bg='#f5f3d9', borderwidth=0, highlightthickness=0, height=30)
canvasRedC.create_oval(5,5, 20, 20, outline='#ff0d0d', fill='#ff0d0d', width=1)
canvasBlueC.create_oval(5,5, 20, 20, outline='#58f863', fill='#58f863', width=1)

# Page assignment
intro.grid(row=0, column=0)
home.grid(row=0, column=0)
maps.grid(row=0, column=0)

# Load the intro Panel
loadIntro()

# Start main root frame loop
root.mainloop()
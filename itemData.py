
#Mengintansiaisi produk-produk pada supermarket beserta letaknya pada denah yang direpresentasikan sebagai node.
item_place = [
    ('mineral water', 'B7'), ('soda', 'C7'), ('yoghurt', 'B9'), ('milk', 'C9'),
    ('magnum classic', 'B9'), ('haagen dazs cookies and cream', 'C9'), ('glico wings mochi duren', 'B11'), ('aice chocolate', 'C11'),
    ('chicken nugget', 'E7'), ('chicken wings', 'E9'), ('sausage', 'F9'),
    ('chicken breast', 'E9'), ('whole chicken', 'F9'), ('chicken thigh', 'E11'), ('beef tenderloin', 'F11'),
    ('bleach', 'B1'), ('dish soap', 'C1'), ('floor cleaner', 'D1'), ('detergent', 'E1'), ('disinfectant', 'B3'), ('toilet cleaner', 'C3'), ('air freshener', 'D3'), ('camphor', 'E3'),
    ('indomie goreng', 'B3'), ('indomie rendang', 'C3'), ('samyang buldak', 'D3'), ('samyang carbonara', 'E3'), ('mie sedap kari ayam', 'B5'), ('mie sedap goreng', 'C5'), ('indomie kari ayam', 'D5'), ('lemonilo goreng', 'E5'),
    ('corned beef', 'B5'), ('sardines chili', 'C5'), ('tuna', 'D5'), ('tuna mayo', 'E5'), ('sardines original', 'B7'), ('canned corn', 'C7'), ('canned fruits', 'E7'),
    ('soap', 'G1'), ('shampoo', 'H1'), ('toothbrush', 'I1'), ('toothpaste', 'J1'), ('mouthwash', 'G3'), ('lotion', 'H3'), ('facewash', 'I3'), ('conditioner', 'J3'),
    ('cookies', 'G3'), ('chips', 'H3'), ('chocolate bars', 'I3'), ('nuts', 'J3'), ('crackers', 'G5'), ('wafer', 'H5'), ('candy', 'I5'), ('biscuit', 'J5'),
    ('salt', 'G5'), ('sugar', 'H5'), ('blackpepper', 'I5'), ('onion powder', 'J5'), ('chili sauce', 'H7'), ('soy sauce', 'I7'), ('sweet soy sauce', 'J7'),
    ('broccoli', 'A1'), ('spinach', 'B1'), ('carrots', 'C1'), ('onions', 'D1'), ('garlic', 'E1'), ('apples', 'G1'), ('bananas', 'H1'), ('oranges', 'I1'), ('grapes', 'J1'),
    ('croissant', 'G8'), ('baguette', 'G10'), ('wheat bread', 'H7'), ('dorayaki', 'I7'), ('donut', 'J7'), ('bagel', 'H11'), ('muffin', 'I11'), ('eclair', 'J11'), ('pretzel', 'K8'), ('macaroon', 'K9'), ('pie', 'K10')
]

#Mengintansiasi node pada denah. Skala pada denah dimisalkan menjadi 12x12 node.
nodes = [
    'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11',
    'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11',
    'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
    'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11',
    'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11',
    'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11',
    'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11',
    'H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11',
    'I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11',
    'J0', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11',
    'K0', 'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11',
    'L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11',
]


#membuat dictionary yang berisi neighbor dari masing-masing node, node yang dijadikan rak produk tidak didefiniskan neighbornya.
route = {
    'A1'         : ['A2', 'B1'],
    'A2'         : ['A1', 'A3'],
    'A3'         : ['A2', 'A4', 'B3'],
    'A4'         : ['A3', 'A5'],
    'A5'         : ['A4', 'A6', 'B5'],
    'A6'         : ['A5', 'A7'],
    'A7'         : ['A6', 'A8', 'B7'],
    'A8'         : ['A7', 'A9'],
    'A9'         : ['A8', 'A10', 'B9'],
    'A10'        : ['A9', 'A11'],
    'A11'        : ['A10', 'B11'],
    'B1'         : ['A1', 'C1'],
    'B3'         : ['A3', 'C3'],
    'B5'         : ['A5', 'C5'],
    'B7'         : ['A7', 'C7'],
    'B9'         : ['A9', 'C9'],
    'B11'        : ['A11', 'C11'],
    'C1'         : ['B1', 'D1'],
    'C3'         : ['B3', 'D3'],
    'C5'         : ['B5', 'D5'],
    'C7'         : ['B7', 'D7'],
    'C9'         : ['B9', 'D9'],
    'C11'        : ['B11', 'D11'],
    'D1'         : ['C1', 'E1'],
    'D3'         : ['C3', 'E3'],
    'D5'         : ['C5', 'E5'],
    'D7'         : ['C7', 'D8', 'E7'],
    'D8'         : ['D7', 'D9'],
    'D9'         : ['C9', 'D8', 'D10', 'E9'],
    'D10'        : ['D9', 'D11'],
    'D11'        : ['C11', 'D10', 'E11'],
    'E1'         : ['D1', 'F1'],
    'E3'         : ['D3', 'F3'],
    'E5'         : ['D5', 'F5'],
    'E7'         : ['D7', 'F7'],
    'E9'         : ['D9', 'F9'],
    'E11'        : ['D11', 'E11'],
    'F1'         : ['E1', 'F2', 'G1'],
    'F2'         : ['F1', 'F3'],
    'F3'         : ['E3', 'F2', 'F4', 'G3'],
    'F4'         : ['F3', 'F5'],
    'F5'         : ['E5', 'F4', 'F6', 'G5'],
    'F6'         : ['F5', 'F7'],
    'F7'         : ['E7', 'F6', 'G7'],
    'F9'         : ['E9', 'G9'],
    'F11'        : ['E11', 'G11'],
    'G1'         : ['F1', 'H1'],
    'G3'         : ['F3', 'H3'],
    'G5'         : ['F5', 'H5'],
    'G7'         : ['F7', 'G8', 'H7'],
    'G8'         : ['G7', 'G9'],
    'G9'         : ['F9', 'G8', 'G10'],
    'G10'        : ['G9', 'G11'],
    'G11'        : ['F11', 'G10', 'H11'],
    'H1'         : ['G1', 'I1'],
    'H3'         : ['G3', 'I3'],
    'H5'         : ['G5', 'I5'],
    'H7'         : ['G7', 'I7'],
    'H11'        : ['G11', 'I11'],
    'I1'         : ['H1', 'J1'],
    'I3'         : ['H3', 'J3'],
    'I5'         : ['H5', 'J5'],
    'I7'         : ['H7', 'J7'],
    'I11'        : ['H11', 'J11'],
    'J1'         : ['I1', 'K1'],
    'J3'         : ['I3', 'K3'],
    'J5'         : ['I5', 'K5'],
    'J7'         : ['I7', 'K7'],
    'J11'        : ['I11', 'K11'],
    'K1'         : ['J1', 'K2', 'L1'],
    'K2'         : ['K1', 'K3'],
    'K3'         : ['J3', 'K2', 'K4'],
    'K4'         : ['K3', 'K5'],
    'K5'         : ['J5', 'K4', 'K6'],
    'K6'         : ['K5', 'K7'],
    'K7'         : ['J7', 'K6', 'K8'],
    'K8'         : ['K7', 'K9'],
    'K9'         : ['K8', 'K10'],    
    'K10'        : ['K9', 'K11'],
    'K11'        : ['J11', 'K10', 'L11'],
    'L1'         : ['K1'],
    'L11'        : ['K11']
}

#mendefinisikan node yang dijadikan rak pada denah.
rack = [
    'A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0', 'I0', 'J0',
    'H8', 'I8', 'J8', 'H9', 'I9', 'J9', 'H10', 'I10', 'J10',
    'B2', 'C2', 'D2', 'E2',
    'B4', 'C4', 'D4', 'E4',
    'B6', 'C6', 'D6', 'E6',
    'G2', 'H2', 'I2', 'J2',
    'G4', 'H4', 'I4', 'J4',
    'G6', 'H6', 'I6', 'J6',
    'B8', 'C8',
    'B10', 'C10',
    'E8', 'F8',
    'E10', 'F10'
]

#mendefinisikan node yang berada pada perempatan dalam denah
empat = [
    'F3', 'F5', 'D9'
]
#mendefinisikan node yang berada pada pertigaan berbentuk T terbalik
tiga_down = [
    'A3', 'A5', 'A7', 'A9'
]
#mendefinisikan node yang berada pada pertigaan berbentuk T
tiga_up = [
    'K3', 'K5', 'K7' , 'G9'
]
#mendefinisikan node yang berada pada pertigaan berbentuk T menghadap ke kanan
tiga_right = [
    'F1', 'K1', 'D7', 'G7'
]
#mendefinisikan node yang berada pada pertigaan berbentuk T menghadap ke kiri
tiga_left = [
    'F7', 'D11', 'G11', 'K11'
]
#mendefinikan node yang berada pada tikungan ke kanan
right_corner = [
    'A11'
]
#mendefinikan node yang berada pada tikungan ke kiri
left_corner = [
    'A1'
]
#mendefinikan node yang berada pada jalan yang lurus(horizontal)
horizontal = [
    'A2', 'F2', 'K2',
    'A4', 'F4', 'K4',
    'A6', 'F6', 'K6',
    'A8', 'D8', 'G8', 'K8', 'K9',
    'A10', 'D10', 'G10', 'K10'
]
#mendefinikan node yang berada pada jalan yang lurus(vertikal)
vertical = [
    'B1', 'C1', 'D1', 'E1', 'G1', 'H1', 'I1', 'J1',
    'B3', 'C3', 'D3', 'E3', 'G3', 'H3', 'I3', 'J3',
    'B5', 'C5', 'D5', 'E5', 'G5', 'H5', 'I5', 'J5',
    'B7', 'C7', 'E7', 'H7', 'I7', 'J7',
    'B9', 'C9', 'E9', 'F9',
    'B11', 'C11', 'E11', 'F11', 'H11', 'I11', 'J11',
    'L11'
]

#mendefinikan node yang kosong/tidak ada isinya
blanks = [
    'K0', 'L0', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10'
]

#menginformasikan program berada pada step ke berapa
numStep = 0
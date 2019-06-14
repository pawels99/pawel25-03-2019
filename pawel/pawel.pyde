def setup():
    size(400,400)
    global id_phto
    id_phto = loadImage("photo.jpg.jpg")
def draw():
    global  id_phto
    image(id_phto, 0,0,400,400)
    
    #były błędy literówkowe i rozszerzeniemusiałeś mieć ukryte i jak dodłeś, to zrobiło się podwójne

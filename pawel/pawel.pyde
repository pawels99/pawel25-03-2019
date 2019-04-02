def setup():
    size(400,400)
    global id_phto
    id_photo = loadImage("photo.jpg")
def draw():
    global  id_phto
    image(id_photo, 0,0,400,400)

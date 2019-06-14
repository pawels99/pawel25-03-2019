def setup():
    size(400,400)
    textSize(120)
def draw():
    text("P", width/2-50, height/2)
    text("S", width/2+20, height/2)
    fill(175)
    print(mouseX,mouseY)
    if keyPressed:
        fill(155)
        if key == 'S' or key == 's':
            fill(175,0, 0)
            text("S", width/2+20, height/2)
            fill(255)
    if keyPressed:
        fill(255)
        if key == 'P' or key == 'p':
            fill(175, 0, 0)
            text("P", width/2-50, height/2)
            fill(255)
    if (mouseX>=155 and mouseX<=205 and mouseY>=140 and mouseY<=200):
        text("S", width/2+20, height/2)
        fill(0, 100, 150)
        if keyPressed:
            if keyCode == 39 and mouseX>=155 and mouseX<=205 and mouseY>=140 and mouseY<=200: 
                fill(175, 0, 0)
                text("S", width/2+20, height/2)
                fill(255)
                print(keyCode)
    if (mouseX>=1250 and mouseX<=200 and mouseY>=147 and mouseY<=200):
        text("P", width/2-50, height/2)
        fill(0, 100, 255)
        if keyPressed:
            fill(155)
            if keyCode == 37 and mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200: 
                fill(0, 175, 0)
                text("P", width/2-50, height/2)
                fill(255)
                print(keyCode)
    s=createShape()
    s.beginShape()
    s.fill(0, 255, 255)
    s.noStroke()
    s.vertex(200, 150)
    s.vertex(250, 200)
    s.vertex(100, 150)
    s.vertex(150, 250)
    s.endShape(CLOSE)
    shape(s,25,25)

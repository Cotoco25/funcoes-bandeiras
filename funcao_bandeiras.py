from turtle import*
from time import sleep
t = Turtle()
t.speed(0)

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()


def desenha_franca():
    desenha_retangulo(-200, 200, 50, 150, "#012153") #color picker extension usado(colorzilla)
    desenha_retangulo(-150, 200, 50, 150, "white")
    desenha_retangulo(-100, 200, 50, 150, "#D00921")

desenha_franca()
sleep(1)
t.clear()

def formatacao():
    t.pensize(5)
    t.color("black")
    t.pu()
    t.goto(-450,300)
    t.pd()
    t.goto(450,300)
    t.goto(450,-300)
    t.goto(-450,-300)
    t.goto(-450,300)
    t.pensize(1)

def desenha_retangulo_cam(x, x2, y, y2, color):
    t.color(color)
    t.begin_fill()
    t.goto(x,y)
    t.goto(x,y2)
    t.goto(x2,y2)
    t.goto(x2,y)
    t.goto(x,y)
    t.end_fill()



def desenha_estrela_camaroes(size, color):
    t.pu()
    t.goto(-39,50)
    t.pd()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.lt(72)
        t.fd(size)
        t.rt(144)
    t.end_fill()


def desenha_camaroes():
    desenha_retangulo_cam(-150, -450, 300, -300, "seagreen")
    desenha_retangulo_cam(150, -150, 300, -300, "firebrick")
    desenha_retangulo_cam(450, 150, 300, -300, "yellow")
    desenha_estrela_camaroes(30, "yellow")
    formatacao()

desenha_camaroes()
sleep(1)
t.clear()

def desenha_retangulo_canada(x, x2, y, y2, color):
    t.pu()
    t.goto(x,x2)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(y,x2)
    t.goto(y,y2)
    t.goto(x,y2)
    t.goto(x,x2)
    t.end_fill()

def desenha_folha_canada(color):
    t.pu()
    t.goto(0,-200)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.rt(180)
    t.fd(10)
    t.rt(91)
    t.fd(100)
    t.lt(100)
    t.fd(100)
    t.rt(120)
    t.fd(40)
    t.lt(70)
    t.fd(100)
    t.rt(130)
    t.fd(40)
    t.lt(110)
    t.fd(70)
    t.rt(130)
    t.fd(70)
    t.lt(85)
    t.fd(35)
    t.rt(110)
    t.fd(60)
    t.lt(60)
    t.fd(6)
    t.lt(90)
    t.fd(80)
    t.rt(155)
    t.fd(40)
    t.lt(90)
    t.fd(10)
    t.lt(20)
    t.fd(70)
    t.goto(0,-200)

    t.rt(68.7)
    t.fd(10)
    t.lt(91)
    t.fd(100)
    t.rt(100)
    t.fd(100)
    t.lt(120)
    t.fd(40)
    t.rt(70)
    t.fd(100)
    t.lt(130)
    t.fd(40)
    t.rt(110)
    t.fd(70)
    t.lt(130)
    t.fd(70)
    t.rt(85)
    t.fd(35)
    t.lt(110)
    t.fd(60)
    t.rt(60)
    t.fd(6)
    t.rt(90)
    t.fd(80)
    t.lt(155)
    t.fd(40)
    t.rt(90)
    t.fd(10)
    t.rt(20)
    t.fd(70)
    t.end_fill()

def desenha_canada():
    desenha_retangulo_canada(-450, 300, -220, -300, "red")
    desenha_retangulo_canada(220, 300, 450, -300, "red")
    desenha_folha_canada("red")
    formatacao()

desenha_canada()
sleep(1)
t.clear()

t.setheading(0)

def retangulo_chile(color, x, y, x2, y2):
    t.color(color)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.goto(x2,y)
    t.rt(90)
    t.goto(x2,y2)
    t.rt(90)
    t.goto(x,y2)
    t.rt(90)
    t.goto(x,y)
    t.rt(90)
    t.end_fill()

def retangulo_branco_chile(x, y, x2, y2, color):
    t.pu()
    t.goto(x,y)
    t.pd()

    t.color(color)
    t.begin_fill()
    t.goto(x2,y)
    t.goto(x2,y2)
    t.goto(x,y2)
    t.goto(x,y)
    t.end_fill()

def estrela_chile(x, y, size, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.lt(72)
        t.fd(size)
        t.rt(144)
    t.end_fill()

def desenha_chile():
    retangulo_chile("royalblue", -450, 300, 450, -300)
    retangulo_chile("darkred", -450, 0, 450, -300)
    retangulo_branco_chile(-150, 0, 450, 300, "white")
    estrela_chile(-400, 185, 70, "white")
    formatacao()

desenha_chile()
sleep(1)
t.clear()

def retangulo_comores(x,y,x2,y2,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(x2,y)
    t.goto(x2,y2)
    t.goto(x,y2)
    t.goto(x,y)
    t.end_fill()

def triangulo_comores_verde(x,y,z,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(0,0)
    t.goto(x,z)
    t.goto(x,y)
    t.end_fill()

def meia_lua_comores(size, x, y, z, color1, color2):
    t.up()
    t.goto(x,z)
    t.begin_fill()
    t.color(color1)
    t.circle(size)
    t.end_fill()
    t.up()
    t.goto(y,z)
    t.begin_fill()
    t.color(color2)
    t.circle(size)
    t.end_fill()

def triangulo_comores(size, x, y, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.lt(72)
        t.fd(size)
        t.rt(144)
    t.end_fill()


def desenhar_comores():
    retangulo_comores(-450,300,450,150,"yellow")
    retangulo_comores(-450,0,450,-150,"red")
    retangulo_comores(-450,-150,450,-300,"blue")
    triangulo_comores_verde(-450,300,-300, "seagreen")
    meia_lua_comores(100, -320, -280, -100, "white", "seagreen")
    triangulo_comores(13, -317, 70, "white")
    triangulo_comores(13, -317, 30, "white")
    triangulo_comores(13, -317, -15, "white")
    triangulo_comores(13, -317, -60, "white")
    formatacao()

desenhar_comores()

sleep(1)
t.clear()

def retangulo_georgia(x,y,size1,size2,z,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.rt(z)
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.fd(size1)
        t.lt(90)
        t.fd(size2)
        t.lt(90)
    t.end_fill()


def simbolo_georgia(x,y):
    t.up()
    t.goto(x,y)
    t.lt(90)
    t.pd()
    t.pensize(5)
    t.color("red")
    t.begin_fill()
    for i in range(4):
        t.fd(20)
        t.rt(90)
        t.fd(40)
        t.lt(90)
        t.fd(40)
        t.rt(90)
    t.rt(90)
    t.end_fill()

def desenha_georgia():
    retangulo_georgia(-50,300,600,100,90,"red")
    t.rt(90)
    retangulo_georgia(-450,-50,900,100,180,"red")
    simbolo_georgia(-330,170)
    simbolo_georgia(-300,-200)
    simbolo_georgia(180,140)
    simbolo_georgia(180,-170)
    formatacao()

desenha_georgia()

sleep(1)
t.clear()

def desenha_irlanda():
    desenha_retangulo_cam(-150, -450, 300, -300, "seagreen")
    desenha_retangulo_cam(150, -150, 300, -300, "white")
    desenha_retangulo_cam(450, 150, 300, -300, "orange")
    formatacao()

desenha_irlanda()

sleep(1)
t.clear()

def estrela_davi(x, y, size, color):
    t.pu()
    t.goto(x,y)
    t.pd()

    t.color(color)
    t.pensize(10)

    for _ in range(3):
        t.fd(size)
        t.lt(120) 
    t.pensize(1)

def retangulo_israel(x,y,x2,y2,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color("steelblue")
    t.begin_fill()
    t.goto(x2,y)
    t.goto(x2,y2)
    t.goto(x,y2)
    t.goto(x,y)
    t.end_fill()

def desenha_israel():
    estrela_davi(-100,-50,200,"steelblue")
    t.lt(180)
    estrela_davi(100,50,200,"steelblue")
    retangulo_israel(-450,190,450,260,"steelblue")
    retangulo_israel(-450,-190,450,-260,"steelblue")
    formatacao()

desenha_israel()

sleep(1)
t.clear()

def desenha_italia():
    desenha_retangulo_cam(-150, -450, 300, -300, "seagreen")
    desenha_retangulo_cam(150, -150, 300, -300, "white")
    desenha_retangulo_cam(450, 150, 300, -300, "red")
    formatacao()

desenha_italia()

sleep(1)
t.clear()

def retangulo_monaco(x, y, x2, y2, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(x2, y)
    t.goto(x2, y2)
    t.goto(x, y2)
    t.goto(x, y)
    t.end_fill()

def desenha_monaco():
    retangulo_monaco(-450,300,450,-300,"firebrick")
    retangulo_monaco(-450,0,450,-300,"white")
    formatacao()

desenha_monaco()

sleep(1)
t.clear()

def desenha_polonia():
    retangulo_monaco(-450,300,450,-300,"white")
    retangulo_monaco(-450,0,450,-300,"firebrick")
    formatacao()

desenha_polonia()

sleep(1)
t.clear()

def desenha_nigeria():
    desenha_retangulo_cam(-150, -450, 300, -300, "seagreen")
    desenha_retangulo_cam(150, -150, 300, -300, "white")
    desenha_retangulo_cam(450, 150, 300, -300, "seagreen")
    formatacao()

desenha_nigeria()

sleep(1)
t.clear()

def desenha_quadrado_panama(x,y,z,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(y,y)
    t.goto(y,z)
    t.goto(x,z)
    t.goto(x,y)
    t.end_fill()

def estrela_panama(x,y,size,color):
    t.setheading(0)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.lt(72)
        t.fd(size)
        t.rt(144)
    t.end_fill()

def desenha_panama():
    desenha_quadrado_panama(-450,0,-300,"steelblue")
    desenha_quadrado_panama(450,0,300,"firebrick")
    estrela_panama(-325,185,70,"steelblue")
    estrela_panama(135,-120,70,"firebrick")
    formatacao()

desenha_panama()

sleep(1)
t.clear()


banco_de_bandeiras = {
    "franca": desenha_franca,
    "camaroes": desenha_camaroes,
    "canada": desenha_canada,
    "chile": desenha_chile,
    "comores": desenhar_comores,
    "georgia": desenha_georgia,
    "irlanda": desenha_irlanda,
    "israel": desenha_israel,
    "italia": desenha_italia,
    "monaco": desenha_monaco,
    "polonia": desenha_polonia,
    "nigeria": desenha_nigeria,
    "panama": desenha_panama,
}



funcao_da_bandeira = banco_de_bandeiras[textinput("Menu de Bandeiras", "Qual bandeira você quer desenhar?\n(Ex: franca, camaroes, canada, chile, comores, georgia, irlanda, israel, italia, monaco, polonia, nigeria, panama)")]
funcao_da_bandeira()

mainloop()
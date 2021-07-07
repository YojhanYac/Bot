
def resp(respBot):
    print("{:>50}".format(respBot))

def respBot(respUser):
    if "hola" in respUser.lower():
        resp("la función te dice hola!!")
    elif "chau" in respUser.lower():
        resp("Chau! :)")
    elif "bien" in respUser.lower():
        resp("buenisimo, tratemos de mejorarlo")
    elif "mal" in respUser.lower():
        resp("continuemos con un juego, te parece?")
    elif "si" in respUser.lower():
        resp("de acuerdo, qué propones?")
    elif "no" in respUser.lower():
        resp("y si mejor me haces preguntas tú?")
    elif "bueno" in respUser.lower():
        resp("comencemos!")
    else:
        resp("no hay una respuesta para lo escrito aún")

respUser = ""

resp("Holaa!")

while "chau" not in respUser.lower():
    respUser = input()
    respBot(respUser)
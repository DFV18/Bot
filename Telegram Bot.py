import requests as req


def main():
    URL_MENSAJE = "https://api.telegram.org/bot1943187472:AAHl6kFfARl1MiCIs09rEcADcZR0asEkIyY/sendMessage?chat_id=-589260794&text=Hola que tal"
    consulta = req.get(URL_MENSAJE)
    if (consulta.status_code == 200):
        print("Mensaje enviado")
    else:
        print("ERROR al enviar mensaje")


if  (__name__ == "__main__"):
     main()


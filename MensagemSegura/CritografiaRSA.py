class CritografiaRSA:

    def criptografar(self, msg, chvE, chvN):
        msg, chvE, chvN = list(msg), int(chvE), int(chvN)
        for cont in range(len(msg)):
            msg[cont] = ord(msg[cont])
            msg[cont] = (msg[cont] ** chvE) % chvN 
            msg[cont] = str(msg[cont])
        msg = " ".join(msg)
        print(f"\n{msg}")  

    def descriptografar(self, msgCrip, chvD, chvN):
        msgCrip, chvD, chvN = msgCrip.split(), int(chvD), int(chvN)
        for cont in range(len(msgCrip)):
            msgCrip[cont] = int(msgCrip[cont])
            msgCrip[cont] = (msgCrip[cont] ** chvD) % chvN
            msgCrip[cont] = chr(msgCrip[cont])   
        msgCrip = "".join(msgCrip)
        print(f"\n{msgCrip}")
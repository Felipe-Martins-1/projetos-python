import random

class GeradorSenha:
    def __init__(self, qtdCaracteres, letrasMaiusculas, letrasMinusculas, numeros, simbolos, tudo):
        self.qtdCaracteres = qtdCaracteres
        self.letrasMaiusculas = letrasMaiusculas
        self.letrasMinusculas = letrasMinusculas
        self.numeros = numeros
        self.simbolos = simbolos       
        self.tudo = tudo
        self.selecionarTipo()      

    def selecionarCaracteres(self, caracteres):
        resultado = []
        for c in range(self.qtdCaracteres): 
            caracter = caracteres[random.randint(0, len(caracteres) - 1)]
            resultado.append(caracter)
        resultado = "".join(resultado)
        print(f"\n{resultado}")
 
    def selecionarTipo(self):
        letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letrasMinusculas = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"
        simbolos = "!@#$%^&*"
        if self.letrasMaiusculas == True and self.letrasMinusculas == True and self.numeros == True and self.simbolos == True and self.tudo == True or self.tudo == True:
            self.selecionarCaracteres(letrasMaiusculas + letrasMinusculas + numeros + simbolos)  
        elif self.letrasMaiusculas == True and self.letrasMinusculas == True and self.numeros == True and self.simbolos == False:
            self.selecionarCaracteres(letrasMaiusculas + letrasMinusculas + numeros)    
        elif self.letrasMaiusculas == True and self.letrasMinusculas == True and self.numeros == False and self.simbolos == False:
            self.selecionarCaracteres(letrasMaiusculas + letrasMinusculas)
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == False and self.simbolos == False:
            self.selecionarCaracteres(letrasMaiusculas)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == False and self.simbolos == False:
            print("\nPRECISA SELECIONAR ALGUM TIPO DE CARACTERE")
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == False and self.simbolos == True:
            self.selecionarCaracteres(simbolos)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == True and self.simbolos == True:
            self.selecionarCaracteres(numeros + simbolos)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == True and self.simbolos == True:
            self.selecionarCaracteres(letrasMinusculas + numeros + simbolos)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == False and self.simbolos == True:
            self.selecionarCaracteres(letrasMinusculas + simbolos)
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == True and self.simbolos == False:
            self.selecionarCaracteres(letrasMaiusculas + numeros)
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == False and self.simbolos == True:
            self.selecionarCaracteres(letrasMaiusculas+ simbolos)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == True and self.simbolos == False:
            self.selecionarCaracteres(letrasMinusculas + numeros)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == False and self.simbolos == False:
            self.selecionarCaracteres(letrasMinusculas)
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == True and self.simbolos == True:
            self.selecionarCaracteres(letrasMaiusculas + numeros + simbolos)
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == True and self.simbolos == False:
            self.selecionarCaracteres(numeros)
        else:
            self.selecionarCaracteres(letrasMaiusculas + letrasMinusculas + simbolos)
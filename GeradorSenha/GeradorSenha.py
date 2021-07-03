from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

class GeradorSenha:
    def __init__(self, qtdCaracteres, letrasMaiusculas, letrasMinusculas, numeros, simbolos, tudo):
        self.qtdCaracteres = qtdCaracteres
        self.letrasMaiusculas = letrasMaiusculas
        self.letrasMinusculas = letrasMinusculas
        self.numeros = numeros
        self.simbolos = simbolos       
        self.tudo = tudo
        self.senha = ""
        self.caracteres = ""
        self.selecionarTipo()
        self.selecionarCaracteres()    
 
    def selecionarTipo(self):
        simbolos = "!@#$%^&*"
        if self.letrasMaiusculas == True and self.letrasMinusculas == True and self.numeros == True and self.simbolos == True and self.tudo == True or self.tudo == True:
            self.caracteres = ascii_uppercase + ascii_lowercase + digits + simbolos
        elif self.letrasMaiusculas == True and self.letrasMinusculas == True and self.numeros == True and self.simbolos == False:
            self.caracteres = ascii_uppercase + ascii_lowercase + digits 
        elif self.letrasMaiusculas == True and self.letrasMinusculas == True and self.numeros == False and self.simbolos == False:
            self.caracteres = ascii_uppercase + ascii_lowercase
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == False and self.simbolos == False:
            self.caracteres = ascii_uppercase
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == False and self.simbolos == False:
            print("\nPRECISA SELECIONAR ALGUM TIPO DE CARACTERE")
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == False and self.simbolos == True:
            self.caracteres = simbolos
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == True and self.simbolos == True:
            self.caracteres = digits + simbolos
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == True and self.simbolos == True:
            self.caracteres = ascii_lowercase + digits + simbolos
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == False and self.simbolos == True:
            self.caracteres = ascii_lowercase + simbolos
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == True and self.simbolos == False:
            self.caracteres = ascii_uppercase + digits
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == False and self.simbolos == True:
            self.caracteres = ascii_uppercase+ simbolos
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == True and self.simbolos == False:
            self.caracteres = ascii_lowercase + digits
        elif self.letrasMaiusculas == False and self.letrasMinusculas == True and self.numeros == False and self.simbolos == False:
            self.caracteres = ascii_lowercase
        elif self.letrasMaiusculas == True and self.letrasMinusculas == False and self.numeros == True and self.simbolos == True:
            self.caracteres = ascii_uppercase + digits + simbolos
        elif self.letrasMaiusculas == False and self.letrasMinusculas == False and self.numeros == True and self.simbolos == False:
            self.caracteres = digits
        else:
            self.caracteres = ascii_uppercase + ascii_lowercase + simbolos
        
    def selecionarCaracteres(self):
        for i in range (self.qtdCaracteres):
            self.senha += choice(self.caracteres)
        print(f"\n{self.senha}")
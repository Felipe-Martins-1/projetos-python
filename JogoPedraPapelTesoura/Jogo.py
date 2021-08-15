from time import sleep
from random import choice

class Jogo:
    def __init__(self, nome, resposta):
      self.nome = nome
      self.respJogador = resposta
      self.respBot = ["pedra", "papel", "tesoura"]
      self.validarRespostaJogador()

    def validarRespostaJogador(self):
      if self.respJogador in ["pedra", "papel", "tesoura"]:
        self.compararRespostas()
      else:
        print("Resposta inválida!")
        sleep(2)
    
    def compararRespostas(self):

      # RESPOSTA DO BOT
      self.respBot = choice(self.respBot)
      print(f"Resposta do Bot: {self.respBot}")

      # POSSIBILIDADES DO JOGADOR GANHAR
      if self.respJogador == "pedra" and self.respBot == "tesoura" or self.respJogador == "tesoura" and self.respBot == "papel" or self.respJogador == "papel" and self.respBot == "pedra":
        print(f"{self.nome} venceu!")
      
      # POSSIBILIDADES DO BOT GANHAR
      elif self.respBot == "pedra" and self.respJogador == "tesoura" or self.respBot == "tesoura" and self.respJogador == "papel" or self.respBot == "papel" and self.respJogador == "pedra":
        print("Bot venceu!")
        
      else:
        print("Empate!")
      
      sleep(4)
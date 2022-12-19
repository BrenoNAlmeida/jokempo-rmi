# saved as Server.py
import Pyro4
import random
import os

@Pyro4.expose
class Jokempo(object):
    def jokempo(self, player):
        options = ['pedra', 'papel', 'tesoura']
        computer = random.choice(options)
        if player == computer:
            return f'computador - {computer}!\nEmpate'
        elif player == 'pedra' and computer == 'tesoura':
            return f'computador - {computer}!\n Você ganhou'
        elif player == 'pedra' and computer == 'papel':
            return f'computador - {computer}!\n Você perdeu'
        elif player == 'papel' and computer == 'pedra':
            return f'computador - {computer}!\nVocê ganhou'
        elif player == 'papel' and computer == 'tesoura':
            return f'computador - {computer}!\nVocê perdeu'
        elif player == 'tesoura' and computer == 'papel':
            return f'computador - {computer}!\nVocê ganhou'
        elif player == 'tesoura' and computer == 'pedra':
            return f'computador - {computer}!\nVocê perdeu'
        else:
            return 'Opção inválida'

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Jokempo)   # register the greeting maker as a Pyro object
ns.register("example.jokempo", uri)   # register the object with a name in the name server

print("jokempo online.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
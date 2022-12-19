# saved as client.py
import Pyro4
jokempo = Pyro4.Proxy("PYRONAME:example.jokempo")    # use name server object lookup uri shortcut
while True:
	print('--------------JOKEMPÔ-------------------')
	print("Escolha uma opção:")
	print("1 - Pedra")
	print("2 - Papel")
	print("3 - Tesoura")
	print("0 - Sair")
	print('---------------------------------')

	escolha = int(input('sua escolha: '))
	jogada =''
	if escolha == 1:
		jogada = 'pedra'
	elif escolha == 2:
		jogada = 'papel'
	elif escolha == 3:
		jogada = 'tesoura'
	elif escolha == 0:
		break
	else:
		print("Opção inválida")

	print(jokempo.jokempo(jogada))
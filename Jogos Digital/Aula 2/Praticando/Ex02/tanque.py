import random

class Tank:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return f"{self.name} ({self.armor} armor, {self.ammo} shells)"
        else:
            return f"{self.name} (DEAD)"

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(f"{self.name} fires on {enemy.name}")
            enemy.hit()
        else:
            print(f"{self.name} has no shells!")

    def hit(self):
        self.armor -= 20
        print(f"{self.name} is hit!")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(f"{self.name} explodes!")

#INTERAÇÃO COM O USUÁRIO PARA SOLICITAR A QUANTIDADE DE TANQUES PARA O JOGO
number_tanks = int(input("Quantos tanques deseja criarno jogo? [Min 2, Max 10]: "))

while number_tanks < 2 or number_tanks > 10:
    print("Estamos permitindo nesse jogo apenas quantidades entre 2 ou 10 tanques!")
    number_tanks = int(input("Quantos tanques deseja criarno jogo? [Min 2, Max 10]: "))

#CRIAÇÃO DO DICIONÁRIO
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
custom_tanks = {}

for i in range(number_tanks):
    tank_name = input("Digite o nome do tanque que deseja criar: ")
    custom_tanks[letras[0]] = Tank(tank_name)
    del letras[0]

#variavel 'jogadores' armazena as letras(chaves) correspondentes aos itens do dicionário de jogadores
jogadores = []
for tanque in custom_tanks:
    jogadores.append(tanque)

empate = False

while len(custom_tanks) > 1:
    #Sorteio de Ataque
    attacker_index = random.randint(0, len(jogadores) - 1)

    #Selecao do tanque alvo
    alvos_disponiveis = []
    print("Atacante da rodada", custom_tanks[jogadores[attacker_index]].name)
    print(":ista de alvos disponíveis: ")
    for x, y, in custom_tanks.items():
        if custom_tanks[jogadores[attacker_index]].name not in y.name:
            print(x, y.name)
            alvos_disponiveis.append(x)

    target_index = input("Selecione a letra correspondente de que voce deseja atingir: ")
    while target_index not in alvos_disponiveis:
        target_index = input("Selecione um alvo valido: ")

    #ATINGINDO o tanque alvo
    custom_tanks[jogadores[attacker_index]].fire_at(custom_tanks[target_index])
    print("Blindagem restante de ", custom_tanks[jogadores[attacker_index]].name, end=" ")
    print(": ", custom_tanks[target_index].armor)

    #Eliminando alvo, caso sua blindagem esgote
    if not custom_tanks[target_index].alive:
        del custom_tanks[target_index]
        if target_index in jogadores:
            jogadores.remove(target_index)

    #Exibindo informações gerais da partida
    print("----------- Status Geral -----------")
    for item in custom_tanks:
        print("----------------------")
        print("Jogador ", custom_tanks[item].name)
        print("Blindagem ", custom_tanks[item].armor)
        print("Balas ", custom_tanks[item].ammo)
        print("----------------------")

#TANQUE SOBREVIVENTE
if empate:
    print("Empate!")
else:
    print("Vencedor: ")
    for tanque in custom_tanks:
        print(custom_tanks[tanque])


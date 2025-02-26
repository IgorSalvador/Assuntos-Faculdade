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

# Criando 5 tanques
tanks = [Tank(f"Tank {i+1}") for i in range(5)]

# Simulação da batalha
def battle_simulation(tanks):
    while len([tank for tank in tanks if tank.alive]) > 1:
        alive_tanks = [tank for tank in tanks if tank.alive]
        attacker = random.choice(alive_tanks)
        target = random.choice([tank for tank in alive_tanks if tank != attacker])
        
        attacker.fire_at(target)
        
        # Remover tanques destruídos
        tanks = [tank for tank in tanks if tank.alive]
        
        print("\nEstado atual dos tanques:")
        for tank in tanks:
            print(tank)
        print("----------------------------")

    print(f"\nO vencedor é {tanks[0].name}!")

# Iniciar a simulação
battle_simulation(tanks)

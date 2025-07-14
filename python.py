import random
import time

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.is_defending = False

    def attack(self, target):
        critical = random.random() < 0.2  # 20% chance for critical hit
        damage = self.attack_power * (2 if critical else 1)
        if target.is_defending:
            damage = max(1, damage // 2)  # Half damage if defending
        target.hp -= damage
        print(f"⚔️ {self.name} hits {target.name} for {damage} damage!" + (" (Critical! 💥)" if critical else ""))
        if target.hp <= 0:
            print(f"💀 {target.name} is defeated!")

    def defend(self):
        self.is_defending = True
        print(f"🛡️ {self.name} is defending!")

    def reset_defense(self):
        self.is_defending = False

def game_loop():
    player = Character("Hero", 100, 15)
    monster = Character("Monster", 80, 20)
    potions = 3

    print("\n🎮 **Battle Start!**")
    while True:
        # Player's Turn
        print(f"\n❤️ {player.name}: {player.hp} HP | {monster.name}: {monster.hp} HP")
        choice = input("Choose (1: Attack, 2: Defend, 3: Heal): ")
        player.reset_defense()

        if choice == "1":
            player.attack(monster)
            if monster.hp <= 0:
                print("🎉 **You Win!**")
                break
        elif choice == "2":
            player.defend()
        elif choice == "3" and potions > 0:
            heal = random.randint(15, 25)
            player.hp += heal
            potions -= 1
            print(f"🧪 +{heal} HP! ({potions} potions left)")
        else:
            print("⚠️ Invalid choice!")

        # Monster's Turn (if alive)
        if monster.hp > 0:
            monster_choice = random.choice(["attack", "defend"])
            if monster_choice == "attack":
                monster.attack(player)
                if player.hp <= 0:
                    print("😵 **You Lost...**")
                    break
            else:
                monster.defend()
        time.sleep(1)

if __name__ == "__main__":
    game_loop()
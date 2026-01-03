import sqlite3
import time
import random

conn = sqlite3.connect("evo.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS evo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER DEFAULT 0,
    score INTEGER DEFAULT 100,
    atack INTEGER DEFAULT 0,
    defense INTEGER DEFAULT 0,
    speed INTEGER DEFAULT 0,
    mass INTEGER DEFAULT 0,
    diet TEXT,
    satiety INTEGER DEFAULT 50,
    energy INTEGER DEFAULT 50,
    health INTEGER DEFAULT 0
)
""")
conn.commit()

jaw_catalog = [
    {"name_jaw": "Зубчатые Терки", "food_type_jaw": "Травоядное", "bite_force_jaw": 1, "price_jaw": 10},
    {"name_jaw": "Роговой Клюв", "food_type_jaw": "Травоядное", "bite_force_jaw": 2, "price_jaw": 15},
    {"name_jaw": "Жернова", "food_type_jaw": "Травоядное", "bite_force_jaw": 1, "price_jaw": 10},
    {"name_jaw": "Кинжальные Клыки", "food_type_jaw": "Хищное", "bite_force_jaw": 3, "price_jaw": 10},
    {"name_jaw": "Капканные Челюсти", "food_type_jaw": "Хищное", "bite_force_jaw": 4, "price_jaw": 15},
    {"name_jaw": "Дробители Костей", "food_type_jaw": "Хищное", "bite_force_jaw": 5, "price_jaw": 20}
]

body_catalog = [
    {"name_body": "Маленькое Тело", "mass_body": 30, "durability_body": 1, "speed_body": 1, "health_body" : 25, "price_body": 10,},
    {"name_body": "Среднее Тело", "mass_body": 80, "durability_body": 3, "speed_body": 0, "health_body" : 50, "price_body": 15},
    {"name_body": "Массивное Тело", "mass_body": 230, "durability_body": 6, "speed_body": -1, "health_body" : 100, "price_body": 20}
]

limbs_catalog = [
    {"name_limbs": "Быстрые Лапы", "speed_limbs": 4, "price_limbs": 25},
    {"name_limbs": "Массивные Лапы", "speed_limbs": 2, "price_limbs": 10}
]

def main_menu():
    print(f"\n{'–'*5} Добро пожаловать в Evo {'–'*5}")
    print("1 – Новое существо")
    print("2 – Загрузить существо")
    print("0 – Выход")

def play_game(name_character):
    while True:
        cursor.execute("SELECT name, age, score, atack, defense, speed, mass, diet, satiety, energy, health FROM evo WHERE name = ?", (name_character,))
        stats = cursor.fetchone()
        name, age, score, atack, defense, speed, mass, diet, satiety, energy, health = stats

        if health <= 0:
            print(f"Существо {name_character} умерло...")
            cursor.execute("DELETE FROM evo WHERE name = ?", (name_character,))
            conn.commit()
            time.sleep(3)
            break
        
        print(f"\n--- {name.upper()} ---")
        print(f"Состояние: Сытость {satiety} | Энергия {energy}")
        print("1. Статистика | 2. Действие | 0. Выход в меню")
        
        main_interact = input("Действие: ")
        if main_interact == "1":
            print(f"\n{'Название':<10} | {'ДНК':<5} | {'Здоровье':<5} |{'Атака':<5} | {'Защита':<5} | {'Скорость':<5}")
            print(f"{name:<10} | {score:<5} | {health:<5} | {atack:<5} | {defense:<6} | {speed:<5}")

        elif main_interact == "2":
            print(f"\n{'-'*5}Действия{'-'*5}")
            if diet == "Хищное":
                print("\n1. Отправиться на охоту")
            elif diet == "Травоядное":
                print("\n1. Искать растение")
            interact = input("Действие: ")
            if interact == "1" and diet == "Хищное":
                if energy >= 20:
                    print("\nВы выдвинулись на охоту")
                    time.sleep(2)
                    print("Процесс поиска добычи...")
                    time.sleep(3)
                    diet_prey = random.randint(1, 100)
                    if diet_prey <= 20:
                        prey_power = random.randint(1,12)
                        if prey_power <= 3:
                            print("Найден - слабый хищник")
                        elif prey_power <= 7 and prey_power > 3:
                            print("Найден - опасный хищник")
                        elif prey_power <= 10 and prey_power > 7:
                            print("Найден - очень опасный хищник")
                        elif prey_power > 10:
                            print("Найден - верховный хищник")
                        time.sleep(2)
                        print("Хищник нападает на вас")
                        time.sleep(2)
                        user_luck = random.randint(1,5)
                        user_total_power = user_luck + atack
                        if prey_power <= user_total_power:
                            print("Вы выиграли схватку")
                            cursor.execute("UPDATE evo SET score = score + ? , energy = energy - ?, satiety = satiety + ? WHERE name = ?", (prey_power*3, prey_power, prey_power, name_character))
                        if prey_power > user_total_power:
                            damage = random.randint(1, prey_power)
                            print("Вы проиграли схватку, вам нанесли {damage} урона")
                            cursor.execute("UPDATE evo SET energy = energy - ?, satiety = satiety - ?, health = health - ? WHERE name = ?", (prey_power, prey_power, damage, name_character))
                        conn.commit()
                        continue
                    elif diet_prey > 20:
                        print("Добыча найдена")
                        time.sleep(2)
                        print("Вы бежите за добычей")
                        time.sleep(2)
                        prey_power = random.randint(1,7)
                        prey_speed = random.randint(1,5)
                        user_luck = random.randint(1,5)
                        user_total_speed = user_luck + speed
                        if user_total_speed >= prey_speed:
                            print("Добыча поймана")
                            cursor.execute("UPDATE evo SET score = score + ? WHERE name = ?", (prey_speed*2, name_character))
                            time.sleep(2)
                            print("Вы атакуете ее")
                        elif user_total_speed < prey_speed:
                            print("Добыча убежала")
                            cursor.execute("UPDATE evo SET energy = energy - ?, satiety = satiety - ? WHERE name = ?", (prey_speed*2, prey_speed, name_character))
                            continue
                        user_total_power = user_luck + atack
                        if prey_power <= user_total_power:
                            time.sleep(2)
                            print("Охота успешна!")
                            cursor.execute("UPDATE evo SET score = score + ? , energy = energy - ?, satiety = satiety + ? WHERE name = ?", (prey_power*2, prey_power, prey_power*2, name_character))
                        elif prey_power > user_total_power:
                            time.sleep(2)
                            print("Охота не удалась")
                            cursor.execute("UPDATE evo SET energy = energy - ?, satiety = satiety - ? WHERE name = ?", (prey_power*2, prey_power, name_character))
                        conn.commit()
                elif energy < 20:
                    print("[!] Для охоты нужно минимум 20 Энергии")
            elif interact == "1" and diet == "Травоядное":
                if energy >= 10:    
                    print("\nВы выдвинулись на поиск растения")
                    time.sleep(2)
                    find_plant = random.randint(1, 100)
                    if find_plant <= 65:
                        print("Найдено растение")
                        cursor.execute("UPDATE evo SET score = score + 3, satiety = satiety + 15, energy = energy - 5 WHERE name = ?", (name_character,))
                        conn.commit()
                        time.sleep(2)
                    elif find_plant <= 75:
                        print("Вы съели ядовитое растение")
                        cursor.execute("UPDATE evo SET satiety = satiety - 5, energy = energy - 10, health = health - 5 WHERE name = ?", (name_character,))
                        conn.commit()
                        time.sleep(2)
                    elif find_plant <= 85:
                        predator_speed = random.randint(1, 5)
                        print("Обнаружен хищник!")
                        time.sleep(2)
                        user_luck = random.randint(1, 5)
                        user_total_speed = user_luck + speed
                        if predator_speed <= user_total_speed:
                            print("Вам удалось сбежать")
                            cursor.execute("UPDATE evo SET satiety = satiety - 10, energy = energy - 15 WHERE name = ?", (name_character,))
                            conn.commit()
                            time.sleep(2)
                        elif predator_speed > user_total_speed:
                            print("Хищник догнал вас!")
                            time.sleep(2)
                            print("Вы обороняетесь")
                            time.sleep(2)
                            predator_power = random.randint(1,10)
                            user_luck = random.randint(1,5)
                            user_total_power = user_luck + defense
                            if predator_power <= user_total_power:
                                print("Вам удалось отбиться")
                                cursor.execute("UPDATE evo SET satiety = satiety - 15, energy = energy - 20, health = health - ? WHERE name = ?", (predator_power, name_character))
                                conn.commit()
                            elif predator_power > user_total_power:
                                probability_death = random.randint(1,100)
                                if probability_death <= 75:
                                    print("Вы сбежали с ранами")
                                    cursor.execute("UPDATE evo SET satiety = satiety - 20, energy = energy - 30, health = health - ? WHERE name = ?", (predator_power*2, name_character))
                                    conn.commit()
                                elif probability_death <= 100:
                                    print("Вы не смогли спастись")
                                    cursor.execute("UPDATE evo SET health = health - health WHERE name = ?", (name_character,))
                                    conn.commit()
                    elif find_plant <= 100:
                        print("Растения не найдены")
                        cursor.execute("UPDATE evo SET satiety = satiety - 5, energy = energy - 5 WHERE name = ?", (name_character,))
                        conn.commit()
        elif main_interact == "0":
            break

def new_game():
    while True:
        time.sleep(0.5)
        name_character = input("Введите название существа: ").lower().strip()
        cursor.execute("SELECT name FROM evo WHERE name = ?", (name_character,))
        if cursor.fetchone():
            print("[!] Существо с таким именем уже существует")
        elif name_character == "":
            print("[!] Имя не может быть пустым")
        else:
            cursor.execute("INSERT INTO evo (name) VALUES (?)", (name_character,))
            conn.commit()
            print("Имя записано")
            break

    for catalog, table, fields in [
        (jaw_catalog, "atack = atack + ?, diet = ?", ["bite_force_jaw", "food_type_jaw"]),
        (body_catalog, "defense = defense + ?, speed = speed + ?, mass = mass + ?, health = health + ?", ["durability_body", "speed_body", "mass_body", "health_body"]),
        (limbs_catalog, "speed = speed + ?", ["speed_limbs"])
    ]:
        while True:
            cursor.execute("SELECT score FROM evo WHERE name = ?", (name_character,))
            recorded_score = cursor.fetchone()[0]
            print(f"\nТекущий баланс: {recorded_score} ДНК")
            
            for i, item in enumerate(catalog, 1):
                print(f"{i}. {list(item.values())[0]} | Цена: {list(item.values())[-1]}")
            
            choice = input("Выберите номер или название: ")
            selected = None
            if choice.isdigit() and 0 < int(choice) <= len(catalog):
                selected = catalog[int(choice)-1]
            else:
                selected = next((x for x in catalog if list(x.values())[0] == choice), None)

            if selected:
                price = list(selected.values())[-1]
                if recorded_score >= price:
                    vals = [selected[f] for f in fields] + [price, name_character]
                    cursor.execute(f"UPDATE evo SET {table}, score = score - ? WHERE name = ?", vals)
                    conn.commit()
                    break
                else: print("[!] Дорого")
            else: print("[!] Ошибка ввода")

    print(f"\n{'–'*5} Существо создано! {'–'*5}")
    play_game(name_character)

def load_game():
    cursor.execute("SELECT name FROM evo")
    characters = cursor.fetchall()
    if not characters:
        print("[!] Сохранений не найдено")
        return
    
    print("\n{:-^20}".format(" ВАШИ СОХРАНЕНИЯ "))
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char[0]}")
    
    choice = input("Выберите номер существа или 0 для выхода: ")
    if choice.isdigit() and 0 < int(choice) <= len(characters):
        selected_name = characters[int(choice) - 1][0]
        play_game(selected_name)

while True:
    main_menu()
    choice = input("Выбери действие: ")
    if choice == "1":
        new_game()
    elif choice == "2":
        load_game()
    elif choice == "0":
        break
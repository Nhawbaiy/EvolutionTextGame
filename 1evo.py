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
    satiety INTEGER DEFAULT 0,
    energy INTEGER DEFAULT 0,
    health INTEGER DEFAULT 0,
    max_health INTEGER,
    max_energy INTEGER,
    max_satiety INTEGER,
    vision INTEGER DEFAULT 0
)
""")
conn.commit()

jaw_catalog = [
    {"name_jaw": "Примитивные Жвала", "food_type_jaw": "Травоядное", "bite_force_jaw": 2, "price_jaw": 10},
    {"name_jaw": "Примитивные Жернова", "food_type_jaw": "Травоядное", "bite_force_jaw": 2, "price_jaw": 15},
    {"name_jaw": "Рот-Присоска", "food_type_jaw": "Травоядное", "bite_force_jaw": 1, "price_jaw": 10},
    {"name_jaw": "Роговые Пластины", "food_type_jaw": "Хищное", "bite_force_jaw": 3, "price_jaw": 10},
    {"name_jaw": "Костяной Клюв", "food_type_jaw": "Хищное", "bite_force_jaw": 4, "price_jaw": 15},
    {"name_jaw": "Зубастый Капкан", "food_type_jaw": "Хищное", "bite_force_jaw": 5, "price_jaw": 30}
]

body_catalog = [
    {"name_body": "Крошечное Тело", "mass_body": 10, "durability_body": 1, "speed_body": 0, "health_body" : 10, "max_health_body" : 10, "max_energy_body" : 10, "max_satiety_body" : 10, "price_body": 10,},
    {"name_body": "Маленькое Тело", "mass_body": 30, "durability_body": 3, "speed_body": 0, "health_body" : 30, "max_health_body" : 30, "max_energy_body" : 30, "max_satiety_body" : 30, "price_body": 20},
    {"name_body": "Среднее Тело", "mass_body": 85, "durability_body": 6, "speed_body": 0, "health_body" : 85, "max_health_body" : 85, "max_energy_body" : 85, "max_satiety_body" : 85, "price_body": 35}
]

limbs_catalog = [
    {"name_limbs": "Расставленные Конечности", "speed_limbs": 1, "price_limbs": 20},
    {"name_limbs": "Прямые Конечности", "speed_limbs": 2, "price_limbs": 25}
]
paws_catalog = [
    {"name_paws" : "Примитивные Пернатые Захваты", "speed_paws" : 1, "price_paws" : 15},
    {"name_paws" : "Столбчатые  Опоры", "speed_paws" : 2, "price_paws" : 15},
    {"name_paws" : "Перепончатые Ласты", "speed_paws" : 1, "price_paws" : 15}
]
eyes_catalog = [
    {"name_eyes" : "Фасеточные Сферы", "vision_eyes" : 3, "price_eyes" : 35},
    {"name_eyes" : "Световые Пятна", "vision_eyes" : 1, "price_eyes" : 20},
    {"name_eyes" : "Без Глаз", "vision_eyes" : 0, "price_eyes" : 0}
]

def main_menu():
    print(f"\n{'–'*5} Добро пожаловать в Evo {'–'*5}")
    print("1 – Новое существо")
    print("2 – Загрузить существо")
    print("0 – Выход")

def play_game(name_character):
    while True:
        cursor.execute("SELECT name, age, score, atack, defense, speed, mass, diet, satiety, energy, health, max_health, max_energy, max_satiety, vision FROM evo WHERE name = ?", (name_character,))
        stats = cursor.fetchone()
        name, age, score, atack, defense, speed, mass, diet, satiety, energy, health, max_health, max_energy, max_satiety, vision = stats

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
                print(f"\n1. Отправиться на охоту ({max_energy//5} энергии)")
            elif diet == "Травоядное":
                print(f"\n1. Искать растение ({max_energy//5} энергии)")
            print("2. Отдохнуть")
            interact = input("Действие: ")
            if interact == "1" and diet == "Хищное":
                if energy >= max_energy//5:
                    print("\nВы выдвинулись на охоту")
                    time.sleep(2)
                    print("Процесс поиска добычи...")
                    time.sleep(3)
                    find_prey = random.randint(1, 100)
                    use_vision = 1 + (vision * 0.2)
                    find_prey = find_prey / use_vision
                    find_prey = round(find_prey)
                    if find_prey <= 70:
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
                                cursor.execute("UPDATE evo SET score = score + ? , energy = MAX(energy - ?, 0), satiety = MIN(satiety + ?, ?) WHERE name = ?", (prey_power*3, max_energy//5, prey_power, max_satiety, name_character))
                            if prey_power > user_total_power:
                                damage = random.randint(1, prey_power)
                                print(f"Вы проиграли схватку, вам нанесли {damage} урона")
                                cursor.execute("UPDATE evo SET energy = MAX(energy - ?, 0), satiety = MAX(satiety - ?, 0), health = health - ? WHERE name = ?", (max_energy//5, prey_power, damage, name_character))
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
                                cursor.execute("UPDATE evo SET score = score + ?, energy = MAX(energy - ?, 0) WHERE name = ?", (prey_speed*2, max_energy//5, name_character))
                                time.sleep(2)
                                print("Вы атакуете ее")
                            elif user_total_speed < prey_speed:
                                print("Добыча убежала")
                                cursor.execute("UPDATE evo SET energy = MAX(energy - ?, 0), satiety = MAX(satiety - ?, 0) WHERE name = ?", (max_energy//5, prey_speed, name_character))
                                continue
                            user_total_power = user_luck + atack
                            if prey_power <= user_total_power:
                                time.sleep(2)
                                print("Охота успешна!")
                                cursor.execute("UPDATE evo SET score = score + ? , energy = MAX(energy - ?, 0), satiety = MIN(satiety + ?, ?) WHERE name = ?", (prey_power*2, max_energy//5, prey_power*2, max_satiety, name_character))
                            elif prey_power > user_total_power:
                                time.sleep(2)
                                print("Охота не удалась")
                                cursor.execute("UPDATE evo SET energy = MAX(energy - ?,0), satiety = MAX(satiety - ?, 0) WHERE name = ?", (max_energy//5, prey_power, name_character))
                            conn.commit()
                            time.sleep(2)
                    elif find_prey >=100:
                        print("Добыча не найдена")
                        time.sleep(2)
                elif energy < max_energy//5:
                    print("[!] Нехватает энергии")
                    time.sleep(2)
            elif interact == "1" and diet == "Травоядное":
                if energy >= max_energy//5:    
                    print("\nВы выдвинулись на поиск растения")
                    time.sleep(2)
                    find_plant = random.randint(1, 100)
                    use_vision = 1 + (vision * 0.2)
                    find_plant = find_plant / use_vision
                    find_plant = round(find_plant)
                    if find_plant <= 60:
                        print("Найдено растение")
                        found_food = random.randint(1, max(1, satiety//2))
                        wasted_energy = max_energy//5
                        cursor.execute("UPDATE evo SET score = score + 3, satiety = MIN(satiety + ?, ?), energy = MAX(energy - ?, 0) WHERE name = ?", (found_food, max_satiety, max_energy//5, name_character))
                        conn.commit()
                        time.sleep(2)
                    elif find_plant <= 75:
                        print("Вы съели ядовитое растение")
                        plant_toxicity = random.randint(1, max(1, health//4))
                        wasted_energy = max_energy//5
                        cursor.execute("UPDATE evo SET score = score + 3, health = health - ?, energy = MAX(energy - ?, 0) WHERE name = ?", (plant_toxicity, wasted_energy, name_character))
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
                            wasted_satiety = random.randint(1, max(1, satiety//3))
                            wasted_energy = max_energy//5
                            cursor.execute("UPDATE evo SET satiety = MAX(satiety - ?, 0), energy = MAX(energy - ?, 0) WHERE name = ?", (wasted_satiety, wasted_energy, name_character))
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
                                time.sleep(2)
                                wasted_satiety = random.randint(1, max(1, satiety//2))
                                wasted_energy = max_energy//5
                                cursor.execute("UPDATE evo SET satiety = MAX(satiety - ?, 0), energy = MAX(energy - ?, 0) WHERE name = ?", (wasted_satiety, wasted_energy, name_character))
                                conn.commit()
                            elif predator_power > user_total_power:
                                probability_death = random.randint(1,100)
                                if probability_death <= 75:
                                    print("Вы сбежали с ранами")
                                    time.sleep(2)
                                    damage = random.randint(1, max(1, health//2))
                                    wasted_satiety = random.randint(1, max(1, satiety//2))
                                    wasted_energy = max_energy//5
                                    cursor.execute("UPDATE evo SET health = health - ?, satiety = MAX(satiety - ?, 0), energy = MAX(energy - ?, 0) WHERE name = ?", (damage, wasted_satiety, wasted_energy, name_character))
                                    conn.commit()
                                elif probability_death <= 100:
                                    print("Вы не смогли спастись")
                                    time.sleep(2)
                                    cursor.execute("UPDATE evo SET health = health - health WHERE name = ?", (name_character,))
                                    conn.commit()   
                    elif find_plant <= 100:
                        print("Растения не найдены")
                        cursor.execute("UPDATE evo SET satiety = satiety - 5, energy = energy - 5 WHERE name = ?", (name_character,))
                        conn.commit()
                        time.sleep(2)
                elif energy < max_energy//5:
                    print("[!] Нехватает энергии")
                    time.sleep(2)
            elif interact == "2":
                print("Вы отдыхаете...")
                time.sleep(2)
                add_h = max(0, max_health - health)
                add_e = max(0, max_energy - energy)
                total_cost = add_h + add_e
                wasted_total_cost = total_cost / 2
                wasted_total_cost = round(wasted_total_cost)
                if total_cost == 0:
                    print("[!] Вы уже полностью полны сил!")
                    time.sleep(2)
                elif satiety >= total_cost:
                    cursor.execute("""UPDATE evo SET satiety = satiety - ?, health = health + ?, energy = energy + ? WHERE name = ?""", (wasted_total_cost, add_h, add_e, name_character))
                    conn.commit()
                    print(f"[+] Вы восстановили {add_h} ХП и {add_e} Энергии.")
                    time.sleep(2)
                else:
                    print("[!] Вам недостаточно сытости для полного восстановления")
                    time.sleep(2)
        elif main_interact == "0":
            break

def new_game():
    print(f"\n{'-'*5}Поздравляю, ваше существо только что вышло из воды на сушу, давайте создадим его{'-'*5}")
    time.sleep(2)
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
        (body_catalog, "defense = defense + ?, speed = speed + ?, mass = mass + ?, health = health + ?, max_health = ?, max_energy = ?, max_satiety = ?, energy = energy + ?, satiety = satiety + ?", ["durability_body", "speed_body", "mass_body", "health_body", "max_health_body", "max_energy_body", "max_satiety_body", "max_energy_body", "max_satiety_body"]),
        (limbs_catalog, "speed = speed + ?", ["speed_limbs"]),
        (paws_catalog, "speed = speed + ?", ["speed_paws"]),
        (eyes_catalog, "vision = vision + ?", ["vision_eyes"])
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
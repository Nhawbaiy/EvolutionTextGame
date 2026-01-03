import sqlite3
import time

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
    bite INTEGER DEFAULT 0,
    punch INTEGER DEFAULT 0,
    diet TEXT,
    satiety INTEGER DEFAULT 50,
    energy INTEGER DEFAULT 50
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
    {"name_body": "Маленькое Тело", "mass_body": 30, "durability_body": 1, "speed_body": 1, "price_body": 10},
    {"name_body": "Среднее Тело", "mass_body": 80, "durability_body": 3, "speed_body": 0, "price_body": 15},
    {"name_body": "Массивное Тело", "mass_body": 230, "durability_body": 6, "speed_body": -1, "price_body": 20}
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
        cursor.execute("SELECT name, age, score, atack, defense, speed, mass, diet, satiety, energy FROM evo WHERE name = ?", (name_character,))
        stats = cursor.fetchone()
        name, age, score, atack, defense, speed, mass, diet, satiety, energy = stats
        
        print(f"\n--- {name.upper()} ---")
        print(f"Состояние: Сытость {satiety} | Энергия {energy}")
        print("1. Статистика | 2. Действие | 0. Выход в меню")
        
        interact = input("Действие: ")
        if interact == "1":
            print(f"\n{'Название':<10} | {'ДНК':<5} | {'Атака':<5} | {'Защита':<5} | {'Скорость':<5}")
            print(f"{name:<10} | {score:<5} | {atack:<5} | {defense:<6} | {speed:<5}")
        elif interact == "0":
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
        (body_catalog, "defense = defense + ?, speed = speed + ?, mass = mass + ?", ["durability_body", "speed_body", "mass_body"]),
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
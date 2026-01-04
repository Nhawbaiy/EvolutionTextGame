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
    vision INTEGER DEFAULT 0,
    attractiveness INTEGER DEFAULT 60,
    jaw TEXT,
    body TEXT,
    limbs TEXT,
    paws TEXT,
    eyes TEXT
)
""")
conn.commit()

jaw_catalog1 = [
    {"name_jaw": "Примитивные Жвала", "diet_jaw": "Травоядное", "bite_force_jaw": 2, "price_jaw": 10},
    {"name_jaw": "Примитивные Жернова", "diet_jaw": "Травоядное", "bite_force_jaw": 2, "price_jaw": 15},
    {"name_jaw": "Рот-Присоска", "diet_jaw": "Травоядное", "bite_force_jaw": 1, "price_jaw": 10},
    {"name_jaw": "Роговые Пластины", "diet_jaw": "Хищное", "bite_force_jaw": 3, "price_jaw": 10},
    {"name_jaw": "Костяной Клюв", "diet_jaw": "Хищное", "bite_force_jaw": 4, "price_jaw": 15},
    {"name_jaw": "Зубастый Капкан", "diet_jaw": "Хищное", "bite_force_jaw": 5, "price_jaw": 25}
]

body_catalog1 = [
    {"name_body": "Крошечное Тело", "mass_body": 10, "durability_body": 1, "speed_body": 0, "health_body" : 10, "max_health_body" : 10, "max_energy_body" : 10, "max_satiety_body" : 10, "price_body": 10,},
    {"name_body": "Маленькое Тело", "mass_body": 30, "durability_body": 3, "speed_body": 0, "health_body" : 30, "max_health_body" : 30, "max_energy_body" : 30, "max_satiety_body" : 30, "price_body": 20},
    {"name_body": "Среднее Тело", "mass_body": 85, "durability_body": 6, "speed_body": 0, "health_body" : 85, "max_health_body" : 85, "max_energy_body" : 85, "max_satiety_body" : 85, "price_body": 30}
]

limbs_catalog1 = [
    {"name_limbs": "Расставленные Конечности", "speed_limbs": 1, "price_limbs": 15},
    {"name_limbs": "Прямые Конечности", "speed_limbs": 2, "price_limbs": 20}
]
paws_catalog1 = [
    {"name_paws" : "Примитивные Пернатые Захваты", "speed_paws" : 1, "price_paws" : 15},
    {"name_paws" : "Столбчатые  Опоры", "speed_paws" : 2, "price_paws" : 15},
    {"name_paws" : "Перепончатые Ласты", "speed_paws" : 1, "price_paws" : 15}
]
eyes_catalog1 = [
    {"name_eyes" : "Фасеточные Сферы", "vision_eyes" : 2, "price_eyes" : 25},
    {"name_eyes" : "Световые Пятна", "vision_eyes" : 1, "price_eyes" : 15},
    {"name_eyes" : "Очень примитивное зрение", "vision_eyes" : 0, "price_eyes" : 0}
]

evolutions_jaw = {
    "Примитивные Жвала" : [
        {"name_jaw" : "Листорезы", "desc" : "Тонкие самозатачивающиеся края для аккуратного срезания мягкой зелени.", "diet_jaw" : "Травоядное", "bite_force_jaw" : 2, "price_jaw" : 20},
        {"name_jaw" : "Древогрызы", "desc" : "Мощные долотообразные выросты, способные скалывать твердую кору и древесину.", "diet_jaw" : "Травоядное", "bite_force_jaw" : 3, "price_jaw" : 25}
    ],
    "Примитивные Жернова" : [
        {"name_jaw" : "Мукомольные Пластины", "desc" : "Широкие ребристые поверхности для перетирания жестких злаков и сухих семян в кашицу.", "diet_jaw" : "Травоядное", "bite_force_jaw" : 2, "price_jaw" : 30},
        {"name_jaw" : "Тёрочные Массивы", "desc" : "Множество мелких зазубрин, предназначенных для пережевывания твердой травы.", "diet_jaw" : "Травоядное", "bite_force_jaw" : 2, "price_jaw" : 30}
    ],
    "Роговые Пластины" : [
        {"name_jaw" : "Клиновидная Гильотина", "desc" : "Хирургически острые пластины, работающие как ножницы для мгновенного отсечения конечностей.", "diet_jaw" : "Хищное", "bite_force_jaw" : 5, "price_jaw" : 35},
        {"name_jaw" : "Зазубренный Захват", "desc" : "Грубые наросты, которые намертво фиксируют жертву, не давая ей вырваться.", "diet_jaw" : "Хищное", "bite_force_jaw" : 4, "price_jaw" : 30}
    ],
    "Костяной Клюв" : [
        {"name_jaw" : "Дробящий Керн", "desc" : "Тяжелый монолитный клюв для раскалывания самых твердых орехов и защиты врага.", "diet_jaw" : "Травоядное", "bite_force_jaw" : 3, "price_jaw" : 20},
        {"name_jaw" : "Гарпунный Резец", "desc" : "Острый изогнутый клинок для точечных ударов и вспарывания плоти.", "diet_jaw" : "Хищное", "bite_force_jaw" : 5, "price_jaw" : 35}
    ],
    "Зубастый Капкан" : [
        {"name_jaw" : "Дробящие Стыки", "desc" : "Массивные суставные челюсти, созданные для дробления панцирей и костей под огромным давлением.", "diet_jaw" : "Хищное", "bite_force_jaw" : 6, "price_jaw" : 45},
        {"name_jaw" : "Ударные Клыки", "desc" : "Пружинный механизм для молниеносного «хлопка», оглушающего добычу при первом контакте.", "diet_jaw" : "Хищное", "bite_force_jaw" : 6, "price_jaw" : 45}
    ]
}

evolutions_paws = {
    "Примитивные Пернатые Захваты" : [
        {"name_paws" : "Пернатые Тиски", "desc" : "Мощные лапы с утолщенными сухожилиями, предназначенные для мертвого захвата и удержания сопротивляющейся добычи.", "speed_paws" : 1, "price_paws" : 20},
        {"name_paws" : "Серповидные Пернатые Когти", "desc" : "Длинные, изогнутые лезвия, созданные для глубоких рваных ран при атаке с воздуха или на высокой скорости.", "speed_paws" : 1, "price_paws" : 20}
    ],
    "Столбчатые  Опоры" : [
        {"name_paws" : "Упорные Трехпалы", "desc" : "Широко расставленные пальцы, обеспечивающие идеальный баланс и устойчивость на неровных поверхностях.", "speed_paws" : 4, "price_paws" : 40},
        {"name_paws" : "Опорные Когти", "desc" : "Короткие, тупые и очень прочные наросты, которые работают как альпинистские кошки, помогая карабкаться по крутым склонам.", "speed_paws" : 3, "price_paws" : 35},
        {"name_paws" : "Растопыренные Когти", "desc" : "Длинные пальцы, увеличивающие площадь опоры, что позволяет уверенно передвигаться по рыхлому грунту или песку.", "speed_paws" : 3, "price_paws" : 35}
    ],
    "Перепончатые Ласты" : [
        {"name_paws" : "Перепончатые Стопы", "desc" : "Пальцы, соединенные эластичной кожей, превращающие лапу в эффективное весло для быстрого плавания и маневров в воде.", "speed_paws" : 2, "price_paws" : 15}
    ]
}
evolutions_eyes = {
    "Фасеточные Сферы" : [
        {"name_eyes" : "Спектральные Мозаики", "desc" : "Сложные многогранные глаза, способные различать ультрафиолет или тепловое излучение, делая скрытую добычу видимой.", "vision_eyes" : 5, "price_eyes" : 50}
    ],
    "Световые Пятна" : [
        {"name_eyes" : "Светочувствительные Чаши", "desc" : "Углубления в тканях, которые позволяют не только фиксировать свет, но и определять примерное направление на источник опасности или еды.", "vision_eyes" : 3, "price_eyes" : 35},
        {"name_eyes" : "Фасеточные Гроздья", "desc" : "Группы простых линз, собранные в единый массив. Обеспечивают широкий угол обзора и мгновенную фиксацию любого движения вокруг.", "vision_eyes" : 4, "price_eyes" : 40}
    ]
}

def main_menu():
    print(f"\n{'–'*5} Добро пожаловать в Evo {'–'*5}")
    print("1 – Новое существо")
    print("2 – Загрузить существо")
    print("0 – Выход")

def play_game(name_character):
    while True:
        cursor.execute("SELECT name, age, score, atack, defense, speed, mass, diet, satiety, energy, health, max_health, max_energy, max_satiety, vision, attractiveness, jaw, body, limbs, paws, eyes FROM evo WHERE name = ?", (name_character,))
        stats = cursor.fetchone()
        name, age, score, atack, defense, speed, mass, diet, satiety, energy, health, max_health, max_energy, max_satiety, vision, attractiveness, jaw, body, limbs, paws, eyes = stats
        if health <= 0:
            print(f"Существо {name_character} умерло...")
            time.sleep(3)
            return None
        
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
            print(f"3. Искать партнера ({max_energy//5} энергии)")
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
                    elif find_prey <=100:
                        print("Добыча не найдена")
                        cursor.execute("UPDATE evo SET energy = MAX(energy - ?,0) WHERE name = ?", (max_energy//5, name_character))
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
            elif interact == "3":
                time.sleep(1)
                print("Вы ищете партнера...")
                find_partner = random.randint(1,100)
                if find_partner <= 50:
                    cursor.execute("UPDATE evo SET energy = MAX(energy - ?, 0) WHERE name = ?", (max_energy//5, name_character))
                    conn.commit()
                    time.sleep(5)
                    print("Особь найдена")
                    time.sleep(2)
                    print("Вы привлекаете внимание особи...")
                    time.sleep(3)
                    attractiveness_shift = (attractiveness - 50)
                    low_attractiveness = max(1, 1 - attractiveness_shift)
                    high_attractiveness = min (100, 100 - attractiveness_shift)
                    attract_attention = random.randint(low_attractiveness, high_attractiveness)
                    if attract_attention <= 49:
                        print("Вы успешно привлекли внимание особи, партнер найден")
                        time.sleep(2)

                        while True:
                            name_descendant = input("Введите название потомка: ").lower().strip()
                            cursor.execute("SELECT name FROM evo WHERE name = ?", (name_descendant,))
                            if cursor.fetchone():
                                print("[!] Существо с таким именем уже существует")
                                continue
                            if name_descendant == "":
                                print("[!] Имя не может быть пустым")
                                continue
                            cursor.execute("""
                                INSERT INTO evo (name, score, atack, defense, speed, mass, diet, satiety, energy, health, max_health, max_energy, max_satiety, vision, attractiveness, jaw, body, limbs, paws, eyes)
                                SELECT ?, score, atack, defense, speed, mass, diet, max_satiety, max_energy, max_health, max_health, max_energy, max_satiety, vision, attractiveness, jaw, body, limbs, paws, eyes 
                                FROM evo WHERE name = ?
                            """, (name_descendant, name_character))
                            conn.commit()
                            cursor.execute("DELETE FROM evo WHERE name = ?", (name_character,))
                            conn.commit()
                            print(f"Потомок {name_descendant} успешно создан!")
                            break

                        while True:
                            print(f"\n{'-'*5}РЕДАКТОР ПОТОМКА{'-'*5}")
                            print("1. Эволюционировать часть тела")
                            print("0. Завершить создание")
                            editor_choice = input("Действие: ")
                            if editor_choice == "0":
                                print("Эволюция завершена!")
                                return name_descendant
                            if editor_choice == "1":
                                cursor.execute("SELECT jaw, paws, eyes, body, score FROM evo WHERE name = ?", (name_descendant,))
                                res = cursor.fetchone()
                                current_stats = {"jaw": res[0], "paws": res[1], "eyes": res[2], "body": res[3], "score": res[4]}
                                evolutions_map = {
                                    "1": {"name": "Челюсти", "col": "jaw", "cat": evolutions_jaw, "curr": current_stats["jaw"]},
                                    "2": {"name": "Лапы", "col": "paws", "cat": evolutions_paws, "curr": current_stats["paws"]},
                                    "3": {"name": "Глаза", "col": "eyes", "cat": evolutions_eyes, "curr": current_stats["eyes"]}
                                }
                                print("\nВыберите часть тела:")
                                for key, data in evolutions_map.items():
                                    print(f"{key}. {data['name']} (Сейчас: {data['curr']})")
                                print("0. Назад")
                                part_choice = input("Выбор: ")
                                if part_choice == "0" or part_choice not in evolutions_map:
                                    continue
                                choice_data = evolutions_map[part_choice]
                                options = choice_data["cat"].get(choice_data["curr"], [])
                                if not options:
                                    print(f"\n[!] Для {choice_data['curr']} нет доступных эволюций.")
                                    time.sleep(1)
                                    continue
                                for i, opt in enumerate(options, 1):
                                    name = opt.get("name") or opt.get("name_jaw") or opt.get("name_paws") or opt.get("name_eyes")
                                    price = opt.get("price") or opt.get("price_jaw") or opt.get("price_paws") or opt.get("price_eyes")
                                    description = opt.get("desc", "Описание отсутствует")
                                    print(f"{i}. {name}")
                                    print(f"   └─ {description}")
                                    print(f"   └─ Цена: {price} ДНК")
                                buy_choice = input("Покупка: ")
                                if buy_choice == "0" or not buy_choice.isdigit() or int(buy_choice) > len(options):
                                    continue
                                selected_variant = options[int(buy_choice) - 1]
                                new_name = selected_variant.get("name") or selected_variant.get("name_jaw") or selected_variant.get("name_paws") or selected_variant.get("name_eyes")
                                price = selected_variant.get("price") or selected_variant.get("price_jaw") or selected_variant.get("price_paws") or selected_variant.get("price_eyes")
                                column = choice_data["col"]
                                if current_stats["score"] >= price:
                                    all_options = jaw_catalog1 + body_catalog1 + limbs_catalog1 + paws_catalog1 + eyes_catalog1
                                    for ev_list in evolutions_jaw.values(): all_options.extend(ev_list)
                                    for ev_list in evolutions_paws.values(): all_options.extend(ev_list)
                                    for ev_list in evolutions_eyes.values(): all_options.extend(ev_list)
                                    old_part_name = current_stats[column]
                                    old_part_data = next((item for item in all_options if list(item.values())[0] == old_part_name), None)
                                    stats_map = {
                                        "bite_force_jaw": "atack",
                                        "speed_paws": "speed",
                                        "vision_eyes": "vision",
                                        "durability_body": "defense"
                                    }
                                    updates = []
                                    params = []
                                    for key, db_column in stats_map.items():
                                        new_val = selected_variant.get(key, 0)
                                        old_val = old_part_data.get(key, 0) if old_part_data else 0
                                        diff = new_val - old_val
                                        if diff != 0:
                                            updates.append(f"{db_column} = {db_column} + ?")
                                            params.append(diff)
                                    updates.append(f"{column} = ?")
                                    params.append(new_name)
                                    updates.append("score = score - ?")
                                    params.append(price)
                                    if updates:
                                        query = f"UPDATE evo SET {', '.join(updates)} WHERE name = ?"
                                        params.append(name_descendant)
                                        cursor.execute(query, tuple(params))
                                        conn.commit()
                                        print(f"[+] Успешно! {old_part_name} -> {new_name}")
                                    else:
                                        print("[+] Успешно!")
                                else:
                                    print("[!] Недостаточно ДНК!")
                                time.sleep(1)
                    elif attract_attention <= 100:
                        print("Вы не смогли привлечь внимание особи, партнер не найден")
                        time.sleep(2)
                elif find_partner <=100:
                    cursor.execute("UPDATE evo SET energy = MAX(energy - ?, 0) WHERE name = ?", (max_energy//5, name_character))
                    conn.commit()
                    time.sleep(5)
                    print("Партнер не найден")
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
        (jaw_catalog1, "atack = atack + ?, diet = ?, jaw = ?", ["bite_force_jaw", "diet_jaw", "name_jaw"]),
        (body_catalog1, "defense = defense + ?, speed = speed + ?, mass = mass + ?, health = health + ?, max_health = ?, max_energy = ?, max_satiety = ?, energy = energy + ?, satiety = satiety + ?, body = ?", ["durability_body", "speed_body", "mass_body", "health_body", "max_health_body", "max_energy_body", "max_satiety_body", "max_energy_body", "max_satiety_body", "name_body"]),
        (limbs_catalog1, "speed = speed + ?, limbs = ?", ["speed_limbs", "name_limbs"]),
        (paws_catalog1, "speed = speed + ?, paws = ?", ["speed_paws", "name_paws"]),
        (eyes_catalog1, "vision = vision + ?, eyes = ?", ["vision_eyes", "name_eyes"])
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
    return name_character

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
        return selected_name

while True:
    main_menu()
    choice = input("Выбери действие: ")
    current_character = None
    if choice == "1":
        current_character = new_game()
    elif choice == "2":
        current_character = load_game()
    elif choice == "0":
        break
    while current_character is not None:
        current_character = play_game(current_character)
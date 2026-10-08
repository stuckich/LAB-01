from dataclasses import dataclass
import sys

@dataclass
class UserProfile:
    surname: str          # Фамилия (Семья)
    name: str             # Имя
    group: str            # Группа
    city: str             # Город
    age_in_years: int     # Возраст в полных годах (от 1 до 120)
    favorite_subject: str # Любимый предмет
    study_hours: float    # Количество часов подготовки (неотрицательное дробное)

def get_profile():
    print("--- Заполнение профиля пользователя ---")
    
    surname = input("Введите фамилию: ").strip()
    name = input("Введите имя: ").strip()
    group = input("Введите группу: ").strip()
    city = input("Введите город: ").strip()
    
    while True:
        try:
            age = int(input("Введите возраст в полных годах (от 1 до 120): "))
            if 1 <= age <= 120:
                break
            print("Ошибка: возраст должен быть в диапазоне от 1 до 120.")
        except ValueError:
            print("Ошибка: введите целое число.")
            
    favorite_subject = input("Введите любимый предмет: ").strip()
    
    while True:
        try:
            hours = float(input("Введите количество часов подготовки на неделе: "))
            if hours >= 0:
                break
            print("Ошибка: количество часов не может быть отрицательным.")
        except ValueError:
            print("Ошибка: введите число (можно дробное, через точку).")

    return UserProfile(surname, name, group, city, age, favorite_subject, hours)

if __name__ == "__main__":
    profile = get_profile()
    
    print("\n--- Результаты профиля ---")
    print(f"1. Семья (Фамилия): {profile.surname}")
    print(f"2. Имя: {profile.name}")
    print(f"3. Группа: {profile.group}")
    print(f"4. Город: {profile.city}")
    print(f"5. Возраст: {profile.age_in_years} лет")
    print(f"6. Любимый предмет: {profile.favorite_subject}")
    print(f"7. Часов подготовки в неделю: {profile.study_hours}")

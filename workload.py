def main():
    subjects = []
    
    for i in range(1, 3):
        print(f"--- Предмет {i} ---")
        name = input("Введите название предмета: ")
        
        while True:
            try:
                count = int(input("Введите количество занятий за неделю (целое неотрицательное): "))
                if count >= 0:
                    break
                print("Количество занятий не может быть отрицательным.")
            except ValueError:
                print("Пожалуйста, введите целое число.")
                
        while True:
            try:
                duration = int(input("Введите продолжительность одного занятия в минутах (положительное целое): "))
                if duration > 0:
                    break
                print("Продолжительность должна быть больше нуля.")
            except ValueError:
                print("Пожалуйста, введите целое число.")
        
        subjects.append({"name": name, "count": count, "duration": duration})
    
    print("\n--- Доступное время ---")
    while True:
        try:
            weekly_available_hours = float(input("Введите доступное время на неделю в часах: "))
            if weekly_available_hours >= 0:
                break
            print("Доступное время не может быть отрицательным.")
        except ValueError:
            print("Пожалуйста, введите число.")

    print("\n" + "="*30)
    print("РЕЗУЛЬТАТЫ РАСЧЕТОВ")
    print("="*30)

    total_weekly_workload_hours = 0.0

    for sub in subjects:
        subject_hours = (sub["count"] * sub["duration"]) / 60.0
        total_weekly_workload_hours += subject_hours
        print(f"Нагрузка по предмету '{sub['name']}': {subject_hours:.2f} ч./нед.")

    free_hours_per_week = weekly_available_hours - total_weekly_workload_hours
    free_hours_four_weeks = free_hours_per_week * 4

    print(f"\nОбщая нагрузка за неделю: {total_weekly_workload_hours:.2f} ч.")
    print(f"Доступно всего времени в неделю: {weekly_available_hours:.2f} ч.")
    print(f"Свободное время за одну неделю: {free_hours_per_week:.2f} ч.")
    print(f"Свободное время за четыре недели: {free_hours_four_weeks:.2f} ч.")

if __name__ == "__main__":
    main()

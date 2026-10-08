first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

temp = first_room
first_room = second_room
second_room = temp

print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)

import time
import random

player_name = str(input("Введите ваше имя: "))
pet_name = str(input("Введите имя вашего питомца: "))
hunger = 100 # шкала голода
health = 100 # шкала здоровья
fatigue = 100 # шкала утомлённости
age = 0 # дней питомцу

def print_stats(): # печатаем статистику питомца
	global age
	age = age + 1
	print(".-.-.-.-.-.-.-.-.-Статистика-.-.-.-.-.-.-.-.-.\nУровень голода вашего питомца:", hunger, "\nУровень здоровья вашего питомца:", health, "\nУровень утомлённости вашего питомца:", fatigue, "\nДней питомцу:", age, "\n(^˵OωO˵^)\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
	time.sleep(2)

def skip_time(): # пропускаем 1 день
	global hunger, health, fatigue, pet_name
	print("Спустя 1 день...")
	hunger = hunger - 20
	fatigue = fatigue - 20
	illness()
	time.sleep(2)
	choise()

def feed(): # кормим питомца
	global hunger, health, fatigue, pet_name
	print("Вы покормили питомца",pet_name)
	hunger = 100
	fatigue = fatigue - 20
	illness()
	time.sleep(2)
	choise()

def play(): # играем с питомцем
	global hunger, health, fatigue, pet_name
	print("Вы поиграли с питомцем", pet_name)
	hunger = hunger - 20
	fatigue = 100
	illness()
	time.sleep(2)
	choise()

def treat(): # лечим питомца
	global hunger, health, fatigue, pet_name
	print("Вы вылечили питомца", pet_name)
	hunger = hunger - 20
	fatigue = fatigue - 20
	health = 100
	time.sleep(2)
	choise()

def choise(): # выбираем действие
	global hunger, health, fatigue, pet_name
	stats_check()
	print_stats()
	move = int(input("\nВыберите действие: Пропустить день(1), Покормить питомца(2), Поиграть с питомцем(3), Лечить питомца(4): "))
	if move == 1:
		skip_time()
	elif move == 2:
		feed()
	elif move == 3:
		play()
	elif move == 4:
		treat()
	else:
		print("Некорректный ввод. Напишите команду заново")
		time.sleep(2)
		choise()

def stats_check(): # проверяем статы питомца
	global hunger, health, fatigue, pet_name
	if hunger == 0:
		health = 0

	if health == 0:
		print("\n.-.-.-.-.-.-.-.-.-Ваш питомец умер-.-.-.-.-.-.-.-.-.\n(^˵XwX˵^)\nGame Over\nПрожито:", age, "дней")
		input()
		exit()
	elif fatigue == 0:
		print("\n.-.-.-.-.-.-.-.-.-Ваш питомец заскучал-.-.-.-.-.-.-.-.-.\n(^˵#w#˵^)\nGame Over\nПрожито:", age, "дней")
		input()
		exit()

def illness(): # шанс питомца заболеть
	global hunger, health, fatigue, pet_name
	illness_chanse = random.randint(0, 100)
	if illness_chanse <= 10:
		print(pet_name, "заболел. Похоже, его стоит вылечить")
		health = health - 20
	else:
		health = health

print("Добро пожаловать в Python-тамагочи!(by fra1ny)")
time.sleep(1.5)
choise()
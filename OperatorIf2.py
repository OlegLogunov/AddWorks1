print("Введите вес Вашей посылки: ")
height = int(input())

if height <= 2:
    cost_del = 50
elif 2 < height <= 10:
    cost_del = 50 + 20 * (height - 2)
elif height > 10:
    cost_del = 200

print ("Стоимость доставки составляет",cost_del,"руб.")
print ("Спасибо за выбор нашей логистической компании!")

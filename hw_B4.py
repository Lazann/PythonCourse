import random
print ('Угадай цифру от 1 до 100')
numb = random.randint(1,100)
X = 0
while X < 7:
    Xnumb = int(input('введите цифру:'))
    X +=1
    if Xnumb < numb:
        print('Эта цифра слишком маленькая')
    if Xnumb > numb:
        print('Эта цифра слишком большая')
    if Xnumb == numb:
        print ('Ты угадал! Правильный ответ', numb)
        break
    if X == 7:
        break
print('Загаданная цифра это', numb)

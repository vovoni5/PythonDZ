'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.'''

s = int(input('Введите сумму загадонных чисел: '))
p = int(input('Введите произведение загадонных чисел: '))

for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            if x <= 1000 and y <= 1000 :
                print(f'первое число ="{x}", второе число ="{y}"')
                break
            else :
                print('Петя жулик!')
                break
        
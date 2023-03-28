from random import choice

answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

def answer_the_question():
    question = input()
    print(choice(answers))
    print("Хотите ли вы задать еще вопрос?")

print('Привет друг, я магический шар, и я знаю ответ на любой ваш вопрос.\n'
      'Ответ может быть только односложным, так что задавайте правильные вопросы😉')
name = input("Давайте узнаем друг дуга, как вас зовут?\n")
print(f'Привет {name}, приятно познакомиться')

print("Каким же будет ваш вопрос, я жду не дождусь, чтобы вам ответить")
answer_the_question()
while True:
    users_guestion = input()
    if users_guestion.lower() in ('lf', 'да', 'da', 'rjytxyj', 'конечно', 'yes'):
        print("Так задавайте")
        answer_the_question()
    elif users_guestion.lower() in ('ytn', 'нет', 'net', 'yt', 'не', 'ne', 'no', 'nope'):
        print('Возвращайся если возникнут вопросы!')
        break
    else:
        print('Не понял🙄')
        continue
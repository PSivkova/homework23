# Использование %:
#     Переменные: количество участников первой команды (team1_num).
#     Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
team1_num = 5
print('В команде Мастера кода участников: %d!' % team1_num)

#     Переменные: количество участников в обеих командах (team1_num, team2_num).
#     Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
team2_num = 6
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))
#
# Использование format():
#     Переменные: количество задач решённых командой 2 (score_2).
#     Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
#
#     Переменные: время за которое команда 2 решила задачи (team1_time).
#     Пример итоговой строки: "Волшебники данных решили задачи за 18015.2 с !"
team1_time = 18015.2
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
#
# Использование f-строк:
#     Переменные: количество решённых задач по командам: score_1, score_2
#     Пример итоговой строки: "Команды решили 40 и 42 задач"
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
#
#     Переменные: исход соревнования (challenge_result).
#     Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
challenge_result = 'победа команды Мастера кода'
print(f'Результат битвы: {challenge_result}!')
#
#     Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
#     Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
tasks_total = score_1 + score_2
ime_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {ime_avg} секунды на задачу!')

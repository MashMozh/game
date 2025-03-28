import random
def student_1(a,b,c,d,e):
    theory=500+a
    tasks=500+b
    luck=500+c
    teacher=500+d
    condition=500+e
    print("theory=", theory,
     "tasks=", tasks,
     "luck=", luck,
     "teacher=", teacher,
     "condition=", condition)
    return student_1

def student_2(a,b,c,d,e):
    theory=500+a
    tasks=500+b
    luck=500+c
    teacher=500+d
    condition=500+e
    print("theory=", theory,
     "tasks=", tasks,
     "luck=", luck,
     "teacher=", teacher,
     "condition=", condition)
    return student_2
def student_3(a,b,c,d,e):
    theory=500+a
    tasks=500+b
    luck=500+c
    teacher=500+d
    condition=500+e
    print("theory=", theory,
     "tasks=", tasks,
     "luck=", luck,
     "teacher=", teacher,
     "condition=", condition)
    return student_3

def day_1_1():
  cases=[1,2,3,4,5,6,7,8,9,10]
  m = random.choice(cases)
  match m:
    case 1:
     e=50
     a,b,c,d=(0,)*4
     print("Ты проснулся, а сегодня замечательная погода, "
           "+ вайб(состояние)")
    case 2:
     e = -50
     a, b, c, d = (0,) * 4
     print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
           "Весь день на стрессе(состояние ухудшилось)")
    case 3:
     с = 100
     a, b, e, d = (0,) * 4
     print("Сегодня тыувидел падающую звезду и "
           "загадал желание - плюс удача")
    case 4:
     print("Ты нравишься старшекурснику/старшекурснице."
           " тебе скинули расписанные билеты с полезными пометками "
           "(йоу, да ты красотка/мачо""+ теория")
     a = 80
     e, b, c, d = (0,) * 4
    case 5:
     c = -80
     d= -60
     a, b, e = (0,) * 3
     print("Рассыпать соль — к ссорам и неудачам. "
          "Твои отношения с преподавателем и удача снизились")
    case 6:
     b = 80
     a, e, c, d = (0,) * 4
     print("Ты попал на бал великих математиков, они тебе все объяснили"
          " доступным языком(тралалело тралала)")
    case 7:
     b =- 70
     a, e, c, d = (0,) * 4
     print("Под окном орут студенты "
          "и тебе трудно сконцентрироваться (УК РФ ст.105…..)"
          "-задачи")
    case 8:
     a = -80
     e, b, c, d = (0,) * 4
     print("Тебя отвлекает шум машин за окном "
          "(за намеренный прокол колеса штраф дают, "
          "одумайся. УК РФ ст.167)""-теория(")
    case 9:
     d = 50
     a, b, c, e = (0,) * 4
     print("Ты улыбался другу, а преподаватель подумал,"
          " что ему, он поздоровался с тобой"
          " и улыбнулся в ответ""+ к отношению с преподвавателем")
    case 10:
     d = -90
     a, b, c, e = (0,) * 4
     print("На твоём телефоне произошел глюк и он отправил сообщение"
          " в 3 часа ночи не в ту группу,"
          " а в группу с преподавателем из за чего он проснулся "
          "- отношения с преподавателем")

  k=int(input())
  match k:
    case 1:
     student_1(a, b, c, d, e)
    case 2:
     student_2(a, b, c, d, e)
    case 3:
        student_3(a, b, c, d, e)


day_1_1()
input()
day_1_1()
input()
day_1_1()
input()

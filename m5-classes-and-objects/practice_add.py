class User:
    #nickname
    #password(в хэшированном виде, число)
    #age


class Video:
    #title (заголовок, строка)
    #duration (продолжительность, секунды)
    #time_now (секунда остановки(изначально 0))
    #adult_mode (ограничение по возрасту
    #bool (False по умолчанию))


class UrTube:
    #users (список объектов User)
    #videos (список объектов Video)
    #current_user (текущий пользователь, User)

    #log_in, принимает на вход: nickname, password и пытается найти пользователя в users с такими же логином и паролем
    #    current_user меняется на найденного (если такой пользователь существует)
    #    Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    #register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
    #    если пользователя не существует(с таким же nickname)
    #    Если существует, выводит на экран: "Пользователь {nickname} уже существует"
    #После регистрации, вход выполняется автоматически.

    #log_out для сброса текущего пользователя на None.

    #add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
    #    названием видео ещё не существует
    #В противном случае ничего не происходит.

    #get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово
    #Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'(не учитывать регистр).

    #watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего
    #не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр
    #После текущее время просмотра данного видео сбрасывается
   #     Для watch_video особенности:
   # Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
   # Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
   # В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
   # Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к.есть ограничения 18 +
   # Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
   # После воспроизведения нужно выводить: "Конец видео"

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)  # Добавление видео

print(ur.get_videos('лучший'))  # Проверка поиска
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')  # Проверка на вход пользователя и возрастное ограничение
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Проверка входа в другой аккаунт
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')  # Попытка воспроизведения несуществующего видео
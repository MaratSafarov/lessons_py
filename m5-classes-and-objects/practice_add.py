import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __hash__(self):
        return hash(self.nickname)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return

    def register(self, nickname, password, age):  # регистрация нового пользователя
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # автоматический вход после регистрации

    def log_out(self):
        self.current_user = None  # сброс текущего пользователя на None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:  # проверка, вошел ли пользователь
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        video = None  # поиск видео по точному совпадению заголовка
        for v in self.videos:
            if v.title == title:
                video = v
                break
        if not video:
            return

        if video.adult_mode and self.current_user.age < 18:  # проверка возрастного ограничения
            print("Вам нет 18 лет, пожалуйста покиньте страницу.")
            return

        for second in range(1, video.duration + 1):
            print(second, end=' ', flush=True)  # вывод каждой секунды
            time.sleep(1)  # пауза в 1 секунду между выводами

        print("Конец видео")
        video.time_now = 0  # сброс времени просмотра после завершения


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
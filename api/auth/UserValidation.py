
class UserValidation:
    error = dict()

    def validate_register(self, login, password, confirm_password, nickname):
        self.error = dict()
        self.check_login(login)
        self.check_password(password)
        self.check_confirm(password, confirm_password)
        self.check_nickname(nickname)
        return self.error

    def check_login(self, login):
        if len(login) == 0:
            self.error['login'] = 'Логин не должен быть пустым'
        elif len(login) < 5:
            self.error['login'] = 'Логин недостаточно длинный'

    def check_nickname(self, nickname):
        if len(nickname) == 0:
            self.error['nickname'] = 'Никнейм не может быть пустым'

    def check_password(self, password):
        if len(password) == 0:
            self.error['password'] = 'Пароль не должен быть пустым'
        elif len(password) < 8:
            self.error['password'] = 'Пароль недостаточно длинный'
        for el in password:
            if el in '0123456789':
                break
        else:
            self.error['password_number'] = 'Пароль должен содержать число'
        for el in password:
            if el in '#@!$%&*^./,;?][()|-=+':
                break
        else:
            self.error['password_symbol'] = 'Пароль должен содержать специальный символ'

    def check_confirm(self, password, confirm_password):
        if password != confirm_password:
            self.error['confirm_password'] = 'Пароли не совпадают'
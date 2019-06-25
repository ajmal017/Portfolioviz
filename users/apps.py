from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # saving profile for a user with signals
    def ready(self):
        import users.signals
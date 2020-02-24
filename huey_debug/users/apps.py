from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "huey_debug.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import huey_debug.users.signals  # noqa F401
        except ImportError:
            pass

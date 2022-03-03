from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db import connection


class RiverConfig(object):
    prefix = "RIVER"

    def __init__(self):
        self.cached_settings = None

    @property
    def settings(self):
        if self.cached_settings:
            return self.cached_settings
        else:
            from django.conf import settings

            allowed_configurations = {
                "CONTENT_TYPE_CLASS": ContentType,
                "GROUP_CLASS": Group,
                "INJECT_MODEL_ADMIN": False,
                "PERMISSION_CLASS": Permission,
                "USER_CLASS": settings.AUTH_USER_MODEL,
            }
            river_settings = {}
            for key, default in allowed_configurations.items():
                river_settings[key] = getattr(
                    settings,
                    self.get_with_prefix(key),
                    default,
                )

            river_settings["IS_MSSQL"] = connection.vendor == "microsoft"
            self.cached_settings = river_settings

            return self.cached_settings

    def get_with_prefix(self, config):
        return f"{self.prefix}_{config}"

    def __getattr__(self, item):
        if item in self.settings:
            return self.settings[item]
        else:
            raise AttributeError(item)


app_config = RiverConfig()

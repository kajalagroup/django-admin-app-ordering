from django.apps import AppConfig
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AppOrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_ordering"
    verbose_name = _("app ordering")

    def ready(self):
        def get_app_list(self, request, app_label=None):
            from app_ordering.models import Profile, AdminApp

            app_dict = self._build_app_dict(request, app_label)

            default_p = (
                Profile.objects.filter(is_default=True)
                .prefetch_related("admin_apps__admin_models")
                .first()
            )
            if not default_p:
                # Sort the apps alphabetically.
                app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

                # Sort the models alphabetically within each app.
                for app in app_list:
                    app["models"].sort(key=lambda x: x["name"])

                return app_list

            m_app_orders = {}

            for admin_app in default_p.admin_apps.all():
                assert isinstance(admin_app, AdminApp)
                m_app_orders[admin_app.app_label] = {
                    "order": admin_app.order,
                    "visible": admin_app.visible,
                    "modules": {},
                }
                for admin_model in admin_app.admin_models.all():
                    m_app_orders[admin_app.app_label]["modules"][admin_model.object_name] = {
                        "order": admin_model.order,
                        "visible": admin_model.visible,
                    }

            app_list = sorted(
                app_dict.values(),
                key=lambda x: (
                    1000
                    if x["app_label"] not in m_app_orders
                    else m_app_orders[x["app_label"]]["order"],
                    x["name"].lower(),
                ),
            )

            for app in app_list:
                app["visible"] = (
                    app["app_label"] not in m_app_orders
                    or m_app_orders[app["app_label"]]["visible"]
                )

                app_modules = m_app_orders.get(app["app_label"], {}).get("modules", {})
                app["models"].sort(
                    key=lambda x: (
                        1000
                        if x["object_name"] not in app_modules
                        else app_modules[x["object_name"]]["order"],
                        x["name"],
                    )
                )
                for model in app["models"]:
                    model["visible"] = True
                    # model['visible'] = True if model["object_name"] not in app_modules else app_modules[model["object_name"]]['visible']

            return app_list

        admin.AdminSite.get_app_list = get_app_list
        from . import signals as signals_init  # noqa

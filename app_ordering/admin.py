from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.urls import reverse
from app_ordering.services import sync_apps
from django.contrib.messages import add_message, SUCCESS
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase

from app_ordering.models import Profile, AdminApp, AdminModel


class AdminAppInlineAdmin(SortableTabularInline):
    model = AdminApp
    readonly_fields = (
        "edit_link",
        "app_label",
    )
    extra = 0

    def edit_link(self, instance):
        url = reverse(
            "admin:%s_%s_change" % (instance._meta.app_label, instance._meta.model_name),
            args=[instance.pk],
        )
        if instance.pk:
            return mark_safe('<a href="{u}">edit</a>'.format(u=url))
        else:
            return ""


class AdminModelInlineAdmin(SortableTabularInline):
    model = AdminModel
    extra = 0
    readonly_fields = ('object_name', )


class ProfileAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["created", "name", "is_default"]
    autocomplete_fields = ('users', 'groups')
    inlines = [
        AdminAppInlineAdmin,
    ]

    def changelist_view(self, request, extra_context=None):  # pylint: disable=too-many-locals
        sync_app = request.POST.get("sync_app")
        if sync_app:
            sync_apps()
            add_message(request, SUCCESS, _("all apps are synched"))  # noqa

        return super().changelist_view(request, extra_context)


class AdminAppAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = [
        "created",
        "app_label",
    ]
    inlines = [
        AdminModelInlineAdmin,
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(AdminApp, AdminAppAdmin)

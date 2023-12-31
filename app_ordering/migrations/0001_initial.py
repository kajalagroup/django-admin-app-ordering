# Generated by Django 4.2.3 on 2023-07-17 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminApp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "app_label",
                    models.CharField(max_length=200, verbose_name="app label"),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, default=1, verbose_name="order"
                    ),
                ),
                ("visible", models.BooleanField(default=True, verbose_name="visible")),
            ],
            options={
                "verbose_name": "admin app",
                "verbose_name_plural": "admin apps",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, unique=True, verbose_name="name"),
                ),
                (
                    "is_default",
                    models.BooleanField(default=False, verbose_name="is default"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, to="auth.group", verbose_name="groups"
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        blank=True, to=settings.AUTH_USER_MODEL, verbose_name="users"
                    ),
                ),
            ],
            options={
                "verbose_name": "profile",
                "verbose_name_plural": "profiles",
            },
        ),
        migrations.CreateModel(
            name="AdminModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "object_name",
                    models.CharField(max_length=200, verbose_name="object name"),
                ),
                ("order", models.PositiveIntegerField(default=1, verbose_name="order")),
                ("visible", models.BooleanField(default=True, verbose_name="visible")),
                (
                    "admin_app",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admin_models",
                        to="app_ordering.adminapp",
                        verbose_name="admin app",
                    ),
                ),
            ],
            options={
                "verbose_name": "admin model",
                "verbose_name_plural": "admin models",
                "ordering": ["order"],
            },
        ),
        migrations.AddField(
            model_name="adminapp",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="admin_apps",
                to="app_ordering.profile",
                verbose_name="profile",
            ),
        ),
    ]

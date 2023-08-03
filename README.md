# Django admin app ordering

**Django admin app ordering** is a Django app to able order module app in your Django app, it also support to toggle app or model.

Summary this are features:
- Sorting admin app, models.
- Toggle admin app, models.
- Configure sorting/visibility app(model) for certain users or groups.

![screenshot](https://raw.githubusercontent.com/kajalagroup/django-admin-app-ordering/develop/screenshot.png)


## Install

```
pip install django-admin-app-ordering
```

Add "app_ordering" and "adminsortable2" to app list:

```
INSTALLED_APPS = [
    ....
    "app_ordering",
    "adminsortable2"
]
````

**adminsortable2** is third party to help you to manipulate sorting easier.

Add get_package_template_dir("app_ordering") to TEMPLATES.DIR
Remember to import get_package_template_dir in the settings.py

```
from app_ordering.helpers import get_package_template_dir
```

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            get_package_template_dir("app_ordering"),
        ],
        ...
    },
]
```


## Profile:
- Default profile will be used as default if you don't set any specific profile for logged in user.
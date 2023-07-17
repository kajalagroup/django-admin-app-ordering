from os import path


def app_ordering_get_template_dir():
    current_dir = path.dirname(__file__)
    return path.join(current_dir, 'templates')

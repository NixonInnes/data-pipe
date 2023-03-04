import yaml
import importlib.util

def is_truthy(value):
    return value.lower() in ("true", "yes", "1", "on")


def load_module_from_file(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def camelcase(string):
    return "".join(
        [
            word.capitalize() if not all([char.isupper() for char in word]) else word 
            for word in string.split('_')
        ]
    )


def load_settings_from_yaml(filepath):
    from app import settings

    with open(filepath, 'r') as f:
        loaded = yaml.load(f, Loader=yaml.FullLoader)
    for key, value in loaded.items():
        settings.set(key, value)

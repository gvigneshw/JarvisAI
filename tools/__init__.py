import importlib
import pkgutil


for module in pkgutil.iter_modules(__path__):

    module_name = module.name

    importlib.import_module(
        f"{__name__}.{module_name}"
    )
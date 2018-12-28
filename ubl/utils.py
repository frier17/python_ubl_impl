
class Singleton(type):
    # define the singleton behaviour for the document template
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance


def key_gen(item, flags=(), registry=None):
    from enum import IntFlag
    key = None

    def generator(x):
        return ''.join(str.title(x).split('_'))
    valid_flags = [x is True for x in flags if isinstance(x, IntFlag)]
    valid_members = [x.__members__ for x in flags if isinstance(x, IntFlag)]

    if any(valid_flags):
        key = generator(item.name)
    elif isinstance(item, str) and any(valid_members):
        key = generator(item)
    elif isinstance(item, str) and item in registry:
        key = item
    return key

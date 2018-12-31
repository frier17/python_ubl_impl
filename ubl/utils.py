
class Singleton(type):
    # define the singleton behaviour for the document template
    __slots__ = ()

    def __call__(cls, *args, **kwargs):
        try:
            return cls._instance
        except (AttributeError, ValueError):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance

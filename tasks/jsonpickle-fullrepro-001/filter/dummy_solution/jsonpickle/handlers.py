class BaseHandler:
    def __init__(self, context=None):
        self.context = context

    def flatten(self, *args, **kwargs):
        return object()

    def restore(self, *args, **kwargs):
        return object()


class Registry:
    pass


def register(*args, **kwargs):
    return None


def unregister(*args, **kwargs):
    return None

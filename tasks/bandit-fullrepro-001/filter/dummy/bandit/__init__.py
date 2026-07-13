UNDEFINED = None
LOW = None
MEDIUM = None
HIGH = None


class Cwe:
    def __init__(self, id=0):
        raise NotImplementedError

    def link(self):
        return None

    def as_dict(self):
        return None

    def as_jsons(self):
        return None

    def from_dict(self, data):
        return None


class Issue:
    def __init__(self, severity, *args, **kwargs):
        raise NotImplementedError

    def filter(self, severity, confidence):
        return None

    def as_dict(self, with_code=True, max_lines=3):
        return None

    def from_dict(self, data, with_code=True):
        return None

    def get_code(self, max_lines=3, tabbed=False):
        return None

    def __eq__(self, other):
        return False


def _dummy_decorator(*args, **kwargs):
    def decorate(function):
        def wrapped(*call_args, **call_kwargs):
            return None

        return wrapped

    return decorate


checks = _dummy_decorator
test_id = _dummy_decorator
takes_config = _dummy_decorator


def accepts_baseline(function):
    def wrapped(*args, **kwargs):
        return None

    return wrapped

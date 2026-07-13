class _DummyValue:
    pass


def encode(*args, **kwargs):
    return _DummyValue()


def decode(*args, **kwargs):
    return _DummyValue()


def register(*args, **kwargs):
    return None


def unregister(*args, **kwargs):
    return None


def load_backend(*args, **kwargs):
    return None


def remove_backend(*args, **kwargs):
    return None


def set_preferred_backend(*args, **kwargs):
    return None


def set_encoder_options(*args, **kwargs):
    return None


def set_decoder_options(*args, **kwargs):
    return None


def enable_fallthrough(*args, **kwargs):
    return None


class Pickler:
    def __init__(self, *args, **kwargs):
        pass

    def flatten(self, *args, **kwargs):
        return _DummyValue()

    def reset(self):
        return None


class Unpickler:
    def __init__(self, *args, **kwargs):
        pass

    def restore(self, *args, **kwargs):
        return _DummyValue()

    def register_classes(self, *args, **kwargs):
        return None

    def reset(self):
        return None


class JSONBackend:
    def __init__(self, *args, **kwargs):
        pass

    def encode(self, *args, **kwargs):
        return _DummyValue()

    def decode(self, *args, **kwargs):
        return _DummyValue()

    dumps = encode
    loads = decode

    def load_backend(self, *args, **kwargs):
        return None

    def remove_backend(self, *args, **kwargs):
        return None

    def set_preferred_backend(self, *args, **kwargs):
        return None

    def set_encoder_options(self, *args, **kwargs):
        return None

    def set_decoder_options(self, *args, **kwargs):
        return None

    def enable_fallthrough(self, *args, **kwargs):
        return None


json = JSONBackend()

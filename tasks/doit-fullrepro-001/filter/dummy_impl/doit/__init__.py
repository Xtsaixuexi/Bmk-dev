
__version__ = '0.0-dummy'

class DummyError(Exception):
    pass
class DummyFail(Exception):
    report = True
    traceback = ''
    def __init__(self, *a, **kw):
        self.message = a[0] if a else ''
        super().__init__(*a)
    def get_msg(self): return str(self.message)
    def get_name(self): return self.__class__.__name__
class Dummy:
    DEFAULT_VERBOSITY = 1
    cmd_options = ()
    base_options = ()
    DOIT_CMDS = ()
    BIN_NAME = 'doit'
    def __init__(self, *a, **kw): pass
    def __call__(self, *a, **kw): return None
    def __iter__(self): return iter(())
    def __len__(self): return 0
    def __bool__(self): return False
    def __getitem__(self, key): raise KeyError(key)
    def __contains__(self, key): return False
    def __getattr__(self, name): return None
    def __enter__(self): return self
    def __exit__(self, *a): return False

def dummy_func(*a, **kw):
    return None

def __getattr__(name):
    if name in {'InvalidCommand','InvalidDodoFile','InvalidTask','CmdParseError','DatabaseException','TaskFailed','TaskError','UnmetDependency','SetupError','DependencyError','BaseFail','CatchedException'}:
        return type(name, (DummyFail if name in {'TaskFailed','TaskError','UnmetDependency','SetupError','DependencyError','BaseFail','CatchedException'} else DummyError,), {})
    if name and name[0].isupper():
        return type(name, (Dummy,), {})
    return dummy_func

def get_var(name, default=None): return None
def get_initial_workdir(): return None
def run(task_creators): return None
def create_after(*a, **kw):
    def dec(f): return f
    return dec
def task_params(*a, **kw):
    def dec(f): return f
    return dec
class Globals:
    dep_manager = None

__all__ = ['_cd_temp']

import contextlib
import os

@contextlib.contextmanager
def _cd_temp(_path):
    _cwd = os.getcwd()

    assert os.path.exists(_path), 'Unreachable directory'
    os.chdir(_path)

    try:
        yield
    except Exception as e:
        os.chdir(_cwd)
        raise e
    finally:
        os.chdir(_cwd)

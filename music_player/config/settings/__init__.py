import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

if env.bool('DEBUG'):
    from .development import *
else:
    from .production import *

try:
    from loaded import *
except ModuleNotFoundError:
    from spycalc import *


print(add_one(3))
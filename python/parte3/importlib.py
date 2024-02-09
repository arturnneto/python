import isInstance
import importlib
import closure

"""
Como recarregar módulos
"""

print(isInstance.lista)

for i in range(2):
    importlib.reload(isInstance)
    print()

# A script to see which modules you currently have installed

import sys, pkgutil


print("Python builtins: \n" + ("="*15) + "\n" + str(sys.builtin_module_names))

print("\n" + ("="*100) + "\n")

mods = list(mod[1] for mod in pkgutil.iter_modules())

print("Installed Modules: \n" + ("="*18) + "\n" + str(mods))
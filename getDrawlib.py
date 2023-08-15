# [Imports]
import os
import sys
import json
import importlib.util

# [Dep Functions]
def fromPath(path):
    path = path.replace("\\",os.sep)
    spec = importlib.util.spec_from_file_location("module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# [Config]
configFile = os.path.abspath(os.path.join(os.path.dirname(__file__),"config.json"))
args = sys.argv[1:]
for i,arg in enumerate(args):
    if "configFile" in arg:
        configFile = args[i+1]
mainConfig = json.loads(open(configFile,'r').read())

# [Load drawlib]
if mainConfig["drawlib"] == "PACKAGED":
    from libs import packaged_drawlib as drawlib
else:
    drawlib = fromPath(mainConfig["drawlib"])

# [Function]
def getDrawlib():
    return drawlib
import json

def getConfigurations():
    configfile = open(".pyidmconfig.json")
    return json.loads(configfile)

def getConfiguration(key):
    return getConfigurations().get(key)

def configure(key, value):
    
    configurations = getConfigurations()
    configurations[key] = value

    configfile = open(".pyidmconfig.json", "w")
    configfile.write(json.dumps(configurations))
    configfile.close()

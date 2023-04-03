import yaml, os

def read_yaml():
    with open("example.yaml", "r") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)

cpath:  str  = os.getcwd()
yfiles: list = []

# lists all files in current dir and /scrolls
for yf in os.listdir(cpath):
    if ".yaml" in yf:
        yfiles.append(yf)
if os.path.exists(f"{cpath}/scrolls"):
    for yf in os.listdir(f"{cpath}/scrolls"):
        if ".yaml" in yf:
            yfiles.append(yf)

if yfiles:
    pass # main road of the file
    print (yfiles)
else:
    exit()

import yaml, os

def read_yaml(name: str):
    with open(f"{name}", "r") as stream:
        return yaml.safe_load(stream)

class DocOpened:

    def __init__(self, fname: str):
        self.fname    = fname
        self.file     = read_yaml(fname)
        self.chapters      = self.file["Chapters"]
        self.chapters_list = self.chapters.keys()

    def unveil_chapter(self, chapter: str):
        chapter          = self.chapters[chapter] #dict
        chapter_sections = chapter.keys()         #list

class Explore:

    def __init__(self, files: list):
        self.files = files
        self.selec = 0
        self.dcop  = None

    def run(self):
        self.dcop = DocOpened(self.files[self.selec])

    def list_doc(self):
        pass #return self.files

    def switch_doc(self, name: str):
        self.selec = self.files.index(name)

# --------------------------------------------------
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
    se = Explore(yfiles)
    se.run()
else:
    exit()

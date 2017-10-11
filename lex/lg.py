SEP=';'

class lg:
    '''class representing lg table'''


    def __init__(self,ct,classname):
        self.name = classname
        self.classtable = ct #table of classes (e.g., table of classes)
        self.attributes = [] # list of features in occurring order

        self.entries = [] # list of entries

    def load_class(self,filename):
        f = open(filename,'r')
        self.read_attributes(f)
        print(self.attributes)
        for text in f:
            text = text.strip()
            print([a[1:-1] for a in text.split(SEP)])
            #if len(text) > 0:
            #    self.entries.append(entry(text,self))
        f.close()


    def read_attributes(self,file):
        line = file.readline()
        atts = line.split(SEP)
        self.attributes = [a[1:-1] for a in atts]

    def load_lg(self,filename):
       self.load_class(filename)

    def __str__(self):
        return self.name

    #def print_lg(self):
    #    #print([str(c) for c in self.classtable.get_constructions(self)])
    #    for e in self.entries:
    #        print(self.classtable.get_all_entry_features())
    #        print(self.name,':',e)






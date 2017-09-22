MWECAT='cat'
POS='pos'
LEMMA='lemma'
PERSON='person'
NUMBER='number'
NUMBER1='number1'
FUNC='func'
HUM='hum'
OPT='opt'
ADJUNCT='insert'
CONST='const'
ORDER='order'
SUBTYPE='subtype'
LOGICAL='logical'
MOOD='mood'
CONTROLLER='controller'
FIXED='fixed'

TRUE='true'
FALSE='false'
OR='OR'

class change:
    #fields:
    #author
    #date
    #type: auto, manual, semi-auto
    #description of procedure: a url
    #entrynode id
 

    def __init__(self,author,date,changetype,description,entrynodeid):
       self.author = author
       self.date = date
       self.changetype = changetype
       self.description = description
       self.entrynodeid = entrynodeid

    def toTex(self):
       s = '\\textbf{Change:}\n\\begin{itemize}\n'
       s += '\\item Author: '+self.author+'\n'
       s += '\\item Date: '+self.date+'\n'
       s += '\\item Type: '+self.changetype+'\n'
       s += '\\item Description: '+self.description+'\n'
       s += '\\item modified node: '+self.entrynodeid+'\n'
       s += '\\end{itemize}'
       return s


class feats:
    # representation of a feature structure
    #field a dictionary: either str -> str or str -> feats

    def __init__(self):
       self.feats = {}


    def addStrFeat(self,attribute,value):
       self.feats[attribute] = value

    def addFsFeat(self,attribute,fs):
       self.feats[attribute] = fs

    def toTex(self):
      s = '\\begin{itemize}\n'
      for a in self.feats:
          v = self.feats[a]
          #print(a,v,type(v))
          if type(v) is str:
             val = v
          else:
             val = v.toTex()
          s += '\\item '+a+': '+val+'\n'  
 
      s += '\\end{itemize}\n' 
      return s



class entry:
   #fields:
   # entry id
   # properties: dictionary of properties (attribute,values)
   # tree family: a sequence of abstract syntactic trees representing elementary structures of the entry
   # history: a sequence of changes (a Change class to be defined)   
  
   def __init__(self,ident):
      self.ident = ident
      self.properties = feats()
      self.trees = []
      self.history = []


   def __str__(self):
      return self.ident

   def addTree(self,tree):
      self.trees.append(tree)

   def addProperty(self,attribute,value):
       self.properties.addStrFeat(attribute,value)
   
   def addFsProperty(self,attribute,fs): 
       self.properties.addFsFeat(attribute,fs)

 
   def addChange(self,change):
       self.history.append(change)


   def toTex(self):
      s = '\\section{'+self.ident+'}\n'
      s += '\\subsection{Changes}\n\\begin{itemize}\n'
      for ch in self.history:
         s += '\\item ' + ch.toTex() +'\n'
      s += '\\end{itemize}\n'
      s += '\\subsection{Properties}\n'
      s += self.properties.toTex()
 

      s += '\n\\subsection{Trees}\n\n'
      for t in self.trees:
         s += '\\begin{figure}[h]\n'
         s += '\\begin{tikzpicture}\n'
         s += '\\tikzset{level 1+/.style={level distance=80pt}}\n'
         s += '\Tree'+t.toTex()+'\n'
         s += '\\end{tikzpicture}\n'
         s += '\\end{figure}\n'
      return s


class node:
    #fields
    #id: node id
    #feats: a dictionary -> a set of (att:str,value:str) or of(att:str,feats)
    #oblChildren: a set of obligatory children
    #optChildren

    def __init__(self,ident):
       self.ident = ident
       self.feats = {}
       self.oblChildren = []
       self.otherChildren = []

    def addFeat(self,att,val):
         self.feats[att] = val

    def setChildren(self,children):
        self.oblChildren = children


    def addChild(self,child):
        self.oblChildren.append(child)


    def addOtherChildren(self,child):
        self.otherChildren.append(child)

    def isLeaf(self):
      return len(self.oblChildren) == 0


    ## Beware: a known possible bug comparison of label should be with k (as it it is the attribute to be compared)  
    def featsToTex(self,label):
       s=''
       s+='id='+self.ident+'\\\\'
       for k in self.feats:
           if self.feats[k] != label:
             #print('**'+k+'='+label+'**')
             s+=str(k)+'='+str(self.feats[k])+'\\\\'
       return s[0:len(s)-2]
      

    def toTex(self,level=0,color='black'):
      label = self.feats.get(LOGICAL,self.feats.get(CONST,self.feats.get(POS)))
      if label is None:
         return "MISSING LABEL"
      s = ''
      if not self.isLeaf():
         s = '[.' 
      s += '{\color{'+color+'}\\lfs{'+str(label)+'}{'+self.featsToTex(label)+'}}\n'
      for c in self.oblChildren:
         s += (' '*((level+1)*4))+c.toTex(level=(level+1))+'\n'
      for c in self.otherChildren:
         s += (' '*((level+1)*4))+c.toTex(level=(level+1),color='blue')+'\n'

      if not self.isLeaf():
         s += ' '*(level*4)+' ]'
      s = s.replace('\n\n','\n')
      return normalizeForLatex(s)

    def __str__(self):
       return "[id="+self.ident+":::"+str(self.feats)+"](children="+str([str(ch) for ch in self.oblChildren])+")"

    

def normalizeForLatex(s):
   s = s.replace('à','\\grave{a}')
 
   return s

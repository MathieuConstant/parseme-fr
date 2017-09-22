from mwe import *
from entryfactory import *


def generateAbandonnerASonSort():
  #e = entry('abandonner-a-son-sort-1')
  #print(e)

  s = createNode('idtest',cat='id',const='SENT')

  n0=createNode('n0',const='NP',hum=TRUE,func='subj')
  s.addChild(n0)
  
  vp = createNode('vp',const='VP')
  verb = createNode('abandonner',pos='VERB',lemma='abandonner')
  vp.addChild(verb)
  s.addChild(vp)

  n1 = createNode('n1',const='NP',func='obj')
  s.addChild(n1)

  pp = createNode('pp',const='PP',func='obl',opt=TRUE)
  prepa = createNode('prepa',pos='ADP',lemma='à')
  pp.addChild(prepa)
  np = createNode('np',const='NP') 
  pp.addChild(np)
  poss1 = createNode('poss1',pos='DET',subtype='poss',number1='n1.number',person='n1.person') ##add agreement as feat structure
  np.addChild(poss1)
  sort = createNode('sort',pos='NOUN',lemma='sort',number='sing')
  np.addChild(sort)
  s.addChild(pp)
  
  return s


def generateAvoirBesoin():
   s = createNode('avoirbesoin',const='SENT')

   n0 = createNode('n0',const='NP',func='subj')
   s.addChild(n0)
   

   vp = createNode('vp',const='VP')
   s.addChild(vp)
   verb= createNode('avoir@v',pos='VERB',lemma='avoir')
   vp.addChild(verb)
   
   n1=createNode('n1',const='NP',func='obj')
   s.addChild(n1)
   

   ornode3 = createNode("ornode3",logical=OR)
   np11 = createNode("np11",const='NP',adjunct=FALSE,number='sg')
   noun = createNode('besoin@n',pos='NOUN',lemma='besoin')
   np11.addChild(noun)
   np12 = createNode('np12',const='NP',adjunct=FALSE)
   det = createNode('det',pos='DET')
   adjunct = createNode('adjunct',const='ADJUNCT')
   np12.setChildren([det,noun,adjunct])
   np13 = createNode('np13',const='NP',fixed=TRUE,adjunct=FALSE)
   grand = createNode('grand.adjunct',const='ADJUNCT',lemma='grand')
   np13.setChildren([grand,noun])
   ornode3.setChildren([np11,np12,np13])
   n1.addChild(ornode3)
   
   ornode = createNode('or',logical=OR)
   n1.addChild(ornode)
   pp = createNode('pp',const='PP')
   ornode.addChild(pp)
   prepde = createNode('prepde',pos='ADP',lemma='de')
   pp.addChild(prepde)
   ornode2 = createNode('ornode2',logical=OR)
   pp.addChild(ornode2)
   inf = createNode('inf',const='INF',controller='n0')
   np = createNode('np',const='NP')
   ornode2.addChild(inf)
   ornode2.addChild(np)

   compl = createNode('compl',const='COMPL',mood='subjunctive')
   ornode.addChild(compl)

   return s

def generateAvoirBesoinEntry():
    e = entry('avoirbesoin.entry')
    #author,date,changetype,description,entrynodeid

    ch = change('Mathieu Constant','20/09/2017','semi-auto','No url provided for description of the procedure','avoirbesoin.entry')
    ch2 = change('Agata Savary','22/09/2017','manual','No url','besoin@n')
    s = generateAvoirBesoin()
    e.addTree(s)
    e.addChange(ch)
    e.addChange(ch2)
    e.addProperty('mwetype','lvc')
    e.addProperty('mwepos','verb')
    criteria = feats()
    e.addFsProperty('criteria',criteria)
    criteria.addStrFeat('CRAN','false')
    criteria.addStrFeat('ZERO','true')
    return e



def generateLatex(entry):
  s = ''
  s+='\\documentclass[8pt,landscape,a3]{amsart}\n'
  s+='\\usepackage[utf8]{inputenc}\n'
  s+='\\usepackage[a3paper]{geometry}\n'                
  #% See geometry.pdf to learn the layout options. There are lots.
  #\geometry{letterpaper}                   % ... or a4paper or a5paper or ... 
  #%\geometry{landscape}                % Activate for for rotated page geometry
  # %\usepackage[parfill]{parskip}    % Activate to begin paragraphs with an empty line rather than an indent
  #\usepackage{graphicx}
  #\usepackage{amssymb}
  #\usepackage{epstopdf}
  s+='\\usepackage{tikz-qtree}\n'
  s += '\\usepackage{covington}\n'


  s+='\\begin{document}\n'
  s+=entry.toTex()+'\n'
  s+='\\end{document}\n'
  return s
 


s=generateAbandonnerASonSort()
s=generateAvoirBesoinEntry()
print(generateLatex(s))



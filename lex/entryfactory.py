from mwe import *


def createConstituent(id,const):
    return createNode(id,const=const)

def createNP(id):
   return createConstituent(id,'NP')

def createVP(id):
   return createNode(id,const='VP')

def createNPHum(id):
    return createNode(id,const='NP',hum='true')

def createNPSubj(id):
    return createNode(id,const='NP',func='subj')


def createLexicalNode(id,pos,lemma):
    return createNode(id,pos=pos,lemma=lemma)


def createNode(id,pos=None,lemma=None,hum=None,const=None,func=None,cat=None,adjunct=None,opt=None,subtype=None,order=None,number=None,number1=None,person=None,logical=None,mood=None,controller=None,fixed=None):
    e = node(id)
    if pos is not None:
       e.addFeat(POS,pos)
    if lemma is not None:
       e.addFeat(LEMMA,lemma)
    if hum is not None:
       e.addFeat(HUM,hum)
    if const is not None:
       e.addFeat(CONST,const)
    if func is not None:
       e.addFeat(FUNC,func)
    if cat is not None:
       e.addFeat(MWECAT,cat)
    if adjunct is not None:
       e.addFeat(ADJUNCT,adjunct)
    if opt is not None:
       e.addFeat(OPT,opt)
    if subtype is not None:
       e.addFeat(SUBTYPE,subtype)
    if order is not None:
       e.addFeat(ORDER,order)
    if number is not None:
       e.addFeat(NUMBER,number)
    if number1 is not None:
       e.addFeat(NUMBER1,number1)
    if person is not None:
       e.addFeat(PERSON, person)
    if logical is not None:
       e.addFeat(LOGICAL,logical)
    if mood is not None:
       e.addFeat(MOOD,mood)
    if controller is not None:
       e.addFeat(CONTROLLER,controller)
    if fixed is not None:
       e.addFeat(FIXED,fixed)
    return e


 
      




from Compiler.Strings.StringProcessor import StringProcessor as stringprocc
import Compiler.overhead as overhead 

def readInstructions(file):
    f = open(file, 'r')
    contentInArchive = f.readlines()
    lista = []
    for i in contentInArchive:
        lista.append(i.rstrip())
    return(lista)

class Compiler():
    def __init__(self, sess, file):
        self.sess = sess 
        self.stringProcc = stringprocc(1)
        self.instructions = readInstructions(file)
        self.endFile = './output.py'
    def fillInstructions(self, instructions):
        self.instructions = instructions
    def interpret(self):
        f = open(self.endFile, 'a')
        for i in self.instructions:
            comp = self.stringProcc.parceString(i)
            for i in comp:
                f.write(i)
        f.close()        
    def addOver(self):
        overhead.returnOverhead()
    def addLast(self):
        overhead.addOthers()


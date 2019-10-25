import Strings.StringProcessor as stringprocc
import overhead as ov
class Compiler():
    def __init__(self, sess):
        self.sess = sess 
        self.stringProcc = stringprocc(1)
        self.instructions = []
        self.overhead = ov(1)

    def fillInstructions(self, instructions):
        self.instructions = instructions
    def interpret(self):
        
        return(inter)
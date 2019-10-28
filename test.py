from Compiler.compiler import Compiler


c = Compiler(1, './definition.def')
c.addOver()
c.interpret()
c.addLast()
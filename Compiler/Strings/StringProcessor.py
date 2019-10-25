
def loadRules():
    f = open('./rules.ro', 'r')
    contentInArchive = f.readlines()
    lista = []
    for i in contentInArchive:
        lista.append(i.rstrip())
    return(lista)

class StringProcessor():
    def __init__(self, session):
        self.session = session
        self.ruleSet = loadRules()
        self.sintactic = []
    def parceString(self, string):
        arrayOfInstructions = string.split(' ')
        print(self.ruleSet)
        if(arrayOfInstructions[0] not in self.ruleSet):
            sintactic.append('Sintactic error, rule not in rule set.')
        else:
            if(arrayOfInstructions[0] == 'lstm'):
                numCells = 0
                recurrActivation = 'softmax'
                activation = 'softmax'
                last = False
                i = ''
                cont = 1
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if( i == 'numCell'):
                        numCells = arrayOfInstructions[cont+1]
                    if( i == 'recurrActivation'):
                        recurrActivation = arrayOfInstructions[cont+1]
                    if( i == 'activation'):
                        activation = arrayOfInstructions[cont+1]
                    if(i == 'last'):
                        last = True 
                    cont = cont + 1    
                cantidad = arrayOfInstructions[len(arrayOfInstructions)-2]
                if(last == False):
                    return('model.add(LSTM('+numCells+', dropout = 0.1, recurrent_dropout = 0.1, return_sequences = True, unroll = True, recurrent_activation = '+recurrActivation+",bias_initializer='RandomNormal',implementation=1))")
                else:
                     return('model.add(LSTM('+numCells+', dropout = 0.1, recurrent_dropout = 0.1, unroll = True, recurrent_activation = '+recurrActivation+" ,bias_initializer='RandomNormal',implementation=1))")
                    

loadRules()
a = StringProcessor('one')
print(a.parceString('lstm ( numCell 5 activation relu drop 0.1 ) 5 .') )

            
            

    
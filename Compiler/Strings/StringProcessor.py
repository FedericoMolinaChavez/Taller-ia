import os

def loadRules():
    print(os.listdir())
    f = open('./Compiler/Strings/rules.ro', 'r')
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
        print(arrayOfInstructions)
        arrayOfSol = []
        if(arrayOfInstructions[0] not in self.ruleSet):
            sintactic.append('Sintactic error, rule not in rule set.')
        else:
            if(arrayOfInstructions[0] == 'lstm'):
                numCells = '0'
                recurrActivation = 'softmax'
                activation = 'softmax'
                last = 'False'
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
                        last = 'True' 
                    cont = cont + 1    
                cantidad = arrayOfInstructions[len(arrayOfInstructions)-2]
                for i in range(0,int(cantidad)):
                    if(last == 'False'):
                        arrayOfSol.append('model.add(LSTM('+numCells+', dropout = 0.1, recurrent_dropout = 0.1, return_sequences = True, unroll = True, recurrent_activation = '+"'"+recurrActivation+"'"+",bias_initializer='RandomNormal',implementation=1)) \n")
                    else:
                        arrayOfSol.append('model.add(LSTM('+numCells+', dropout = 0.1, recurrent_dropout = 0.1, unroll = True, recurrent_activation = '+"'"+recurrActivation+"'"+" ,bias_initializer='RandomNormal',implementation=1)) \n")
                return arrayOfSol
            if(arrayOfInstructions[0] == 'dense'):
                units = 0
                activation = ''
                use_bias = False 
                kernel_initializer = 'glorot_uniform'  
                kernel_regularizer = 'None'  
                bias_regularizer = 'None' 
                activity_regularizer= 'None' 
                kernel_constraint = 'None' 
                bias_constraint = 'None'
                i = ''
                cont = 1
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if (i == 'units'):
                        units = arrayOfInstructions[cont+1]
                    if ( i == 'activation'):
                        activation = arrayOfInstructions[cont + 1]
                    if (i == 'use_bias'):
                        bias = arrayOfInstructions[cont + 1]
                    if (i == 'kernel_initializaer'):
                        kernel_initializer = arrayOfInstructions[cont + 1]
                    if (i == 'bias_regularizer'):
                        bias_regularizer = arrayOfInstructions[cont + 1]
                    if (i== 'activity_regulizer'):
                        activity_regularizer = arrayOfInstructions[cont + 1]
                    if ( i == 'kernel_constraint'):
                        kernel_constraint = arrayOfInstructions[cont + 1]
                    if ( i == 'bias_constraint'):
                        bias_constraint = arrayOfInstructions[cont + 1]
                    cont = cont + 1  
                cantidad = arrayOfInstructions[len(arrayOfInstructions)-2]
                print(cantidad)
                for i in range(0,int(cantidad)):
                    arrayOfSol.append('model.add(Dense('+units+', activation ='+"'"+activation+"'"+', use_bias= '+ bias+ ', kernel_initializer= '+ "'"+ kernel_initializer + "'"+', kernel_regularizer=' + kernel_regularizer + ', bias_regularizer =' + bias_regularizer + ', activity_regularizer='+ activity_regularizer+ ', kernel_constraint='+ kernel_constraint + ', bias_constraint=' + bias_constraint + '))\n')
                return arrayOfSol
            if (arrayOfInstructions[0] == 'embedding'):
                input_dim = 0
                output_dim = 0
                embedding_initializer = 'uniform'
                embeddings_regularizer= None
                embeddings_constraint=None
                mask_zero = False
                input_length = None 
                i = ''
                cont = 1
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if (i == 'input_dim'):
                        input_dim = arrayOfInstructions[cont + 1]
                    if (i == 'output_dim'):
                        output_dim = arrayOfInstructions[cont + 1]
                    if (i == 'embedding_initializer'):
                        embedding_initializer = arrayOfInstructions[cont + 1]
                    if (i == 'embeddings_regularizer'):
                        embeddings_regularizer = arrayOfInstructions[cont + 1]
                    if (i == 'embeddings_constraint'):
                        embeddings_constraint = arrayOfInstructions[cont + 1]
                    if (i == 'mask_zero'):
                        mask_zero = arrayOfInstructions[cont + 1]
                    if (i == 'input_length'):
                        input_length = arrayOfInstructions[cont + 1]
                    cont = cont + 1      
                cantidad = arrayOfInstructions[len(arrayOfInstructions)-2]
                print(cantidad)
                for i in range(0,int(cantidad)):
                    arrayOfSol.append('model.add(Embedding('+input_dim+' , '+output_dim + ', input_length='+ input_length+'))\n')
                return arrayOfSol
            if(arrayOfInstructions[0] == 'cnn'):
                d = '1d'
                filters = ''
                kernel_size = '0'
                strides = '1'
                padding = 'valid'
                data_format = 'channels_last'
                dilation_rate = '1'
                activation = 'None'
                use_bias = 'True'
                kernel_initializer = 'glorot_uniform'
                bias_initializer = 'zeros'
                kernel_regularizer = 'None'
                activity_regularizer = 'None'
                kernel_constraint = 'None'
                bias_constraint = 'None'
                bias_regularizer = 'None'
                i = ''
                cont = 1
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if(i == 'd'):
                        d = arrayOfInstructions[cont + 1]
                    if(i == 'filters'):
                        filters = str(arrayOfInstructions[cont + 1])
                    if(i == 'kernel_size'):
                        kernel_size = '('+arrayOfInstructions[cont + 1]+','+arrayOfInstructions[cont + 1]+')'
                    if(i == 'strides'):
                        if(d == '2d'):
                            strides = '('+arrayOfInstructions[cont + 1]+','+arrayOfInstructions[cont + 1]+')'
                        else:
                            strides = arrayOfInstructions[cont + 1]
                    if(i == 'padding'):
                        padding = arrayOfInstructions[cont + 1]
                    if(i == 'data_format'):
                        data_format = arrayOfInstructions[cont + 1]
                    if(i == 'dilation'):
                        if(d == '2d'):
                            dilation = '('+arrayOfInstructions[cont + 1]+','+arrayOfInstructions[cont + 1]+')'
                        else:
                            dilation = arrayOfInstructions[cont + 1]
                    if(i == 'activation'):
                        activation = arrayOfInstructions[cont + 1]
                    if(i == 'use_bias'):
                        use_bias = arrayOfInstructions[cont + 1]
                    if(i == 'kernel_initializer'):
                        kernel_initializer = arrayOfInstructions[cont + 1]
                    if(i == 'bias_initializer'):
                        bias_initializer = arrayOfInstructions[cont + 1]
                    if(i == 'kernel_regularizer'):
                        kernel_regularizer = arrayOfInstructions[cont + 1]
                    if(i == 'bias_regularizer'):
                        bias_regularizer = arrayOfInstructions[cont + 1]
                    if(i == 'activity_regularizer'):
                        activity_regularizer = arrayOfInstructions[cont + 1]
                    if(i == 'kernel_constraint'):
                        kernel_constraint = arrayOfInstructions[cont + 1]
                    if(i == 'bias_constraint'):
                        bias_constraint = arrayOfInstructions[cont + 1]
                    cont = cont + 1
                cantidad = arrayOfInstructions[len(arrayOfInstructions)-2]
                print(cantidad)
                for i in range(0,int(cantidad)):
                    if(d == '1d'):   
                        arrayOfSol.append('model.add(Conv1D('+filters+' , '+kernel_size+', strides='+strides+', padding= '+ "'"+padding+ "'"+', data_format= '+ "'"+ data_format + "'"+ ', dilation_rate=' + dilation_rate + ', activation =' + activation + ', use_bias='+ use_bias+', kernel_initializer = '+ "'"+kernel_initializer+ "'"+', bias_initializer='+ "'"+bias_initializer+"'"+', kernel_regularizer='+kernel_regularizer +', bias_regularizer='+bias_regularizer+', activity_regularizer ='+ activity_regularizer +', kernel_constraint ='+kernel_constraint+', bias_constraint='+bias_constraint+'))\n')
                    else:
                        arrayOfSol.append('model.add(Conv2D('+filters+','+kernel_size+', strides='+strides+', padding= '+"'"+ padding+"'"+ ', data_format= '+"'"+  data_format +"'"+ ', dilation_rate=' + dilation_rate + ', activation =' + activation + ', use_bias='+ use_bias+', kernel_initializer = '+"'"+kernel_initializer+"'"+', bias_initializer='+"'"+ bias_initializer+"'"+', kernel_regularizer='+kernel_regularizer +', bias_regularizer='+bias_regularizer+', activity_regularizer ='+activity_regularizer+', kernel_constraint ='+kernel_constraint+', bias_constraint='+bias_constraint+'))\n')
                return arrayOfSol
            if(arrayOfInstructions[0] == 'pool'):
                pool_size = "2"
                strides = 'None'
                padding = 'valid'
                data_format = 'channels_last'
                d = '1d'
                i = ''
                cont = 1
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if(i == 'pool_size'):
                        pool_size = arrayOfInstructions[cont + 1]
                    if(i == 'strides'):
                        strides = arrayOfInstructions[cont + 1]
                    if(i == 'padding'):
                        padding = arrayOfInstructions[cont + 1]
                    if(i == 'data_format'):
                        data_format = arrayOfInstructions[cont + 1]
                    if(i == 'd'):
                        d = arrayOfInstructions [cont + 1]
                    cont = cont + 1
                if(d == '1d'):
                    arrayOfSol.append('model.add(MaxPooling1D('+'pool_size ='+pool_size+', strides= '+ strides+ ', padding= '+ "'"+ padding + "'"+ ', data_format=' + "'"+ data_format+ "'"+'))\n')
                else:
                    arrayOfSol.append('model.add(MaxPooling1D('+'pool_size ='+pool_size+', strides= '+ strides+ ', padding= '+ "'"+ padding + "'"+ ', data_format=' + "'"+ data_format+ "'"+'))\n')
                return(arrayOfSol)
            if(arrayOfInstructions[0] == 'flatten'):
                arrayOfSol.append('model.add(Flatten())\n')
                return(arrayOfSol)
            if(arrayOfInstructions[0] == 'optim'):
                type = 'adam'
                cont = 1
                i = arrayOfInstructions[1]
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if(i  == 'adam'):
                        arrayOfSol.append('optimizerx =  optimizers.Adam(lr=0.001) \n')
                        
                    if(i  == 'SGD'):
                        arrayOfSol.append('optimizerx = optimizers.SGD(lr=0.01) \n')
                    if(i  == 'adagrad'):
                        arrayOfSol.append('optimizerx = optimizers.Adagrad(lr=0.01)')
                    if(i  == 'RMSprop'):
                        arrayOfSol.append('optimizerx = optimizers.RMSprop(lr=0.001) \n')
                    if(i  == 'Adamax'):
                        arrayOfSol.append('optimizerx = optimizers.Adamax(lr=0.002) \n')
                    if(i  == 'Nadam'):
                       arrayOfSol.append('optimizerx = optimizers.Nadam(lr=0.002) \n')
                    cont = cont + 1
                return(arrayOfSol)
            if(arrayOfInstructions[0] == 'loss'):
                arrayOfSol.append("model.compile(loss ="+ arrayOfInstructions[1] +", optimizer = optimizerx,metrics=['accuracy']) \n")
                return(arrayOfSol)
            if(arrayOfInstructions[0] == 'global'):
                batch_size = 10
                epochs = 10
                drop = 0.01
                r_drop = 0.01
                cont = 1
                i = arrayOfInstructions[1]
                while i != ')':
                    i = arrayOfInstructions[cont]
                    if(i == 'batch_size'):
                        arrayOfSol.append('batch_size ='+arrayOfInstructions[cont + 1]+'\n')
                    if(i == 'epochs'):
                        arrayOfSol.append('epochs ='+arrayOfInstructions[cont + 1]+'\n')
                    if(i == 'drop'):
                        arrayOfSol.append('drop ='+arrayOfInstructions[cont + 1]+'\n')
                    if (i == 'r_drop'):
                        arrayOfSol.append('r_drop ='+arrayOfInstructions[cont + 1]+'\n')
                    cont = cont + 1
                return(arrayOfSol)
            if(arrayOfInstructions[0] == 'conjunto'):
                arrayOfSol.append('trainx,trainy,testx,testy,valx,valy = trueCreateFeatureVector('+"'"+arrayOfInstructions[2]+"'"+','+"'"+arrayOfInstructions[3]+"'"+')\n')
                return(arrayOfSol)
            if(arrayOfInstructions[0] == 'Reshape'):
                shape = arrayOfInstructions[2]
                input_shape = arrayOfInstructions[3]
                arrayOfSol.append('model.add(Reshape( '+ shape+ ', input_shape ='+input_shape+')) \n')
                return(arrayOfSol)

            
            

    
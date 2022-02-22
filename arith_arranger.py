'''
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
'''
def run(stri, default=False):
    string = [st for st in stri]
    try:
        if len(string) > 5:
            raise TypeError('\nError: Too many problems')
        else:

            lista_gen = []
            for i in range(len(string)):
                values = string[i].split()
                try:
                    if values[1] == '/' or values[1] == '*':
                        raise TypeError('\nError: Operator must be + or -.')
                    elif ((values[0].isdigit() == False) or (values[2].isdigit() == False)):
                        raise TypeError('\nError:Numbers must only contain digits.')
                    elif ((len(values[0])> 4) or (len(values[2])>4)):
                        raise TypeError('\nError:Numbers cannot be more than four digits.')
                    else:
                        if values[1] == '+':
                            operation  = int(values[0]) + int(values[2]) 
                        elif values[1] == '-':
                            operation  = int(values[0]) - int(values[2])
                        lineas = '--'
                        for i in range(len(str(operation))):
                            lineas =  '-' + lineas
                        a = len(values[0])
                        b = len(values[2])
                        large = max(a,b)
                        small = min(a,b)
                        #print(large)
                        if a == large:
                            lineas = "-"*(len(values[0])+2)
                            space1 = ' '*(len(lineas) - (small+1))
                            if default == True:
                                lista = ["  "+values[0], values[1]+space1+values[2],lineas, space1+str(operation)]
                            else:
                                lista = ["  "+values[0], values[1]+space1+values[2],lineas]
                        else:
                            lineas = "-"*(len(values[2])+2)
                            space1 = ' '*(len(lineas) - (large+1))
                            space2 = ' '*(len(lineas) - (small))
                            if default ==  True:
                                lista = [space2 + values[0], values[1]+space1+values[2],lineas, space1+str(operation)]
                            else:
                                lista = [space2 + values[0], values[1]+space1+values[2],lineas]
                        lista_gen.append(lista)
                
                        
                except TypeError as ve:
                    print(ve)

            for arr in zip(*lista_gen):
                            print('    '.join(arr))
    except TypeError as ve:
        print(ve)

        
if __name__ == '__main__':
    string = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    result = True
    run(string)
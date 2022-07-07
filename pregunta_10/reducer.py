#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    #curvalue = 0
    #maximo = 0
    lista_aux = []

    for line in sys.stdin:

        lista_line = line.split("\t")
        key = lista_line[0]
        val = int(lista_line[1])
        #val = int(val)

        if key == curkey:
            lista_aux.append(val)
            lista_aux.sort()
        else:
            if curkey is not None:
                lista_aux_2 = str(lista_aux)[1:-1].strip().replace(" ","")
                sys.stdout.write("{}\t{}\n".format(curkey, lista_aux_2))
                lista_aux = []
                #sys.stdout.write("{}\n".format(val))
            

            curkey = key
            lista_aux.append(val)
            lista_aux.sort()
    lista_aux_2 = str(lista_aux)[1:-1].strip().replace(" ","")
    sys.stdout.write("{}\t{}\n".format(curkey, lista_aux_2))
    #sys.stdout.write("{}\n".format(val))
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    #curvalue = 0
    maximo = 0
    minimo = 100000000

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            if val >= maximo:
                maximo = val
            else:
                maximo = maximo
            
            if val <= minimo:
                minimo = val
            else:
                minimo = minimo
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))

            curkey = key
            maximo = val
            minimo = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo,minimo))
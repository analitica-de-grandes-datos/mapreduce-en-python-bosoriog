#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    total = 0
    conteo = 0
    media = 0

    for line in sys.stdin:

        linea = line.strip()
        key, val, cont = linea.split("\t")
        val = int(val)
        cont = int(cont)

        if key == curkey:
            total += val
            conteo += cont
            media = total/conteo
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(total), media))

            curkey = key
            total = val
            conteo = cont
            media = total/conteo

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(total),media))
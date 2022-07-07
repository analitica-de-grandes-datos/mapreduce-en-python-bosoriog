#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for line in sys.stdin:
        linea = line.strip()
        key, val = linea.split("\t")

        sys.stdout.write("{},{}\n".format(val, str(key)))
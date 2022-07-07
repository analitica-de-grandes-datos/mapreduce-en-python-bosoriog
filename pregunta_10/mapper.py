#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        linea = line.strip()
        lista = linea.split("\t")
        abcd = lista[1].split(",")

        for letra in abcd:
            sys.stdout.write("{}\t{}\n".format(letra,lista[0]))

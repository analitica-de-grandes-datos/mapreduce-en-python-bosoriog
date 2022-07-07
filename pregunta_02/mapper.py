#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        linea = line.strip()
        lista = linea.split(",")    
        sys.stdout.write("{}\t{}\n".format(lista[3],lista[4]))

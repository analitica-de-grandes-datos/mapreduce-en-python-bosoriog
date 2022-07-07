#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        linea = line.strip()
        lista = linea.split("  ")    
        sys.stdout.write("{}\t{}\t1\n".format(lista[0],lista[2]))
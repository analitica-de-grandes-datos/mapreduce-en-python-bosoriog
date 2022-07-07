#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None

    lista_aux = []

    for line in sys.stdin:
        linea = line.strip()
        lista_aux.append(linea)
        
    sorted_rows = sorted(lista_aux, key=lambda x: (int(x.split("\t")[2])))

    for valor in sorted_rows[:6]:
        valor_lista = valor.split("\t")
        key = valor_lista[0]
        fecha = valor_lista[1]
        val = valor_lista[2]

        sys.stdout.write("{}  {}  {}\n".format(key,fecha,val))
    #sys.stdout.write("{}\n".format(sorted_rows))
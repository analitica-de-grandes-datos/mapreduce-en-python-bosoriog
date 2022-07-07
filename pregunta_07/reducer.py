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
        
    sorted_rows = sorted(lista_aux, key=lambda x: (x.split("\t")[0],int(x.split("\t")[1])), reverse=False)

    for valor in sorted_rows:
        valor_lista = valor.split("\t")
        key = valor_lista[0]
        fecha = valor_lista[2]
        val = valor_lista[1]

        sys.stdout.write("{}  {}  {}\n".format(key,fecha,val))
    
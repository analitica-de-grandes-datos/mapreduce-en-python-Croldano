#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
        
        limpiarlinea = row.strip()
            
        letra, numero = limpiarlinea.split(",") 

        sys.stdout.write(f"{letra}\t{numero}\n")
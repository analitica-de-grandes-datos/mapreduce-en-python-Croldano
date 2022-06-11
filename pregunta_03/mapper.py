#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
        
        Limpiar_linea = row.strip()
            
        letra, numero = limpiar_linea.split(",") 

        sys.stdout.write(f"{letra}\t{numero}\n")
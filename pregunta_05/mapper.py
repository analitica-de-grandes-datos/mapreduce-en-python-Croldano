#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:

        divido = row.strip().split("   ")
        col01 = divido[1]
        dividefecha= col01.split("-")
        mes = dividefecha[1]
  
        sys.stdout.write(f"{mes}\t1\n")
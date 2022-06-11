#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
        
        divide = row.strip().split("   ")
        col01 = divide[0]
    
        sys.stdout.write(f"{col01}\t1\n")
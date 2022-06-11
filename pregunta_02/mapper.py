#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
  
    for row in sys.stdin:
        divide = row.split(",")
        col2 = divide[3]
        col3 = divide[4]
    
        sys.stdout.write(f"{col2}\t{col3}\n")

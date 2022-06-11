#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
      
        divide = row.strip().split("   ")
        col00 = divide[0]
        col01 = divide[1]
        col02 = divide[2]
  
    
        sys.stdout.write(f"{col00}\t{col01}\t{col02}\n")
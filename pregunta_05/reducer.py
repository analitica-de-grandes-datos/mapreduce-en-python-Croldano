#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    keyname = None
    total = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
 
        if key == keyname:

            total += val
        else:

            if keyname is not None:
               
                sys.stdout.write("{}\t{}\n".format(keyname, total))

            kayname = key
            total = val

    sys.stdout.write("{}\t{}\n".format(keyname, total))
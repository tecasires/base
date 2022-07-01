from operator import ne
import os

def value_replace(file, old_text, new_text):
    file, old_text, new_text = str(file), str(old_text), str(new_text)    
    # The input file.
    in_file = open(file, "rt")

    # The output file which stores result.
    out_file_name = file + '.out'
    out_file = open(out_file_name, "wt")

    # Iteration for each line in the input file.
    for line in in_file:
        # replacing the string and write to output file.
        out_file.write(line.replace(old_text, new_text))

    # Closing the input and output files.
    in_file.close()
    out_file.close()

    # Delete old file.
    cmd = 'del ' + file
    os.system(cmd)
    
    # Rename modified new file to old file.
    cmd = '\nmove ' + out_file_name + ' ' + file
    os.system(cmd)


# value_replace('casa.txt', 'CASA', 'CASITA')

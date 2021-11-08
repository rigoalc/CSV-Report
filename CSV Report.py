# Rodrigo Alcover
# 7/11/2021
# CIS-216-12292 
# Python Programming


def read_csv():
    
    header = True
    my_list = []
    
    print("Year |  Min |  Max |  Avg")
    print("==== | ==== | ==== | ====")

    with open('MIGRNDRA.csv') as my_file:# Open a file for reading with open(path)
        for line in my_file.readlines():# Use .readlines()
            if header:
                    header = False
                    line = line.strip()
                    if not line:
                        continue
                    values = line.split(',')
                    month = int(values[0])
                    day = int(values[1])
                    year = int(values[2])
                    temp = float(values[3])
                    my_list.append(values)
                    return my_list
                    
                
read_csv()

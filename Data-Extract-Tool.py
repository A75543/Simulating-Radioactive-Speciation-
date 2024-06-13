from prettytable import *
def read_file_and_split(filename):
    words_list = []
    data = []

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            if line.strip():  # strip() removes leading/trailing whitespaces
                # Split the line into words using whitespace as separator
                words = line.split()
                # Extend the list with the words from the current line
                words_list.append(words)
            else:
                # If the line is blank, add line to data 
                data.append(words_list)
                words_list = []   
    return data

def list_to_string(words_list):
    return ' '.join(words_list)

def extrac_data(input_file, output_file,element):
    # Open the input file for reading and output file for writing
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        save_next_lines = False
        saved_lines = set()
        
        # Read each line in the input file
        for line_number, line in enumerate(infile, start=1):
            # Check if the line contains the word "Pu"
            if element in line:
                # If it does, save the line and set flag to save next lines
                if line not in saved_lines:
                    outfile.write(f"Line {line_number}: {line.strip()}\n")
                    saved_lines.add(line)
                    save_next_lines = True
            elif save_next_lines:
                if line.strip():
                    outfile.write(line)
                else:
                    outfile.write('\n')
                    save_next_lines = False

def Table(filename):
    line_num = []

    myTable = PrettyTable(["Line","Reaction Name", "A", "C","log k"]) 
    data = read_file_and_split(filename+".dat")
    #data[chunk][line][word]Cs
    array = []
    block = []
    for i in range(len(data)):
        Title = list_to_string(data[i][0][2:])
        Line = list_to_string(data[i][0][0:2])
        block.append(Line)
        block.append(Title)
        #print(Title, end="\t")
        temp_flag = False
        log_flag = False
        A_C = False
        for line in range(len(data[i])):
            if "-analytic" in data[i][line]:        #find analytic line
                temp_flag = True
                if data[i][line][3] != "00.00000E+0":
                    block.append(data[i][line][1])
                    block.append(data[i][line][3])
                else:
                    block.append("Na")
                    block.append("Na")
            if "log_k" in data[i][line]:            #find log k
                block.append(data[i][line][1])
                temp_flag = True
        if temp_flag == False:
            block.append("NA")
        if log_flag == False:
            block.append("NA")
        array.append(block)
        block = []

    reac_counter = 0
    for i in range(len(array)):
        if "NA" not in array[i][2:4]:
            if array[i][1] and array[i][2] != "00.00000E+0":
                reac_counter = reac_counter + 1
                myTable.add_row([array[i][0], array[i][1], array[i][2],array[i][3],array[i][4]])    #Write Table
            else:
                myTable.add_row([array[i][0], array[i][1], array[i][2],array[i][3],array[i][4]])    #Write Table
    print("There are",reac_counter,"temperature dependent reaction for")
    print(myTable)
    output = input("Enter output file name: ")
    with open(output+'.csv' , 'w', newline='') as f_output:
        f_output.write(myTable.get_csv_string())

#Main
input_file = str(input("Please enter input file name: "))
output_file = str(input("Please enter output file name: "))
element = str(input("Please enter element name: "))
extrac_data(input_file+".dat", output_file+".dat", element)
print("Data Extracted Successfully")
Table(output_file)
import re

#file1 = open("d3_input.txt","r")
#lines = file1.readlines()

test_inputs = ["""................
......67*.......
.........55.....
""", """................
......67*.......
......55.55.....
""", """................
..........67....
........*55.....
........4.......
""", """................
..........67....
........*55.....
................
""", """................
......67*55.....
""", """................
.........67.....
........*.......
.....8888888....
""", """................
......67........
........*.......
........55.......
""", """................
.....67..4......
........*55.....
""", """................
........4.......
........*.......
........4.......
""", """................
......55.67.....
........*.......
..... 4.........
"""]

input_index = 0
for input in test_inputs:
    lines = input.split('\n')
    matrix = []

    solution_1 = []

    for line in lines:
        matrix_row = []
        #line = line.strip('\n')
        for char in line:
            matrix_row.append(char)
        matrix.append(matrix_row)

    #print(matrix[0])

    number_holder = []

    for row_key, row in enumerate(matrix):
        num_constructor = {
            "number": "",
            "start_index":0,
            "end_index":0,
            "row":0,
            "part_check": False
        }
        #print(row)
        for key, char in enumerate(row):
            next_char = key + 1
            if next_char < len(row):
                #print("Key:",key,"Char:",row[key],"Next Char:",row[next_char])
                if re.search(r"\d", row[key]):
                    num_constructor["number"] += row[key]
                    #print(num_constructor["number"])
                if re.search(r"\D", row[next_char]):

                    if(num_constructor["number"] != ""):
                        x = re.compile(num_constructor["number"])
                        #print("Start Index:", re.search(x, ''.join(row)).start())
                        #print("End Index:", re.search(x, ''.join(row)).end())
                        
                        num_constructor["start_index"] = re.search(x, ''.join(row)).start(0)
                        num_constructor["end_index"] = re.search(x, ''.join(row)).end(0)
                        num_constructor["row"] = row_key
                        
                        number_holder.append(num_constructor)
                        
                        num_constructor = {
                            "number": "",
                            "start_index":0,
                            "end_index":0,
                            "row":0,
                            "part_check": False
                        }

    height = len(matrix)
    width = len(matrix[0])

    for item in number_holder:
        item["same"] = {}
        item["same"]["start"] = {True: item["start_index"] - 1, False: 0} [item["start_index"] > 0]
        item["same"]["end"] = {True: item["end_index"] + 1, False: width - 1} [item["end_index"] < width]

        if item["row"] > 0:
            item["above"] = {}
            item["above"]["start"] = {True: item["start_index"] - 1, False: 0} [item["start_index"] > 0]
            item["above"]["end"] = {True: item["end_index"] + 1, False: 0} [item["end_index"] < width]

        if item["row"] < height - 1:
            item["below"] = {}
            item["below"]["start"] = {True: item["start_index"] - 1, False: 0} [item["start_index"] > 0]
            item["below"]["end"] = {True: item["end_index"] + 1, False: 0} [item["end_index"] < width]

    #print(number_holder)


    for item in number_holder:
        if "above" in item:
            for i in range(item["above"]["start"],item["above"]["end"]):
                if(re.search(r"\W", matrix[item["row"] - 1][i]) and not re.search(r"\.", matrix[item["row"] - 1][i])):
                    #print(item, "Above:", matrix[item["row"] - 1][i])
                    item["part_check"] = True
        if "same" in item:
            for i in range(item["same"]["start"],item["same"]["end"]):
                if(re.search(r"\W", matrix[item["row"]][i]) and not re.search(r"\.", matrix[item["row"]][i])):
                    #print(item, "Same:", matrix[item["row"]][i])
                    item["part_check"] = True
        if "below" in item:
            for i in range(item["below"]["start"],item["below"]["end"]):
                if(re.search(r"\W", matrix[item["row"] + 1][i]) and not re.search(r"\.", matrix[item["row"] +1 ][i])):
                    #print(item, "Below:", matrix[item["row"] + 1][i])
                    item["part_check"] = True

    #print(number_holder)

    for item in number_holder:
        if item["part_check"] == True:
            solution_1.append(int(item["number"]))
        #if item["part_check"] == False:
            #print(item)

    print('For input #%s' % input_index)
    print("Part 1:", sum(solution_1))
    input_index += 1

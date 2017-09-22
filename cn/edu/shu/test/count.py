def handler():
    s = list()
    file_index = 1
    with open("bc1") as read_file:
        for index, line in enumerate(read_file):
            if len(line) < 2:
                continue
            result = str(line).strip()
            s.append(result)
            if len(s) == 500:
                with open("177-170" + "_" + str(file_index) + ".txt", 'w') as write_file:
                    write_file.write("".join(s))
                    file_index += 1
                s.clear()


def trip():
    s = list()
    with open("177-170" + "_" + str(1) + "_result.txt", "r") as read_file:
        for index, line in enumerate(read_file):
            if "phone" not in line:
                continue
            result = str(line).split(":")
            s.append(str(result[1]).strip())
    with open("177-170" + "_" + str(1) + "_have_result.txt", "w") as write_file:
        write_file.write("".join(s))


def remove(file_index):
    s = list()
    s_result = list()
    with open("177-170" + "_" + str(file_index) + ".txt", "r") as read_file:
        for index, line in enumerate(read_file):
            lista = line.split(",")
            for item in lista:
                s.append(item)
    with open("177-170" + "_" + str(1) + "_have_result.txt") as read_s_file:
        for index, line in enumerate(read_s_file):
            listb = line.split(",")
            for item in listb:
                s_result.append(item)
    for item in s_result:
        if item in s:
            s.remove(item)
    with open("177-170" + "_" + str(file_index) + "_no_result.txt", "w") as write_file:
        write_file.write(",".join(s))


def total(status):
    strs = ""
    b_list = list()
    with open("177-170_1_result.txt") as read_file:
        with open("1pattern_result.txt", "w") as write_file:
            import re

            pattern = 'phone\s*.{11,16}result\s*' + str(status)
            for line in read_file:
                if len(line) > 2:
                    strs += line.strip()
            a_list = re.findall(pattern, strs)
            for item in a_list:
                b_list.append(item[6:17])
            write_file.write(",".join(b_list))


if __name__ == '__main__':
    trip()
    remove(1)
    # total(7)
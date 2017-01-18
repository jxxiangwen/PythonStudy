if __name__ == '__main__':
    start = 124.1
    end = 180
    count = 0
    with open("/home/jxxiangwen/util/test.p") as read_file:
        for line in read_file:
            result = line.split()
            if len(result) < 5:
                continue
            for item in result:
                if start <= float(item) <= end:
                    count += 1
    print(count)

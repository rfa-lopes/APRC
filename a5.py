import csv


def a5(input_file_path):

    count_tcp = 0
    count_conections = 0

    line1 = {}
    line2 = {}
    tmp = 0

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("[*] File: " + input_file_path)
            else:
                protocol = str(row[7])
                if protocol == "TCP":
                    if tmp == 0:
                        line1 = row
                        tmp = 1
                    else:
                        line2 = row

                        src_addr1 = str(line1[3])
                        dest_addr1 = str(line1[4])
                        src_port1 = int(line1[5])
                        dest_port1 = int(line1[6])
                        flags1 = str(line1[8])

                        src_addr2 = str(line2[3])
                        dest_addr2 = str(line2[4])
                        src_port2 = int(line2[5])
                        dest_port2 = int(line2[6])
                        flags2 = str(line2[8])

                        if (
                            src_addr1 == dest_addr2
                            and dest_addr1 == src_addr2
                            and src_port1 == dest_port2
                            and dest_port1 == src_port2
                        ):
                            count_tcp += 1
                            if (
                                "S" in flags1
                                and "F" in flags1
                                and "A" in flags1
                                and "S" in flags2
                                and "F" in flags2
                                and "A" in flags2
                            ):
                                count_conections += 1
                            tmp = 0
                        else:
                            line1 = row
                            tmp = 1
            line_count += 1
    print(f"[*] Processed {line_count} lines")
    print("\n=========================RESULT===================================")
    print("Conexões TCP (all): " + str(count_tcp))
    print("Conexões TCP (started and finished): " + str(count_conections))
    print("==================================================================")
    print("\n\n")


def main():
    print("\n\n")
    print(
        "[Aggregate the two flows representing the same TCP connection; count the total number of TCP connections "
        + "collected, and the total number of TCP connections that started and finished correctly (the ones where flags show "
        + "that the connection has been opened, used, and finalized by both sides). Explain the several possible technical reasons"
        + " that justify why there are TCP connections that were not started or ended correctly.]\n"
    )
    a5("Enunciado/www.fct.unl.pt.csv")
    a5("Enunciado/bigFlows.csv")


if __name__ == "__main__":
    main()

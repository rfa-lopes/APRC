import csv


def a3(input_file_path):

    ip_addrs = {}

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("[*] File: " + input_file_path)
            else:
                source_address = str(row[3])
                destination_address = str(row[4])
                bytes_ = int(row[10])

                if isExternalAddress(input_file_path, source_address):
                    if source_address not in ip_addrs:
                        # print("[+] New ip addr found: " + source_address)
                        ip_addrs[source_address] = 0
                    ip_addrs[source_address] += bytes_

                if isExternalAddress(input_file_path, destination_address):
                    if destination_address not in ip_addrs:
                        # print("[+] New ip addr found: " + destination_address)
                        ip_addrs[destination_address] = 0
                    ip_addrs[destination_address] += bytes_
            line_count += 1
    print(f"[*] Processed {line_count} lines.")
    print("\n===========================RESULT=================================")
    print(sorted(ip_addrs.items(), key=lambda x: x[1], reverse=True)[0:50])
    print("==================================================================")
    print("\n\n")


def isExternalAddress(file, address):
    if file == "Enunciado/www.fct.unl.pt.csv":
        if address != "193.136.126.43" and address.split(".")[0] != "10":
            return True

    if file == "Enunciado/bigFlows.csv":
        addr_split = address.split(".")
        if addr_split[0] != "172" and (addr_split[1] != "16" or addr_split[1] != "31"):
            return True
    return False


def main():
    print("\n\n")
    print(
        "[Determine the 50 most popular IP addresses external to the domain by number of bytes.]\n"
    )
    a3("Enunciado/www.fct.unl.pt.csv")
    a3("Enunciado/bigFlows.csv")


if __name__ == "__main__":
    main()

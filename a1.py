import csv


def a1(input_file_path):

    protocols_bytes = {}
    protocols_packets = {}

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("[*] File: " + input_file_path)
            else:
                protocol = row[7]
                packets = row[9]
                bytes_ = row[10]

                if protocol not in protocols_bytes or protocol not in protocols_packets:
                    # print("[+] New protocol found: " + str(protocol))
                    protocols_bytes[str(protocol)] = int(0)
                    protocols_packets[str(protocol)] = int(0)

                protocols_bytes[str(protocol)] += int(bytes_)
                protocols_packets[str(protocol)] += int(packets)
            line_count += 1
    print(f"[*] Processed {line_count} lines")
    print("\n========================RESULT====================================")
    print("By Bytes:")
    print(protocols_bytes)
    print("\nBy Packets:")
    print(protocols_packets)
    print("==================================================================")
    print("\n\n")


def main():
    print("\n\n")
    print(
        "[Compute the total number of packets and bytes (in and out) per"
        + " protocol (TCP, UDP, ICMP, …) contained in the flows.]\n"
    )
    a1("Enunciado/www.fct.unl.pt.csv")
    a1("Enunciado/bigFlows.csv")


if __name__ == "__main__":
    main()

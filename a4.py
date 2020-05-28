import csv
import pandas as pd


def a4(input_file_path, port_dic):

    ports_usage_flows = {}
    ports_usage_packets = {}

    def init_or_insert_variables(port, nr_packets):
        if port not in ports_usage_flows or port not in ports_usage_packets:
            # print("[+] New port found: " + source_port)
            ports_usage_flows[port] = 0
            ports_usage_packets[port] = 0

        ports_usage_flows[port] += 1
        ports_usage_packets[port] += nr_packets

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("[*] File: " + input_file_path)
            else:
                source_port = int(row[5])
                destination_port = int(row[6])

                packets = int(row[9])

                init_or_insert_variables(source_port, packets)
                init_or_insert_variables(destination_port, packets)

            line_count += 1
    print(f"[*] Processed {line_count} lines.")

    dataFlows = sort_to_key_value(convertPortNumbers(ports_usage_flows, port_dic))
    dataPackets = sort_to_key_value(convertPortNumbers(ports_usage_packets, port_dic))

    print("\n==========================RESULT==================================")
    print("By Flows:")
    print(pd.DataFrame(dataFlows.items(), columns=["Port", "Flows"]))

    print("\nBy Packets:")
    print(pd.DataFrame(dataPackets.items(), columns=["Port", "Packets"]))
    print("==================================================================")
    print("\n\n")


def sort_to_key_value(data):
    return {
        k: v
        for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)[0:50]
    }


def convertPortNumbers(data, port_dic):
    for i in port_dic.keys():
        value = port_dic[i]
        if value == "":
            value = i
        try:
            port_n = int(i)
            if port_n in data:
                data[value + "(" + str(port_n) + ")"] = data.pop(port_n)
        except ValueError:
            continue
    return data


def getPortNamesFromFile():
    dic = {}
    with open("Utils/service-names-port-numbers.csv", mode="r") as infile:
        reader = csv.reader(infile)
        line = 0
        for rows in reader:
            if line != 0:
                dic[rows[1]] = rows[0]
            line += 1
    return dic


def main():
    print("\n\n")
    print(
        "[What are the top 50 (or less if their variety is smaller) most popular "
        + "applications used by the computers in the domain?]\n"
    )
    # Only for the bigFlows.csv file:
    a4("Enunciado/bigFlows.csv", getPortNamesFromFile())


if __name__ == "__main__":
    main()

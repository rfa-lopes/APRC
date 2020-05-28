import csv
from IPGeolocation import IPGeolocationAPI
from IPGeolocation import GeolocationParams
import matplotlib.pyplot as plt


def b2(input_file_path):

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
                        ip_addrs[source_address] = int(0)
                    ip_addrs[source_address] += bytes_

                if isExternalAddress(input_file_path, destination_address):
                    if destination_address not in ip_addrs:
                        # print("[+] New ip addr found: " + destination_address)
                        ip_addrs[destination_address] = int(0)
                    ip_addrs[destination_address] += bytes_

            line_count += 1

    sorted_list = sorted(ip_addrs.items(), key=lambda x: x[1], reverse=True)[0:50]
    ips_addrs = []
    for ip_bytes in sorted_list:
        ips_addrs.append(ip_bytes[0])
    print(f"[*] Processed {line_count} lines from file: " + input_file_path)
    print("\n==========================RESULT==================================")
    data = getGeoLocation(ips_addrs)
    print(str(data))
    getGraph(data)
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


def getGraph(data):
    keys = data.keys()
    values = data.values()
    plt.bar(keys, values)
    plt.show()


def getGeoLocation(ips_addrs):
    key1 = "2b86ff119e424fb1b83352f12b1344aa"
    key2 = "dad4b6d19dd04b05a5becebc78404901"
    ipgeolocationApi = IPGeolocationAPI(key2)

    ip_geo_location = {}
    i = 0

    for ip in ips_addrs:
        geolocation = ipgeolocationApi.getGeolocation()
        geolocationParams = GeolocationParams()
        geolocationParams.setIPAddress(ip)
        geolocation = ipgeolocationApi.getGeolocation(geolocationParams)
        country_name = geolocation["country_name"]

        if country_name not in ip_geo_location:
            ip_geo_location[country_name] = int(0)

        ip_geo_location[country_name] += int(1)

        print("                               ", end="\r")
        print("[" + str(i) + "]" + country_name, end="\r")
        i += 1

    sorted_list = {
        k: v
        for k, v in sorted(
            ip_geo_location.items(), key=lambda item: item[1], reverse=True
        )
    }
    return sorted_list


def main():
    print("\n\n")
    print(
        "[Option 2: Consider the two files and represent in a 2D chart the"
        + " geographic position of the IP addresses outside the domain computed in a.3.]\n"
    )
    b2("Enunciado/www.fct.unl.pt.csv")
    b2("Enunciado/bigFlows.csv")


if __name__ == "__main__":
    main()

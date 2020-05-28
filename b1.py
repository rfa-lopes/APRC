import csv
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


def b1(input_file_path):

    chart_by_time_in = {}
    chart_by_time_out = {}

    start_time = ""
    counter = 0

    timeFrame = getTimeFrameInSecound(input_file_path)

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        csv_line = 0
        for row in csv_reader:
            if line_count == 0:
                print("[*] File: " + input_file_path)
            else:
                start_time_ = str(row[0])  # time start
                end_time_ = str(row[1])  # time end

                if line_count == 1:
                    start_time = start_time_

                time = getTimeDiffInSecound(start_time, start_time_)
                if time >= timeFrame:
                    counter += 1
                    start_time = start_time_

                source_addr = str(row[3])
                dest_addr = str(row[4])
                bytes_ = int(row[10])

                if counter not in chart_by_time_out or counter not in chart_by_time_in:
                    chart_by_time_out[counter] = 0
                    chart_by_time_in[counter] = 0

                if isExternalAddress(input_file_path, source_addr):
                    chart_by_time_out[counter] += bytes_

                if isExternalAddress(input_file_path, dest_addr):
                    chart_by_time_in[counter] += bytes_

            line_count += 1
    print(f"[*] Processed {line_count} lines from file: " + input_file_path)

    print("\n=========================RESULT===================================")
    print("IN: " + str(chart_by_time_in))
    getGraph(chart_by_time_in)
    print("\nOUT: " + str(chart_by_time_out))
    getGraph(chart_by_time_out)
    print("==================================================================")
    print("\n\n")


def getGraph(data):
    keys = data.keys()
    values = data.values()
    plt.bar(keys, values)
    plt.show()


def getTimeDiffInSecound(start, to):
    # 28/04/2020  15:44:38
    fmt = "%Y-%m-%d %H:%M:%S"
    d1 = datetime.strptime(start, fmt)
    d2 = datetime.strptime(to, fmt)
    diff = d2 - d1
    return int(diff.total_seconds())


def getTimeFrameInSecound(file):
    if file == "Enunciado/www.fct.unl.pt.csv":
        return 60
    if file == "Enunciado/bigFlows.csv":
        return 5


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
        "[Option 1: Provide two charts representing the average bit rate per time unit that "
        + "crossed the interface or the router in and out during the collecting period. The "
        + "resolution of these charts in the horizontal axe (time) should contain at least 60 "
        + "bars, or values. Thus, if the collection period is 1 hour, each bar represents at most "
        + "1 minute. If the collection period is 5 minutes, each bar represents at most 5 seconds.]\n"
    )
    b1("Enunciado/www.fct.unl.pt.csv")
    b1("Enunciado/bigFlows.csv")


if __name__ == "__main__":
    main()

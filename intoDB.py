import csv
import sqlite3
import os


def intoDb(table_name, input_file_path):

    conn = sqlite3.connect("database/database.db")

    c = conn.cursor()

    c.execute(
        f"""CREATE TABLE {table_name} (
		start_date TEXT, 
		end_date TEXT, 
		duration_s REAL, 
		source_addr TEXT, 
		destination_addr TEXT, 
		source_port INTEGER, 
		destination_port INTEGER,
		protocol TEXT,
		flags TEXT,
		packets INTEGER,
		bytes INTEGER)"""
    )
    print(f"\n[+] CREATE TABLE: {table_name}")

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'\n\n\t{row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}  |  {row[4]}  |  {row[5]}  |  {row[6]}  |  {row[7]}  |  {row[8]}  |  {row[9]}  |  {row[10]} \n\n')
                line_count += 1
            else:
                # print(f'\t{row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}  |  {row[4]}  |  {row[5]}  |  {row[6]}  |  {row[7]}  |  {row[8]}  |  {row[9]}  |  {row[10]} ')
                c.execute(
                    f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        row[0],  # time start
                        row[1],  # time end
                        row[2],  # duration (s)
                        row[3],  # source address
                        row[4],  # destination address
                        row[5],  # source port
                        row[6],  # destination port
                        row[7],  # protocol
                        row[8],  # flags
                        row[9],  # packets
                        row[10],  # bytes
                    ),
                )
                line_count += 1
        conn.commit()
        conn.close()
        print(
            f"Processed {line_count} lines from file: "
            + input_file_path
            + "; to: database.db; into table: "
            + table_name
        )


def main():
    os.remove("database/database.db")
    intoDb("fctTable", "Enunciado/www.fct.unl.pt.csv")
    intoDb("bigFlowsTable", "Enunciado/bigFlows.csv")


if __name__ == "__main__":
    main()

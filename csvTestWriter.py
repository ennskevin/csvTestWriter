### first arg is path to csv file to be emulated
### second arg is number of random items (excluding header) to output

import sys
import csv
import string
import random

def main():
    with open(sys.argv[1], newline="") as f:
        reader = csv.reader(f, delimiter=",")
        fields = next(reader)
        numFields = len(fields)
        averages = [0] * numFields

        for _ in range(3):
            row = next(reader)
            for i in range(len(row)):
                averages[i] += len(row[i])

        for i in range(len(fields)):
            averages[i] /= 3

    with open("output.csv", "w", newline="") as out:
        alphabet = string.ascii_letters + string.digits
        writer = csv.writer(out)
        writer.writerow(fields)

        for _ in range(int(sys.argv[2])):
            newRow = []
            for i in range(numFields):
                length = max(1, int(random.gauss(averages[i], 2)))
                newRow.append(''.join(random.choice(alphabet) for _ in range(length)))
            writer.writerow(newRow)

    return


if __name__ == "__main__":
    main()
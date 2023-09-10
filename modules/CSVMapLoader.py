import csv
class MapLoader:
    def load_from_file(self, filename):
        output_array = []
        with open(filename, 'r')as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                output_array.append(tuple(row))
        return output_array
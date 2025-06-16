import csv

input_file = 'sample_report.csv'
output_file = 'anonymized_report.csv'

with open(input_file, mode='r', newline='') as infile, \
        open(output_file, mode='w', newline='') as outfile:

    reader = csv.DictReader(infile)

    fieldnames = [field for field in reader.fieldnames if field != 'username']

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:

        row.pop('username', None)
        writer.writerow(row)

print(f"Anonymized file created: {output_file}")

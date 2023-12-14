from pymarc import Record, Field, Subfield, MARCWriter
import glob
import shutil
import os

def parse_line_to_field(line, tag, record):
    # Set the record leader for 'LDR' tag
    if tag == 'LDR':
        record.leader = line[5:].strip()
        return None

    # Process other fields
    try:
        data = line[5:].strip()
    except ValueError:
        print(f"Skipping malformed line: {line}")
        return None

    # Handle control fields (tags < 010)
    if tag < '010':
        return Field(tag=tag, data=data)

    # Handle data fields (tags >= 010)
    data = data.lstrip().split('$')
    indicators = data.pop(0)
    indicators = [indicators[0] if len(indicators) > 0 else ' ', 
                  indicators[1] if len(indicators) > 1 else ' ']

    # Create Subfield instances
    subfields = []
    for subfield in data:
        if subfield:
            code, value = subfield[0], subfield[1:]
            subfields.append(Subfield(code, value))

    return Field(tag=tag, indicators=indicators, subfields=subfields)

def text_to_marc(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'wb') as outfile:
        writer = MARCWriter(outfile)
        record = None

        for line in infile:
            line = line.strip()
            if not line:
                continue

            # Extract tag from the line
            tag = line[1:4]

            if tag == 'LDR':
                if record:
                    writer.write(record)
                record = Record()
                parse_line_to_field(line, tag, record)
                continue

            field = parse_line_to_field(line, tag, record)
            if field is not None and record is not None:
                record.add_field(field)

        if record:
            writer.write(record)

        writer.close()

# Set the input and output folder paths
input_folder = 'input/'
output_folder = 'output_mrc/'
processed_folder = 'processed_text/'

for folder in [output_folder, processed_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

for filename in glob.glob(os.path.join(input_folder, '*.txt')):
    input_file_path = filename
    output_file_path = os.path.join(output_folder, os.path.splitext(os.path.basename(filename))[0] + '.mrc')

    text_to_marc(input_file_path, output_file_path)
    shutil.move(filename, os.path.join(processed_folder, os.path.basename(filename)))

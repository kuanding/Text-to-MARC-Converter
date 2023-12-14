
# Text to MARC Converter

## Introduction
This Python script converts text files containing MARC (Machine-Readable Cataloging) record data into actual MARC files. It's designed to process text files where each line represents a MARC field, handling both control and data fields, and outputs standard `.mrc` files suitable for use in library systems and other MARC-compatible tools.

## Installation
To run this script, you will need Python installed on your machine. Additionally, the script depends on the `pymarc` library for handling MARC records.

### Requirements
- Python (3.6 or higher recommended)
- pymarc library

You can install `pymarc` using pip:

```bash
pip install pymarc
```

## Usage
To use the script, place your text files in the `input/` directory. Run the script, and it will process each file, converting it to a MARC file in the `output_mrc/` directory. Processed text files are then moved to the `processed_text/` directory.

### Running the Script
Navigate to the script's directory and run:

```bash
python text2marc.py
```

## Script Functionality
- **Input Handling**: Reads text files from the `input/` folder.
- **MARC Conversion**: Each line in the input files is expected to represent a MARC field. The script converts these lines into MARC fields, handling both control fields (tags < 010) and data fields (tags >= 010).
- **Output Generation**: Converted MARC records are written to `.mrc` files in the `output_mrc/` folder.
- **File Management**: After processing, text files are moved to the `processed_text/` folder.
- **Error Handling**: The script includes basic error handling, such as skipping malformed lines.

## Notes
- Ensure that the input text files are correctly formatted, with each line representing a MARC field.
- The script is set up to handle common MARC field structures but may need adjustments for specific custom formats.

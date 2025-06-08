# HelloAsso to Brevo CSV Converter

This Python script converts member data exported from HelloAsso into a CSV format compatible with Brevo (formerly Sendinblue).

## Description

The script takes a CSV export from HelloAsso containing member/adherent information and converts it into a format that can be imported into Brevo. It handles the field mapping and generates unique contact IDs for each record.

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download this repository
2. Make sure you have Python 3.x installed
3. Make the script executable (optional):
   ```bash
   chmod +x convert_to_brevo.py
   ```

## Usage

Basic usage:

```bash
python convert_to_brevo.py -i input_file.csv
```

With custom output file:

```bash
python convert_to_brevo.py -i input_file.csv -o output_file.csv
```

Remove expired adherents (adhesion date older than 1 year):

```bash
python convert_to_brevo.py -i input_file.csv --remove-expired
```

### Command Line Arguments

```
usage: convert_to_brevo.py [-h] -i INPUT [-o OUTPUT] [--remove-expired]

Convert HelloAsso CSV to Brevo format

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input HelloAsso CSV file
  -o OUTPUT, --output OUTPUT
                        Output Brevo CSV file (default: output_for_brevo.csv)
  --remove-expired      Remove adherents with adhesion dates older than 1 year
```

## Input Format

The script expects a CSV file exported from HelloAsso with the following fields:

- Email payeur
- Prénom adhérent
- Nom adhérent
- Date de la commande

## Output Format

The script generates a CSV file with the following fields:

- EMAIL
- PRENOM
- NOM
- DATE_ADHESION

## Example

Input file (HelloAsso format):

```csv
Référence commande;Date de la commande;Statut de la commande;Nom adhérent;Prénom adhérent;Email payeur;...
123456;01/01/2023;Validé;Doe;John;john@example.com;...
```

Output file (Brevo format):

```csv
EMAIL,PRENOM,NOM,DATE_ADHESION
john@example.com,John,Doe,01/01/2023
```

## Features

- Converts HelloAsso CSV format to Brevo format
- Removes time component from dates
- Optional filtering of expired adherents (adhesion date older than 1 year)
- Handles UTF-8 encoding
- Strips whitespace from fields

## Error Handling

The script includes basic error handling and will display error messages if:

- The input file cannot be found
- The input file is not in the correct format
- There are permission issues with reading/writing files
- Date parsing fails (in this case, the record is kept)

## License

This project is open source and available under the MIT License.

#!/usr/bin/env python3
import csv
import argparse
import uuid
from datetime import datetime, timedelta

def generate_contact_id():
    """Generate a unique contact ID."""
    return str(uuid.uuid4().int)[:6]

def clean_date(date_str):
    """Remove time component from date string if present."""
    return date_str.split()[0] if ' ' in date_str else date_str

def is_date_older_than_one_year(date_str):
    """Check if the date is more than one year old."""
    try:
        # Parse the date string (format: DD/MM/YYYY)
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        one_year_ago = datetime.now() - timedelta(days=365)
        return date_obj < one_year_ago
    except ValueError:
        # If date parsing fails, keep the record
        return False

def convert_helloasso_to_brevo(input_file, output_file, remove_expired=False):
    """Convert HelloAsso CSV to Brevo format."""
    # Define the field mapping
    field_mapping = {
        'Email payeur': 'EMAIL',
        'Prénom adhérent': 'PRENOM',
        'Nom adhérent': 'NOM',
        'Date de la commande': 'DATE_ADHESION'
    }

    # Read HelloAsso CSV and write Brevo CSV
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        
        # Read HelloAsso data
        reader = csv.DictReader(infile, delimiter=';')
        
        # Create Brevo writer
        brevo_fields = ['EMAIL', 'PRENOM', 'NOM', 'DATE_ADHESION']
        writer = csv.DictWriter(outfile, fieldnames=brevo_fields)
        writer.writeheader()

        # Process each row
        for row in reader:
            # Clean the date
            adhesion_date = clean_date(row['Date de la commande'].strip())
            
            # Skip if date is older than one year and remove_expired is True
            if remove_expired and is_date_older_than_one_year(adhesion_date):
                continue

            # Create new row with Brevo format
            brevo_row = {
                'EMAIL': row['Email payeur'].strip(),
                'PRENOM': row['Prénom adhérent'].strip(),
                'NOM': row['Nom adhérent'].strip(),
                'DATE_ADHESION': adhesion_date
            }
            writer.writerow(brevo_row)

def main():
    parser = argparse.ArgumentParser(description='Convert HelloAsso CSV to Brevo format')
    parser.add_argument('-i', '--input', required=True, help='Input HelloAsso CSV file')
    parser.add_argument('-o', '--output', default='output_for_brevo.csv', help='Output Brevo CSV file (default: output_for_brevo.csv)')
    parser.add_argument('--remove-expired', action='store_true', help='Remove adherents with adhesion dates older than 1 year')
    
    args = parser.parse_args()
    
    try:
        convert_helloasso_to_brevo(args.input, args.output, args.remove_expired)
        print(f"Conversion completed successfully. Output written to {args.output}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

if __name__ == '__main__':
    main() 
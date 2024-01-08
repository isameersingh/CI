# Data Extraction
import PyPDF2
import json
 
def extract_form_data(pdf_path):
    form_data = {}
 
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            try:
                annotations = page['/Annots']
 
                if annotations:
                    for annotation in annotations:
                        field = annotation.get_object()
                        if '/T' in field:
                            field_name = field['/T']
                            field_value = None
 
                            # Check for '/V' directly
                            if '/V' in field:
                                field_value = field['/V']
                            else:
                                # Look for '/V' within the '/MK' (markup) dictionary
                                if '/MK' in field and '/V' in field['/MK']:
                                    field_value = field['/MK']['/V']
 
                            form_data[field_name] = field_value
            except KeyError as error:
                pass
    return form_data
 
def save_to_json(data, json_path):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)
 
# Example usage
pdf_path = r"C:\Users\User\Downloads\SUR_APP1_Commercial2 1.pdf"
form_data = extract_form_data(pdf_path)
print(form_data)
print("Thankyou  ")
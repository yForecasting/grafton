#! /usr/bin/python

# import statements
import pandas as pd
import os 
import json
import ast
from json.decoder import JSONDecodeError

# replace the original data by the anonymised data
def anonymise_text(text, pseudonyms_dict):
    # text is the data to anonymise
    # pseudonyms_dict are dicts of the pseudonyms
    # return the anonymised text
    
    for original_value, replacement_value in pseudonyms_dict.items():
        text = str(text).lower().replace(original_value, replacement_value)
    return text

# check if consent is present
def consent_present(text, consent_list):
    # text is the original data
    # consent_list is a list of users with consent
    # return if consent is present
    
    if any(consent_given.lower() in str(text).lower() for consent_given in consent_list):
        # consent is present
        return True
    else:
        # consent is not present
        return False

# anonymise csv file, xml file
def anonymise_file(pseudonyms_dict, consent_list, flat_file, export_file):
    # pseudonyms_dict is a dict containing original values (key) and their replacement values (value)
    # consent_list is a list retaining only users with consent
    # flat_file is a file containing data to anonymise
    # export_file is a file containing anonymised data at the end
    
    # read original data file
    original_data = open(flat_file, "r", errors="surrogateescape")
    print("Original data read.")
        
    # make export file
    anonymised_data = open(export_file, mode="w", errors="surrogateescape")
    print("Export started.")
    print("Wait for the end of script signature!")
        
    # anonymise data
    for line in original_data:
        if consent_present(line, consent_list if len(consent_list) > 0 else pseudonyms_dict):
            anonymised_line = anonymise_text(line, pseudonyms_dict)
            anonymised_data.write(anonymised_line)
        else:
            anonymised_data.write(line)
                
    # close the files properly
    original_data.close()
    anonymised_data.close()
    
    # grafton complete
    print("Grafton complete.")

# anonymise json file
def anonymise_json_file(pseudonyms_dict, consent_list, flat_file, export_file):
    # pseudonyms_dict is a dict containing original values (key) and their replacement values (value)
    # consent_list is a list retaining only users with consent
    # flat_file is a file containing data to anonymise
    # export_file is a file containing anonymised data at the end
    
    # read original data file
    original_data = open(flat_file, "r", errors="surrogateescape")        
    original_data_loaded = json.load(original_data)
    print("Original data read.")

    # make export file
    anonymised_data = open(export_file, "w", errors="surrogateescape")        
    print("Export started.")
    print("Wait for the end of script signature!")

    # anonymise data
    anonymised_json_data = []
    for line in original_data_loaded:
        if consent_present(line, consent_list if len(consent_list) > 0 else pseudonyms_dict):
            anonymised_line = anonymise_text(line, pseudonyms_dict)                
            anonymised_json_data.append(ast.literal_eval(anonymised_line))
        else:
            anonymised_json_data.append(line)
    json.dump(anonymised_json_data, anonymised_data, indent = 4) 
        
    # close the files properly
    original_data.close()
    anonymised_data.close()
    
    # grafton complete
    print("Grafton complete.")

# fallback when file has invalid format (e.g. JSON extension with csv content)
def anonymise_fallback(pseudonyms_dict, consent_list, flat_file, export_file):
    # pseudonyms_dict is a dict containing original values (key) and their replacement values (value)
    # consent_list is a list retaining only users with consent
    # flat_file is a file containing data to anonymise
    # export_file is a file containing anonymised data at the end
    
    # start grafton fallback
    print("Grafton fallback started.")
    
    # read original data file
    original_data = open(flat_file, "r", errors="surrogateescape")
    print("Grafton fallback - Original data read.")
          
    # make export file
    anonymised_data = open(export_file, "w", errors="surrogateescape")        
    print("Grafton fallback - Export started.")
    print("Grafton fallback - Wait for the end of script signature!")
    
    # anonymise data
    line = original_data.readline()
    while line:
        if consent_present(line, consent_list if len(consent_list) > 0 else pseudonyms_dict):
            anonymised_line = anonymise_text(line, pseudonyms_dict)
            anonymised_data.write(anonymised_line)
        else:
            anonymised_data.write(line)        
        line = original_data.readline()
    
    # close the files properly
    original_data.close()
    anonymised_data.close()
    
    # grafton fallback complete
    print("Grafton fallback complete.")
    
    # grafton complete
    print("Grafton complete.")
    
# handler for opening a file following the extension of that file
def anonymise_file_handler(pseudonyms_dict, consent_list, flat_file, export_file):
    # pseudonyms_dict is a dict containing original values (key) and their replacement values (value)
    # consent_list is a list retaining only users with consent
    # flat_file is a file containing data to anonymise
    # export_file is a file containing anonymised data at the end
    
    # retrieve file extension
    filename, file_extension = os.path.splitext(flat_file)
    
    # csv extension
    if file_extension == ".csv":
        anonymise_file(pseudonyms_dict, consent_list, flat_file, export_file)
        
    # json extension
    elif file_extension == ".json":
        anonymise_json_file(pseudonyms_dict, consent_list, flat_file, export_file)
        
    # xml extension
    elif file_extension == ".xml":
        anonymise_file(pseudonyms_dict, consent_list, flat_file, export_file)
        
    # extension not supported
    else:
        print("Extension not supported.")
        print("Grafton not executed.")
        
# anonymisation process
def anonymise(pseudonyms_file, consent_file, flat_file, export_file, enable_grafton_fallback=True):
    # pseudonyms_file is a file containing original values and their replacement values
    # consent_file is a file retaining only users with consent
    # flat_file is a file containing data to anonymise
    # export_file is a file containing anonymised data at the end
    # enable_grafton_fallback is a bool used to enable grafton fallback
    
    try:

        # read pseudonyms
        pseudonyms = pd.read_csv(pseudonyms_file, sep=";")

        # make dicts of pseudonyms
        pseudonyms_dict = pseudonyms.iloc[:, 0:2].set_index('original').T.to_dict('records')[0]

        # read consent
        consent_list = []
        try:
            consent = pd.read_csv(consent_file, sep=";")
            if not consent.empty:
                consent_list = consent.iloc[:, 0].to_list()  # list to check, with consent
        except Exception as err:
            pass  
        
        # execute anonymisation process
        anonymise_file_handler(pseudonyms_dict, consent_list, flat_file, export_file)
    except IOError:
        # IOError
        print("File not found or path is incorrect.")
    except UnicodeDecodeError as err:
        # UnicodeDecodeError
        print(err)
    except JSONDecodeError as err:
        # JSONDecodeError
        print(f"{flat_file} has invalid format.")
        if enable_grafton_fallback:
            anonymise_fallback(pseudonyms_dict, consent_list, flat_file, export_file)
        else:
            print("Please enable grafton fallback to achieve success.")
            print("Grafton failed due invalid file format.")
    finally:
        print("---- end of script ----")

# main
def main():
    # execute anonymisation process
    anonymise(pseudonyms_file="pseudonyms.csv", consent_file ="consent.csv", flat_file="flatfile.csv", export_file="flatfile_dataexport_consent.csv", enable_grafton_fallback=True)

if __name__ == '__main__':
    # main()
    anonymise(pseudonyms_file="pseudonyms.csv", consent_file ="consent.csv", flat_file="flatfile.csv", export_file="flatfile_dataexport_consent.csv", enable_grafton_fallback=True)

#! /usr/bin/python

import pandas as pd

# replace the original data by the anonymised data
def anonymise_text(text, pseudonyms_dict):
    # text is the data to anonymise
    # pseudonyms_dict are dicts of the pseudonyms
    # return the anonymised text
    
    for original_value, replacement_value in pseudonyms_dict.items():
        text = text.lower().replace(original_value, replacement_value)
    return text

# check if consent is present
def consent_present(text, consent_list):
    # text is the original data
    # consent_list is a list of users with consent
    # return if consent is present
    
    if any(consent_given.lower() in text.lower() for consent_given in consent_list):
        # consent is present
        return True
    else:
        # consent is not present
        return False


# anonymise data of flat file
def ff_anonymise(pseudonyms_file, consent_file, flat_file, export_file, csvsep=";"):
    # pseudonyms_file is a file containing a list of original values and their replacement values
    # consent_file is a file retaining only users with consent
    # flat_file is a file containing data to anonymise
    # export_file is a file containing anonymised data at the end
    # the default csv seperator is ";"
    
    line1 = 0
    line = 0
    
    # anonymisation process
    try:
        
        # read pseudonyms list
        pseudonyms_list = pd.read_csv(pseudonyms_file, sep=csvsep)
        
        # make dicts of pseudonyms
        pseudonyms_dict = pseudonyms_list.iloc[:, 0:2].set_index('original').T.to_dict('records')[0]

        # read consent list
        consent_list = pd.read_csv(consent_file, sep=csvsep)
        consent_list = consent_list.iloc[:, 0].to_list()  # list to check, with consent
        
        # read original data file
        original_data = open(flat_file, "r", errors="surrogateescape")
        print("Original data read.")
        
        # make export file
        anonymised_data = open(export_file, mode="w", errors="surrogateescape")
        print("Export started.")
        print("Wait for the end of script signature!")
        
        # anonymise data
        for line in original_data:
            line1 = line
            if consent_present(line, consent_list):
                anonymised_line = anonymise_text(line, pseudonyms_dict)
                anonymised_data.write(anonymised_line)
                
        # close the files properly
        original_data.close()
        anonymised_data.close()
        
        # end of script
        print("Flat File GDPR Anonymiser complete.")
    except IOError:
        # IOError
        print("File not found or path is incorrect.")
    except UnicodeDecodeError:
        # UnicodeDecodeError
        print("Error at line:")
        print(line1)
        print(line)
        pass
    finally:
        print("---- end of script ----")


def main():
    # execute anonymisation process
    ff_anonymise(pseudonyms_file="pseudonyms.csv", consent_file ="consent.csv", flat_file="flatfile.csv", export_file="flatfile_dataexport_consent.csv")

if __name__ == '__main__':
    main()

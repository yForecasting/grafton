#! /usr/bin/python

import pandas as pd


# import csv

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def find_one(text, lis):
    if any(consent_given.lower() in text.lower() for consent_given in lis):
        return True
    else:
        return False


def ff_anonymise(pseudonyms, consent, flatfile, export, csvsep=";"):
    line1 = 0
    line = 0
    try:
        # read pseudonyms list
        ps = pd.read_csv(pseudonyms, sep=csvsep)
        # make dicts of pseudonyms
        d1 = ps.iloc[:, 0:2].set_index('original').T.to_dict('records')
        d1 = d1[0]
        # read consent list
        cs = pd.read_csv(consent, sep=csvsep)
        cs = cs['consent_given'].to_list()  # list to check, with consent

        # read big flat file
        my_file_handle = open(flatfile, "r", errors="surrogateescape")
        print("File read.")
        # make export file
        new_file = open(export, mode="w", errors="surrogateescape")
        print("export started.")
        print("Wait for end of script signature !")
        # do the replacement string logic
        for line in my_file_handle:
            line1 = line
            if find_one(line, cs):
                li = replace_all(line, d1)
                new_file.write(li)
        # close the files properly
        my_file_handle.close()
        new_file.close()
        # end of script
        print("Flat File GDPR Anonymiser complete.")
    except IOError:
        print("File not found or path is incorrect")
    except UnicodeDecodeError:
        print("Error at line:")
        print(line1)
        print(line)
        pass
    finally:
        print("---- end of script ---- ")


def main():
    ff_anonymise(pseudonyms="pseudonyms.csv", consent="consent.csv", flatfile="flatfile.csv",
                 export="flatfile_dataexport_consent.csv")


if __name__ == '__main__':
    main()

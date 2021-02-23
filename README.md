# Flat File GDPR Anonymiser
Flat File GDPR Anonymiser anonymises flat files with an user customisable list and exports data with informed consent only.

This tool works with any extension, but is initially designed to anonymise the file flatfile.csv:

1. with a list of replacement values pseudonyms.csv
2. retaining only users with consent in a list in consent.csv

The anonymised file (any extension possible again) is then saved to the current directory and named by default flatfile_dataexport_consent.csv.

The script has default names for all the lists and files to anonymise, but these can be altered if needed.

## Installation

1. Install python3.7+
2. Create a virtual env where you want to install:

    ```
    $> python3 -m venv flat_file_gdpr_anonymiser
    ```

3. Activate the environment

    ```
    $> source flat_file_gdpr_anonymiser/bin/activate
    ```

4. Install the package with pip

     ```
    $> pip install flat_file_gdpr_anonymiser
     ```
	 
## Usage example for cli

To anonymise flat files with Flat File GDPR Anonymiser use the function ff_anonymise:

```
ff_anonymise(pseudonyms = "pseudonyms.csv", consent = "consent.csv", flatfile = "flatfile.csv", export = "flatfile_dataexport_consent.csv")
```

Or execute main.py to deploy the code with default variables:

```
main.py
```





<p align="center">
	<img src="https://raw.githubusercontent.com/yForecasting/grafton/main/grafton/grafton_hex.svg" width="150" height="150">	
</p>


# Grafton

<img src="https://img.shields.io/badge/Maintained%20by-Vives%20AI%20Lab-red"> [![Downloads](https://static.pepy.tech/personalized-badge/grafton?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/grafton) <img src="https://img.shields.io/badge/python-v3.7%2B-blue"> <img src="https://img.shields.io/badge/pypi-v0.1.7-blue">


Grafton is a GDPR anonymizer for any file using informed consent, encoding key and randomising numbers

It can anonymize various input files such as CSV, json, XML or other flat files. In line with the GDPR legislation, the mandatory fields have been anonymized, so that any detection of the subjects is prevented. 

The encryption key for this anonymization process is provided in a separate file (CSV) and must be stored securely afterwards. In accordance with the GDPR, data is only retained when informed consent is given. Consent can be provided in a separate CSV file. The tracked numbers can also be randomized within a similar order of magnitude. 

**The use of this package does not guarantee compliance with the GDPR. This package only performs the steps described above.**

This package is developed by the AI team at [VIVES University of Applied Sciences](https://www.vives.be/en/research/centre-expertise-business-management).

---
Grafton works with any extension, but is initially designed to anonymise the file flatfile.csv:

1. with a list of replacement values pseudonyms.csv
2. retaining only users with consent in a list in consent.csv

The anonymised file (any extension possible again) is then saved to the current directory and named by default flatfile_dataexport_consent.csv.

The script has default names for all the lists and files to anonymise, but these can be altered if needed.

## Installation

1. Install python3.7+
2. Create a virtual env where you want to install:

    ```
    $> python3 -m venv grafton
    ```

3. Activate the environment

    ```
    $> source grafton/bin/activate
    ```

4. Install the package with pip

     ```
    $> pip install grafton
     ```
	 


## Contributing

Contribution is welcomed! 

Start by reviewing the [contribution guidelines](CONTRIBUTING.md). After that, take a look at a [good first issue](https://github.com/yForecasting/grafton/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).


## Disclaimer
`grafton` does not save, publish or share with anyone any identifiable user information.  
The use of this package does not guarantee compliance with the GDPR. This package only performs the steps described above. 

## Support

The [AI team](https://www.vives.be/nl/onderzoek/business-management/ai-voor-sales-predictie-een-omgeving-met-beperkte-historische-data) at Vives builds and maintains grafton to make it simple and accessible. A special thanks to Ruben Vanhecke and Filotas Theodosiou for their contribution.






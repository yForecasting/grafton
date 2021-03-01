"""Flat File GDPR Anonymiser can anonymise different input files such as CSV, json, XML, ... It handles the files to read/write as a flat file. In line with the GDPR legislation, the required fields are anonimised, so that any further tracking of the subjects is prevented. The key of this anonimisation process is provided in a separate file (CSV) and should be securely stored afterwards. In line with GDPR, only records with informed consent are retained. The approval of consent can be provided in a separate CSV file. The use of this package does not guarantee GDPR compliance. This package performs only the steps described above"""

from flat_file_gdpr_anonymiser.__main__ import (
  main,
)

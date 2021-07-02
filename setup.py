"""grafton setup"""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Yves R. Sagaert",
    author_email="yves.r.sagaert@pm.me",
    name='grafton',
    license="GNU GPLv3",
    description='grafton anonymises data in any input file using an encoding key and informed consent list.',
    version='v0.1.4',
    long_description='This package grafton can anonymise different input files such as CSV, json, XML, ... It handles the files to read/write as a flat file. In line with the GDPR legislation, the required fields are anonimised, so that any further tracking of the subjects is prevented. The key of this anonimisation process is provided in a separate file (CSV) and should be securely stored afterwards. In line with GDPR, only records with informed consent are retained. The approval of consent can be provided in a separate CSV file. The use of this package does not guarantee GDPR compliance. This package performs only the steps described above.',
    url='https://github.com/yForecasting/grafton',
    packages=setuptools.find_packages(),
    include_package_data=True,
    # entry_points={'gui_scripts': ['anon=grafton.__main__:main']},
    python_requires=">=3.5",
    # Enable install requires when publishing on the normal PyPi
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
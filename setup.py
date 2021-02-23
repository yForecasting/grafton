"""flat_file_gdpr_anonymiser setup"""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Yves R. Sagaert",
    author_email="yves.r.sagaert@pm.me",
    name='flat_file_gdpr_anonymiser',
    license="GNU GPLv3",
    description='Flat File GDPR Anonymiser anonymises flat files with an user customisable csv list.',
    version='v0.1',
    long_description='Flat File GDPR Anonymiser anonymises flat files with an user customisable csv list.',
    url='https://github.com/yForecasting/flat_file_gdpr_anonymiser',
    packages=setuptools.find_packages(),
    include_package_data=True,
    # entry_points={'gui_scripts': ['anon=flat_file_gdpr_anonymiser.__main__:main']},
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
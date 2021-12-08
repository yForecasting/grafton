"""grafton setup"""
from os import path
import setuptools

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
    

setuptools.setup(
    author="Yves R. Sagaert",
    author_email="yves.r.sagaert@gmail.com",
    name='grafton',
    license="GNU GPLv3",
    description='grafton anonymises data in any input file using an encoding key and informed consent list.',
    version='v0.1.8',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yForecasting/grafton',
    packages=setuptools.find_packages(),
    include_package_data=True,
    # entry_points={'gui_scripts': ['anon=grafton.__main__:main']},
    python_requires=">=3.5",
    # Enable install requires when publishing on the normal PyPi
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
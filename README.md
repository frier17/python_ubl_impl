# python_ubl_impl
Python implementation of the OASIS Universal Business Language (version 2.1)

## UNIVERSAL BUSINESS LANGUAGE (UBL) PYTHON IMPLEMENTATION

This project is aimed at producing collections of business documents based on
 the [OASIS UBL 2.2 specification](http://docs.oasis-open.org/ubl/os-UBL-2
 .1/UBL-2.1.html).

 One of the goals of this project is to reduce development time in business
 applications requiring electronic documents as proof of business. The
 ideology adopted for developing this implementation is built off from the
 concept:

 "Every business service consist of activities performed at a cost and
requiring feedback (proof of transaction)."

This project focuses on generating proofs of transactions and not
business services, activities, or other such business components. Developers
can further extend this package to meet such needs or further improve the
existing business documents to meet their requirements.

## Getting Started

The package will be made available through the PiPy repository for packages.

### Prerequisites

This package was built in Python 3.6 and tested on a Linux installation.
Ensure the dependent packages or tools are installed. Prerequisite of this
package includes:
Python 3.6 or later
Pytest test runner
Behave test runner

### Usage

This project was designed to provide the following services for application
developers:

+ Enable developers design and develop business application which are
compliant with the UBL specification
+ Provide a python package or implementation of the UBL specification that
will enable fast and easy integration of the UBL specification
+ Serve as a foundational work in building business application that uses
clearly defined schemas or business objects in communicating between several
processes
+ Provide an efficient means of communicating business, assets, processes and
 services in a widely accepted specification
+ Provide a guideline for database schemas and objects which are derived from
 UBL specification

This project may be used in various python framework or extended to suit
desired python framework. Current implementation provide most of the UBL
specifications as simple Python objects with attributes set to the same name
(using a naming convention) to ease mapping of existing document types to
implemented Python business document object. Implemented business document
objects may be extended using the provided hooks (**\_\_extension\_\_,
\_\_meta\_\_, \_\_registry\_\_, \_\_annotations\_\_, and  \_\_desc\_\_**)

The UBL defined documents and business components (BEIE, ASBIE etc.) have  a
large list of attributes matching to data.
These fields can be configured dynamically or statically from a configuration
 file. This will enable various businesses simply specify their parameters,
 attributes to ignore or hide, compulsory fields etc. and have the
 application create corresponding datatypes using the Python type function (e
 .g:  **type('BSOType', bases, members)** ) to make dynamic classes.

### Installing

Developers will be able to download the package using pip command:
pip install python_ubl_impl


## Tests

All project tests are saved in the tests directory. Behave tests are saved in
 the features
directory while functional tests are in the unittest directory.

Behave tests were written with the python behave framework as the target test
 runner while functional tests were written for pytest framework.

Simply run the various tests from command line using appropriate commands and
 flags. Consult respective test frameworks for further details.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With
This package was built using Python 3.6

## Contributing
Individuals interested in contributing to this project can do. Kindly adhere
to any defined code of conducts or procedure. For more information on
joining the project contact [frier17](https://github.com/frier17)

## Versioning
Version control was done using git version control
For document history, see the [repository](https://github.com/frier17/python_ubl_impl).

## Authors
Initial design work and code base created by:
* **A. Friday** - *Initial work* - [frier17](https://github.com/frier17)

See also the list of [contributors](https://github.com/frier17/python_ubl_impl) who
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE
.md) file for details

## Acknowledgments
This work was made possible from the immense work done by OASIS Technical
Committee on the Universal Business Langauge. Their detail definition of
business document schemas and processes form the foundation upon which this
project was created.


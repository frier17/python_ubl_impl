# UNIVERSAL BUSINESS LANGUAGE (UBL) PYTHON IMPLEMENTATION

This project is aimed at producing collections of business documents based on
 the [OASIS UBL 2.2 specification](http://docs.oasis-open.org/ubl/os-UBL-2
 .1/UBL-2.1.html)
 One of the goals of this project is to reduce development time in business
 applications requiring electronic documents as proof of business. The
 ideology adopted for developing this implementation is built off from the
 concept:
 "Every business service consist of activities performed at a cost and
requiring feedback (proof of transaction)."
This application is focused on generating proofs of transactions and not
business services, activities, or other such business component. Developers
can further extend this package to meet such needs or further improve the
existing proofs of transaction or business document.

## Getting Started

The package will be made available through the PiPy repository for packages.

### Prerequisites

This package was built in Python 3.6 and tested on a Linux installation.
Ensure the dependent packages or tools are installed. Prerequisite of this
package includes:
Python 3.6 or later
Pytest test runner
Behave test runner

### Installing

Developers will be able to download the package using pip command:
pip install python_ubl_impl


## Running the tests

All tests are in the tests directory. Behave tests are saved in the features
directory while functional tests are in the unittest directory.

Behave tests were written with the python behave framework as the target test
 runner while functional tests were written for pytest framework.

Simply run the various tests from command line using appropriate commands and
 flags. Consult respective test frameworks for further details.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing
Individuals interested in contributing to this project can do. Kindly adhere
to any defined code of conducts or procedure. For more information on
joining the project contact [frier17](https://github.com/frier17)

## Versioning
Version control was done using git version control
For document history, see the [repository](https://github.com/your/project/tags).

## Authors

* **Aniefiok Friday** - *Initial work* - [frier17](https://github.com/frier17)

See also the list of [contributors](https://github.com/your/project/) who
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE
.md) file for details

## Acknowledgments
This work was made possible from the immense work done by OASIS Technical
Committee on the Universal Business Langauge. Their detail definition of
business document schemas and processes form the foundation upon which this
project was created.


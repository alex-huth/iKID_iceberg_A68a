# KID/iKID (icebergs)

[![Documentation Status](https://readthedocs.org/projects/kid/badge/?version=latest)](https://kid.readthedocs.io/en/latest/?badge=latest)

This is the source code for Huth et al. (2022) Ocean currents break up a tabular iceberg. It includes the iKID module, the A68 data/model input files, and post-processing scripts.

# What files are what

| File/directory    | Purpose |
| --------------    | ------- |
| src/              | Source code for icebergs |
| driver/           | A driver for creating a stand-alone (uncoupled to ocean/atmosphere) model |
| build/            | A workspace for building a stand alone executable using src/ and driver/ |
| tests/            | Test cases (A68) |
| docs/             | A workspace for generating documentation with doxygen and sphinx |
| postprocessing/   | Post-processing for generating the figures in the paper |

# Installation

The KID/iKID module requires an installation of MOM6. See https://github.com/NOAA-GFDL/MOM6-examples, and wiki therein. After installing MOM6, replace MOM6-examples/src/icebergs with this module. The A68a test relies on the stand-alone driver provided in the current repository. Build instructions are in build/README.

# Disclaimer

The United States Department of Commerce (DOC) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. DOC has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information. Any claims against the Department of Commerce stemming from the use of its GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.

This project code is made available through GitHub but is managed by NOAA-GFDL at https://gitlab.gfdl.noaa.gov.

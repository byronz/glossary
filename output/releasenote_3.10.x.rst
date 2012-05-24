=========================
DALTS 3.10.x Release Note
=========================

.. sidebar:: Summary

    :Version: 3.10.x
    :Library: liblwtsrel.lib
    :DAL API: 6.7.0B1.6
    :Test Kit: 2.6.0
    :TRP: 1.0.3
    :Date: April 11 2012
    :Authors: - Byron Zhu
              - Sam Shen

.. contents::
    :depth: 2

--------
Overview
--------

Welcome to the release 3.10.x!

DALTS 3.10.x provides the first phase test cases (SEC without CERT feature)
support for any potential pilot projects.

The full feature testing will be covered in 3.11.x. (target end of Q2 2012)

Compatibility Matrix
====================

.. csv-table::
  :header-rows: 1

  Modules,API,UTC,Status,Remark
${ModuleMatrix}

----

.. Warning::

    * DAL API - Please rigorously select the version, the latest one might not be the adequate version for your project!
    * DAL Test Suite - Please select the latest version since it generally includes more bug fixes.
    * Integration Test Kit - Every DALTS has a corresponding kit version, please refer to `PI Test Specification Wiki`_

.. _PI Test Specification Wiki:
   http://sharepoint.hq.k.grp/sites/pi/testspec/doc%20%20test%20kits/kits_dalts.aspx

Nagra Products
==============

DALTS provides the full test coverage of API implementations to a dozen of
Nagra CA products. The test variants indicate the module combination and some
basic system requirements from product perspective.

System Requirements
-------------------

.. csv-table::
  :header-rows: 1

  Variants,Tasks,Timers,Semaphores,Filters
${Requirements}

Module Matrix
-------------

.. csv-table::
  :header-rows: 1

${VariantMatrix}

-----

${Products}


DAL API
=======

DALTS is compatiable with the following `DAL API version`_

.. _DAL API version:
    http://ist.hq.k.grp/cgi-bin/WebObjects/ist.woa/wa/inspectRecord?entityName=CAKSoftwareComponent&id=642

${DALAPI}

EMI
===

The supported EMI list categorized by module.

${EMI}

-------
Changes
-------

${Changes}

---------
Bug Fixes
---------

${Bugs}

----------
Validation
----------

This section presents the

Environment
===========

Win32

    * MS Visual Studio 2008
    * OpenSSL *1.0.0e*

Coverage
========

DALTS test strategy is to cover the latest DAL API version as early as possible.
It happens that some of the test cases cannot be validated at release time. The
quality of these cases remains at engineering level. This section lists the full
list of untested cases.

.. warning::

    - SEC-ECC-xxxx

----------------
Testing Material
----------------

Streams
=======

DMX
---
- DaXXXC_Basic_DMX-DSC-ITS-1_XX.XX.ts

PSI
---
- DaXXXC_Basic_PSI-ITS-1_XX.XX.ts
- DaXXXC_Basic_PSI-ITS-2_XX.XX.ts
- DaXXXC_Basic_PSI-ITS-3_XX.XX.ts
- DaXXXC_Basic_PSI-ITS-4_XX.XX.ts
- DaXXXC_Basic_PSI-ITS-5_XX.XX.ts
- DaXXXC_Basic_PSI-ITS-6_XX.XX.ts
- DaXXXC_Basic_PSI-ITS-7_XX.XX.ts
- DaXXXC_Hybrid_PSI-ITS-8_XX.XX.ts
- DaXXXC_Hybrid_PSI-ITS-9_XX.XX.ts
- DaXXXC_Hybrid_PSI-ITS-10_XX.XX.ts

DSC
---
- DaXXXC_Basic_DMX-DSC-ITS-1_XX.XX.ts
- DaXXXA_Basic_DSC-ITS-1_XX.XX.ts
- DaXXX3_Basic_DSC-ITS-2_XX.XX.ts

SCR
---
- DaXXXA_Basic_SCR-ITS-1_XX.XX.ts
- DaXXXA_Basic_SCR-ITS-2_XX.XX.ts
- DaXXXA_Basic_SCR-ITS-3_XX.XX.ts
- DaXXXA_Basic_SCR-ITS-4_XX.XX.ts
- DaXXXT_Basic_SCR-ITS-5_XX.XX.ts
- DaXXXT_Basic_SCR-ITS-6_XX.XX.ts
- DaXXXT_Basic_SCR-ITS-7_XX.XX.ts
- DaXXXT_Basic_SCR-ITS-8_XX.XX.ts
- DaXXXC_Basic_SCR-ITS-9_XX.XX.ts
- DaXXXA_Basic_SCR-ITS-10_XX.XX.ts
- DaXXXA_Basic_SCR-ITS-11_XX.XX.ts

IBT
---
- DaXXXX_PushVOD-DIL-ITS-1_XX.XX.ts
- DaXXXX_PushVOD-DIL-ITS-3_XX.XX.ts

PTL
---
- DaXXXX_PushVOD-DIL-ITS-1_XX.XX.ts

DIS
---
- DaXXXX_PushVOD-DIL-ITS-1_XX.XX.ts
- DaXXXX_PushVOD-DIL-ITS-2_XX.XX.ts

------
Notice
------

Contact
=======

Partners
--------
* For any issue, please directly contact your **project integrator** or **project coordinator** in Nagra

Integrators
-----------

* To request a DALTS library, please submit your request on `C2 Library Request`_
* To get support from customer care, please create a ticket on `C2 Product Support`_
* If a problem is found and confirmed, please submit a **problem request**  on `IST DTE Request`_
* Other problems, please contact dtesen.support@nagra.com / +41 21 732 04 45

.. _C2 Library Request:
   https://c2.hq.k.grp/WebClient/IS/Libraries/CAK_DALTS/IS_CAK_KDA_DALTS_request_CAK_DALTS.asp?product=dalts
.. _C2 Product Support:
   https://c2.hq.k.grp/WebClient/IS/Support/caksupport/Search_CVSProject.asp
.. _IST DTE Request:
   http://ist.hq.k.grp/cgi-bin/WebObjects/ist.woa/wa/menu?activity=Request&entityName=DTE_Request#anchor

-----

.. topic:: Stubs

    Stubs are now removed from the DALTS source code and skillfully integrated
    with the DALAPI and CAKAPI files in Perforce. When CAKAPI link dependences
    exist, stubs will be provided automatically to fit the manufacturer's
    environment.

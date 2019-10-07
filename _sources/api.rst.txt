Developer interface
===================

.. module:: get_vat_eu

Main Interface
--------------

Examples for the most relevant api functions can be viewed in the test
file. get_vat_eu's API uses `type hints`_ instead of assertions to check input and 
output types.

.. _type hints: https://docs.python.org/3/library/typing.html

.. autofunction:: request_vat_information
.. autofunction:: parse_address_string
.. autofunction:: vat_adheres_to_specifications
.. autofunction:: parse_response
.. autofunction:: prettify_trader_information
.. autofunction:: pipeline

Exceptions
----------

.. autoexception:: VIESServiceError
.. autoexception:: ResponseIOError
.. autoexception:: ResponseVatNumberNotConforming
.. autoexception:: CannotGetTraderName
.. autoexception:: CannotGetTraderAddress
.. autoexception:: VatNotValid
.. autoexception:: AddressStringNotCorrespondingToExpectedFormat
.. autoexception:: CountryCodeNotImplemented

Specifications
==============

Introduction
------------

- specific rules are divided by the two letter country code
- variables are specified using the curly braces shell style

Structure
---------

Object returned by the pipeline function
````````````````````````````````````````

``IT``
~~~~~~

::


    {'name': '${name}', 'address': '${full address}', 'city': '${city}', 'province': '${province}', 'post_code': '${post code}', 'vat_number': '${vat number}', 'country_code': 'IT'}


Rules
-----

Address string
``````````````
The SOAP API returns different kind of address strings.

No specification was found in this case. Rules are derived empirically.

``IT``
~~~~~~

::


    '${address} ${house_number} \n${postal_code} ${city} ${PROVINCE}\n'


Postal code
```````````

- https://publications.europa.eu/code/en/en-390105.htm

VAT number
``````````

- https://it.wikipedia.org/wiki/Partita_IVA#Numeri_IVA_nell'Unione_europea

Province
````````

``IT``
~~~~~~

The conventions followed are published as part of the ``ISO 3166-2:IT`` standard:

- https://it.wikipedia.org/wiki/ISO_3166-2:IT#Province

#
# api.py
#
"""The main file."""

from .constants import (common_defaults, urls, countries)
from .exceptions import (CannotGetAnyRelevantInformation, VatNotValid, AddressStringNotCorrespondingToExpectedFormat)


# TODO handle exceptions:
# TODO they get raised like this: zeep.exceptions.Fault: SERVICE_UNAVAILABLE
"""
    - INVALID_INPUT: The provided CountryCode is invalid or the VAT number is empty; 
    - GLOBAL_MAX_CONCURRENT_REQ: Your Request for VAT validation has not been processed; the maximum number of concurrent requests has been reached. Please re-submit your request later or contact TAXUD-VIESWEB@ec.europa.eu for further information": Your request cannot be processed due to high traffic on the web application. Please try again later; 
    - MS_MAX_CONCURRENT_REQ: Your Request for VAT validation has not been processed; the maximum number of concurrent requests for this Member State has been reached. Please re-submit your request later or contact TAXUD-VIESWEB@ec.europa.eu for further information": Your request cannot be processed due to high traffic towards the Member State you are trying to reach. Please try again later. 
    - SERVICE_UNAVAILABLE: an error was encountered either at the network level or the Web application level, try again later; 
    - MS_UNAVAILABLE: The application at the Member State is not replying or not available. Please refer to the Technical Information page to check the status of the requested Member State, try again later; 
    - TIMEOUT: The application did not receive a reply within the allocated time period, try again later. 
"""

def request_vat_information(vat_number: str, country_code: str = countries['code']['default']):
    r"""Make a SOAP request and expect a response."""

    response = None

    return response


def parse_address_string(address_string: str, country_code: str):
    r"""Get relevant information from the address string.


    .. note:: From empirical evidence, an address string is structured like this:
        IT: '${address} ${house_number} \n${postal_code} ${city} ${PROVINCE}\n'
    """

    trader_information = dict()

    if country_code == 'IT':
        if (address_string.endswith(countries['IT']['address string']['separator'])
            and countries['IT']['address string']['separator'] in address_string[0:-1]):

            # Divide the original string in two parts. Ignore the final empty string.
            buf = address_string.split(countries['IT']['address string']['separator'])[:-1]

            # The address part is the first substring. Remove spaces around the string borders.
            address_substring = buf[0].strip(countries['IT']['address string']['delimiter'])
            # Postal code, city, province.
            pc_cty_prv_substring = buf[1]

            # Get the other substring into its various components
            buf = pc_cty_prv_substring.split(countries['IT']['address string']['delimiter'])

            # We know that province and postal code are not composed by delimiters.
            postal_code = buf[0]
            province = buf[-1]
            # A city might contain spaces.
            city = countries['IT']['address string']['delimiter'].join(buf[1:-1])


            # Check that the province is composed of 2 uppercase letter characters.
            # Check that the postal code correponds to the standard.
            # if not: raise
            #


            trader_information['address'] = address_substring
            trader_information['postal code'] = postal_code
            trader_information['province'] = province
            trader_information['city'] = city
        else:
            raise AddressStringNotCorrespondingToExpectedFormat


    return trader_information


def parse_response(response: dict):
    r"""Parses the reponse and get the relevant fields."""
    assert 'countryCode' in response
    assert 'vatNumber' in response
    assert 'requestDate' in response
    assert 'valid' in response
    assert 'traderName' in response
    assert 'traderCompanyType' in response
    assert 'traderAddress' in response
    assert 'traderStreet' in response
    assert 'traderPostcode' in reponse
    assert 'traderCity' in reponse
    assert 'traderNameMatch' in reponse
    assert 'traderCompanyTypeMatch' in reponse
    assert 'traderStreetMatch' in reponse
    assert 'traderPostcodeMatch' in reponse
    assert 'traderCityMatch' in reponse
    assert 'requestIdentifier' in reponse


    trader_information = dict()

    if response['valid']:
        if (response['traderStreet'] is None or response['traderCity'] is None
                or response['traderPostcode'] is None):
            if response['traderAddress'] is None:
                raise CannotGetAnyRelevantInformation
            else:
                trader = parse_address_string(response['traderAddress'])
                trader_information['city'] = trader['city']
                trader_information['province'] = trader['province']
                trader_information['post code'] = trader['post code']
        else:
            trader_information['city'] = response['traderCity']
            trader_information['province'] = response['traderCity']
            trader_information['post code'] = response['traderPostCode']
    else:
        raise VatNotValid

    return trader_information

def dict_to_json(information: dict):

    translated_to_json = None

    return translated_to_json

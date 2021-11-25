from lxml import etree
#import sys

def validate(xml_path: str, xsd_path: str) -> bool:
    try:
        xmlschema_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)
    except etree.XMLSchemaParseError:
        print("XSD schema file is not valid")
        return False

    try:
        xml_doc = etree.parse(xml_path)
    except etree.XMLSyntaxError:
        print("XML file is not valid")
        return False

    result = xmlschema.validate(xml_doc)

    logs = xmlschema.error_log

    for index, error in  enumerate(logs):
        print("ERROR %d FILE %s ON LINE %s: %s" % (index, error.filename, error.line, error.message))

    return result
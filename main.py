from validator import validate
import argparse, os

def validate_file(f: str):
    if not os.path.isfile(f):
        raise argparse.ArgumentTypeError("{0} does not exist or is not file".format(f))
    return f

def validate_path(f: str):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f

def validate_xml_result(xml: str, schema: str):
    if validate(xml, schema):
        print('Valid! :)')
    else:
        print('Not valid! :(')

#parse arguments
ap = argparse.ArgumentParser()

ap.add_argument("-f", "--xmlfile", type=validate_path, metavar='XML_PATH', required=True,
   help="Path to XML file")
ap.add_argument("-s", "--schema", type=validate_file, metavar='SCHEMA_PATH', required=True,
   help="Path to XSD schema file")

args = ap.parse_args()

#valdiate xml files
file_path = args.xmlfile;
if(os.path.isdir(file_path)):
    for filename in os.listdir(file_path):
        if filename.endswith('.xml'):
            fullname = os.path.join(file_path, filename)
            print("FILE: %s" % (filename))
            validate_xml_result(fullname, args.schema)
else:
    validate_xml_result(file_path, args.schema)


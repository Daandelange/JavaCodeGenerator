import os 
from bs4 import BeautifulSoup as bs
from decode.convert_to_readable import DecodeAndDecompress
from parsers.style_parser import StyleParser
import json

# decoded_xml = DecodeAndDecompress.convert("simple_class_diagram.drawio")
decoded_xml = DecodeAndDecompress.convert("diagram_single_class.drawio")

# DecodeAndDecompress.write_xml_file("simple_class_diagram", decoded_xml)
# graph_model = bs(decoded_xml, "lxml")
# root = graph_model.find('root')
# root_children = root.children

# print(len(root_children))

# for x in range(5):
#     print(next(root_children).attrs)


parser_style = StyleParser(decoded_xml)
# parser_style.convert_to_style_tree()
print(json.dumps(parser_style.convert_to_style_tree(), indent=4))
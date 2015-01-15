import xml.etree.ElementTree as ET

tree = ET.parse('configFile.xml')
root = tree.getroot()

zoomFar = root[1].text
print zoomFar

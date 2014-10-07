from lxml import etree as ET
 
 
class ToXML():
    
    def __init__ (self, filename = "devicesandicons.xml"):
    
        self.root = ET.Element('root')
        self.tree = ET.ElementTree(self.root)
        self.filename=filename
        #self.tree.write(self.filename, pretty_print=True, xml_declaration = True)
        
        
    def add(self, pictureFileName, deviceName, pictureWidth, pictureHeight):
        self.device = ET.SubElement(self.root, "device")
        self.deviceName = ET.SubElement(self.device, "deviceName")
        self.deviceName.text = str(deviceName)
        self.pictureFile = ET.SubElement(self.device, "pictureFile")
        self.pictureFile.text = str(pictureFileName)
        self.pictureWidth = ET.SubElement(self.device, "pictureWidth")
        self.pictureWidth.text = str(pictureWidth)
        self.pictureHeight = ET.SubElement(self.device, "pictureHeight")
        self.pictureHeight.text = str(pictureHeight)
      
        #print ET.tostring(self.root, pretty_print=True, xml_declaration = True)
        self.tree.write(self.filename, pretty_print=True, xml_declaration = True)
    

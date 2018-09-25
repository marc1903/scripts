import os
from xml.etree.ElementTree import ElementTree


xml_folder_path = 'C:\\Users\\Marc\\Desktop\\Globo\\darkflow-master\\kiss_model\\kiss_annotation\\'
xml_folder = os.listdir(xml_folder_path)

image_folder_path = 'C:\\Users\\Marc\\Desktop\\Globo\\darkflow-master\\kiss_model\\kiss\\'
image_folder = os.listdir(image_folder_path)

xml_new_path_text = 'kiss_model/kiss/'

count = 1

for image in image_folder:
    print(count)
    count += 1
    
    for xml_file in xml_folder:
        if xml_file[:-4] == image[:-4]:
            #print(xml_file)
            #print(image)
            tree = ElementTree(file = xml_folder_path + xml_file)
            root = tree.getroot()
            
            for child in root:
                if child.tag == 'filename':
                    #print(child.text)
                    child.text = image
                    #print(child.text)
                     
                if child.tag == 'path':
                    #print(child.text)
                    child.text = xml_new_path_text + image
                    #print(child.text)
            tree.write(xml_folder_path + xml_file)
                         
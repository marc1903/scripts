import os



xml_folder_path = 'C:\\Users\\Marc\\Desktop\\Globo\\darkflow-master\\kiss_model\\kiss_annotation\\'
xml_folder = os.listdir(xml_folder_path)

image_folder_path = 'C:\\Users\\Marc\\Desktop\\Globo\\darkflow-master\\kiss_model\\kiss\\'
image_folder = os.listdir(image_folder_path)

count = 1
check = 0
for image in image_folder:
    

    for xml in xml_folder:
        if xml[:-4] == image[:-4]:
            os.rename(image_folder_path + image, image_folder_path + '{:05}'.format(count) + '.jpg')
            os.rename(xml_folder_path + xml, xml_folder_path + '{:05}'.format(count) + '.xml')

            count += 1
       
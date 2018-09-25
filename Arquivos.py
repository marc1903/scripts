import os
import glob
import shutil

#folderXML = os.listdir("/home/davint-1/Desktop/Marc/SUN2012/Annotations")

count = 1

# for folders in folderXML:
#     if(folders != '.DS_Store'):
#         if(folders == "misc"):
#             for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/misc/*.xml'):
#                  for line in open(file):
#                     if line.startswith("door "):
#                         nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                         #shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/doorsSUN")
#                         os.remove(nome)
#                         print(count)
#                         count += 1
#                         break
#         else:
#             folder2 = os.listdir("/home/davint-1/Desktop/Marc/SUN2012/Annotations/" + folders)
#             for folder3 in folder2:
#                 count = 1
#                 path = '/home/davint-1/Desktop/Marc/SUN2012/Annotations/'+ str(folders) + '/' +str(folder3) +'/*.xml'
#                 for file in glob.glob(path):
#                     for line in open(file):
#                         if line.startswith("door "):
#                             nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                             #shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/doorsSUN")
#                             os.remove(nome)
#                             print(count)
#                             count += 1
#                             break



verificador = 0

# for folders in folderXML:
#     if(folders != '.DS_Store'):
#         if(folders == "misc"):
#             for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/misc/*.xml'):
#                 for line in open(file):
#                     verificador = 0
#                     for word in line.split():
#                         if word == 'staircase':
#                             nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                             shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/stairsSUN")
#                             print(count)
#                             count += 1
#                             verificador = 1
#                             break
#                     if(verificador == 1):
#                         break
#         else:
#             folder2 = os.listdir("/home/davint-1/Desktop/Marc/SUN2012/Annotations/" + folders)
#             for folder3 in folder2:
#                 path = '/home/davint-1/Desktop/Marc/SUN2012/Annotations/'+ str(folders) + '/' +str(folder3) +'/*.xml'
#                 for file in glob.glob(path):
#                     verificador = 0
#                     for line in open(file):
#                         for word in line.split():
#                             if word == 'staircase':
#                                 nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                                 shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/stairsSUN")
#                                 print(count)
#                                 count += 1
#                                 verificador = 1
#                                 break
#                         if(verificador == 1):
#                             break

# for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/b/bedroom/*.xml'):
#     verificador = 0
#     for line in open(file):
#         for word in line.split():
#             if (word == 'door'):
#                 verificador = 1
#                 break
#         if(verificador == 1):
#             break
#     if(verificador == 0):
#         nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#         shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/indoorSUN")
#         print(nome)
#         print(count)
#         count += 1

# for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/b/bedroom/*.xml'):
#         for line in open(file):
#             if line.startswith("door "):
#                 nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                 print(nome)
#                 print(count)
#                 count += 1
#                 #shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/doorsSUN")
#                 break


###############  verifica nome de arquivos iguais ##################

#diretorio2 = os.listdir('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Annotation_Doors_Half_Open/')
#diretorio1 = os.listdir('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Half_Open/')

#count = 0
#for arquivo in diretorio1:
#    verificador = 0
#    file1 = arquivo[:-4]
#    for arquivo2 in diretorio2:
#        file2 = arquivo2[:-4]
#        if (file1 == file2):
#            verificador = 1
#
#    if(verificador == 0):
#        count += 1
#        print(file1)
#        print(arquivo)
#        # os.remove('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Half_Open/' + arquivo)
#        shutil.copy('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Half_Open/' + arquivo, "/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_temp/")
#        print(count)




# =============================================================================
#
#                           MODIFICAÇÃO ARQUIVOS XML
#
# =============================================================================

from xml.etree.ElementTree import Element, ElementTree
#from xml.dom import minidom

dirName1 = "C:\\Users\\Marc\\Desktop\\Lab DaVinti\\gvc_dataset_v01\\dataset\\opened_doors\\"
dir1 = os.listdir(dirName1)
dirName2 = "C:\\Users\\Marc\\Desktop\\Lab DaVinti\\temp\\annotations\\opened_doors\\"
dir2 = os.listdir(dirName2)

category = "opened_doors"
for arquivo1 in dir1:
    verificador = 0
    nomeImg = arquivo1[:-4]
    #print(arquivo1)
    #print(nomeImg)
    for arquivo2 in dir2:
        nomeXML = arquivo2[:-4]
        #print(arquivo2)
        #print(nomeXML)
        if nomeImg == nomeXML:
            tree = ElementTree(file = dirName2 + arquivo2)
            root = tree.getroot()

            for child in root:
                print(child.tag)
                if child.tag == "folder":
                    child.text =  category
                elif child.tag == "filename":
                    print(child.text)
                    child.text = nomeImg + ".jpg"
                elif child.tag == "path":
                    child.text =  category + "/" + arquivo1
                elif child.tag == "object":
                    for item in child:
                        print(item.tag)
                        if item.tag == "name":
                            print(item.text)
                            if item.text == "stair":
                                item.text = "ascending_stair"
                            elif item.text == "topViewStair":
                                item.text = "descending_stair"
                            elif item.text == "doubleDoor":
                                item.text = "double_door"
                                print(arquivo2)
                            elif item.text == "halfOpenDoor":
                                item.text = "half_opened_door"
                            elif item.text == "openDoor":
                                item.text = "opened_door"
                            elif item.text == "Doors_Lift":
                                item.text = "elevator_door"

            tree.write(dirName2 + arquivo2)
            break

# =============================================================================
#             root[0].text = category       #folder
#
#             #print(root.getchildren())
#             #tagName = root.find("filename")
#             #print(tagName.tag)
#             #print(tagName.text)
#             #print(tagName.attrib)
#             if root[1].text.endswith(".png"):
#                 #print(root[1].tag)              #filename
#                 #print(root[1].text)
#                 root[1].text = nomeImg + ".jpg"
#                 #print(root[1].text)
#
#             #print(root[2].tag)                  #path
#             #print(root[2].text)
#             root[2].text = category + "/" + arquivo1
#             #print(root[2].text)
#
#
#             #print(root[6][0].text)              #name
#             root[6][0].text = category
#             #print(root[6][0].text)
#
#             tree.write(dirName2 + arquivo2)
#             verificador = 1
#         if verificador == 1:
#             break
# =============================================================================

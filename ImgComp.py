
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


##### COMPARANDO DUAS IMAGENS E DELENTANDO IGUAIS #####


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"    err = 0 (imagens iguais)
    # the two images are
    return err


dir1 = '/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_stairs/Stairs_temp/'
arq1 = os.listdir(dir1)
dir2 = '/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_temp/'
arq2 = os.listdir(dir2)

count = 0
countArq = 0


for img in arq1:
    verificador = 0
    countArq += 1
    print('Stair -> {0} = {1}'.format(countArq, img))

    try:
        imageA = cv2.imread(dir1 + img)
        imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        heightA, widthA = imageA.shape
    except:
        print('Erro no arquivo {}'.format(img))
        #os.remove(dir1 + img)
        verificador = 1

    for img2 in arq2:
        if(verificador):
            break
        try:
            imageB = cv2.imread(dir2 + img2)
            imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            heightB, widthB = imageB.shape
        except:
            print('Erro no arquivo {}'.format(img2))
            #os.remove(dir2 + img2)

        if not(heightA != heightB or widthA != widthB):
            m = mse(imageA,imageB)
            if(m == 0):
                print(m)
                print(img + '-> img1')
                print(img2 + '-> img2')
                count += 1
                print('count iguals = {0}'.format(count))

















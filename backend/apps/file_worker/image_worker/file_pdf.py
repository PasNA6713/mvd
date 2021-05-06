import cv2

import numpy as np
from PIL import Image
from pdf2image import convert_from_path
massive = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '']

import uuid
import os

from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.core.files import File

from apps.file_worker.models import ImgModel, FormatedImgModel

from loguru import logger


def config_detection(app, count_line, min_area, max_area, min_angle,
                     max_angle, min_height, max_height, min_width, max_width):
    if len(app) >= count_line \
            and cv2.contourArea(app) > min_area and cv2.contourArea(app) < max_area \
            and cv2.minAreaRect(app)[1][0] > min_height and cv2.minAreaRect(app)[1][0] < max_height \
            and cv2.minAreaRect(app)[1][1] > min_width and cv2.minAreaRect(app)[1][1] < max_width:
        return True

def detect_rect(model_id):
    file_model = ImgModel.objects.get(pk=model_id)

    pages = convert_from_path(file_model.file.path)
    imglist = []
    check = False
    numerals = False
    main_img = ''
    for page in pages:
        img = np.asarray(page)
        imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thrash = cv2.threshold(imgGry, 240, 255, cv2.CHAIN_APPROX_NONE)
        contours, hierarchy = cv2.findContours(
            thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for ind, contour in enumerate(contours):
            approx = cv2.approxPolyDP(
                contour, 0.027 * cv2.arcLength(contour, True), True)
            if config_detection(app=approx, count_line=4,
                                min_area=350, max_area=1000,
                                min_angle=-80, max_angle=4,
                                min_height=14, max_height=30,
                                min_width=34, max_width=40):
                cv2.drawContours(img, [approx], 0, (252, 254, 0), 2)
                thrash = imgGry[approx[0][0][1]:approx[0][0]
                                [1]+36, approx[0][0][0]:approx[0][0][0]+18]
                if numerals:
                    index = 0
                    x = approx.ravel()[0]
                    y = approx.ravel()[1] - 5

                    for i in range(3):
                        thrash[i] = [255 for x in thrash[i]]
                    for j in range(len(thrash)):
                        thrash[j][-3:] = 255

                    if thrash.sum()>159500:
                        index = ''
                    else:
                        print('№',ind)
                        print(thrash)
                        thrash = thrash.reshape(1,thrash.shape[0],thrash.shape[1],1)
                    cv2.putText(img, '',(x, y), cv2.FONT_HERSHEY_COMPLEX, 1.3, (255, 0, 0))
        imS = cv2.resize(img, (1200, 900))

        img = Image.fromarray(img)
        img = img.convert('RGB')
        if check:
            imglist.append(img)
        else:
            main_img = img
            check = True

    filename = str(uuid.uuid4())+'.pdf'
    main_img.save(filename, save_all=True, append_images=imglist)

    with open(filename, 'rb') as fi:
        formated_model = FormatedImgModel(file=File(fi), parent=file_model)
        formated_model.save()
    os.remove(filename)
    with open(formated_model.file.path, 'rb') as short_report:
        return HttpResponse(FileWrapper(short_report), content_type=f'application/pdf')
    #     cv2.imwrite('output.jpg',img)
    #     cv2.imshow('shapes', imS)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

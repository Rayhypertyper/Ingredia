
from paddleocr import PaddleOCR

import os
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from langdetect import detect
# from logoretriever import brand
from rapidfuzz import fuzz, process 

ocr = PaddleOCR(use_textline_orientation=True, lang='en')

def has_number(text: str) -> bool:
    """Return True if the string contains at least one number."""
    return any(char.isdigit() for char in text)

def extract_text(img, brand):
# img = 'dietcoke.jpg'

    # img = cv2.imread(img)

    results = ocr.predict(img) # The magic

    text = results[0]['rec_texts']

    boo = False
    arr = []
    # print(results)
    # for line in text:
    #     if 'dients:' in line.lower():
    #         boo = True
    #     if boo:
    #         a = line.split(',')
    #         for i in a:
    #             arr.append(i)
    #             print(i)
        # print(line

    # for box in results[0]['rec_polys']:
    #     poly = np.array(box, dtype=np.int32)
    #     cv2.polylines(img, [poly], isClosed=True, color=(0,255,0), thickness=2)
    boxes = []
    for poly, text in zip(results[0]["rec_polys"], results[0]["rec_texts"]):
        poly = np.array(poly, dtype=np.int32)
        rect = cv2.minAreaRect(poly)
        (w,h) = rect[1]
        
        # box = cv2.boxPoints(rect)
        # area = w * h
        boxes.append((min(w,h), text))

        # cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        # cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    boxes = sorted(boxes, key=lambda b:b[0], reverse=True)
    count = 0
    # for area, text in boxes[:3]:
    #     product = boxes[:3][1]
    #     if count == 2:
    #         break
    #     lang = detect(text)
    #     if lang == "fr":
    #         pass
    #     else:
    #         count+=1
    #         print(text)
    print(boxes)
    # product = boxes[:3][1][1]
    # product = product.lower()
    logoz = boxes[:3][0][1]
    for i in boxes[1:]:
        if not has_number(i[1]):
            product = i[1]
            product = product.lower()
            break

    # try:
    #     lang = detect(boxes[:3][1][1])
    # except:
    #     pass
    # print(boxes[:3][1][1], lang)
    # langu = detect(boxes[:3][2][1])
    # langua = detect(boxes[:4][3][1])
    # if lang != 'en':
    #     product = boxes[:3][2][1]
    #     print(boxes[:3][2][1])
    # if lang != 'en' and langu != 'en':
    #     product = boxes[:4][3][1]
    # product = f"{boxes[:3][1][1]} {boxes[:3][2][1]} {boxes[:4][3][1]}"
    logoz = logoz.split()
    brand = brand.split()
    print(f"brand = {brand}")
    for word in logoz:
        match, score, idx = process.extractOne(word, brand, scorer=fuzz.partial_ratio)
        print(f"OCR word: {word} -> Closest match: {match} (score={score})")
    logo = match # This is the brand
    # product = boxes[:3][1][1] # This is the product
    return logo, product
    # logoz = rulles, brand = ruffle brand or wtv

        # if 2 have already been printed fine, then moev on
    # cv2.imwrite("ocr_boxes.jpg", img)
# Retrieves the logo using google cloud
from google.cloud import vision
import cv2
# from PIL import Image
import numpy as np
import time

# cap = cv2.VideoCapture(0)

# last_detection_time = 0
# logos_cache = []
# while True:
#     ret, frame = cap.read()

#     now = time.time()
#     if now - last_detection_time > 1:
#         last_detection_time = now
#         _, buffer = cv2.imencode('.jpg',frame)
#         content = buffer.tobytes()

client = vision.ImageAnnotatorClient()

def detect_logo(image_bytes: bytes):
    # with open("dietcoke.jpg", "rb") as image_file:
    #     content = image_file.read()

    image = vision.Image(content=image_bytes)
    response = client.logo_detection(image=image) # The magic
    logos = response.logo_annotations

    if logos:
        print(("Logos:"))
        logos_cache = logos
        # for logo in logos:
        #     print(logo.description)

        brand = logos[0].description
        return brand
    else:
        brand = None
        logo_cache = []
        

    
    # if logos_cache:
    #     for logo in logos_cache:
    #         vertices = [(v.x, v.y) for v in logo.bounding_poly.vertices]
    #         if len(vertices) == 4:
    #             cv2.polylines(frame, [np.array(vertices, dtype=int)], True, (0, 255, 0), 2)
    #         cv2.putText(frame, logo.description,
    #                     (vertices[0].x, vertices[0].y - 10),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # logos[0] is what we want

    # cv2.imshow("Camera Logo Detection", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break


# cap.release()
# cv2.destroyAllWindows()    
# brand = brand
# print(brand)
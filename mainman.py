import requests
import json
import re, requests
import cv2
from foodscraper import my_dict
# from textretriever import product, logo
# from logoretriever import brand
import textretriever
import logoretriever
base_url = "https://world.openfoodfacts.net"
url = f"{base_url}/cgi/search.pl"

cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     raise RuntimeError("Could not open camera")


def clean_and_split(s: str):
    """Remove periods, strip 'Contains:', and split extra ingredients."""
    if not isinstance(s, str):
        return []

    # Remove periods
    s = s.replace('.', '')

    # If "Contains:" exists, split into main + contains list
    if "Contains:" in s:
        main, contains = s.split("Contains:", 1)
        parts = [main.strip()] + [c.strip() for c in contains.split(',')]
    else:
        parts = [s.strip()]

    # Capitalize only first word for each part
    cleaned = []
    for p in parts:
        if p:
            p = p.strip()
            p = p[0].upper() + p[1:] if len(p) > 1 else p.upper()
            cleaned.append(p)
    return cleaned

while True:
    # ret, frame = cap.read()
    # cv2.imshow("live camera, press space to capture", frame)
    # key = cv2.waitKey(1)

    # if key == 32:
    if True:
        frame = cv2.imread("images/poptarts.png") 
        success, buffer = cv2.imencode(".jpg", frame)

        image_bytes = buffer.tobytes()
        brand = logoretriever.detect_logo(image_bytes)
        logo, product = textretriever.extract_text(frame, brand)
        print(f"logo: {logo}, product: {product}")
        term = f"{logo} {product}"
        params = {
            "search_terms": term,
            "json": 1,
            "page_size": 10,
            "cc": "us",   # Country = United States
            "lc": "en"    # Language = English
        }

        headers = {
            'User-Agent': 'Carscanogen/1.0 (nitrotypefan1@gmail.com)'
        }
        auth = ('off', 'off')

        response = requests.get(url, headers=headers, params=params, auth=auth, timeout=10)
        response.raise_for_status()
        data = response.json()
        # print(data)
        results = data.get('products', [])
        print(f"products: {results[0].get('ingredients_text_en')}")
        ingredients = results[0].get('ingredients_text_en')
        # print(data.get('products', []))
        # barcode = results[0].get('_id')

        # url = f"{base_url}/api/v0/product/{barcode}.json"

        # headers = {
        #     'User-Agent': "Carscanogen/1.0 (nitrotypefan1@gmail.com)"
        # }

        # auth = ('off', 'off')

        # response = requests.get(url, headers=headers, auth=auth, timeout=10)

        # response.raise_for_status()

        # product = response.json()
        # product_data = product.get('product', {})
        # ingredients = product_data.get('ingredients_text_en') # taking stuff from category can manually add things like acrywhatever
        # ingredientso = product_data.get('ingredients_text')
        # score = product_data.get('nutriscore_grade')
        # categories = product_data.get('categories_tags')
        # print(ingredients)
        # print(f"product: {product_data}")
        # print(ingredientso)
        # print(score)
        # print(categories)




        # Step 1: Split into top-level ingredients (respecting parentheses)
        parts = re.split(r',\s*(?![^()]*\))', ingredients)

        final_list = []

        for item in parts:
            item = item.strip()
            if '(' in item and ')' in item:
                # Extract main ingredient and sub-ingredients
                main, inside = re.match(r'^(.*?)\s*\((.*?)\)$', item).groups()
                final_list.extend(clean_and_split(main.strip()))
                # Split sub-ingredients by comma
                subs = [s.strip() for s in inside.split(',')]
                for s in subs:
            # Handle "and/or" inside parentheses too
                    if "and/or" in s:
                        final_list.extend([p.strip() for p in re.split(r"\s*and/or\s*", s)])
                    else:
                        final_list.extend(clean_and_split(s))
            else:
                if "and/or" in item:
                    final_list.extend(clean_and_split([p.strip() for p in re.split(r"\s*and/or\s*", item)]))
                else:
                    final_list.extend(clean_and_split(item))
        final_list = list(set(final_list))
        print(final_list)

        # print(parsed_list)
        # Expected output: ['salt', 'potatoes', 'vegetable oil', 'sunflower oil', 'canola oil', 'corn oil']
        # here we can add acrylics or wtv if it has category of chips or whatever
        boo = True
        for i in final_list:
            i = i.capitalize()
            if i in my_dict:
                print(f"Addative: {i}")
                print(f"Status: {my_dict[i]['status']}")
                if my_dict[i]['type'] != '':    
                    print(f"Type: {my_dict[i]['type']}")
                print(f"Effect: {my_dict[i]['effect']}")
                boo = False
        if boo:
            print('No carcinogenic ingredients found')
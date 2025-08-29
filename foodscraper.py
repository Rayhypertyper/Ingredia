# from playwright.sync_api import sync_playwright
# import re
# from carcinogens import carcinogens, carcinogens1

# web scraped a website to retrieve additives and side effects

# def run(playwright):
#     browser = playwright.chromium.launch()
#     page = browser.new_page()
#     page.goto("https://www.cspi.org/page/chemical-cuisine-food-additive-safety-ratings#ratings")
#     Caution_rows = page.locator('tr[role="row"]:not([data-classname="safe"])')
#     rows_len = Caution_rows.count()
#     my_dict = {}
    
#     pattern = r'^(.*?)\s*\((.*?)\)$'
#     for i in range(rows_len):
#         row = Caution_rows.nth(i)
#         ingredient = row.locator('.cell-content')
#         ingredient = ingredient.all_inner_texts()
#         # row_text = row.inner_text()
#         # problem = row.locator('[data-column-id="cell_3"]').inner_text()
#         # problem = problem.inner_text()
#         if 'Safe' in ingredient[1]:
#             pass
#         else:
#             # for index, text in enumerate(ingredient):
                
#             #     # print(f"Ingredient: {ingredient}")
#             #     if index == 0:
#             #         print(f"Name: {text}")
#             #     elif index == 1:
#             #         print(f"Status: {text}")
#             #     elif index == 2:
#             #         print(f"Type: {text}")
#             #     else:
#             #         print(f"Effect: {text}")
#             match = re.search(pattern, ingredient[0])
            

#             name = ingredient[0]
#             # if name == 'sugar' or name == "salt":
#             #     break
#             status = ingredient[1]
#             type = ''
#             effect = ingredient[3]
#             if match:
#                 name1 = match.group(1)
#                 name2 = match.group(2)
#                 my_dict[name1] = {"status": status, "type": type, "effect": effect}
#                 my_dict[name2] = {"status": status, "type": type, "effect": effect}

            
            
#             my_dict[name] = {"status": status, "type": type, "effect": effect}
#             # print(f"Issue: {problem}")
            
#             # print('----')
#     # print(my_dict)
#     my_dict.update(carcinogens)
#     my_dict.update(carcinogens1)
#     print(my_dict)
#     # for key, value in my_dict:
#     #     print(f"my_dict[{key}] = {{"status": {value['status']}, "type": {value['type']}, "effect": {value['effect']}}}")
#     # return my_dict # This is the grand list

# with sync_playwright() as playwright:
#     my_dict = run(playwright)#

# results of web scrape
my_dict = {'Name': {'status': 'Rating', 'type': '', 'effect': 'Health Concern'}, 'Acesulfame potassium': {'status'
: 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Allulose': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Digestive'}, 'Aloe vera': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Annatto': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Artificial and natural flavoring': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Cancer'}, 'Artificial sweeteners': {'status': 'Caution', 'type': '', 'effect': ''}, 'Aspartame': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Equal, AminoSweet': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Aspartame (Equal, AminoSweet)': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Autolyzed yeast extract': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Azodicarbonamide': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Brazzein': {'status': 'Caution', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Brominated vegetable oil': {'status': 'Avoid', 'type': '', 'effect': 'Neurological & Behavioral'}, 'bvo': {'status': 'Avoid', 'type': '', 'effect': 'Neurological & Behavioral'}, 'Brominated vegetable oil (bvo)': {'status': 'Avoid', 'type': '', 'effect': 'Neurological & Behavioral'}, 'Butylated hydroxyanisole': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'bha': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Butylated hydroxyanisole (bha)': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Butylated hydroxytoluene': {'status': 
'Caution', 'type': '', 'effect': 'Cancer'}, 'bht': {'status': 'Caution', 'type': '', 'effect': 'Cancer'}, 'Butylated hydroxytoluene (bht)': {'status': 'Caution', 'type': '', 'effect': 'Cancer'}, 'Caffeine': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Neurological & Behavioral'}, 'Cannabidiol (CBD)\xa0': {'status': 'Caution', 'type': '', 'effect': ''}, 'Caramel coloring': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Carboxymethyl cellulose (cmc, cellulose gum), sodium carboxymethyl cellulose': {'status': 'Caution', 'type': '', 'effect': 'Digestive'}, 'Carmine': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'cochineal': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Carmine (cochineal)': {'status': 
'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Carrageenan': {'status': 'Caution', 'type': '', 'effect': 'Cancer'}, 'Casein': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'sodium caseinate': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Casein (sodium caseinate)': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Corn Syrup': {'status': 'Cut Back', 'type': '', 'effect': 'Obesity'}, 'Cyclamate': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Dextrose': {'status': 'Cut Back', 'type': '', 'effect': 'Obesity'}, 'Diacetyl': {'status': 'Caution', 'type': '', 'effect': 'Respiratory'}, 'Fructose': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'Ginkgo biloba': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Guarana': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Neurological & Behavioral'}, 'Gums: arabic, furcelleran, gellan, ghatti, guar, karaya, locust bean, tragacanth, xanthan': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'High-fructose corn syrup': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'High-maltose corn syrup': {'status': 'Cut Back', 
'type': '', 'effect': ''}, 'HSH': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'hydrogenatated starch hydrolysate': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'HSH (hydrogenatated starch hydrolysate)': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'HVP': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'hydrolyzed vegetable protein': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'HVP (hydrolyzed vegetable protein)': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Invert sugar': {'status': 'Cut Back', 'type': '', 'effect': 'Obesity'}, 'Isomalt': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Lactitol': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Lactose': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Maltitol': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 
'Mannitol': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Monatin': {'status': 'Caution', 
'type': '', 'effect': ''}, 'Monk fruit extract': {'status': 'Caution', 'type': '', 'effect': ''}, 'MSG': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'monosodium glutamate': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'MSG (monosodium glutamate)': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Mycoprotein - Quorn': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Olestra': {'status': 'Avoid', 'type': '', 'effect': 'Digestive'}, 'olean': {'status': 'Avoid', 'type': '', 'effect': 'Digestive'}, 'Olestra (olean)': {'status': 'Avoid', 'type': '', 'effect': 'Digestive'}, 'Phosphoric acid; phosphates': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'Polydextrose': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Polysorbate 60, 65, and 80': {'status': 'Caution', 'type': '', 'effect': 'Digestive'}, 'Potassium bromate': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Potassium chloride': {'status': 'Certain People Should Avoid', 'type': '', 'effect': ''}, 'potassium salt': {'status': 'Certain People Should Avoid', 'type': '', 'effect': ''}, 'Potassium chloride (potassium salt)': {'status': 'Certain People Should Avoid', 'type': '', 'effect': ''}, 'Potassium iodate': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Propylene glycol': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Propyl gallate': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Quinine': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Saccharin': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Salatrim': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Salt': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'Sea salt': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'Sodium benzoate': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'benzoic acid': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Sodium benzoate (benzoic acid)': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Sodium nitrate (nitrite)\xa0': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Sorbitol': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Sucralose': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Splenda': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Sucralose (Splenda)': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Sugar': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'sucrose': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'Sugar (sucrose)': {'status': 'Cut Back', 'type': '', 'effect': 'Cardiovascular'}, 'Sulfites': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'sulfur dioxide, sodium bisulfite': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Sulfites (sulfur dioxide, sodium bisulfite)': {'status': 'Certain People Should Avoid', 'type': '', 'effect': 'Allergies & Sensitivities'}, 'Synthetic food dyes': {'status': 'Avoid', 'type': '', 'effect': 'Neurological & Behavioral'}, 'Tagatose': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'TBHQ': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'tert-butylhydroquinone': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'TBHQ (tert-butylhydroquinone)': {'status': 'Avoid', 'type': '', 'effect': 'Cancer'}, 'Titanium dioxide': {'status': 'Avoid', 'type': '', 'effect': 'DNA damage'}, 'Trans fat': {'status': 'Avoid', 'type': '', 'effect': 'Cardiovascular'}, 'partially hydrogenated vegetable oil': {'status': 'Avoid', 'type': '', 'effect': 'Cardiovascular'}, 'Trans fat (partially hydrogenated vegetable oil)': {'status': 'Avoid', 'type': '', 'effect': 'Cardiovascular'}, 'Transglutaminase': {'status': 'Caution', 'type': '', 'effect': 'Food-borne Illness'}, '"meat glue"': {'status': 'Caution', 'type': '', 'effect': 'Food-borne Illness'}, 'Transglutaminase ("meat glue")': {'status': 'Caution', 'type': '', 'effect': 'Food-borne Illness'}, 'Xylitol': {'status': 'Cut Back', 'type': '', 'effect': 'Digestive'}, 'Acetaldehyde': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Acrylamide': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Aflatoxins': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Alcoholic beverages': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Areca nut': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Arecoline': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Benzene': 
{'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Betel quid': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Bracken fern': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Caffeic acid': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Captafol': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Chlorothalonil': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Clonorchis sinensis': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Coffee': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'DDT': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Deltamethrin': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Diazinon': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Ethyl carbamate': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Furan': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Ginkgo biloba extract': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Glyphosate': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Heterocyclic aromatic amines': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Kava extract': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Lead': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Malathion': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Mate': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Methyl eugenol': {'status': 
'Caution', 'type': '2B', 'effect': 'cancer'}, 'Nitrate': {'status': 'Cut Back', 'type': '2A', 'effect': 
'cancer'}, 'Nitrite': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Ochratoxin A': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Opisthorchis viverrini': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Pickled vegetables': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 
'Polycyclic aromatic hydrocarbons': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Processed meat': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Pyrrolizidine alkaloids': {'status': 'Caution', 'type': '2B', 'effect': 'cancer'}, 'Red meat': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Salted fish': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Smokeless tobacco': {'status': 'Avoid', 'type': '1', 'effect': 'cancer'}, 'Very hot beverages': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Aristolochic Acids': {'status': 'Avoid', 'effect': 'cancer'}, 'Arsenic': {'status': 'Avoid', 'effect': 'cancer'}, 'Cadmium': {'status': 'Avoid', 'effect': 'cancer'}, 'Diethylstilbestrol': {'status': 'Avoid', 'effect': 'cancer'}, 'Nitrate or nitrite': {'status': 'Cut Back', 'type': '2A', 'effect': 'cancer'}, 'Riddelliine': {'status': 'Caution', 'effect': 'cancer'}, 'Safrole': {'status': 'Caution', 'effect': 'cancer'}, 'Styrene': {'status': 'Caution', 'effect': 'cancer'},
"Citrus Red 2": {
        "status": "Avoid",
        "type": "",
        "effect": "Possible carcinogen; used to color orange peels but linked to bladder and liver tumors in animal studies"
    },
    "Orange B": {
        "status": "Avoid",
        "type": "",
        "effect": "Linked to intestinal tumors in animal studies; very limited safe use but potential carcinogen"
    },
    "Green 3": {
        "status": "Caution",
        "type": "",
        "effect": "Possible link to bladder tumors in animals; not strongly studied in humans but unnecessary synthetic dye"
    },
    "Red 40": {
        "status": "Cut Back",
        "type": "",
        "effect": "Associated with hyperactivity/attention issues in children; may contain contaminants with carcinogenic potential"
    },
    "Yellow 5": {
        "status": "Avoid",
        "type": "",
        "effect": "Contains carcinogens. Can also trigger allergic-type reactions (hives, asthma) especially in sensitive individuals; linked to hyperactivity"
    },
    "Yellow 6": {
        "status": "Caution",
        "type": "",
        "effect": "Contains carcinogens. Possible links to adrenal tumors in animal studies; associated with hyperactivity and allergic reactions"
    },
    "Blue 1": {
        "status": "Caution",
        "type": "",
        "effect": "Generally considered low-toxicity, but linked to allergic reactions and behavioral concerns in children"
    },
    "Blue 2": {
        "status": "Avoid",
        "type": "",
        "effect": "Animal studies show brain tumors at high doses; linked to behavioral concerns in children"
    },
    "Red 3": {
        "status": "Avoid",
        "type": "",
        "effect": "Recognized carcinogen in animals (thyroid tumors); FDA already banned it in cosmetics, now moving to food"
    }}


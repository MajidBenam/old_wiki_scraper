import requests
from bs4 import BeautifulSoup as soup
import re
import json
from urllib.parse import unquote
from googletrans import Translator
from main_scraper import * 

def get_madrid_coords():
    url = "https://www.google.com/maps/place/madrid/"
    resp=requests.request(method="GET",url=url)

    soup_parser = soup(resp.text, "html.parser")

    html_content = soup_parser.html

    #_script = html_content.find_all("script")[7]

    #matches=re.findall("(-\d+\.\d{7})",_script.text)
    #print(matches[0],matches[1])
    print(html_content)

from selenium import webdriver
import geckodriver_autoinstaller

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

import time

geckodriver_autoinstaller.install()

def get_sth():
    my_list = ['Firuzkuh', 'Bactra', 'Balkh', 'Pendjikent', 'Sakala', 'Balkh', 'Gandhara', 'Takshasila-Sirkap', 'Takshasila-Sirsukh', 'Purushapura', "Chang'an", 'Luoyang', 'Luoyang', 'Changan', 'Jiang', 'Huining', 'Zhongdu', 'Kaifeng', 'Caizhou', 'Kaifeng', 'Shengle', 'Pingcheng', 'Luoyang', 'Daxingcheng', 'Luoyang', "Chang'an", "Chang'an", 'Luoyang', "Chang 'an", 'Hao', 'Zhongzhou', 'Dadu', 'Shangdu', 'Cairo', 'Memphis', 'Mendes', 'Cairo', 'Cairo', 'Cairo', 'Memphis', 'Per-Ramesse', 'Thebes', 'Alexandria', 'Alexandria', 'Memphis', 'Memphis', 'Al-Qatai', 'Fustat', 'Aksum', 'Aachen', 'Aix la Chapelle', 'Aix La Chapelle', 'Paris', 'Paris', 'Paris', 'Paris', 'Paris', 'Badami', 'Manyakheta', 'Kalyana', 'Delhi', 'Devagiri', 'Agra', 'Ujjain', 'Pataliputra', 'Pataliputra', 'Malkhed', 'Pratisthana', 'Benakataka', 'Vidisha', 'Pataliputra', 'Padmapura', 'Vijayanagara', 'Penukonda', 'Chandraigiri', 'Kufa', 'Baghdad', 'Al-Raqqah', 'Samarra', 'Baghdad', 'Merv', 'Baghdad', 'Ashur', 'Kalhu', 'Due-Sharrukin', 'Ninevah', 'Pasargadae', 'Susa', 'Amed', 'Tabriz', 'Baghdad', 'Shiraz', 'Isfahan', 'Maragha', 'Tabriz', 'Sultaniya', 'Nisa', 'Hekatompylos', 'Rhagae', 'Ectatana', 'Ctesiphon', 'Nisa', 'Hekatompylos', 'Rhagae', 'Ectatana', 'Ctesiphon', 'Tabriz', 'Qazvin', 'Isfahan', 'Ctesiphon', 'Dastagird', 'Ecbatana', 'Ctesiphon', 'Seleucid-on-the-Tigris', 'Merv', 'Rayy', 'Isfahan', 'Baghdad', 'Hamadan', 'Ravenna', 'Rome', 'Rome', 'Rome', 'Rome', 'Mediolanum', 'Ravenna', 'Rome', 'Rome', 'Kyoto', 'Asuka', 'Naniwa', 'Asuka', 'Fujiwara', 'Kyoto', 'Kyoto', 'Nara', 'Kyoto', 'Samarkand', 'Kashgar', 'Bukhara', 'Balasagun', 'Suyab', "Ch'ien-Ch'Ã¼an", 'Mahidharapura', 'Yasodharapura', 'Kulen Hills', 'Hariharalaya', 'Yasodharapura', 'Koh Ker', 'Yasodharapura', 'Angkor', 'Isanapura', 'Sambhupura', 'Vyadhapura/Angkor Borei', 'Vyadhapura/Angkor Borei', 'Temu', 'Nafuna', 'Naravaranagara', 'Niani', 'Gao', 'none', 'Boro Khoton', 'Central Capital', 'Liao-yang', "Ta-T'ung", 'Beijing', 'Karakorum', 'Khanbaliq', 'Mumocheng', 'Ordu Balik', 'none', 'Taxila (Sirkap)', 'Bania', 'Mansura', 'Thatta', 'Muhammed Tur', 'Thatta', 'Thatta', 'Napata', 'Memphis', 'Napata', 'Meroe', 'Damascus', 'Harran', 'Mahdia', 'Al-Mansuriya', 'Cairo', 'Constantinople', 'Constantinople', 'Constantinople', 'Constantinople', 'Hattusa', 'Hattusa', 'Sardis', 'Lysimacheia', 'Adrianople', 'Constantinople', 'Edirne', 'Istanbul', 'Gordion', 'Nicomedia', 'Constantinople', 'Konya', 'Bukhara', 'Samarkand', 'Herat', 'Zarfar', 'Zarfar', 'Zabid', 'Sanaa', 'Dhu Jibla']
    #PATH = "/home/majid/dev/selenium/"

    # /home/majid/.mozilla/firefox/qtgamvz4.default-release
    profile = webdriver.FirefoxProfile(
        '/home/majid/.mozilla/firefox/qtgamvz4.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('intl.accept_languages', 'en-US, en')

    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired)
    
    potential_lat_on_info = {}
    my_file_name = "Long_lat.json"
    for item in my_list:
        if item not in potential_lat_on_info.keys():
            driver.get(f"https://www.google.com/maps/place/{item}")
            time.sleep(8)
            print(driver.current_url)
            potential_lat_on_info[item] = driver.current_url
    
            with open(my_file_name, "w") as outfile:
                json.dump(potential_lat_on_info, outfile)



def search_sth():
    my_list = ['Firuzkuh', 'Bactra', 'Balkh', 'Pendjikent', 'Sakala', 'Gandhara', 'Takshasila-Sirkap', 'Takshasila-Sirsukh', 'Purushapura', "Chang'an", 'Luoyang', 'Changan', 'Jiang', 'Huining', 'Zhongdu', 'Kaifeng', 'Caizhou', 'Shengle', 'Pingcheng', 'Daxingcheng', "Chang 'an", 'Hao', 'Zhongzhou', 'Dadu', 'Shangdu', 'Cairo', 'Memphis', 'Mendes', 'Per-Ramesse', 'Thebes', 'Alexandria', 'Al-Qatai', 'Fustat', 'Aksum', 'Aachen', 'Aix la Chapelle', 'Aix La Chapelle', 'Paris', 'Badami', 'Manyakheta', 'Kalyana', 'Delhi', 'Devagiri', 'Agra', 'Ujjain', 'Pataliputra', 'Malkhed', 'Pratisthana', 'Benakataka', 'Vidisha', 'Padmapura', 'Vijayanagara', 'Penukonda', 'Chandraigiri', 'Kufa', 'Baghdad', 'Al-Raqqah', 'Samarra', 'Merv', 'Ashur', 'Kalhu', 'Due-Sharrukin', 'Ninevah', 'Pasargadae', 'Susa', 'Amed', 'Tabriz', 'Shiraz', 'Isfahan', 'Maragha', 'Sultaniya', 'Nisa', 'Hekatompylos', 'Rhagae', 'Ectatana', 'Ctesiphon', 'Qazvin', 'Dastagird', 'Ecbatana', 'Seleucid-on-the-Tigris', 'Rayy', 'Hamadan', 'Ravenna', 'Rome', 'Mediolanum', 'Kyoto', 'Asuka', 'Naniwa', 'Fujiwara', 'Nara', 'Samarkand', 'Kashgar', 'Bukhara', 'Balasagun', 'Suyab', "Ch'ien-Ch'Ã¼an", 'Mahidharapura', 'Yasodharapura', 'Kulen Hills', 'Hariharalaya', 'Koh Ker', 'Angkor', 'Isanapura', 'Sambhupura', 'Vyadhapura/Angkor Borei', 'Temu', 'Nafuna', 'Naravaranagara', 'Niani', 'Gao', 'none', 'Boro Khoton', 'Central Capital', 'Liao-yang', "Ta-T'ung", 'Beijing', 'Karakorum', 'Khanbaliq', 'Mumocheng', 'Ordu Balik', 'Taxila (Sirkap)', 'Bania', 'Mansura', 'Thatta', 'Muhammed Tur', 'Napata', 'Meroe', 'Damascus', 'Harran', 'Mahdia', 'Al-Mansuriya', 'Constantinople', 'Hattusa', 'Sardis', 'Lysimacheia', 'Adrianople', 'Edirne', 'Istanbul', 'Gordion', 'Nicomedia', 'Konya', 'Herat', 'Zarfar', 'Zabid', 'Sanaa', 'Dhu Jibla']

    second_list = ['Herat', 'Kabul', 'Peshwar', 'Firuzkuh', 'Bactra', 'Balkh', 'Pendjikent', 'Sakala', 'Takshasila-Sirsukh', 'Takshasila-Sirkap', 'Purushapura', 'Chien-shih', 'Luoyang', "Chang'an", 'Changan', 'Huanbei', 'Zhengzhou', 'Erlitou', 'Nanjing', 'suspected unknown', 'Xianyang', 'Jiang', 'Taosi', 'Huining', 'Zhongdu', 'Kaifeng', 'Caizhou', 'Beijing', 'Pingcheng', 'Shengle', 'Shang', 'Yin', 'Daxingcheng', 'Daliang', "Chang 'an", 'Zhongzhou', 'Hao', 'absent', 'Dadu', 'Shangdu', 'Ciudad Perdida', 'Pocigueica', 'Bonda', 'Pueblito', 'Taironaca', 'Quito', 'none', 'Cairo', 'Memphis', 'Mendes', 'Itjtawyamenemhat', 'Thebes', 'This', 'Naqada', 'Hierakonpolis', 'Abydos', 'Per-Ramesse', 'Alexandria', 'Avaris', 'Tell el Daba', 'Fustat', 'Al-Qatai', 'Madrid', 'Valladolid', 'Toloas', 'Paris', 'Versailles', 'Aachen', 'Aix la Chapelle', 'Aix La Chapelle', 'Unknown', 'Mont Lassois', 'Heuneburg', 'London', 'Kumase', 'Kumasi', 'Khandax', 'Knossos', 'Kona District', 'Kuching', 'Kediri', 'Trowulan', 'Kota Gede', 'Plered', 'Karta', 'Kartosuro', 'Poh Pitu', 'Tamwlang', 'Mataram', 'Mamrati', 'Watu Galuh', 'Wwatan', 'Hazor', 'Jerusalem', 'Shechem', 'Tirzah', 'Samaria', 'Badami', 'Kalyana', 'Manyakheta', 'Delhi', 'Devagiri', 'Agra', 'Tura', 'Pataliputra', 'Ujjain', 'Sosavur', 'Dvarasamudram', 'Kannanur', 'Banavasi', 'Uchchangi', 'Halsi', 'Triparvata', 'Shahjahanabad', 'Fatehpur Sikri', 'Lahore', 'Malkhed', 'Pratisthana', 'Benakataka', 'Vidisha', 'Padmapura', 'Vijayanagara', 'Chandraigiri', 'Penukonda', 'Merv', 'Kufa', 'Baghdad', 'Al-Raqqah', 'Samarra', 'Agade', 'Babylon', 'Kar-Marduk', 'Ninevah', 'Kalhu', 'Due-Sharrukin', 'Ashur', 'Ur', 'Pasargadae', 'Susa', 'Tabriz', 'Amed', 'Awan', 'Shiraz', 'Isfahan', 'unknown', 'Sultaniya', 'Maragha', 'Choga Mish', 'Al Untash Napirisha', 'Anshan', 'Hidalu', 'Madaktu', 'Ectatana', 'Ctesiphon', 'Nisa', 'Hekatompylos', 'Rhagae', 'Tehran', 'Qazvin', 'Dastagird', 'Ecbatana', 'Seleucid-on-the-Tigris', 'Rayy', 'Hamadan', 'Ravenna', 'Rome', 'Avignon', 'Mediolanum', 'Kyoto', 'Fujiwara', 'Asuka', 'Naniwa', 'inferred absent', 'Miwa', 'Kawachi', 'Karako', 'Ikegami-Sone', 'Samarkand', 'Kashgar', 'Bukhara', 'Balasagun', 'Suyab', "Ch'ien-Ch'üan", 'Mahidharapura', 'Yasodharapura', 'Koh Ker', 'Kulen Hills', 'Hariharalaya', 'Angkor', 'Srei Santhor', 'Phnom Penh', 'Lovek', 'Isanapura', 'Sambhupura', 'Vyadhapura/Angkor Borei', 'Temu', 'Nafuna', 'Naravaranagara', 'Sidon', 'Tyre', 'Marrakesh', 'Kaarta', 'Niani', 'Segou', 'Gao', 'Karakorum', 'Khanbaliq', 'Mumocheng', 'Ordu Balik', 'Kumbi Saleh', 'Monte Albán', 'San José Mogote', 'Bergen', 'Cuzco', 'Choquepukio', 'Wimpillay', 'Wari', 'Port Moresby', 'not applicable', 'Taxila (Sirkap)', 'Bania', 'Mansura', 'Thatta', 'Muhammed Tur', 'Yakutsk', 'Napata', 'Meroe', 'Harran', 'Damascus', 'Ayutthaya', 'Rattanakosin', 'Sarazm', 'Mahdia', 'Al-Mansuriya', 'Hattusa', 'Kanish', 'Constantinople', 'Mazaca-Eusebeia', 'Mazaca', 'Sardis', 'Lysimacheia', 'Sogut', 'Bursa', 'Adrianople', 'Karajahisar', 'Erdine', 'Edirne', 'Istanbul', 'Gordion', 'Nicomedia', 'Konya', 'Artulu', 'Tyana', 'Onondaga', 'Afrasiab-Samarkand', 'Kök Tepe', 'Koktepe']
    #PATH = "/home/majid/dev/selenium/"

    # /home/majid/.mozilla/firefox/qtgamvz4.default-release
    profile = webdriver.FirefoxProfile(
        '/home/majid/.mozilla/firefox/qtgamvz4.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('intl.accept_languages', 'en-US, en')

    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired)
    
    potential_lat_on_info = {}
    my_file_name = "Long_lat_search_extra.json"
    for item in second_list:
        if item not in potential_lat_on_info.keys() and item not in my_list:
            driver.get(f"https://www.google.com/maps/place/")
            time.sleep(2)

            search_box = driver.find_element_by_id("searchboxinput")
            search_box.send_keys(item)
            search_box.send_keys(Keys.RETURN)

            time.sleep(8)
            print(driver.current_url)
            potential_lat_on_info[item] = driver.current_url
    
            with open(my_file_name, "w") as outfile:
                json.dump(potential_lat_on_info, outfile)


def long_lat_extractor(json_file_list, capital_polity_mapper_json):
    """
    returns a et of proper long lat and 
    """
    translator = Translator()

    with open(capital_polity_mapper_json) as json_cap_mapper_file:
        capital_polity_mapper = json.load(json_cap_mapper_file)
    final_list_of_dics = []
    for json_file in json_file_list:
        with open(json_file) as json_file:
            my_google_rows = json.load(json_file)
        for cap_name, url_text in my_google_rows.items():
            if "maps/place/" in url_text:
                drop_http = url_text.split("maps/place/")[1]
                google_names = drop_http.split("/")[0]
                google_name = google_names.split(",")[0]
                if "+" in google_names:
                    google_country_name = google_names.split("+")[-1]
                else:
                    google_country_name = "NO_COUNTRY_FROM_GOOGLE"
                if "@" not in drop_http:
                    print(cap_name, " is BAD")
                    continue
                coords = drop_http.split("@")[1]
                lat, lon = float(coords.split(",")[0]) , float(coords.split(",")[1])
                if (lat == 48.2078548 and lon == 16.3414016)  or (lat == 48.2079093 and lon == 16.334848)  or (lat == 48.2079093 and lon == 16.3414016) or (lat == 48.2078548 and lon == 16.334848):
                    print("BAD SEarch", cap_name, json_file)
                    a_dic = {
                        "capital_city": cap_name,
                        "current_country": "NO_COUNTRY_FROM_GOOGLE",
                        "pol_id": capital_polity_mapper[cap_name],
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "maps_url" : "#",
                    }
                    if a_dic not in final_list_of_dics:
                        final_list_of_dics.append(a_dic)
                else:
                    de_country = unquote(google_country_name)
                    en_country_res = translator.translate(de_country, src='de', dest='en')
                    en_country = en_country_res.text
                    a_dic = {
                        "capital_city": cap_name,
                        "current_country": en_country,
                        "pol_id": capital_polity_mapper[cap_name],
                        "latitude": lat,
                        "longitude": lon,
                        "maps_url" : url_text,
                    }
                    if a_dic not in final_list_of_dics:
                        final_list_of_dics.append(a_dic)
            elif "maps/search/" in url_text:
                drop_http = url_text.split("maps/search/")[1]
                google_name = drop_http.split("/")[0]
                google_country_name = "NO_COUNTRY_FROM_GOOGLE"
                if "@" not in drop_http:
                    print(cap_name, " is BAD")
                    continue
                coords = drop_http.split("@")[1]
                lat, lon = float(coords.split(",")[0]) , float(coords.split(",")[1])
                if (lat == 48.2078548 and lon == 16.3414016)  or (lat == 48.2079093 and lon == 16.334848)  or (lat == 48.2079093 and lon == 16.3414016) or (lat == 48.2078548 and lon == 16.334848):
                    print("BAD SEarch", cap_name, json_file)
                    a_dic = {
                        "capital_city": cap_name,
                        "current_country": "NO_COUNTRY_FROM_GOOGLE",
                        "pol_id": capital_polity_mapper[cap_name],
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "maps_url" : "#",
                    }
                    if a_dic not in final_list_of_dics:
                        final_list_of_dics.append(a_dic)
                else:
                    de_country = unquote(google_country_name)
                    en_country_res = translator.translate(de_country, src='de', dest='en')
                    en_country = en_country_res.text
                    a_dic = {
                        "capital_city": cap_name,
                        "current_country": en_country,
                        "pol_id": capital_polity_mapper[cap_name],
                        "latitude": lat,
                        "longitude": lon,
                        "maps_url" : url_text,
                    }
                    if a_dic not in final_list_of_dics:
                        final_list_of_dics.append(a_dic)
            else:
                print("BAD Entry")
                    
    with open("ultimate_cap_file_en.json", "w") as outfile:
        json.dump(final_list_of_dics, outfile)
    return final_list_of_dics


def create_capital_sql(my_ult_json, local=True):
    if local:
        csv_file_for_polity = "my_politys.csv"
        output_file = "capitals.sql"
    else:
        csv_file_for_polity = "CSV_AWS/my_politys.csv"
        output_file = "SQL_AWS/capitals.sql"

    polity_mapper = polity_mapper_maker(csv_file_for_polity)
    with open(my_ult_json) as json_cap_file:
        all_capital_data_list = json.load(json_cap_file)
        with open(output_file, "w") as cap_file:
            all_rows_with_capital_sql = []
            for index, item in enumerate(all_capital_data_list):
                name = item["capital_city"].replace("'", "''")
                current_country = item["current_country"].replace("'", "''")
                longitude =  item["longitude"]
                latitude =  item["latitude"]
                maps_url = item["maps_url"]
                polity_id = polity_mapper[item["pol_id"]]

                a_row = f"INSERT INTO core_capital (id, name, current_country, polity_cap_id, longitude, latitude, is_verified, url_on_the_map) VALUES ({index+1}, '{name}', '{current_country}', {polity_id}, {longitude}, {latitude}, 'false', '{maps_url}');"
                all_rows_with_capital_sql.append(a_row)

            cap_file.write("\n".join(all_rows_with_capital_sql))
            print(f"{len(all_rows_with_capital_sql)} sql insertion rows added to: {output_file}")


def create_subregion_country_sql(my_df, local=True):
    if local:
        output_file = "subregion_and_countrys.sql"
    else:
        output_file = "SQL_AWS/subregion_and_countrys.sql"

    with open(output_file, "w") as subreg_file:
        all_rows_with_subregion_sql = []
        for item in my_df.iterrows():
            name = item[1]["NGA"]
            current_country = item[1]["modern_country"]
            subregion =  item[1]["Seshat_region"]

            a_row = f"UPDATE core_nga SET subregion = '{subregion}', fao_country = '{current_country}' WHERE name = '{name}';"
            all_rows_with_subregion_sql.append(a_row)

        subreg_file.write("\n".join(all_rows_with_subregion_sql))
        print(f"{len(all_rows_with_subregion_sql)} sql insertion rows added to: {output_file}")
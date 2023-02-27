from lxml import etree, html
from bs4 import BeautifulSoup
import requests
import csv
import re
import bs4
import json
import time
import pandas as pd
import os

def read_unique_variables():
    """
    - From Equinox data, ectarct all unique section/subsection/variables
    - return unique general variables
    """

    df = pd.read_excel('Equinox_2020_packaged_xls.xls', sheet_name="Equinox2020_CanonDat")

    unique_general_variables = []
    for row in df.iterrows():
        if row[1]['Section'] == "General variables":
            if row[1]['Variable'] not in unique_general_variables:
                unique_general_variables.append(row[1]['Variable'])
    return unique_general_variables

def ref_span_replacer(my_str, polity_name):
    RefRegex = re.compile('<sup id="cite_ref-(\d{1,4})" class="reference"><a href="#cite_note-(\d{1,4})">\[(\d{1,4})\]</a></sup>')
    catches_all = RefRegex.finditer(my_str)
    #print(catches_all)
    if catches_all:
        for index, catches in enumerate(catches_all):
            if catches.group(1) == catches.group(2) and catches.group(1) == catches.group(3):
                my_str = my_str.replace(catches.group(0), f"[MAJIDBENAM_REF_{catches.group(1)}_{polity_name}]")
                if "_" in polity_name:
                    print(f"underlined polity name: {polity_name}")
            else:
                print(f"MIsMatch at index: {index+1}")
    return my_str




def image_remover(my_str):
    RefRegex = re.compile(r'(<p)>(.*?) src="/w/images(.*?)(</p)>')
    catches_all = RefRegex.finditer(my_str)
    if catches_all:
        for index, catches in enumerate(catches_all):
            my_str = my_str.replace(catches.group(0), "")
    RefRegex_2 = re.compile(r'<div><a href=(.*?) src="/w/images(.*?)"></a></div>')
    catches_all_2 = RefRegex_2.finditer(my_str)
    if catches_all_2:
        for index, catches_2 in enumerate(catches_all_2):
            my_str = my_str.replace(catches_2.group(0), "")
    return my_str
    

def edit_tag_remover(my_str):
    RefRegex = re.compile(r'(<h4|<h2)>(.*?) class="mw-editsection-bracket">\[</span><a href(.*?) class="mw-editsection-bracket">\]</span>(.*?)(</h4|</h2)>')
    catches_all = RefRegex.finditer(my_str)
    if catches_all:
        for index, catches in enumerate(catches_all):
            my_str = my_str.replace(catches.group(0), "")
    return my_str

def linguistic_decider(my_str):
    RefRegex = re.compile(r'(<b>♠ Linguistic family)(.*?)</b>(.*?)(</div>)')
    catches_all = RefRegex.finditer(my_str)
    #print(catches_all)
    if catches_all:
        for index, catches in enumerate(catches_all):
            my_str = my_str.replace(catches.group(1), "</div><div class='meatypart'><b>♠ Linguistic family")

    return my_str

def inner_div_decider(my_str):
    new_str = my_str.replace("♥</b></div><div>", '♥</b>')
    new_str = new_str.replace("</div><div>", '[MAJIDBENAM_BR]')
    return new_str


def gen_var_html_extractor():
    my_politys = []
    with open("polity_ngas.csv", 'r') as pol_csv:
        csv_reader = csv.reader(pol_csv, delimiter=',')
        for row in csv_reader:
            my_politys.append(row[1])
    for polity in my_politys:
        top_html = "<!DOCTYPE html><html><body><h2>"
        bottom_html = "</body></html>"
        with open(f"html_files/full_{polity}.html", "r", encoding='utf-8') as f:
            source= f.read()
            split_general = source.split('<span class="mw-headline" id="General_variables">General variables</span>')[1]
            split_source = split_general.split('<span class="mw-headline" id="Social_Complexity_variables">Social Complexity variables</span>')[0]
            better_source = split_source.replace("  ♣", " ♣").replace(" ♠", "♠").replace("♥ ", "♥")
            best_source = better_source.replace("<dl>", "").replace("</dl>", "").replace("<dd>", "<p>").replace("</dd>", "</p>").replace("\n", "")
            great_source = best_source.replace("<p><br><b>", "<p><b>").replace("<p><br></p>", "").replace("</p><p> <b>♠", "</p><p><b>♠")
            perfect_source = great_source.replace("</p><p><b>♠", "</div><p><b>♠").replace("</p><h4>", "</div><h4>")
            perfect_100 = perfect_source.replace("<p><b>♠", "<div class='meatypart'><b>♠")
            perfect_1000 = perfect_100.replace("</a></div><h4>", "</a></p><h4>").replace("</b></p><h2>", "</b></div>")
            perfect_2000 = perfect_1000.replace("<p>", "<div>").replace("</p>", "</div>")

            better_html_0 = top_html + perfect_2000 +  bottom_html
            better_html = better_html_0.replace("<h2></body>", "</body>")
            if better_html.count('<div') != better_html.count('</div'):
                print(f"{polity}: Number of divs: {better_html.count('<div')} and number of /divs: {better_html.count('</div')}.")
            if better_html.count('<p') != better_html.count('</p'):
                print(f"{polity}: Number of ps: {better_html.count('<p')} and number of /ps: {better_html.count('</p')}.")

            final_html_after_Linguistic_family = linguistic_decider(better_html)
            final_html_after_ref_replacement = ref_span_replacer(final_html_after_Linguistic_family, polity)
            final_html_after_image_removal = image_remover(final_html_after_ref_replacement)
            final_html_after_edit_removal = edit_tag_remover(final_html_after_image_removal)
            final_html_after_inner_par = inner_div_decider(final_html_after_edit_removal)
            

            with open(f"html_files_general/full_general_{polity}.html", "w", encoding='utf-8') as fw:
                fw.write(final_html_after_inner_par)




def general_variables_extractor():
    """
    - Goes through all the Wiki pages
    - Finds all the General Variable Sections
    - Puts all the Unique Variables in a list
    - returns the list of unique genearl description variables
    """
    READ_FROM_LOCAL = True

    UNIQUE_GEN_VARS = ['RA', 'UTM zone', 'Original name', 'Alternative names', 'Peak Date', 'Duration', 'Degree of centralization', 'Supra-polity relations', 'Capital', 'Language', 'Linguistic family', 'Religion Genus', 'Religion Family', 'Religion', 'preceding (quasi)polity', 'relationship to preceding (quasi)polity', 'succeeding (quasi)polity', 'Supracultural entity', 'scale of supra-cultural interaction', 'Alternate Religion Genus', 'Expert', 'Alternate Religion Family', 'Editor','Alternate Religion', 'Linguistic Family', 'Language Genus', 'Religious Tradition',]

    unique_vars_underlined = [my_var.replace(" ", "_").lower() for my_var in UNIQUE_GEN_VARS]

    # UNIQUE_GEN_VARS = ['RA', 'UTM zone', 'Original name ', 'Alternative names ', 'Peak Date ', 'Duration ', 'Degree of centralization', 'Supra-polity relations', 'Capital ', 'Language ', 'Linguistic family ', 'Religion Genus', 'Religion Family', 'Religion', 'preceding (quasi)polity ', 'relationship to preceding (quasi)polity', 'succeeding (quasi)polity ', 'Supracultural entity', 'scale of supra-cultural interaction', 'Alternate Religion Genus', 'Expert', 'Alternate Religion Family', 'Alternate Religion Genus2', 'Editor', 'Alternate Religion Family2', 'Alternate Religion Genus3', 'Alternate Religion', 'Linguistic Family', 'Language Genus', 'Religious Tradition', 'Alternate Religion Family3', 'Alternate Religion2']

    #UNIQUE_GEN_VARS = ['Language Genus']
    my_politys = []
    with open("polity_ngas.csv", 'r') as pol_csv:
        csv_reader = csv.reader(pol_csv, delimiter=',')
        for row in csv_reader:
            my_politys.append(row[1])
    
    # the dic with all the dataframes for variables and values
    big_dic ={}

    for var in UNIQUE_GEN_VARS:
        var_name = var.replace(" ", "_").lower()
        values_df = pd.DataFrame(columns = [var_name, 'polity', 'wiki_value', 'wiki_desc'])
        refs_df = pd.DataFrame(columns = [var_name, 'polity', 'wiki_ref_raw', 'wiki_ref_augmented'])
        big_dic[var_name] = {
            "values_df": values_df,
            "refs_df": refs_df
        }

    for polity in my_politys:
        #print(polity)

        if READ_FROM_LOCAL:
            with open(f"html_files_general_PLUS/full_general_{polity}.html", "r", encoding='utf-8') as f:
                source= f.read()
            soup = BeautifulSoup(source, 'lxml')
            soup_new = soup.find_all('div' , class_ = 'meatypart')

        else:
            source_url_seshatdb = 'http://seshatdatabank.info/browser/' 
            source_url = source_url_seshatdb + polity

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            }
            #source = requests.get(source_url, headers=headers).text
            source = requests.get(source_url, headers=headers)
            soup = BeautifulSoup(source.content.decode('utf-8'), 'lxml')

        #print(polity, end=",")
        for soup_section in soup_new:
            VarRegex = re.compile(r'♠ (.*?) ♣(.*?)♥')
            full_text = str(soup_section.text)
            catch = VarRegex.search(full_text)
            if catch:
                var_name_scraped = catch.group(1).strip().replace(" ", "_").lower()
                if var_name_scraped in unique_vars_underlined:
                    pot_desc_split = full_text.split('♥')
                    if len(pot_desc_split) > 1 and pot_desc_split[1].strip():
                        wiki_desc = pot_desc_split[1].strip()
                    else:
                        wiki_desc = "NO_DESCRIPTION_ON_WIKI"

                    if catch.group(2).strip():
                        wiki_value = catch.group(2).strip()
                    else:
                        wiki_value = "NO_VALUE_ON_WIKI"
                    
                    if wiki_value != "NO_VALUE_ON_WIKI" or wiki_desc != "NO_DESCRIPTION_ON_WIKI":
                        #print("Yooop")
                        big_dic[var_name_scraped]["values_df"] = big_dic[var_name_scraped]["values_df"].append({
                                var_name_scraped : var_name_scraped,
                                'polity': polity,
                                'wiki_value': wiki_value,
                                'wiki_desc': wiki_desc
                                }, ignore_index = True)


            #print("_____")

            
        # END OF FILE  
    return big_dic

    #     # selects the main text
    #     for potential_general_var in UNIQUE_GEN_VARS:
    #         weird_card_game_text = f" {potential_general_var} ♣"
    #         for var in ["Ali"]:
    #             #print(var, ": ", var.text)
    #             if weird_card_game_text in var:
    #                 var_stew = var.split("♣")[1]
    #                 var_meat, var_gravy = var_stew.split("♥")
    #                 var_meat_stripped = var_meat.strip()
    #                 #if var_gravy.startswith("\n</p><p><br>") or var_gravy.startswith("\n</p>"):
    #                 #    var_gravy_stripped = ""
    #                 #elif "</p><p><br>" in var_gravy:
    #                 #    var_gravy_stripped = var_gravy.split("</p><p><br>")[0]
    #                 #else:
    #                 #    var_gravy_stripped = var_gravy.strip()
    #                 #to_be_added = [var_meat_stripped,var_gravy_stripped]
    #                 print(potential_general_var, ": ",var_meat_stripped, " ---->",  var_gravy)
    #                 print("_______")
    #                 #big_dic[potential_general_var].append(to_be_added)
    #                 #print("Bingo: " + polity + var.text)
    #                 #break
    #         #continue

    #     #big_dic[polity] = {}
    #     #for goodie in general_variables:
    #     #    print(goodie.text)
    #         #my_ref.find_previous('a')['href']
    #     if not READ_FROM_LOCAL:
    #         time.sleep(2)
    # return big_dic





###########################################
###########################################
###########################################


def nga_db_writer(my_df_NGA_ONLY, sql_file_name):
    nga_mapper_dic = {}
    with open(sql_file_name, "w") as nga_file:
        all_rows_with_nga_sql = []
        #nga_file.write(a_joined_str)
        for index, my_row in enumerate(my_df_NGA_ONLY.iterrows()):
            nga_name = my_row[1]["NGA"]
            subregion_name = my_row[1]["Subregion"]
            nga_code = my_row[1]["NGACode"]
            latitude = my_row[1]["Latitude"]
            longitude = my_row[1]["Longitude"]
            capital_city = my_row[1]["City"]
            fao_country = my_row[1]["FAO.Country"]

            nga_row = f"INSERT INTO core_nga (id, name, subregion, nga_code, longitude, latitude, capital_city, fao_country) VALUES ({index+1}, '{nga_name}', '{subregion_name}', '{nga_code}', {longitude}, {latitude}, '{capital_city}', '{fao_country}');"
            all_rows_with_nga_sql.append(nga_row)
            nga_mapper_dic[nga_name] = index + 1
            
        nga_file.write("\n".join(all_rows_with_nga_sql))
        print(f"{len(all_rows_with_nga_sql)} sql insertion rows added to: {sql_file_name}")
    return nga_mapper_dic


def nga_polity_rel_db_writer(my_polity_timeline, sql_file_name, nga_mapper, polity_mapper):
    """
    - we need two dics to map nga and polity stuff
    """
    with open(sql_file_name, "w") as nga_pol_rel_file:
        all_rows_with_nga_sql = []
        #nga_pol_rel_file.write(a_joined_str)
        for polity_name, tuple_list_values_dic in my_polity_timeline.items():
            polity_id  = polity_mapper[polity_name]
            for tuple, nga_list in tuple_list_values_dic.items():
                year_from = tuple[0]
                year_to = tuple[1]
                for nga_name in nga_list:
                    nga_id = nga_mapper[nga_name]
                    nga_row = f"INSERT INTO core_ngapolityrel (nga_party_id, polity_party_id, year_from, year_to) VALUES ({nga_id}, {polity_id}, {year_from}, {year_to});"
                    all_rows_with_nga_sql.append(nga_row)
            
        nga_pol_rel_file.write("\n".join(all_rows_with_nga_sql))
        print(f"{len(all_rows_with_nga_sql)} sql insertion rows added to: {sql_file_name}")


def polity_mapper_maker(csv_file, local=True):
    """
    This function assumes an updated CSV file for both local and AWS versions of the databse. 
    """
    root_dir = os.getcwd()
    if local:
        polity_csv_df = pd.read_csv(root_dir + "/" + csv_file)
    else:
        polity_csv_df = pd.read_csv(root_dir + "/CSV_AWS" +csv_file)
    polity_mapper_dic = {}
    for index, row in enumerate(polity_csv_df.iterrows()):
        polity_mapper_dic[row[1]['name']] = row[1]['id']
    return polity_mapper_dic


def polity_timeline_maker(my_df_NGA_POLITY):
    polity_info = {}
    for row in my_df_NGA_POLITY.iterrows():
        if not polity_info.get(row[1]['PolID']):
            polity_info[row[1]['PolID']] = []
            to_be_appended = {
                "NGA": row[1]['NGA'],
                "year_from": row[1]['Start'],
                "year_to": row[1]['End'],
            }
            polity_info[row[1]['PolID']].append(to_be_appended)
            #print("Hallo")
        else:
            to_be_appended = {
                "NGA": row[1]['NGA'],
                "year_from": row[1]['Start'],
                "year_to": row[1]['End'],
            }
            polity_info[row[1]['PolID']].append(to_be_appended)

    polity_timeline = {
        # key1: pol_id
        # key2, value: (year_from, year_to): [NGA1, NGA2, NGA3, etc.]
    }

    for polity, NGA_list in polity_info.items():
        polity_timeline[polity] = {}
        year_from_list = []
        year_to_list = []
        for NGA_dic in NGA_list:
            # create a list of broken down timesteps and check if there are gaps
            # set of all year_froms and year_tos
            year_from_list.append(NGA_dic['year_from'])
            year_to_list.append(NGA_dic['year_to'])
        # after getting all the data, we can create sets and timesteps
        year_from_list_uinque = list(set(year_from_list))
        year_to_list_uinque = list(set(year_to_list))
        
        merged_sorted_years = sorted(year_from_list_uinque + year_to_list_uinque)
        polity_timeline[polity]['years'] = merged_sorted_years
        polity_years_tuples = []
        for i in range(len(merged_sorted_years) - 1):
            polity_years_tuples.append((merged_sorted_years[i], merged_sorted_years[i+1]))
        
        polity_timeline[polity]['years_tuples'] = polity_years_tuples
        
        polity_timeline[polity] = {}
        for my_year_tuple in polity_years_tuples:
            key_2 = my_year_tuple
            value_2 = [] # list of NGAS
            for NGA_dic in NGA_list:
                # an NGA is inculded:
                if my_year_tuple[0] >= NGA_dic["year_from"] and my_year_tuple[1] <= NGA_dic["year_to"]:
                    value_2.append(NGA_dic["NGA"])
            if not value_2:
                print(my_year_tuple, ":", polity)
            polity_timeline[polity][key_2] = value_2
    return polity_timeline


def long_polity_name_updater(my_df_NGA_POLITY, sql_file_name):
    with open(sql_file_name, "w") as long_pol_name_file:
        all_rows_with_long_name_sql = []
        for row in my_df_NGA_POLITY.iterrows():
            name = row[1]['PolID']
            long_name = row[1]['PolName']
            long_name_row = f"UPDATE core_polity SET long_name = '{long_name}' WHERE name = '{name}';"
            if long_name_row in all_rows_with_long_name_sql:
                print(name, " is duplicate.")
            else:
                all_rows_with_long_name_sql.append(long_name_row)


        long_pol_name_file.write("\n".join(all_rows_with_long_name_sql))
        print(f"{len(all_rows_with_long_name_sql)} sql insertion rows added to: {sql_file_name}")


def long_polity_name_updater_PolsVars(my_df_NGA_POLITY, sql_file_name):
    with open(sql_file_name, "w") as long_pol_name_file:
        all_rows_with_long_name_sql = []
        all_rows_with_new_name_sql = []

        for row in my_df_NGA_POLITY.iterrows():
            name = row[1]['PolID']
            if name:
                new_name = row[1]['PolityID'] 
                long_name = row[1]['Longform.Name']
                long_name_row = f"UPDATE core_polity SET long_name = '{long_name}' WHERE name = '{name}';"
                new_name_row = f"UPDATE core_polity SET new_name = '{new_name}' WHERE name = '{name}';"

                if long_name_row in all_rows_with_long_name_sql:
                    print(name, " is duplicate.")
                else:
                    all_rows_with_long_name_sql.append(long_name_row)
                    all_rows_with_new_name_sql.append(new_name_row)


        long_pol_name_file.write("\n".join(all_rows_with_long_name_sql))
        long_pol_name_file.write("\n".join(all_rows_with_new_name_sql))

        print(f"{len(all_rows_with_long_name_sql)} sql insertion rows added to: {sql_file_name}")
        print(f"{len(all_rows_with_new_name_sql)} sql insertion rows added to: {sql_file_name}")
    


def nga_world_region_updater(my_df_NGA_POLITY, sql_file_name):
    region_mapper = {'Europe': 'Europe',
        'SouthwestAsia': 'Southwest Asia',
        'Africa': 'Africa',
        'CentralEurasia': 'Central Eurasia',
        'SouthAsia': 'South Asia',
        'SoutheastAsia': 'Southeast Asia',
        'EastAsia': 'East Asia',
        'Oceania-Australia': 'Oceania-Australia',
        'NorthAmerica': 'North America',
        'SouthAmerica': 'South America'}
    with open(sql_file_name, "w") as world_region_pol_file:
        all_rows_with_world_region_sql = []
        my_pairs = {}
        for row in my_df_NGA_POLITY.iterrows():
            name = row[1]['NGA']
            world_region = region_mapper[row[1]['World Region']]
            #for saved_nga, saved_reg in my_pairs.items():
            #    if saved_nga == name and world_region !=  saved_reg:
            #        print(f"ERROR: {saved_nga}, was already connected to {saved_reg}, and now wants to connecvt to {world_region}")
            world_region_row = f"UPDATE core_nga SET world_region = '{world_region}' WHERE name = '{name}';"
            my_pairs[name] = world_region
            if world_region_row in all_rows_with_world_region_sql:
                print(name, " is duplicate.")
            else:
                all_rows_with_world_region_sql.append(world_region_row)


        world_region_pol_file.write("\n".join(all_rows_with_world_region_sql))
        print(f"{len(all_rows_with_world_region_sql)} sql insertion rows added to: {sql_file_name}")
    
unique_religion_genuses = ['Islam',
 'Graeco-Bactrian Religions',
 'Hephthalite Religions',
 'Zoroastrianism',
 'Buddhism',
 'Hinduism',
 'Ancient Iranian Religions',
 'Chinese State Religion',
 'Ancient East Asian Religion',
 'Mongolian Shamanism',
 'Egyptian Religions',
 'Hellenistic Religions',
 'Christianity',
 'Ancient Javanese Religions',
 'Jain Traditions',
 'Mesopotamian Religions',
 'Roman State Religions',
 'Shinto',
 'Manichaeism',
 'Xiongnu Religions',
 'Hittite Religions',
 'Lydian Religions',
 'Phrygian Religions',
 'Ismaili']

unique_religions = ['Karrami',
 'Hanafi',
 'Shafii',
 'NO_VALUE_ON_WIKI',
 'Roman Catholic',
 'Twelver',
 'Sunni',
 'Shia',
 'Ismaili',
 'Byzantine Orthodox',
 'Mevlevi',
 'Bektasi',
 'Islam']




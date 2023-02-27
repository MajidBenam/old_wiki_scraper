MYINT = ['IntegerField', 'NumberInput']
MYDEC = ['DecimalField', 'NumberInput']
MYTXT = ['CharField', 'TextInput']
# for these we need, the pandas dfs to smartly select the choices, put them in a tuple or list
MYTXT_CH = ['CharField', 'Select']
MYFOREIGN = ['ForeignKey', 'Select']


def tuple_choices_maker_2(my_new_list_of_choices, choice_name):
    my_tuple_choices = []
    str_mid_list = []
    the_name_of_the_tuple = f"{choice_name.upper()}_CHOICES"
    str_top = f"{the_name_of_the_tuple} = (\n"
    str_bot = ")\n\n"

    for item in my_new_list_of_choices:
        #goodie = v[good_key]["colname"]
        str_mid_list.append(f"('{item}', '{item}'),\n")
        str_mid = "".join(str_mid_list)
    full_string = str_top + str_mid + str_bot
    my_tuple_choices.append(full_string)        
                       
    # take care of beginning and end
    my_tuple_choices.insert(0, f"\n##### tuple choices for  {choice_name}.\n")
    my_tuple_choices_str = "".join(my_tuple_choices)
    return the_name_of_the_tuple, my_tuple_choices_str

#'continuity', 'continuation', 'Continuation', 'contination', 'Continuity', 'continunity', 


degree_of_centralization_CHOICES = ['loose', 'confederated state', 'unitary state', 'nominal', 'confederate state', 'quasi-polity', 'suspected unknown', 'none', 'unknown', 'confederation', 'polity', 'NO_VALUE_ON_WIKI', 'nominal allegiance', 'unitary', ]

supra_polity_relations_CHOICES =  ['none', 'vassalage', 'alliance', 'nominal allegiance', 'suspected unknown', 'nominal', 'personal union', 'NO_VALUE_ON_WIKI', 'unknown', 'Nominal', 'Alliance', 'uncoded',]

language_CHOICES = ['Pashto', 'Persian', 'Greek', 'Bactrian', 'Sogdian', 'Pahlavi', 'Brahmi', 'Kharoshthi', 'Tocharian', 'Chinese', 'archaic Chinese', 'Xiangxi', 'Qiandong', 'Chuanqiandian', 'Hmong-Mien', 'Hmongic', 'Middle Chinese', 'Jurchen', 'Khitan', 'Xianbei', 'Manchu language', 'Mongolian language', 'Atanque', 'Shuar', 'Arabic', 'suspected unknown', 'NO_VALUE_ON_WIKI', 'Demotic', 'Ancient Egyptian', 'Late Egyptian', 'demotic Egyptian', 'Castilian Spanish', 'Chuukese', 'French', 'Langues dOil', 'Occitan', 'Latin', 'Old Frankish', 'Germanic', 'Gallic', 'Gaulish', 'English', 'Akan', 'Twi', 'Doric Greek', 'Minoan', 'Early Greek', 'Eteocretan', 'Old Hawaiian', 'Hawaiian', 'Iban', 'Sanskrit', 'Old Javanese', 'Middle Javanese', 'Javanese', 'Canaanite', 'Aramaic', 'Hebrew', 'Kannada', 'Urdu', 'A’chik', 'Prakrit', 'Telugu', 'Tamil', 'Akkadian', 'Sumerian', 'Amorite', 'Old Babylonian', 'Mesopotamian Religions', 'Old Persian', 'Elamite', 'Egyptian', 'Old Elamite', 'Mongolian', 'native Iranian languages', 'Turkic', 'Turkish', 'Babylonian', 'Hurrian', 'Proto-Elamite', 'Old Norse', 'Italian', 'Middle Japanese', 'Old Japanese', 'Late Old Japanese', 'Japanese', 'Early Modern Japanese', 'Old Turkic', 'Iranian', 'Old Khmer', 'Mon', 'Tai', 'Khmer', 'Pali', 'Phoenician', 'Berber', 'Spanish', 'Portuguese', 'Bambara', 'Mande', 'Songhay', 'Russian', 'Georgian', 'Armenian', 'Kereid', 'Tatar', 'Naimans', 'Khalkha', 'Rouran', 'Xiongnu', 'Oirat', 'Zapotec', 'Icelandic', 'Aymara', 'Puquina', 'Quechua', 'Orokaiva', 'unknown', 'Sindhi', 'Punjabi', 'Sakha (Yakut)', 'Merotic', 'Coptic', 'Thai', 'Proto-Indo-European language', 'Nesite', 'Luwian', 'Hattic', 'Hittite', 'Old Assyrian dialect of Akkadian', 'Indo-European language', 'Lydian', 'Ottoman Turkish', 'Phrygian', 'Miami Illinois', 'Cayuga', 'Mohawk', 'Oneida', 'Onondaga', 'Seneca', 'Tuscarora', 'Middle Mongolian', 'Ancient Iranian', 'Chagatai Turkish', 'Sabaic', 'Mainic', 'Qatabanic', 'Hadramawtic', 'Old Arabic']

language_genus_CHOICES = ['NO_VALUE_ON_WIKI', 'Afro-Asiatic', 'Indo-European',
       'suspected unknown']

# Done Merged (language_genus and linguistic_family)
linguistic_family_CHOICES = ['Indo-European', 'Sino-Tibetan', 'NO_VALUE_ON_WIKI', 'Tungusic', 'Altaic', 'Mongolic', 'Chibcha', 'Chicham', 'Afro-Asiatic', 'Oceanic-Austronesian', 'Celtic', 'Niger-Congo', 'Kwa', 'Hamito-Semitic', 'Austronesian', 'Malayo-Polynesian', 'Semitic', 'Indo-Iranian', 'Dravidian', 'isolate language', 'West Semetic', 'isolate', 'suspected unknown', 'language isolate', 'none', 'Germanic', 'Japonic', 'Turkic', 'Austro-Asiatic, Mon-Khmer', 'Austro-Asiatic', 'unknown', 'Mande', 'Songhay', 'Oghuz', 'Kartvelian', 'Manchu-Tungusic', 'Proto-Mongolic', 'Otomanguean', 'Proto-Otomanguean', 'Mixe-Zoquean', 'Aymaran', 'Quechuan', 'Papuan Languages', 'Tai-Kadai', 'Algonquian', 'Iroquois', 'Iranian']

# Done Merged
religion_genus_CHOICES = ['Zoroastrianism', 'Graeco-Bactrian Religions', 'Buddhism', 'Christianity', 'Islam', 'Mongolian Shamanism', 'Hittite Religions', 'Ismaili', 'Lydian Religions', 'Chinese State Religion', 'Egyptian Religions', 'Ancient Iranian Religions', 'Hellenistic Religions', 'Hephthalite Religions', 'Manichaeism', 'Ancient East Asian Religion', 'Jain Traditions', 'Xiongnu Religions', 'Roman State Religions', 'Shinto', 'Phrygian Religions', 'Mesopotamian Religions', 'Hinduism', 'Ancient Javanese Religions', 'Confucianism',]

# Done Merged
religion_family_CHOICES = ['Saivist Traditions', 'Assyrian Religions', 'Republican Religions', 'Imperial Confucian Traditions', 'Shii', 'Bhagavatist Traditions', 'Sunni', 'Vedist Traditions', 'Saivist', 'Islam', 'Chinese Folk Religion', 'Semitic', 'Vaisnava Traditions', 'Ptolemaic Religion', 'Vedic Traditions', 'Japanese Buddhism', 'Orthodox', 'Vaishnava Traditions', 'Shang Religion', 'Atenism', 'Mahayana', 'suspected unknown', 'Japanese State Shinto', 'Saiva Traditions', 'Sufi', 'Chinese Buddhist Traditions', 'Arian', 'Shia', 'Catholic', 'Western Zhou Religion', 'Imperial Cult', 'Theravada', 'Seleucid Religion',]

# Done Merged
religion_CHOICES = ['Islam', 'Shadhil', 'Karrami', 'Hanafi', 'Mevlevi', 'Ismaili', 'Shafii', 'Shia', 'Twelver', 'Byzantine Orthodox', 'Bektasi', 'NO_VALUE_ON_WIKI', 'Sunni', 'Roman Catholic', ]

relationship_to_preceding_entity_CHOICES = ['continuity', 'elite migration', 'cultural assimilation', 'continuation', 'indigenous revolt', 'replacement', 'population migration', 'hostile', 'disruption/continuity', 'continuity/discontinuity', 'NO_VALUE_ON_WIKI', 'suspected unknown', 'vassalage', 'not applicable',]


ALL_GENERAL_VARS_LIST =[
    {
    'varname': 'polity_research_assistant',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The RA(s) who worked on a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "Staff", # Hier 
    },
    {
    'varname': 'polity_utm_zone',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The UTM Zone of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_original_name',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The original name of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_alternative_name',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternative name of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_peak_years',
    'cols': 2,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The peak years of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_duration',
    'cols': 2,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The lifetime of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_degree_of_centralization',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The degree of centralization of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_suprapolity_relations',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The supra polity relations of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_capital',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The capital or the largest settlement of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_language',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The language or the largest settlement of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_linguistic_family',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The linguistic family of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_language_genus',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The language genus of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_religion_genus',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The religion genus of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_religion_family',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The religion family of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_religion',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The religion of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_relationship_to_preceding_entity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The polity relationship to preceding (quasi)polity", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_preceding_entity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The preceding entity of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_succeeding_entity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The succeeding entity of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_supracultural_entity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The supracultural entity of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_scale_of_supracultural_interaction',
    'cols': 2,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The scale_of_supra_cultural_interaction of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_alternate_religion_genus',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternate religion genus of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_alternate_religion_family',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternate religion family of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_alternate_religion',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternate religion  of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_expert',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The expert of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_editor',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The editor of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polity_religious_tradition',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The details of religious traditions.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    }
]


ALL_GENERAL_COLS_LIST =[
{
    'colname': "polity_ra",
    'dtype': MYFOREIGN,
    'varname': 'polity_research_assistant', # key
    'col_exp': "The RA of a polity.",
    'foreign_key': "Seshat_Expert",
    'foreign_key_related_name': "seshat_research_assistant",
    },
    {
    'colname': "utm_zone",
    'dtype': MYTXT,
    'varname': 'polity_utm_zone', # key
    'col_exp': "The details of UTM_ZONE.",
    'max_digits': 5,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "original_name",
    'dtype': MYTXT,
    'varname': 'polity_original_name', # key
    'col_exp': "The details of original_name.",
    'max_digits': 100,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "alternative_name",
    'dtype': MYTXT,
    'varname': 'polity_alternative_name', # key
    'col_exp': "The details of alternative_name.",
    'max_digits': 100,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "peak_year_from",
    'dtype': MYINT,
    'varname': 'polity_peak_years', # key
    'col_exp': "The beginning of the peak years for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "peak_year_to",
    'dtype': MYINT,
    'varname': 'polity_peak_years', # key
    'col_exp':  "The end of the peak years for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "polity_year_from",
    'dtype': MYINT,
    'varname': 'polity_duration', # key
    'col_exp': "The beginning year for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "polity_year_to",
    'dtype': MYINT,
    'varname': 'polity_duration', # key
    'col_exp':  "The end year for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "degree_of_centralization",
    'dtype': MYTXT_CH,
    'varname': 'polity_degree_of_centralization', # key
    'col_exp': "The details of degree_of_centralization.",
    'max_digits': 50,
    'choices': tuple_choices_maker_2(degree_of_centralization_CHOICES, "degree_of_centralization")[0],
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "supra_polity_relations",
    'dtype': MYTXT_CH,
    'varname': 'polity_suprapolity_relations', # key
    'col_exp': "The details of supra polity relations.",
    'max_digits': 50,
    'choices': tuple_choices_maker_2(supra_polity_relations_CHOICES, "supra_polity_relations")[0],
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "capital",
    'dtype': MYTXT,
    'varname': 'polity_capital', # key
    'col_exp': "The capital or the largest settlement of a polity.",
    'max_digits': 70,
    'null_meaning': "This polity did not have a capital or the largest settlement."
    },
    {
    'colname': "language",
    'dtype': MYTXT_CH,
    'varname': 'polity_language', # key
    'col_exp': "The language of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(language_CHOICES, "language")[0],
    'null_meaning': "This polity did not have a language."
    },
    {
    'colname': "linguistic_family",
    'dtype': MYTXT_CH,
    'varname': 'polity_linguistic_family', # key
    'col_exp': "The linguistic family of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(linguistic_family_CHOICES, "linguistic_family")[0],
    'null_meaning': "This polity did not have a linguistic family."
    },
    {
    'colname': "language_genus",
    'dtype': MYTXT_CH,
    'varname': 'polity_language_genus', # key
    'col_exp': "The language genus of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(linguistic_family_CHOICES, "linguistic_family")[0],
    'null_meaning': "This polity did not have a language Genus."
    },
    {
    'colname': "religion_genus",
    'dtype': MYTXT_CH,
    'varname': 'polity_religion_genus', # key
    'col_exp': "The religion genus of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_genus_CHOICES, "religion_genus")[0],
    'null_meaning': "This polity did not have a religion genus."
    },
    {
    'colname': "religion_family",
    'dtype': MYTXT_CH,
    'varname': 'polity_religion_family', # key
    'col_exp': "The religion family of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_family_CHOICES, "religion_family")[0],
    'null_meaning': "This polity did not have a religion family."
    },
    {
    'colname': "religion",
    'dtype': MYTXT_CH,
    'varname': 'polity_religion', # key
    'col_exp': "The religion of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_CHOICES, "religion")[0],
    'null_meaning': "This polity did not have a religion."
    },
    {
    'colname': "relationship_to_preceding_entity",
    'dtype': MYTXT_CH,
    'varname': 'polity_relationship_to_preceding_entity', # key
    'col_exp': "The polity relationship to preceding (quasi)polity",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(relationship_to_preceding_entity_CHOICES, "relationship_to_preceding_entity")[0],
    'null_meaning': "This polity did not have a relationship to preceding (quasi)polity"
    },
    {
    'colname': "preceding_entity",
    'dtype': MYTXT,
    'varname': 'polity_preceding_entity', # key
    'col_exp': "The preceding entity or the largest settlement of a polity.",
    'max_digits': 70,
    'null_meaning': "This polity did not have a preceding entity."
    },
    {'colname': "succeeding_entity",
    'dtype': MYTXT,
    'varname': 'polity_succeeding_entity', # key
    'col_exp': "The succeeding entity or the largest settlement of a polity.",
    'max_digits': 70,
    'null_meaning': "This polity did not have a succeeding entity."
    },
    {
    'colname': "supracultural_entity",
    'dtype': MYTXT,
    'varname': 'polity_supracultural_entity', # key
    'col_exp': "The supracultural entity or the largest settlement of a polity.",
    'max_digits': 100,
    'null_meaning': "This polity did not have a supracultural entity."
    },
    {
    'colname': "scale_from",
    'dtype': MYINT,
    'varname': 'polity_scale_of_supracultural_interaction', # key
    'col_exp': "The lower scale of supra cultural interactionfor a polity.",
    'units': "km squared",
    'min': 0,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "scale_to",
    'dtype': MYINT,
    'varname': 'polity_scale_of_supracultural_interaction', # key
    'col_exp':  "The upper scale of supra cultural interactionfor a polity.",
    'units': "km squared",
    'min': 0,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "alternate_religion_genus",
    'dtype': MYTXT_CH,
    'varname': 'polity_alternate_religion_genus', # key
    'col_exp': "The alternate religion genus of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_genus_CHOICES, "religion_genus")[0],
    'null_meaning': "This polity did not have a alternatereligion genus."
    },
    {
    'colname': "alternate_religion_family",
    'dtype': MYTXT_CH,
    'varname': 'polity_alternate_religion_family', # key
    'col_exp': "The alternate religion family of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_family_CHOICES, "religion_family")[0],
    'null_meaning': "This polity did not have a alternate religion family."
    },
    {
    'colname': "alternate_religion",
    'dtype': MYTXT_CH,
    'varname': 'polity_alternate_religion', # key
    'col_exp': "The alternate religion of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_CHOICES, "religion")[0],
    'null_meaning': "This polity did not have a alternate religion ."
    },
    {
    'colname': "expert",
    'dtype': MYFOREIGN,
    'varname': 'polity_expert', # key
    'col_exp': "The expert of a polity.",
    'foreign_key': "Seshat_Expert",
    'foreign_key_related_name': "seshat_expert",
    'null_meaning': "This polity did not have an expert."
    },
    {
    'colname': "editor",
    'dtype': MYFOREIGN,
    'varname': 'polity_editor', # key
    'col_exp': "The editor of a polity.",
    'foreign_key': "Seshat_Expert",
    'foreign_key_related_name': "seshat_editor",
    'null_meaning': "This polity did not have an editor."
    },
    {
    'colname': "religious_tradition",
    'dtype': MYTXT,
    'varname': 'polity_religious_tradition', # key
    'col_exp': "The details of religious traditions.",
    'max_digits': 100,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    }
]



GEN_VAR_MAPPER = {'ra': 'polity_research_assistant',
 'utm_zone': 'polity_utm_zone',
 'original_name': 'polity_original_name',
 'alternative_names': 'polity_alternative_name',
 'peak_date': 'polity_peak_years',
 'duration': 'polity_duration',
 'degree_of_centralization': 'polity_degree_of_centralization',
 'supra-polity_relations': 'polity_suprapolity_relations',
 'capital': 'polity_capital',
 'language': 'polity_language',
 'linguistic_family': 'polity_linguistic_family',
 'religion_genus': 'polity_religion_genus',
 'religion_family': 'polity_religion_family',
 'religion': 'polity_religion',
 'preceding_(quasi)polity': 'polity_preceding_entity',
 'relationship_to_preceding_(quasi)polity': 'polity_relationship_to_preceding_entity',
 'succeeding_(quasi)polity': 'polity_succeeding_entity',
 'supracultural_entity': 'polity_supracultural_entity',
 'scale_of_supra-cultural_interaction': 'polity_scale_of_supracultural_interaction',
 'alternate_religion_genus': 'polity_alternate_religion_genus',
 'expert': 'polity_expert',
 'alternate_religion_family': 'polity_alternate_religion_family',
 'editor': 'polity_editor',
 'alternate_religion': 'polity_alternate_religion',
 'language_genus': 'polity_language_genus',
 'religious_tradition': 'polity_religious_tradition'}


PERSONNEL_MAPPER = {'Stephen Dean': 101,
 'Alice Williams': 102,
 'Edward A L Turner': 103,
 'Daniel Mullins': 104,
 'Agathe Dupeyron': 105,
 'Jill Levine': 106,
 'Eva Brandl': 107,
 'Po-Ju Tuan': 108,
 'Enrico Cioni': 109,
 'Julia Zinkina': 110,
 'Emilia Tomicka': 111,
 'Malwina Brachmańska': 112,
 'Katheriin Liibert': 113,
 'Jenny Reddish': 114,
 'Rudolf Cesaretti': 115,
 'Peter Francois': 116,
 'Dennis Spencer': 117,
 'Kostis Christakis': 118,
 'Hugh Bennett': 119,
 'Lottie Field': 120,
 'NO_VALUE_ON_WIKI': 121,
 'William Farrell': 122,
 'Marta Bartkowiak': 123,
 'Rosalind Purcell': 124,
 'Dan Hoyer': 125,
 'Joe Figliulo-Rosswurm': 126,
 'Rudolph Cesaretti': 127,
 'Gréine Jordan': 128,
 'AP': 129,
 'Veronica Walker': 130,
 'Samantha Holder': 131,
 'Peter Turchin': 132,
 'Giulia Nazzaro': 133,
 'Robert Harding': 134,
 'Artur Butkiewicz': 135,
 'Katarzyna Mich': 136,
 'Alicja Piślewska': 137,
 'Natalia Szych': 138,
 'Agnieszka Marta Duda': 139,
 'Katarzyna Harabasz': 140,
 'Aleksandra Neumannn': 141,
 'Marika Michalak': 142,
 'Marika Wałęga': 143,
 'Jedrzej Hordecki': 144,
 'Kalin Bullman': 145,
 'Thomas Cressy': 146,
 'Rob Conningham': 147,
 'Ruth Mostern': 148,
 'Andrey Korotayev': 149,
 'J. G. Manning': 150,
 'Juan Carlos Moreno Garcia': 151,
 'Donagh Davis': 152,
 'Peter Rudiack-Gould': 153,
 'Gedeon Lim': 154,
 'Oren Litwin': 155,
 'Selin Nugent': 156,
 'Axel Kristissen': 157,
 'Arni D Juliusson': 158,
 'Garrett Fagan': 159,
 'Nikolay Kradin': 160,
 'Charles Spencer': 161,
 'David Carballo': 162,
 'Alan Covey': 163,
 'Alessandro Ceccarelli': 164,
 'Johannes Preiser-Kapeller': 165,
 'Patrycja Filipowicz': 166,
 'Peter Peregrine': 167,
 'Alexander Sedov': 168}


NAME_DUPLICATE_FIXER = {'Stephen Dean': 'Stephen Dean',
 'Alice Williams': 'Alice Williams',
 'Edward A L Turner': 'Edward A L Turner',
 'Daniel Mullins': 'Daniel Mullins',
 'Agathe Dupeyron': 'Agathe Dupeyron',
 'Jill Levine': 'Jill Levine',
 'Eva Brandl': 'Eva Brandl',
 'Po-Ju Tuan': 'Po-Ju Tuan',
 'Enrico Cioni': 'Enrico Cioni',
 'Julia Zinkina': 'Julia Zinkina',
 'Emilia Tomicka': 'Emilia Tomicka',
 'Malwina Brachmańska': 'Malwina Brachmańska',
 'Katheriin Liibert': 'Katheriin Liibert',
 'Jenny Reddish': 'Jenny Reddish',
 'Rudolf Cesaretti': 'Rudolf Cesaretti',
 'Dennis Spencer': 'Dennis Spencer',
 'Kostis Christakis': 'Kostis Christakis',
 'Hugh Bennett': 'Hugh Bennett',
 'Lottie Field': 'Lottie Field',
 'NO_VALUE_ON_WIKI': 'NO_VALUE_ON_WIKI',
 'William Farrell': 'William Farrell',
 'Marta Bartkowiak': 'Marta Bartkowiak',
 'Rosalind Purcell': 'Rosalind Purcell',
 'Dan Hoyer': 'Dan Hoyer',
 'Joe Figliulo-Rosswurm': 'Joe Figliulo-Rosswurm',
 'Rudolph Cesaretti': 'Rudolph Cesaretti',
 'Gréine Jordan': 'Gréine Jordan',
 'AP': 'AP',
 'Veronica Walker': 'Veronica Walker',
 'Samantha Holder': 'Samantha Holder',
 'Peter Turchin': 'Peter Turchin',
 'Giulia Nazzaro': 'Giulia Nazzaro',
 'Robert Harding': 'Robert Harding',
 'Artur Butkiewicz': 'Artur Butkiewicz',
 'Katarzyna Mich': 'Katarzyna Mich',
 'Alicja Piślewska': 'Alicja Piślewska',
 'Natalia Szych': 'Natalia Szych',
 'Agnieszka Marta Duda': 'Agnieszka Marta Duda',
 'Katarzyna Harabasz': 'Katarzyna Harabasz',
 'Aleksandra Neumannn': 'Aleksandra Neumannn',
 'Marika Michalak': 'Marika Michalak',
 'Marika Wałęga': 'Marika Wałęga',
 'Jedrzej Hordecki': 'Jedrzej Hordecki',
 'Kalin Bullman': 'Kalin Bullman',
 'Thomas Cressy': 'Thomas Cressy',
 'Rob Conningham': 'Rob Conningham',
 'Ruth Mostern': 'Ruth Mostern',
 'Andrey Korotayev': 'Andrey Korotayev',
 'J. G. Manning': 'J. G. Manning',
 'Juan Carlos Moreno Garcia': 'Juan Carlos Moreno Garcia',
 'Donagh Davis': 'Donagh Davis',
 'Gedeon Lim': 'Gedeon Lim',
 'Oren Litwin': 'Oren Litwin',
 'Selin Nugent': 'Selin Nugent',
 'Axel Kristissen': 'Axel Kristissen',
 'Arni D Juliusson': 'Arni D Juliusson',
 'Garrett Fagan': 'Garrett Fagan',
 'Nikolay Kradin': 'Nikolay Kradin',
 'Charles Spencer': 'Charles Spencer',
 'David Carballo': 'David Carballo',
 'Alan Covey': 'Alan Covey',
 'Alessandro Ceccarelli': 'Alessandro Ceccarelli',
 'Johannes Preiser-Kapeller': 'Johannes Preiser-Kapeller',
 'Patrycja Filipowicz': 'Patrycja Filipowicz',
 'Peter Peregrine': 'Peter Peregrine',
 'Alexander Sedov': 'Alexander Sedov',
 "Peter Rudiack-Gould": "Peter Rudiack-Gould",
 "Peter Francois": "Peter Francois",
 # DUPLICATES OR PROBLEMATIC ONES
"Liibert": 'Katheriin Liibert',
'Rudy Cesaretti': 'Rudolf Cesaretti',
'Cesaretti': 'Rudolf Cesaretti',
'RC': 'Rudolf Cesaretti',
"DH": "Dan Hoyer",
"PT": "Peter Turchin",
"PF": "Peter Francois",
"JGM": "J. G. Manning",
"PRG": "Peter Rudiack-Gould",
"WalkerV": "Veronica Walker",
'Will Farrell': 'William Farrell',
'Farrell': 'William Farrell',
'Dan Mullins': 'Daniel Mullins',
'Agathe Dupreyon': 'Agathe Dupeyron',
'Edward Turner': "Edward A L Turner",
"Brachmanska": "Malwina Brachmańska"
}

old_vars_dic = {
    'agricultural_population': 
    {'db_name': 'general', 'main_desc': 'No Explanations.', 'main_desc_source': '', 'notes': 'Notes for the Variable agricultural_population are missing!', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': None, 'col1': {'colname': 'agricultural_population', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'agricultural_population', 'units': 'People', 'scale': 1000}}, 'arable_land': {'db_name': 'general', 'main_desc': 'No Explanations.', 'main_desc_source': '', 'notes': 'Notes for the Variable arable_land are missing!', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': None, 'col1': {'colname': 'arable_land', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'arable_land', 'units': 'mu?', 'scale': 1000}}, 'arable_land_per_farmer': {'db_name': 'general', 'main_desc': 'No Explanations.', 'main_desc_source': '', 'notes': 'Notes for the Variable arable_land_per_farmer are missing!', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': True, 'col1': {'colname': 'arable_land_per_farmer', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'arable_land_per_farmer', 'units': 'mu?', 'scale': 1}}, 'gross_grain_shared_per_agricultural_population': {'db_name': 'general', 'main_desc': 'No Explanations.', 'main_desc_source': '', 'notes': 'Notes for the Variable gross_grain_shared_per_agricultural_population are missing!', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': None, 'col1': {'colname': 'gross_grain_shared_per_agricultural_population', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'gross_grain_shared_per_agricultural_population', 'units': '(catties per capita)', 'scale': 1}}, 'net_grain_shared_per_agricultural_population': {'db_name': 'general', 'main_desc': 'No Explanations.', 'main_desc_source': '', 'notes': 'Notes for the Variable net_grain_shared_per_agricultural_population are missing!', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': None, 'col1': {'colname': 'net_grain_shared_per_agricultural_population', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'net_grain_shared_per_agricultural_population', 'units': '(catties per capita)', 'scale': 1}}, 'surplus': {'db_name': 'general', 'main_desc': 'No Explanations.', 'main_desc_source': '', 'notes': 'Notes for the Variable surplus are missing!', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': True, 'col1': {'colname': 'surplus', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'surplus', 'units': '(catties per capita)', 'scale': 1}}, 'military_expense': {'db_name': 'general', 'main_desc': 'Main Descriptions for the Variable military_expense are missing!', 'main_desc_source': 'https://en.wikipedia.org/wiki/Disease_outbreak', 'notes': 'Not sure about Section and Subsection.', 'cols': 2, 'section': 'Economy Variables', 'subsection': 'State Finances', 'needsSeshatCommon': None, 'col1': {'colname': 'conflict', 'dtype': ['CharField', 'TextInput'], 'varname': 'military_expense'}, 'col2': {'colname': 'expenditure', 'dtype': ['DecimalField', 'NumberInput'], 'varname': 'military_expense', 'units': 'millions silver taels', 'scale': 1, 'decimal_places': 15, 'max_digits': 20}}, 'silver_inflow': {'db_name': 'general', 'main_desc': 'Silver inflow in Millions of silver taels??', 'main_desc_source': '', 'notes': 'Needs suoervision on the units and scale.', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'State Finances', 'needsSeshatCommon': None, 'col1': {'colname': 'silver_inflow', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'silver_inflow', 'units': 'Millions of silver taels??', 'scale': 1000000}}, 'silver_stock': {'db_name': 'general', 'main_desc': 'Silver stock in Millions of silver taels??', 'main_desc_source': '', 'notes': 'Needs suoervision on the units and scale.', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'State Finances', 'needsSeshatCommon': None, 'col1': {'colname': 'silver_stock', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'silver_stock', 'units': 'Millions of silver taels??', 'scale': 1000000}}, 'total_population': {'db_name': 'general', 'main_desc': 'Total population or simply population, of a given area is the total number of people in that area at a given time.', 'main_desc_source': '', 'notes': 'Note that the population values are scaled.', 'cols': 1, 'section': 'Social Complexity Variables', 'subsection': 'Social Scale', 'needsSeshatCommon': None, 'col1': {'colname': 'total_population', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'total_population', 'units': 'People', 'scale': 1000}}, 'gdp_per_capita': {'db_name': 'general', 'main_desc': "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", 'main_desc_source': 'https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848', 'notes': 'The exact year based on which the value of Dollar is taken into account is not clear.', 'cols': 1, 'section': 'Economy Variables', 'subsection': 'Productivity', 'needsSeshatCommon': None, 'col1': {
        'colname': 'gdp_per_capita', 'dtype': ['DecimalField', 'NumberInput'], 'varname': 'gdp_per_capita', 'units': 'Dollars (in 2009?)', 'scale': 1, 'decimal_places': 15, 'max_digits': 20}}, 'drought_events': {'db_name': 'general', 'main_desc': 'number of geographic sites indicating drought', 'main_desc_source': 'https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt', 'notes': 'Notes for the Variable drought_events are missing!', 'cols': 1, 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'needsSeshatCommon': None, 'col1': {'colname': 'drought_events', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'drought_events', 'units': 'Numbers', 'scale': 1}}, 'locust_events': {'db_name': 'general', 'main_desc': 'number of geographic sites indicating locusts', 'main_desc_source': 'https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt', 'notes': 'Notes for the Variable locust_events are missing!', 'cols': 1, 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'needsSeshatCommon': None, 'col1': {'colname': 'locust_events', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'locust_events', 'units': 'Numbers', 'scale': 1}}, 'socioeconomic_turmoil_events': {'db_name': 'general', 'main_desc': 'number of geographic sites indicating socioeconomic turmoil', 'main_desc_source': 'https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt', 'notes': 'Notes for the Variable socioeconomic_turmoil_events are missing!', 'cols': 1, 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'needsSeshatCommon': None, 'col1': {'colname': 'socioeconomic_turmoil_events', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'socioeconomic_turmoil_events', 'units': 'Numbers', 'scale': 1}}, 'crop_failure_events': {'db_name': 'general', 'main_desc': 'number of geographic sites indicating crop failure', 'main_desc_source': 'https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt', 'notes': 'Notes for the Variable crop_failure_events are missing!', 'cols': 1, 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'needsSeshatCommon': None, 'col1': {'colname': 'crop_failure_events', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'crop_failure_events', 'units': 'Numbers', 'scale': 1}}, 'famine_events': {'db_name': 'general', 'main_desc': 'number of geographic sites indicating famine', 'main_desc_source': 'https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt', 'notes': 'Notes for the Variable famine_events are missing!', 'cols': 1, 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'needsSeshatCommon': None, 'col1': {'colname': 'famine_events', 'dtype': ['IntegerField', 'NumberInput'], 'varname': 'famine_events', 'units': 'Numbers', 'scale': 1}}, 'disease_outbreak': {'db_name': 'general', 'main_desc': 'A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.', 'main_desc_source': 'https://en.wikipedia.org/wiki/Disease_outbreak', 'notes': 'Notes for the Variable disease_outbreak are missing!', 'cols': 6, 'section': 'Well Being', 'subsection': 'Biological Well-Being', 'needsSeshatCommon': None, 'col1': {'colname': 'longitude', 'dtype': ['DecimalField', 'NumberInput'], 'varname': 'disease_outbreak', 'units': 'Degrees', 'min': -180, 'max': 180, 'scale': 1, 'decimal_places': 15, 'max_digits': 20}, 'col2': {'colname': 'latitude', 'dtype': ['DecimalField', 'NumberInput'], 'varname': 'disease_outbreak', 'units': 'Degrees', 'min': -180, 'max': 180, 'scale': 1, 'decimal_places': 15, 'max_digits': 20}, 'col3': {'colname': 'elevation', 'dtype': ['DecimalField', 'NumberInput'], 'varname': 'disease_outbreak', 'units': 'Meters', 'max': 5000, 'scale': 1, 'decimal_places': 15, 'max_digits': 20}, 'col4': {'colname': 'sub_category', 'dtype': ['CharField', 'Select'], 'varname': 'disease_outbreak', 'choices': ['Peculiar Epidemics', 'Pestilence', 'Miasm', 'Pox', 'Uncertain Pestilence', 'Dysentery', 'Malaria', 'Influenza', 'Cholera', 'Diptheria', 'Plague']}, 'col5': {'colname': 'magnitude', 'dtype': ['CharField', 'Select'], 'varname': 'disease_outbreak', 'choices': ['Uncertain', 'Light', 'Heavy', 'No description', 'Heavy- Multiple Times', 'No Happening', 'Moderate']}, 'col6': {'colname': 'duration', 'dtype': ['CharField', 'Select'], 'varname': 'disease_outbreak', 'choices': ['No description', 'Over 90 Days', 'Uncertain', '30-60 Days', '1-10 Days', '60-90 Days']}}}

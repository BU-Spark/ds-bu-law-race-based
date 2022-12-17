# Source Dataset

The data used is in Spring 22's google drive. We used the csv files in "Team 1/Processed Data", that are of the format "20XX_patent_grant_processed.csv". 

# Filtering Dataset for CN & KR

The code for filtering the original datasets for only Korean & Chinese Inventors is in `Spring22_Team_1_Filtering_KR_CN_Nov_15.ipynb` (cell 4). 

It creates a file of the format "20XX_CN_KR_patent_grant_processed.csv"


# Extracting Inventor Names

The code for extracting the original names of CN & KR inventors is in `Spring22_Team_1_Extracting_CN_KR_Names_2020_Oct_30.ipynb`. There is similar code in `Spring22_Team_1_Extracting_CN_KR_Names_2005.ipynb`.

It creates a file of the format "20XX_CN_KR_patent_grant_processed_names.csv"

The files generated using this method are in the Data folder of Google Drive. They are:- 

1. `Team_1_Original_Names/2017_CN_KR_patent_grant_processed_names_full.csv`
2. `Team_1_Original_Names/2018_CN_KR_patent_grant_processed_names_full.csv`
3. `Team_1_Original_Names/2019_CN_KR_patent_grant_processed_names.csv`
4. `Team_1_Original_Names/2020_CN_KR_patent_grant_processed_names.csv`
5. `Team_1_Original_Names/2021_CN_KR_patent_grant_processed_names_part1.csv`
6. `Team_1_Original_Names/2021_CN_KR_patent_grant_processed_names_part2.csv`

# Predicting Genders

The code for this section is in `Korean_Chinese_English_Nov22.ipynb`

### Reformat Extracted Names

The extracted data is reformated using code in Reformat section. It combines the extracted data and splits into Chinese & korean datasets:

1. `Team_1_Original_Names/Nov_22_CN_Names.csv`
2. `Team_1_Original_Names/Nov_22_KR_Names.csv`

They are in Google Drive data folder.

### English Names


The function "english_gender_CN" & "english_gender_KR" are used for english translated names gender prediciton. The dictionaries for this are in data folder. Source:- https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/MSEGSJ

1. `wgnd_2_0_name-gender_nocode.csv`
2. `gender_dict_kr.csv`
3. `gender_dict_cn.csv`

### Chinese Names

The class "Gender" & function "chinese_gender" are used for original chinese names gender prediciton. The files used for Chinese Gender prediction are in data folder. Source: -https://github.com/jaaack-wang/gender-predicator

1. `/gender_predicator_main_Naive_Bayes_Gender/ChineseLastNames.txt`
2. `/gender_predicator_main_Naive_Bayes_Gender/dict4Gender.json`

### Korean Names

The function "namsor_extraction_korean" is used for original korean names gender prediciton. The function utilization Namsor API (https://namsor.app/api-documentation/#genderize-name-batch)

### Final Files

The final data files are in Google Drive data folder:-

1. `Team_1_Original_Names/Nov_22_KR_Names_Gender_EN_2_KR.csv`
2. `Team_1_Original_Names/Nov_22_CN_Names_Gender_CN_EN.csv`

# Creating visualizations

Code for visualizations are in 

1. `Dec_3_Visualizations.ipynb`
2. `Nov_22_Visualizations-2.ipynb`
3. `Nov02_Visualizations.ipynb`
4. `visualization.py`

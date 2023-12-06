try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    print("Could not clear console and varaiables")
    
# Goal - to use soil type, Monthly rainfall (2017), length of growing period

import csv

year = '2015'

crops_file_path = 'India_Crop_Data/Crops.csv'

crops = {}

with open(crops_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    district_code_idx = 0
    year_idx = 1
    state_code_idx = 2
    rice_hectares_per_1000_hectares_idx = 5
    rice_production_idx = 6
    rice_kg_per_ha_idx = 7

    for row in csv_reader:  
        
        if row[year_idx] == year:
            
            district_state_code = row[district_code_idx] + "_" + row[state_code_idx]
            
            crop_growth = {
                "Rice_land_use_ha" : 1000 * float(row[rice_hectares_per_1000_hectares_idx]),
                "Rice_yield_kg_per_ha" : float(row[rice_kg_per_ha_idx]),
            }
            
            print(district_state_code)
            
            if crop_growth['Rice_land_use_ha'] > 0:
            
                crops.update({district_state_code : crop_growth})
           
            
rainfall_file_path = 'India_Crop_Data/Monthly_Rainfall.csv'

rainfall = {}

with open(rainfall_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    district_code_idx = 0
    year_idx = 1
    state_code_idx = 2
    january_rainfall_mm_idx = 5

    for row in csv_reader:  
        
        if row[year_idx] == year:
            
            district_state_code = row[district_code_idx] + "_" + row[state_code_idx]
            
            monthly_rainfall_mm = []
            
            for month_idx in range(january_rainfall_mm_idx, january_rainfall_mm_idx + 12):
                monthly_rainfall_mm.append(float(row[month_idx]))
            
            print(district_state_code)
            
            rainfall.update({district_state_code : monthly_rainfall_mm})


soiltype_file_path = 'India_Crop_Data/SoilType.csv'

districts_soil_types = {}

with open(soiltype_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    district_code_idx = 0
    state_code_idx = 2
    soil_type_idx = 5
    
    all_known_soil_types = []

    for row in csv_reader:  
        
        if row[0] != "Dist Code": #Ignore first row
            
            district_state_code = row[district_code_idx] + "_" + row[state_code_idx]
            
            soil_types = row[soil_type_idx]
            
            districts_soils = {}
            
            for soil_type_and_pct in soil_types.split(';'):
                
                split = soil_type_and_pct.split("-")
                
                if len(split) == 1: # Only 1 soil type, assume it is 100%
                    soil_type = split[0].strip()
                    soil_type_pct = 100
                
                else:
                    soil_type = split[0].strip()
                    soil_type_pct = split[1].strip()[0:-1]
                    
                districts_soils.update({soil_type : soil_type_pct})
            print()
            
            
            if soil_type != "NA":
                
                if soil_type not in all_known_soil_types:
                    all_known_soil_types.append(soil_type)
                
                districts_soil_types.update({district_state_code : districts_soils})

     




growing_period_file_path = 'India_Crop_Data/Crop_growing_period.csv'

growing_periods = {}

with open(growing_period_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    district_code_idx = 0
    state_code_idx = 2
    num_growing_days_per_year_idx = 5

    for row in csv_reader:  
        
        district_state_code = row[district_code_idx] + "_" + row[state_code_idx]
    
        growing_periods.update({district_state_code : row[num_growing_days_per_year_idx]})


   
irrigation_file_path = 'India_Crop_Data/Irrigation.csv'

irrigation = {}

with open(irrigation_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    district_code_idx = 0
    year_idx = 1
    state_code_idx = 2
    rice_ha_irrigated_idx = 5

    for row in csv_reader:  
        
        if row[year_idx] == year:
        
            district_state_code = row[district_code_idx] + "_" + row[state_code_idx]
    
            if district_state_code in crops.keys():
                rice_farmland_irrigated_ha = 1000 * float(row[rice_ha_irrigated_idx])
                pct_rice_farmland_irrigated = rice_farmland_irrigated_ha / crops[district_state_code]['Rice_land_use_ha']
                irrigation.update({district_state_code : pct_rice_farmland_irrigated})        




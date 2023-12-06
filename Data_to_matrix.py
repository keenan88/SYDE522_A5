try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    print("Could not clear console and varaiables")
    
# Goal - to use soil type, Monthly rainfall (2017), length of growing period

from Data_extraction import crops, rainfall, matrix_ready_soils, growing_periods, irrigation

x = []
y = []

for dist_state_code in crops.keys():
    if dist_state_code in rainfall.keys():
        if dist_state_code in matrix_ready_soils.keys():
            if dist_state_code in growing_periods.keys():
                if dist_state_code in irrigation.keys():
                    
                    datapoint = \
                        matrix_ready_soils[dist_state_code] + \
                        rainfall[dist_state_code] + \
                        [growing_periods[dist_state_code], 
                        irrigation[dist_state_code]]
                    
                    
                    x.append(datapoint)
                    
                    y.append(crops[dist_state_code]['Rice_yield_kg_per_ha'])
        


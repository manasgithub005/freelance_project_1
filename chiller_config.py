# -*- coding: utf-8 -*-
"""
Created on 7th Nov. 2023

@author: Manas
"""

config = {
    'project': 'NET0LINK',
    'state_name': 'chiller_power',

   
    'filename': './Chiller Plant Data - Aug - Nov 2023 - for_condensor_approach.xlsx',
    'out_dir': './',

    'enable_synth_data': 0,
    'post_files': 0,

    'model_name': [
                    #'CT2_power',
                    #'CT3_power',
                     #'chiller_power'
                     #'CWP1_power',
                    #'CWP2_power',
                    #'CP1_power',
                    #'CP2_power',
                    #'CWF',
                    #'COND_WF',
                    #'CWOT'
                    # 'evap_APPROACH'
                     #'suc_pres'
                     #'dis_pres'
                    
                   
                     ],
    'model_predict':[
                     #['Consumption CT 2'],
                     #['Consumption CT 3'],
                    #['Consumption Chiller'],
                    #  ['Consumption CWP 1'],
                      #['Consumption CWP 2'],
                     #['Consumption CP 1'],
                      #['Consumption CP 2'],
                     # ['Chilled Water Flow Chiller'],
                     # ['Condenser Water Flow Chiller'],
                     #['Cool Water Outlet Chiller']
                      #['Evaporator Approach Chiller'],
                       #['Suction Pressure Chiller']
                        #['Discharge Pressure Chiller']
                  
                    

                     
                    
                     
                    ],
    
    'next_state_pred': [0],
    'model_params': [
                    #['Output Frequency CT 2']
                    #['Output Frequency CT 3'],
                    #['Chiller Loading Chiller'],
                    # ['Output Frequency CWP 1'],
                    #['Output Frequency CWP 2'],
                     #['Output Frequency CP 1'],
                      #['Output Frequency CP 2'],
                     #['Output Frequency CWP 1','Output Frequency CWP 2'],
                     #['Output Frequency CP 1','Output Frequency CP 2'],
                      #['Chiller Setpoint Chiller']
                      #['Chiller Loading Chiller','Cool Water Inlet Chiller','Cool Water Outlet Chiller','Chilled Water Flow Chiller','Suction Pressure Chiller']
                     # ['Chiller Loading Chiller']
                      #['Chiller Loading Chiller']
                    


                        ],
  
    # Data specific
    'validation_split': 0.2,
    'data_bins': 4,

    # ANN Specific
    'batch_size': 4,
    'epochs': 500,

    # Random Forest specific
    'n_trees': 4000,
    'min_samples_leaf': 15,

}

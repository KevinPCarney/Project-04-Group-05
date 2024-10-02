import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass
        
    def makePredictions(self, Weather, Roadway_Type, Model_Year, Passengers_Belted, 
                        Time_of_Day, Speed_Limit, Roadway_Surface):

    
    
        Roadway_Type_Intersection = 0
        Roadway_Type_Street = 0
        Roadway_Type_Highway = 0
        Roadway_Type_Other = 0
        
        Roadway_Surface_Dry = 0
        Roadway_Surface_Wet = 0
            
        Time_of_Day_Morning = 0
        Time_of_Day_Afternoon = 0
        Time_of_Day_Night = 0
    
         # Initialize weather variables
        Clear = Snow = Rain = Cloudy = 0
    
           
        # parse Roadway Type
        if Roadway_Type == "Intersection":
            Roadway_Type_Intersection = 1
        elif Roadway_Type == "Street":    
            Roadway_Type_Street = 1
        elif Roadway_Type == "Highway":    
            Roadway_Type_Highway = 1
        elif Roadway_Type == "Other":  
            Roadway_Type_Other = 1
        else:
            pass
    
        # parse Roadway Surface
        if Roadway_Surface == "Dry":
            Roadway_Surface_Dry = 1
        elif Roadway_Surface == "Wet":
            Roadway_Surface_Wet = 1
        else:
            pass
        
        # parse Time of Day
        if Time_of_Day == "Morning":
            Time_of_Day_Morning = 1
        elif Time_of_Day == "Afternoon":
            Time_of_Day_Afternoon = 1
        elif Time_of_Day == "Night":
            Time_of_Day_Night = 1
        else:
            pass
    
         # Parse weather
        if Weather == "Clear":
            Clear = 1
        elif Weather == "Snow":
            Snow = 1
        elif Weather == "Rain":
            Rain = 1
        elif Weather == "Cloudy":
            Cloudy = 1
    
        #Weather, Roadway_Type, Model_Year, Passengers_Belted, 
         #                   Time_of_Day, Speed_Limit, Roadway_Surface):
    
        input_pred = [[Model_Year, Speed_Limit, Clear, Snow, Cloudy, Rain,
       Passengers_Belted, Time_of_Day_Afternoon, Time_of_Day_Morning,
       Time_of_Day_Night, Roadway_Type_Highway,
       Roadway_Type_Intersection, Roadway_Type_Other,
       Roadway_Type_Street, Roadway_Surface_Dry, Roadway_Surface_Wet
                       ]]
                       
    
        filename = 'car_crash_ml_v2.h5'
        rf_load = pickle.load(open(filename, 'rb'))
    
        X = np.array(input_pred)
       
        preds = rf_load.predict_proba(X)[0]
        preds_singular = rf_load.predict(X)
    
        rtn = {"prob_low_risk": preds[0],
          "prob_high_risk": preds[1],
          "car_crash_pred": "high_risk" if preds_singular[0] == 1 else "low_risk"}
        
        return rtn

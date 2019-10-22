import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import AllAnalyser as aan
import Analyser as an
def diverter (data,choice,filereports):
    q1=data
    if(choice=="all"):
        aan.analyse(data,filereports)
        exit()
    else:
        an.analyse(data,choice,filereports)
        exit()
       

   
    


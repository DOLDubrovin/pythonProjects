#/generation of the DF, using pandas, with HF as a main parameter. 
#//in each observation (obsID). THe Hf is dependent or not dependent from ater parameter
#// such as age (no dependence), sex (no dependence), EF (slightly increasing with a slope 2 revers direction)
#// NYHA dependent of EF with noise
#//HF (HFpEF (EF>55, HYHA 1), HFmrEF(EF=<55,>40), HFrEF (EF=<40)
#HR dependend of HF
#//othe parameter, that will be consedered: mean, SD, assymmetry
#%%         
import pandas as pd
import numpy as np

# %%
n=200   #//number of observations
Age=np.random.randint(18,90,n)#//weparate, becouse of use in Functions
Sex=np.random.choice(["M","F"],n)
EF=70-Age*0.4+np.random.normal(0,5,n)#//Vermutung: correlation with age, sd 5
NYHA_score=(5-EF/15+np.random.normal(0,0.5,n))
NYHA=np.clip(np.round(NYHA_score),1,4).astype(int)
HF=np.where((EF>55)&(NYHA==1), "no HF",
                  np.where ((EF>55), "HFpEF",
                  np.where ((EF>40), "HFmeEF", "HFrEF")))
HR=100-EF*0.8+np.random.normal(0,5,n) # HF empirisch
df1 = pd.DataFrame({
"ObservID":range(1, n+1),#//n+1 besouse the py built to n-1
"Age":Age,
"Sex":Sex,
"EF":EF,
"NYHA":NYHA,
"HF":HF,
"HR":HR
})
print(df1)
import pandas as pd
import numpy as np
n=200
Age=np.random.randint(18,90,n)
df1 = pd.DataFrame({
"PatintID":range(1, n+1),
"Age":Age,
"Sex":np.random.choice(["M","F"]),
"EF": 70-Age*0.4+np.random.normal(0,5,n),
"NYHA":np.random.choice([1,2,3,4],n)
})
print(df1)
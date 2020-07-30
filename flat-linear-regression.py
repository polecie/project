import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model



df = pd.read_excel('price1.xlsx')



get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.area, df.price, color='red', marker='^')
plt.xlabel('площадь (кв.м.)')
plt.ylabel('стоимость (млн.руб)')


reg = linear_model.LinearRegression()



reg.fit(df[['area']],df.price) 


reg.predict([[120]])


reg.predict(df[['area']])

# Y = aX + b

reg.coef_


reg.intercept_


# Стоимость = 0.07148238 * Площадь + 0.8111407046647887


0.07148238 * 120 + 0.8111407046647887


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.area, df.price, color='red', marker='^')
plt.xlabel('площадь (кв.м.)')
plt.ylabel('стоимость (млн.руб)')
plt.plot(df.area, reg.predict(df[['area']]))



pred = pd.read_excel('prediction_price.xlsx')



pred.head(3)



p = reg.predict(pred)



pred['predicted prices'] = p



pred.to_excel('new.xlsx', index=False)





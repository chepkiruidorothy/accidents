
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('US_Accidents.csv')
df.head()
cities_by_accidents = df['City'].value_counts()
print(cities_by_accidents[:10])
# cities_by_accident[:20].plot(kind='barh')

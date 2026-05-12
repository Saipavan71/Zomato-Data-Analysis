import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zomato.csv", encoding='latin1')

#print(df)

#print(df.head())

#print(df.info())

#print("\nNull values before cleaning:\n")
#print(df.isnull().sum())

df['Cuisines'] = df['Cuisines'].fillna('Unknown')

#print("\nNull values after cleaning:\n")
#print(df.isnull().sum())

top_cuisines = df['Cuisines'].value_counts().head(10)

#print("\nTop 10 Cuisines:\n")
#print(top_cuisines)

top_locations = df['Locality'].value_counts().head(10)

#print("\nTop 10 Restaurant Locations:\n")
#print(top_locations)

#print(df['Aggregate rating'])

average_rating = df['Aggregate rating'].mean()

#print("\nAverage Rating:\n")
#print(round(average_rating, 2))

# Top rated restaurants
top_rated = df[['Restaurant Name', 'Aggregate rating']].sort_values(
    by='Aggregate rating', ascending=False).head(10)

#print("\nTop Rated Restaurants:\n")
#print(top_rated)

# Online delivery analysis

online_delivery = df['Has Online delivery'].value_counts()

#print("\nOnline Delivery Availability:\n")
#print(online_delivery)

# Average rating based on online delivery

delivery_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()

#print("\nAverage Rating Based on Online Delivery:\n")
#print(delivery_rating)

# Average cost for two

average_cost = df['Average Cost for two'].mean()

#print("\nAverage Cost for Two:\n")
#print(round(average_cost, 2))

# Most expensive restaurants

expensive_restaurants = df[['Restaurant Name', 'Average Cost for two']].sort_values(
    by='Average Cost for two', ascending=False).head(10)

#print("\nMost Expensive Restaurants:\n")
#print(expensive_restaurants)

# Average cost by cuisine

cuisine_cost = df.groupby('Cuisines')['Average Cost for two'].mean().sort_values(ascending=False).head(10)

#print("\nMost Expensive Cuisines:\n")
#print(cuisine_cost)

# Top 10 cuisines visualization

top_cuisines = df['Cuisines'].value_counts().head(10)

top_cuisines.plot(kind='bar', figsize=(10,5))

plt.title('Top 10 Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Count')

plt.xticks(rotation=45)

plt.tight_layout()

#plt.show()

# Save cleaned dataset

df.to_csv("cleaned_zomato_data.csv", index=False)

print("Cleaned dataset saved successfully")


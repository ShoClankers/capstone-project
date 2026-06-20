
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("IMBD_DTSET.csv")


print("First 3 rows:")
print(df.head(3))


print("\nLast 3 rows:")
print(df.tail(3))


print("\nDataset Information:")
df.info()


print("\nNull Values in Dataset:")
print(df.isnull().sum())


subset_df = df.iloc[40:75]

print("\nSubset (Rows 41 to 75):")
print(subset_df)


highest_votes_movie = df.loc[df['Votes'].idxmax()]

print("\nMovie with Highest Votes:")
print(highest_votes_movie)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['IMDB_Rating'])
plt.title('Boxplot of IMDB Rating')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Runtime'])
plt.title('Boxplot of Runtime')

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.6)
plt.xlabel('Runtime')
plt.ylabel('IMDB Rating')
plt.title('Relationship Between Runtime and IMDB Rating')
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Runtime', y='IMDB_Rating', data=df)
plt.title('Runtime vs IMDB Rating')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['IMDB_Rating'], kde=True, bins=15)
plt.title('Distribution of IMDB Rating')
plt.xlabel('IMDB Rating')
plt.show()


plt.figure(figsize=(8, 5))
sns.histplot(df['Runtime'], kde=True, bins=15)
plt.title('Distribution of Runtime')
plt.xlabel('Runtime')
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(x='Rating', data=df, order=df['Rating'].value_counts().index)
plt.title('Number of Movies by Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


print("\nMovie Counts by Rating:")
print(df['Rating'].value_counts())
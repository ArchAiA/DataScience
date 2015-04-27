# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:50:55 2015

@author: david
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/drinks.csv')


# bar plot of number of countries in each continent
df.continent.value_counts().plot(kind='bar', title='Countries per Continent')
plt.xlabel('Continent')
plt.ylabel('Countries')
plt.show()
#plt.savefig('countries_per_continent.png')


# bar plot of average number of beer servings (per adult per year) by continent
df.groupby('continent').beer_servings.mean().plot(kind='bar', title='Mean Beer Servings per Continent')
plt.xlabel('Continent')
plt.ylabel('Beer Servings')
plt.show()
#plt.savefig('beer_servings_per_continent.png')


# histogram of beer servings (shows the distribution of a numeric column)
df.beer_servings.hist(bins=20)
plt.title('Distribution of Beer Servings')
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')
plt.show()


# density plot of beer servings (smooth version of a histogram)
df.beer_servings.plot(kind='density')
plt.title('Distribution of Beer Servings')
plt.xlabel('Beer Servings')
plt.show()


# grouped histogram of beer servings (shows the distribution for each group)
# this shows a histogram of beer_servings for each continent in a 
# separate chart
df.beer_servings.hist(by=df.continent)
plt.show()

df.beer_servings.hist(by=df.continent, sharex=True)
plt.show()

df.beer_servings.hist(by=df.continent, sharex=True, sharey=True)
plt.show()

df.beer_servings.hist(by=df.continent, sharey=True, layout=(2,3))
plt.show()


# boxplot of beer servings by continent (shows five-number summary and outliers)
df.boxplot(by='continent', column='beer_servings')

# scatterplot of beer servings versus wine servings
df.plot(kind='scatter', x='beer_servings', y='wine_servings', alpha=0.3)
plt.show()

# same scatterplot, except point color varies by 'spirit_servings'
# note: must use 'c=drinks.spirit_servings' prior to pandas 0.15.0
df.plot(kind='scatter', x='beer_servings', y='wine_servings', c='spirit_servings', colormap='Blues')
plt.show()







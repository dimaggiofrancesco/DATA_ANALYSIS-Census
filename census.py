import pandas as pd

census_df = pd.read_csv('census.csv')


# Question 5
# Which state has the most counties in it?

def answer_five():
    answer_5 = census_df[census_df['SUMLEV']==50].groupby("STNAME").size().idxmax()
    print ('ANSWER 5: The state with most counties in it is', answer_5)
answer_five()


# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of
# highest population to lowest population)? Use CENSUS2010POP.

def answer_six():
    answer_6 = census_df[census_df['SUMLEV']==50].groupby('STNAME')['CENSUS2010POP'].nlargest(3).sum(level=0).nlargest(3).index.tolist()
    print ('ANSWER 6: The three most populous states are', answer_6)
answer_six()


# Question 7
# Which county has had the largest absolute change in population within the period 2010-2015?
# (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# This function should return a single string value.

def answer_seven():
    census_filter = census_df[census_df['SUMLEV']==50]
    a = census_filter[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].T
    maximum = a.max()
    minimum = a.min()
    difference = abs(minimum-maximum).idxmax()
    answer_7 = census_filter['CTYNAME'].iloc[difference]
    print ('ANSWER 7: The county with the largest absolute change in population within the period 2010-2015 is', answer_7)
answer_seven()


# Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington',
# and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).

def answer_eight():
    a = census_df[(census_df['REGION']==2) | (census_df['REGION']==1)]
    b = a.loc[a['CTYNAME'].str.startswith('Washington', na=False)]
    c = b[b['POPESTIMATE2015']>b['POPESTIMATE2014']]
    answer_8 = c.loc[:,'STNAME':'CTYNAME'].sort_index(ascending=True)
    print ('ANSWER 8: The answer to question 8 is\n', answer_8)
answer_eight()


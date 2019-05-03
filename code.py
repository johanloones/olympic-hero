# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
#Code starts here
#Load the dataframe from the path using pd.read_csv() and store the dataframe in a variable called 'data'.
data=pd.read_csv(path)
print(data)
#In the dataframe, rename the column Total to Total_Medals
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data)
#Display first 10 records using "head()" function to take a look at the dataframe.
print(data.head(10))


# --------------
#Code starts here

#Create a new column Better_Event that stores 'Summer','Winter' or 'Both' based on the comparision between the total medals won in Summer event and Winter event 
#(i.e. comparision between the Total_Summer and Total_Winter columns) using "np.where()"function.
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',(np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')))

#Find out which has been a better event with respect to all the performing countries by using value_counts() function and 
#store it in a new variable called 'better_event'.
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
#Create a new dataframe subset called 'top_countries' with the columns ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] only
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
print(top_countries)
#Drop the last row from 'top_countries'(The last row contains the sum of the medals)
top_countries.drop(top_countries.tail(1).index,axis=0,inplace=True)
print(top_countries)
#Create a function called 'top_ten' that:
#Takes the dataframe 'top_countries' and a column name as parameters.
def top_ten(x,y):
  
  #Creates a new empty list called 'country_list'
  country_list=[]
  
  #Find the top 10 values for that particular column(for e.g. 'Total_Summer') using "nlargest()" function
  #From the dataframe returned by nlargest function, slices the Country_Name column and stores it in the 'country_list' list
  country_list=x.nlargest(columns=y,n=10).Country_Name
  
  #Returns the 'country_list'
  print(country_list)
  return country_list

#Call the 'top_ten()' function for the three columns :Total_Summer,Total_Winter and Total_Medals and 
#store their respective results in lists called 'top_10_summer', 'top_10_winter' and 'top_10'
top_10_summer=list(top_ten(top_countries,'Total_Summer'))
#top_10_summer=top_ten(x=top_countries,y=['Total_Summer'])
top_10_winter=list(top_ten(top_countries,'Total_Winter'))
top_10=list(top_ten(top_countries,'Total_Medals'))

#Create a new list 'common' that stores the common elements between the three lists('top_10_summer', 'top_10_winter' and 'top_10')
common=list((set(top_10_summer)) & (set(top_10_winter)) & (set(top_10)))
print(common)


# --------------
#Code starts here
#Take the three previously created lists(top_10_summer, top_10_winter, top_10)

#Subset the dataframe 'data' based on the country names present in the list top_10_summer using "isin()" function on the column 
#Country_Name. Store the new subsetted dataframes in 'summer_df'. Do the similar operation using top_10_winter and top_10 and store 
#the subset dataframes in 'winter_df' & 'top_df' respectively.
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

#Take each subsetted dataframe and plot a bar graph between the country name and total medal count according to the event 
#(For e.g. for 'summer_df' plot a bar graph between Country_Name and Total_Summer)
#Modify the axes info accordingly.

fig,(ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1,figsize=(10,15))
plt.tight_layout(pad=10, h_pad=None, w_pad=None, rect=None)
# Bar Plot  Country_Name and Total_Summer for summer_df
ax1.bar(summer_df['Country_Name'],height=summer_df['Total_Summer'])
ax1.set_xlabel('Country Name')
ax1.set_ylabel('Medal Count')
ax1.tick_params(axis='x',rotation=90)
ax1.set_title('Country Summer Medals Count')

# Bar Plot  Country_Name and Total_Winter for winter_df
ax2.bar(winter_df['Country_Name'],height=winter_df['Total_Winter'])
ax2.set_xlabel('Country Name')
ax2.set_ylabel('Medal Count')
ax2.tick_params(axis='x',rotation=90)
ax2.set_title('Country Winter Medals Count')

# Bar Plot  Country_Name and Total_Medal for top_df
ax3.bar(top_df['Country_Name'],height=top_df['Total_Medals'])
ax3.set_xlabel('Country Name')
ax3.set_ylabel('Medal Count')
ax3.tick_params(axis='x',rotation=90)
ax3.set_title('Country Total Medals Count')


# --------------
#Code starts here
#In the dataframe 'summer_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after 
#dividing the two columns Gold_Summer  and Total_Summer. Find the max value of Golden_Ratio and the country associated with it 
#and store them in summer_max_ratio and summer_country_gold respectively.
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=str(list(summer_df['Country_Name'][summer_df['Golden_Ratio'] == summer_max_ratio])[0])
print(summer_max_ratio,summer_country_gold,summer_df.head(5))

#In the dataframe 'winter_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after 
#dividing the two columns Gold_Winter and Total_Winter. Find the max value of Golden_Ratio and the country associated with it 
#and store them in 'winter_max_ratio' and 'winter_country_gold' respectively.
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=str(list(winter_df['Country_Name'][winter_df['Golden_Ratio']== winter_max_ratio])[0])
print(winter_max_ratio,winter_country_gold,winter_df.head(5))

#In the dataframe top_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after 
#dividing the two columns Gold_Total and Total_Medals. Find the max value of Golden_Ratio and the country associated with it 
#and store them in top_max_ratio' and 'top_country_gold' respectively.
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=str(list(top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio])[0])
print(top_max_ratio,top_country_gold,top_df.head(5))


# --------------
#Code starts here
#Drop the last row from the dataframe(The last row contains the total of all the values calculated vertically) 
#and save the result in 'data_1'
data_1=data.drop(data.tail(1).index,axis=0)
print(data_1)

#Update the dataframe 'data_1' to include a new column called Total_Points which is a weighted value where each 
#gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point.(i.e. You need to take weighted 
#value of Gold_Total, Silver_Total and Bronze_Total)
data_1['Total_Points']=data_1['Gold_Total'].apply(lambda x:x*3)+data_1['Silver_Total'].apply(lambda x:x*2)+data_1['Bronze_Total'].apply(lambda x:x*1)

#Find the max value of Total_Points in 'data_1' and the country assosciated with it and store it in variables 'most_points' 
#and 'best_country' respectively.
most_points=data_1['Total_Points'].max()
best_country=str(list(data_1['Country_Name'][data_1['Total_Points']==most_points])[0])
print(data_1.head(5),most_points,best_country)


# --------------
#Code starts here
#Create a single row dataframe called 'best' from 'data' where value of column Country_Name is equal to 'best_country'
#(The variable you created in the previous task)
#list(pd.Series(best_country))
best=data[data['Country_Name'].isin(list(pd.Series(best_country)))]
#Subset 'best' even further by only including the columns : ['Gold_Total','Silver_Total','Bronze_Total']
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
#Create a stacked bar plot of 'best' using "DataFrame.plot.bar()" function
best.plot.bar(stacked=True)
#Name the x-axis as United States using "plt.xlabel()"
plt.xlabel('United States')
#Name the y-axis as Medals Tally using "plt.ylabel()"
plt.ylabel('Medals Tally')
#Rotate the labels of x-axis by 45o using "plt.xticks()"
plt.xticks(rotation=45)



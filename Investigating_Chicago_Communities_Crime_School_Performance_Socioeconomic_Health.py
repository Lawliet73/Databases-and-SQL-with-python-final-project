import sqlite3
import pandas as pd
from tabulate import tabulate


import os
# Set the working directory
os.chdir("C:/Users/kalab/OneDrive/Desktop/py4e/python first programms/dataanalysis IBM/Databases and SQL with python final project")
print("Current Working Directory:", os.getcwd())  # Check if the working directory is correct

#read csv files using pandas and load  into a dataframe(eg. d1=dataframe 1)
d1= pd.read_csv("ChicagoCensusData.csv")
d2= pd.read_csv("ChicagoCrimeData.csv")
d3= pd.read_csv("ChicagoPublicSchools.csv")

#checks if read correctly and dataframes established
#print("Census data table:",d1.head())
#print("\n\nCrime data table",d2.head())
#print("\n\n Public school data",d3.head())


#estabilish a connection to sqlite DB and create a cursor
conn = sqlite3.connect('FinalDB.db')
cur = conn.cursor()

#load the data from the csv files into a table respectively
d1.to_sql("Census_Data",conn,if_exists="replace",index=False)

d2.to_sql("Chicago_Crime_Data",conn,if_exists="replace",index=False)

d3.to_sql("Chicago_Public_schools",conn,if_exists="replace",index=False)


#read the stored data from the SQLite db into a Dataframe

df1= pd.read_sql("SELECT * From Census_Data",conn)
df2= pd.read_sql("SELECT * From Chicago_Crime_Data ",conn)
df3= pd.read_sql("SELECT * From Chicago_Public_schools",conn)

#checks if uploaded correctly and dataframes established
#print ("Uploaded Census data table:",df1.head())
#print("\n\nUploaded Crime data table",df2.head())
#print("\n\n Uploaded Public school data",df3.head())

#Quick overview of data
#print ("OVerview Census data table:",df1.describe())
#print("\n\nOverview Crime data table",df2.describe())
#print("\n\n Overview Public school data",df3.describe())


#core facts



#total number of crimes
#most crime prone areas
#area with most number of crime
noc= '''select count(DISTINCT(CASE_NUMBER)) From Chicago_Crime_Data;'''
cpa= '''SELECT COMMUNITY_AREA_NUMBER FROM Chicago_Crime_Data GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(CASE_NUMBER) DESC LIMIT 1;
'''
amc= '''SELECT CENSUS.COMMUNITY_AREA_NAME, COUNT(CRIME.CASE_NUMBER) AS number_of_crimes
FROM Census_Data CENSUS JOIN Chicago_Crime_Data CRIME ON CENSUS.COMMUNITY_AREA_NUMBER = CRIME.COMMUNITY_AREA_NUMBER
WHERE CRIME.COMMUNITY_AREA_NUMBER = (SELECT COMMUNITY_AREA_NUMBER FROM Chicago_Crime_Data GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(CASE_NUMBER) DESC LIMIT 1)
GROUP BY CENSUS.COMMUNITY_AREA_NAME;'''

cur.execute(noc)
output_noc = cur.fetchall()

cur.execute(cpa)
output_cpa = cur.fetchall()

cur.execute(amc)
output_amc = cur.fetchall()

# Fetch column headers after each query
columns_noc = [description[0] for description in cur.description]  # For noc
cur.execute(cpa)  # Execute again to fetch column headers for cpa
columns_cpa = [description[0] for description in cur.description]  # For cpa
cur.execute(amc)  # Execute again to fetch column headers for amc
columns_amc = [description[0] for description in cur.description]  # For amc

#singular value
print("\n\n\n number of crimes \n\n\n", output_noc[0])
#tables
print("\n\n\n Most crime prone area (Community Area Numbers)",tabulate(output_cpa, headers=columns_cpa, tablefmt="pretty"))
print("\n\n\n most recorded crimes in an area",tabulate(output_amc, headers=columns_amc, tablefmt="pretty"))



#alternatively also in panda possible E.g.
#-community area names and numbers with per capita income less than 11000
s1='''SELECT DISTINCT COMMUNITY_AREA_NAME, COMMUNITY_AREA_NUMBER From Census_Data WHERE PER_CAPITA_INCOME<11000;
'''
dfs1 = pd.read_sql_query(s1, conn)
print("\n\n\n Areas where PER_CAPITA_INCOME<11000 \n\n\n",tabulate(dfs1, headers='keys', tablefmt='grid'))

#- community areas with highest% of households below poverty line
s2='''Select COMMUNITY_AREA_NAME From Census_Data ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5;
'''
dfs2 = pd.read_sql_query(s2, conn)
print("\n\n\n areas with highest percent of households below poverty line \n\n\n",tabulate(dfs2, headers='keys', tablefmt='grid'))
#- community area with highest hardship indices
s3='''SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX From Census_Data where HARDSHIP_INDEX = ( Select max(HARDSHIP_INDEX) FROM Census_Data); 
'''
dfs3 = pd.read_sql_query(s3, conn)
print("\n\n\n areas with highest hardship indices \n\n\n",tabulate(dfs3, headers='keys', tablefmt='grid'))


#crimes involving children
s4='''SELECT CASE_NUMBER From Chicago_Crime_Data where DESCRIPTION in ('SELL/GIVE/DEL LIQUOR TO MINOR', 'ILLEGAL CONSUMPTION BY MINOR');
'''
dfs4 = pd.read_sql_query(s4, conn)
print("\n\n\n crimes involving children \n\n\n",tabulate(dfs4, headers='keys', tablefmt='grid'))

#kidnapping involving a child
s5='''SELECT CASE_NUMBER,date FROM Chicago_Crime_Data WHERE Primary_Type = 'KIDNAPPING' AND Description = 'CHILD ABDUCTION/STRANGER'; 
'''
dfs5 = pd.read_sql_query(s5, conn)
print("\n\n\n kidnapping involving a child \n\n\n",tabulate(dfs5, headers='keys', tablefmt='grid'))

#types of crimes recorded at school
s6='''SELECT DISTINCT PRIMARY_TYPE From Chicago_Crime_Data WHERE LOCATION_DESCRIPTION like "%SCHOOL%";
'''
dfs6 = pd.read_sql_query(s6, conn)
print("\n\n\n types of crimes recorded at school \n\n\n",tabulate(dfs6, headers='keys', tablefmt='grid'))

#average saftey score for diffrent type of schools
s7='''SELECT "Elementary, Middle, or High School", avg(SAFETY_SCORE) From Chicago_Public_schools GROUP BY "Elementary, Middle, or High School";
'''
dfs7 = pd.read_sql_query(s7, conn)
print("\n\n\n average saftey score for diffrent type of schools \n\n\n",tabulate(dfs7, headers='keys', tablefmt='grid'))










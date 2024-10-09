# Project Title: Crime and Census Data Analysis Using Python and SQLite

## Table of Contents
- [Description](#Description)
- [Data Sources](#Data-Sources)
- [Prerequisites](#Prerequisites)
- [Steps](#Steps)
- [Example_Queries_Executed](#Example-Queries-Executed)
- [Pros and Cons of Using Pandas vs. Python Directly for Queries](#Pros-and-Cons-of-Using-Pandas-vs-Python-Directly-for-Queries)
- [Conclusion](#Conclusion)
- [Author](#Author)

## Description
This project involves reading CSV files containing data about Chicago Census, Crime Data, and Public Schools, then performing SQL queries for data analysis using Python. The data is first loaded into a SQLite database, queried using Python, and the results are read into pandas DataFrames for further manipulation and structured output. The analysis focuses on identifying key insights such as crime statistics, socio-economic conditions, and school safety in different areas of Chicago.

## Data Sources
- Chicago Census Data: Socio-economic data for various community areas in Chicago.
- Chicago Crime Data: Crime statistics for Chicago, including case numbers, locations, and types of crimes.
- Chicago Public Schools: Information about public schools in Chicago, including safety scores.

## Prerequisites
You need the following Python libraries installed:

- pandas: For reading and manipulating the data.
- sqlite3: For database management.
- tabulate: For pretty-printing tables.
  
Install any missing libraries with pip:
```pip install pandas sqlite3 tabulate```

## Steps
1. Set the Working Directory
The script sets the working directory to the location where the CSV files are stored.

2. Read CSV Files
Using pandas, the CSV files are loaded into DataFrames (d1, d2, d3) representing Census, Crime, and Public Schools data, respectively.

3. SQLite Connection
A connection to a SQLite database is established, and a cursor object is created to execute SQL queries.

4. Upload Data to SQLite
The CSV data is written to SQLite tables using the to_sql() function, creating the following tables:

- Census_Data
- Chicago_Crime_Data
- Chicago_Public_schools
- SQL Queries and Output

5. The script executes a series of SQL queries to extract meaningful insights, such as:

- Total number of crimes.
- Most crime-prone areas.
- Areas with the highest number of crimes.
- Socio-economic insights (e.g., areas with low per capita income or high hardship index).
- Crimes involving children.
- Crime types recorded at schools.
- Average safety scores for different types of schools.

6. Reading Results into Pandas
The results of the SQL queries are read into pandas DataFrames using the pandas.read_sql_query() function. This allows further manipulation and clean tabular display of the results.

7. Tabular Output
The results are formatted and printed as tables using the tabulate() library, making the output easy to read.

## How to Run
1. Clone the repository or copy the Python script.
2. Ensure you have the necessary CSV files in the working directory:
- ChicagoCensusData.csv
- ChicagoCrimeData.csv
- ChicagoPublicSchools.csv
3. Run the script:
```python analysis_script.py```

## Example Queries Executed:

- Total Number of Crimes
  
 ```SELECT COUNT(DISTINCT CASE_NUMBER) FROM Chicago_Crime_Data;```

- Most Crime-Prone Area

 ```SELECT COMMUNITY_AREA_NUMBER FROM Chicago_Crime_Data GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(CASE_NUMBER) DESC LIMIT 1;```

- Crimes Involving Children

 ```SELECT CASE_NUMBER FROM Chicago_Crime_Data WHERE DESCRIPTION IN ('SELL/GIVE/DEL LIQUOR TO MINOR', 'ILLEGAL CONSUMPTION BY MINOR');```

- Kidnapping Involving a Child

 ```SELECT CASE_NUMBER, date FROM Chicago_Crime_Data WHERE Primary_Type = 'KIDNAPPING' AND Description = 'CHILD ABDUCTION/STRANGER';```

- Average Safety Score for Schools

 ```SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) FROM Chicago_Public_schools GROUP BY "Elementary, Middle, or High School";```

## Pros and Cons of Using Pandas vs. Python Directly for Queries

### Python Directly with SQLite Queries
Pros:

 - Efficiency: SQL is highly efficient for querying and filtering large datasets directly from the database without loading everything into memory.
 - Control: You have more control over how queries are executed and can take advantage of SQL optimization.

Cons:

 - Limited Flexibility: While SQL is powerful for querying, once you get the results, additional manipulations (e.g., data analysis, statistical operations) might require further code in Python.

### Pandas for Reading and Displaying Results
Pros:

 - Easy to Manipulate: After querying the database, pandas makes it easy to handle and manipulate the result set.
 - Readability: DataFrames offer a clean and structured way to display data, especially with built-in methods like .head(), .describe(), and integration with libraries like tabulate for clean table output.
 - Rich Features: Pandas provides numerous built-in functions for analysis, including statistical functions and advanced data transformations.

Cons:

 - Memory Usage: If you're dealing with very large datasets, loading query results into pandas DataFrames could consume significant memory.
 - Less Efficient for Large Datasets: For extremely large datasets, it may be less efficient than directly querying and manipulating the data with SQL.

## Conclusion
This project demonstrates how to analyze real-world data using a combination of Python and SQL for querying, while using pandas for further data handling and visualization. Depending on the dataset size and task, you can decide whether to rely more on SQL for efficiency or on pandas for flexibility and ease of manipulation.

## Author
Kalab Alemayehu

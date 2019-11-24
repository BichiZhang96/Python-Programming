import logging
import pandas as pd
import matplotlib.pyplot as plt
import pylab

logging.basicConfig(filename='Assignment9.log', level=logging.DEBUG)


try:
    movies=pd.read_csv('IMDB-Movie-Data.csv',sep=',')  # read the input csv file
    movies.set_index('Title',inplace=True)  # inplace=True means change the info in the dataframe without creating a new one
    print("The first five rows of the dataframe:\n" , movies.head(),"\n")
    print(movies.info(),"\n")
    print("The column names of my dataset:\n",movies.columns,"\n")
    movies.rename(columns={'Revenue (Millions)':'Revenue','Runtime (Minutes)':'Runtime'},inplace=True)  # use rename function and inplace=True
    print("The new column names of my dataset:\n",movies.columns,"\n")
    print("The average runtime:",movies['Runtime'].mean(),"\n")  # get the average by using mean()
    print("The average revenue:",movies['Revenue'].mean(),"\n")
    print("The longest movie in the dataset:\n",movies.loc[movies['Runtime'].idxmax()],"\n")  # use idxmax to get the index rather than the duration
    print("The shortest movie in the dataset:\n",movies.loc[movies['Runtime'].idxmin()],"\n")
    print("The total number of null values in each column:\n",movies.isnull().sum(axis=0),"\n")  # use isnull().sum(axis=0) to get the number of null values in each column
    print("The Genre has the maximum number of movies in the dataset:\n",
          movies['Genre'].value_counts().idxmax(),movies['Genre'].value_counts().max(),"\n")  # idxmax and max to get the different data
    print("The total number of movies in each Genre:\n",movies['Genre'].value_counts(),"\n")  # use value_counts to get clean data, group by will get the data with all the info with the movies
    movies_new=movies[['Rating','Genre']]  # create a new dataframe to store the two columns
    print("The new dataframe:",movies_new,"\n")
    print('All the movies directed by "Christophe Lourdelet":\n',movies[movies.Director=='Christophe Lourdelet'],'\n')  # condition
    print("All the movies rating above 8.0:\n",movies[movies.Rating>8.0],"\n")
    print("All the movies that were released between 2008 and 2014 and have a rating above 8.5:\n",
          movies[(movies.Rating>8.5) & (movies.Year>=2008) & (movies.Year<=2014)],"\n")
    scatter_plot=plt.figure()  # create a scatter plot
    axes1=scatter_plot.add_subplot(1,1,1)
    axes1.scatter(movies['Rating'],movies['Revenue'])
    axes1.set_title('The relationship between ratings and revenue')
    axes1.set_xlabel('Rating')
    axes1.set_ylabel('Revenue')
    scatter_plot.show()
    pylab.show()  # can not show the figure without this line in my laptop


except FileNotFoundError:
    print("Could not find the input file!")
    logging.info('Could not find the input file!')

except Exception:
    print("An unexpected error occurred")
    logging.info('An unexpected error occurred')


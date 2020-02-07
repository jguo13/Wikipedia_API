 ## Wikipedia API Demo

 ##Requirements: Run pip install wikipedia and pip install pandas to insure you have the wikipedia library downloaded
import wikipedia
import pandas as pd

##Query 1: finding out more about Hamilton, this returns a list of search results.
## There are three possible arguments, the first is the search parameter, the second
## is a limit on the number of results that can show on a page, and the last is a boolean to 
## turn on and off auto-suggestions
search_param = "Hamilton"
num_results = 100
print(wikipedia.search("Hamilton", results = num_results, suggestion = True))

## Query 2: finding wikipedia articles related to longitude and latitude 
## coordinates. These coordinates for example are from a california earthquake
## returns a list of results markes as within 10,000 m, which is also the upper bound of the radius parameter
latitude = 35.3400
longitude = -120.1900
print(wikipedia.geosearch(latitude, longitude, radius = 10000))


#Query 3: Opening up a wikipedia page, and then you can access features in the WikipediaPage
## object like the content (a full printout of the entire page) or images, a list of all the image urls in that page
Columbia_University = wikipedia.WikipediaPage("Columbia University")
# print(Columbia_University.content)
# print(Columbia_University.images)

##with these queries, you can build cool datasets like the following, where you can get a csv of wikipedia articles that happen around earthquake coordinates:

latitude_list = [37.86319, 51.272222222222, 3.244, 18.513815, -40.8158]
longitude_list = [-122.25365, 30.224166666667, 95.825, -72.288193, -72.0028]
radius_list = []
for i in range(0, len(latitude_list)):
	radius_list.append(wikipedia.geosearch(latitude_list[i], longitude_list[i], results = 500, radius = 10000))

radius_summ = []
for i in radius_list:
	for j in i:
		page = wikipedia.WikipediaPage(j)
		radius_summ.append([j, page.summary])

radius_df = pd.DataFrame(radius_summ, columns = ["Name", "Summary"])
radius_df.to_csv("earthquake_hotspots.csv")

# Wikipedia API Profile
The Wikipedia api is a great free api that allows access to all wikipedia articles. There is also a Python library dedicated to making the wikipedia api easier to use with python programming. This library in python is called "wikipedia," so please ensure you have preinstalled it (most easily done by just running `pip install wikipedia` on a terminal)

There are very few restrictions on the API: No need to pay and no need for an apikey. You can retrieve 50 wikipedia pages with every api request.

To read more extensive documentation on the python library wikipedia, visit this url: <https://wikipedia.readthedocs.io/en/latest/code.html>

To read more extensive documentation on the api in general that the library wraps around, visit this url: <https://en.wikipedia.org/w/api.php>

======
## Setup
### Set up your environment
You will need to install the wikipedia library within python. This is most easily done by using python's package manager, pip, through the command `pip install wikipedia`. In addition to wikipedia library, we will be using pandas, a library which makes it very easy to handle data and to write csv files. You can download this library with the command: `pip install pandas`. 
Once this is done, you will need to import those libraries into your python program as so:
```
import wikipedia
import pandas as pd
```

And that's it you're done!

## Example API Queries
### Query 1
This query will walk you thorugh searching wikipedia for the term "Hamilton." There are three possible parameters:
1. query : this is the only required parameter, which means you must add it in every time you call this function. It's just a string, so anything you might put into a wikipedia search you can put here!
2. results = 10 : This is an optional result that will cap the number of results returned in your list. NOTE that the maximum you can set this to is 500. In my example query I did 100 so that my program did not need to be overwhelmed with too much data. The default is 10, if you do not explicitly set it, it will just return a max of ten results.
3. suggestion = True : This boolean value is defaulted to false. If you explicitly set it to True, it will add Wikipedia's auto-suggestions to your list of results in addition to your own matched results. I set it to True because I am bad at spelling and this is nice insurance against typos. 

```
search_param = "Hamilton"
num_results = 100
print(wikipedia.search(search_param, results = num_results, suggestion = True))
```

The above code then prints out all the results. Here is the output:
['Hamilton', 'Alexander Hamilton', 'Hamilton (musical)', 'Linda Hamilton', 'Lewis Hamilton', 'Hamilton, Ontario', 'James Hamilton, Marquess of Hamilton', 'Burr–Hamilton duel', 'Hamilton West, Hamilton, Scotland', 'Hamilton Hamilton', 'Anthony Hamilton', 'Richard Hamilton (basketball)', 'George Hamilton (actor)', 'Elizabeth Douglas-Hamilton, Duchess of Hamilton', 'Leonard Hamilton', 'Josh Hamilton', 'Margaret Hamilton', 'William Hamilton, Duke of Hamilton', 'Carrie Hamilton', 'Hamilton, New Zealand', 'Hamilton, Bermuda', 'Hamilton (album)', 'Nina Douglas-Hamilton, Duchess of Hamilton', 'Peter F. Hamilton', 'Alexander Douglas-Hamilton, 16th Duke of Hamilton', 'Margaret Hamilton (software engineer)', 'Natasha Hamilton', 'Mark Hamilton', 'Holly Hamilton', 'Arthur Hamilton, Lord Hamilton', 'Hamilton Morris', 'Hamilton College', 'Hamilton Academical F.C.', 'James Hamilton, Viscount Hamilton', 'Kim Hamilton', 'Erin Hamilton', 'Hamilton High School (Hamilton, Ohio)', 'Victoria Hamilton', 'Margaret Hamilton (actress)', 'Nicholas Hamilton', 'Duke of Hamilton', 'Scott Hamilton (figure skater)', 'Elizabeth Schuyler Hamilton', 'Hamilton Watch Company', 'Tom Hamilton (musician)', 'Pep Hamilton', 'Argus Hamilton', 'Hamilton Standard', 'Hamilton, New Jersey', 'Laird Hamilton', 'Hamilton Bulldogs', 'David Hamilton (photographer)', 'Ashley Hamilton', 'Booz Allen Hamilton', 'Bernie Hamilton', 'Hamilton–Reynolds affair', 'Andy Hamilton', 'Nicolas Hamilton', 'Hamilton, Mississippi', 'Laura Hamilton', 'Alana Stewart', 'Guy Hamilton', 'Ethan Hamilton', 'LisaGay Hamilton', 'Emma Walton Hamilton', 'Hamilton High School (Hamilton, Alabama)', 'Dunblane massacre', 'Arlan Hamilton', 'Sophie Douglas-Hamilton, Duchess of Hamilton', 'Kipp Hamilton', 'Hamish Hamilton', 'Hamilton High School (Hamilton, Illinois)', 'Alexander Hamilton Jr.', 'Jim Hamilton (rugby union)', 'Sherman Hamilton', 'Bethany Hamilton', 'Susan Hamilton, Duchess of Hamilton', 'Hamilton Hughes', 'Gay Hamilton', 'Emma, Lady Hamilton', 'Albert Fish', 'Ian Hamilton', 'Lynn Hamilton (actress)', 'Archie Hamilton', 'Philip Hamilton', 'Filippa Hamilton', 'Neil Hamilton (actor)', 'Hamilton Sundstrand', 'Anthony Hamilton (musician)', 'Hamilton (name)', 'Dougie Hamilton', 'Hamilton County', 'James Hamilton, 7th Duke of Hamilton', 'Murray Hamilton', 'Christine Hamilton', 'George Hamilton-Gordon', 'Alexander Hamilton (disambiguation)', 'Hamilton Pool Preserve', 'James Hamilton, 2nd Marquess of Hamilton', 'Charles Hamilton']

### Query 2
This query will walk you through searching for a wikipedia page by geography, namely latitude and longitude coordinates. There are 5 parameters:
1. latitude: this is the latitude you are searching for (this is a required parameter you must set it)
2. longitude: this is the longitude you are searching for (this is a required parameter you must set it)
3. title = None: you can add an additional title parameter to search for. For this query I did not set this since I wanted to put in a blind search for the coordinates of an earthquake. (this is optional, the default is None)
4. results = 10: This is the maximum number of results to return. The max value of this is the same as the search function, ie. 500.
5. radius = 1000: This is the radius with which wikipedia will pull results based on the coordinates you give it and it is in meters. The min is 10 and the max is 10000. I've set it to the max in this example to try and get as many results as possible

```
latitude = 35.3400
longitude = -120.1900
print(wikipedia.geosearch(latitude, longitude, radius = 10000))
```

Here is the output: ['La Panza, California', 'La Panza Canyon', 'La Panza Range']

## Query 3
Now that we have all the search results, we can retrieve the actual page and all its classes. The  most important parameter, and the only required parameter, is just the title, which you can set as a string. Here we pull up the page for Columbia University. 

```
Columbia_University = wikipedia.WikipediaPage("Columbia University")
```
## Putting it all together!
Now that you have these three functions we can build a simple python program that inputs a list of past earthquakes and searches for wikipedia pages marked within a 10,000 m radius of that location. Once we have a list of the search results, we pull up the pages and access the class "summary" (which is a summary of the wiki page), and then we gather all these page summaries and save it to a csv called "earthquake_hotspots.csv"
```
latitude_list = [37.86319, 51.272222222222, 3.244, 18.513815, -40.8158]
longitude_list = [-122.25365, 30.224166666667, 95.825, -72.288193, -72.0028]
radius_list = []
```
In the above code, we are building up all the lists we will need. The first is a list of latitudes, the second a list of longitudes. NOTE you must make sure that each index of the two lists corresponds to the same event. For example, if you have an event that occured at 37.86319, -122.25365, you're going to want to just make sure that where you put these two coordinates in the two seperate list is in the same position. Like if you put the latitude coordinate first in the latitude list, make sure to put the corresponding longitude coordinate first as well.

The radius_list is initialized to be empty right now because later we will use it to store our search results.

```
for i in range(0, len(latitude_list)):
	radius_list.append(wikipedia.geosearch(latitude_list[i], longitude_list[i], results = 500, radius = 10000))
```

In the above code, we run a search for every coordinate in the latitude, longitude list, and append the search result names to the radius_list. We will then use these search results in the next part of code to retrieve the results. 

```
radius_summ = []
for i in radius_list:
	for j in i:
		page = wikipedia.WikipediaPage(j)
		radius_summ.append([j, page.summary])
```
In the above code, we initalize an empty list once again, called radius_summ. In this list we will store all our returned page summaries. Then, we create a nested for-loop: In the outer for loop you go over every result in the radius_list, and then because some of the entries in radius_list are themselves list (for example some coordinates turned up just one result while some returned several) we have to then iterate over that inner layer of list. Then we just append each summary into the radius_sum list.

```
radius_df = pd.DataFrame(radius_summ, columns = ["Name", "Summary"])
radius_df.to_csv("earthquake_hotspots.csv")
```

The last step is also the easiest! just go ahead and convert the list into a pandas dataframe (just another data structure which we use mainly bc it has a very easy built in function for csv conversion). Then, you can save it to a csv file. You can give it any name you want, here I chose the name "earth_quake_hotspots.csv." It will be saved in parallel to your python file. And you're done! You can even take this further and create a bot (wikipedia is bot friendly) that can auto generate these results, or even combs pages to try to catch when a major change has been made. (For example, did someone post something crazy on the Trump page?)


======
## Log
1. I started by visiting the installation page for wikipedia:
<https://pypi.org/project/wikipedia/>
2. Then, I ran `pip install` on my local terminal in order to ensure I had the library set up.
3. Then I started reading the documentation, and realized happily that we do not need an api key or any sort of authorization protocol (Note: you do need access tokens to modify wikipedia pages, but most likely if you are reading this you do not need that ability). There is a general etiquitte not to bog down the api with too many requests, and if you need to do exactly that follow the following instructions to contact the wiki api admistrators: <https://www.mediawiki.org/wiki/API:FAQ#Where_can_I_get_more_help?>
4. Then I started playing around with some functions. I found the search, geosearch, and WikipediaPage functions nost powerful, and so I started thinking about the Quakebot and how that auto-generates articles based on earthquake reports. I started to think that a bot that could similarly pull like "entities" that surround a given earthquake coordinate would also be useful to journalists, and so I started to play around with that idea.
5. I looked up an earthquake coordinate, and found that wikipedia could return results that are very closely related to that region. For example, when I gave it the coordinates of an earthquake in southern california, it returned three results all related to La Panza, California, which is where the earthquake happened. From these results I was able to realize that there is actually a canyon there (one of the results is "La Panza Canyon"), implying that this could be on top of a major fault line. 
6. I ran into some issues trying to understand what some of the parameters of the functions did, for example it wasn't very clear to me what the maximum return results could be set as, and the python wikipedia page library was a little lacking in those details. But, I realized that it was really just a wrapper for the rest apis so I found the answers I couldn't on the python documentation page on the original wikipedia api page. 
5. Finally I settled on saving the final output as a csv, and chose to do a quick conversion to a pandas dataframe to do so since a csv would be easy to read and open and manipulate for a journalist. 



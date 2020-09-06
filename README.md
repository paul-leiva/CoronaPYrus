# CoronaPYrus
 ***A program that displays the distribution of COVID-19 cases among the 10 countries with the most cases relative to the rest of the world.***

## Installation Instructions:
#### External/3rd Party Downloads:
-This project makes use of `selenium`. So, you will need to download the latest version of the [Google Chrome WebDriver (ChromeDriver)](https://chromedriver.chromium.org/downloads). If you are on a Windows machine, unzip the file and move chromedriver.exe to your "Program Files (x86)" folder; if you do this, you shouldn't have to touch the code. Otherwise, you will have to explicitly declare/modify the `PATH` based on what you did. (`PATH = "C:\Program Files (x86)\chromedriver.exe"`) If you are on a macOS, then you should unzip the file and take `chromedriver.exe` and put it in your `/usr/local/bin` directory, and `selenium` will default to using that directory. No explicit `PATH` should be necessary.
#### Python Libraries You Will Need to Install
- BeautifulSoup (`pip install beautifulsoup4`)
- selenium (`pip install selenium`)
- matplotlib (`pip install matplotlib`)
<br>**NOTE**: In order to install BeautifulSoup and for this program to work, you **MUST** be using a version of Python3. If you are using Python2, this program will probably not work.

## How to Run this Program:
There is only 1 file to be executed in this repository, which is `CoronaPYrus.py`.
1. Open up a terminal and change to the directory of the `CoronaPYrus.py` file.
2. Once in the directory, execute `python CoronaPYrus.py` or `python3 CoronaPYrus.py` (use `python3` if you have not defaulted your machine to use Python3 instead of Python2.)
![command](/command.png?raw=true)
3. Your pie graph should then be displayed. (Slice colors are randomly assigned)
![Graph](/Graph.png?raw=true)
4. Close the window to terminate the program.

## How this Program Works
1. The program will fetch the total amount of cases and the cases associated with each country from [this site from the World Health Organization (WHO)](https://covid19.who.int/table). The site has dynamically-loaded JavaScript, thus that is the reason why we must use `selenium` and not just the `requests` library. We must use `selenium` to open the site in Google Chrome in automated fashion and then parse the page's code.
![WHOpage](/WHOpage.png?raw=true)
2. The table data is fetched by row. However, since we are only concerned with the 10 countries with the most cases, we will only be dealing with the first 10 rows that are fetched. (Technically, rows 1-10 because row 0 contains arbitrary data when it is retrieved.)
3. We then take the cases for each country and divide by the total number of cases. Add those cases to a list (`case_counts`) and add the country name to another list (`countries`).
4. After we extract the data from the top 10 countries, the remaining amount of cases is associated with the rest of the world, and this data is appended to each respective list.
5. A pie chart of the percentage and cases is displayed.

## Known Bugs and Issues
Small slices of the pie graph can have their percentages "bunched up" or placed very close together.

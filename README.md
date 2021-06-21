# Web-Scraping-IC
The code available on this repository is intended to download the most recent version of the Padrão TISS documentation, which describes how health insurance plans data may be transferred digitally.<br />
<br />
## Requirements
To properly run [**web-scraper.py**](https://github.com/victoraavila/Web-Scraping-IC/blob/main/web-scraper.py), you need to have the most recent version of **Mozilla Firefox** installed.<br />

You also need to have any version greater than **Python 3.6** installed.

The necessary Python modules can be successfully installed by typing the following in your bash terminal: <br />
<br />
```
$   pip3 install -r requirements.txt
```
<br />

Finally, if you are using **Windows**, you have to run the **geckodriver.exe** file located in 'Webdriver Proxy/Windows' to install it. This is necessary to execute Firefox autonomously. Linux users don't need to install geckodriver manually.<br />
<br />
## Running the program
After setting up all the requirements mentioned above, to run the Web Scraper you may access the root folder of this repository on a bash terminal and type the following command:<br />
<br />
```
$   python3 web-scraper.py
```
<br />
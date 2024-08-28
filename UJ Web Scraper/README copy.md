Urban Jungle Trustpilot Reviews Scraper
Overview
This project is a Python-based web scraper designed to extract user reviews and corresponding star ratings from the Trustpilot website for "Urban Jungle." The script automates the process of collecting reviews from multiple pages on the site, organising the data into a structured format suitable for analysis.
Features
•	Web Scraping: Uses the BeautifulSoup library to parse HTML and extract review data.
•	Pagination Handling: Automatically iterates through multiple pages of reviews to collect data.
•	Data Cleaning: Strips unnecessary text from the reviews and extracts only relevant information.
•	Data Structuring: Organises the scraped data into a pandas DataFrame for easy analysis.
Requirements
•	Python 3.x
•	Required Python libraries:
•	beautifulsoup4
•	requests
•	pandas
•	re
Usage
1.	Initial Setup:
•	Ensure all the required Python libraries are installed.
•	Download the Jupyter Notebook file (UJReviews.ipynb).
2.	Running the Scraper:
•	Open the notebook in Jupyter.
•	Execute the cells sequentially to scrape the reviews and star ratings from Trustpilot.
3.	Data Extraction:
•	The scraper will automatically collect reviews and ratings from the first 100 pages of the Trustpilot site.
•	Reviews and their corresponding star ratings are stored in a Python dictionary and subsequently converted into a pandas DataFrame.
4.	Data Output:
•	The final DataFrame containing reviews and their star ratings is displayed at the end of the notebook.
•	You can export this DataFrame to a CSV or any other format as needed.
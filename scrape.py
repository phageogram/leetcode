#!/venv/bin/python3
import requests
import lxml.html
import pandas as pd
from datetime import date

# Initialize variables html and doc storing request from steampowered.com HTMLElement object.
html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)

# Extract target divs from HTML object. I am commenting titles and prices out for later use.
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
"""titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')"""

# Extract tags from new_releases object and store in variable tags_divs as xpath object
tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')

# Initialize an empty list and store tags as lists using .text_content() method. Split with ','
tags = []
tags = [tag.text_content() for tag in
    new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
tags = [tag.split(', ') for tag in tags]

# Convert tags list into df using pd.series().explode(). Store value counts in second column using value_counts()
tag_count = pd.Series(tags).explode().value_counts()

# Function to return top three tags and value count as unindexed string with headers.
def top_three(df):
    result = df.head(3).to_string(index=True, header=False)
    return result

# Initialize variable to store current most popular tags
current_date = str(date.today())
current_most_pop = {current_date: top_three(tag_count)}
ongoing_most_pop = {}
ongoing_most_pop.update(current_most_pop)

# Return top three tags
print(top_three(tag_count))

# Return top three tags historically
print(ongoing_most_pop)
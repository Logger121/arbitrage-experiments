# Arbitrage Calculator based on [oddschecker.com](https://www.oddschecker.com/)

## [Scraping](scraping/)

Initially planned to use a scraper to get the odds off the website but running [web_access_test.py](scraping/web_access_test.py) demonstrates the issues with that, but I still plan to come back to scraping later.

## Simply Copying and Pasting

Since I failed miserably at the web scraper, I decided to just go with copying and pasting the odds straight off the page.

This yields something along the lines of [raw_odds.txt](docs/raw_odds.txt), so I wrote a [script](formatters/filter_raw_odds.py) to clean that up to just [the two opponents and the relevant odds](docs/filtered_odds.txt). Then I wrote a [script](formatters/format_filtered_odds.py) to make this into a [useable CSV file](docs/formatted_odds.csv) (however the odds where still in fractional format).
Obviously the next step was just two put both of these together into [one script](formatters/format_raw_odds.py) and include code to convert the odds into decimals.

## [Calculating Arbitrage](calculators/)

This was a pain.

I spent a while looking at [this graph](assets/wrong_graphs.png), the diagonals representing odds (4/5, 20/1, 13/10), the vertical line representing return on an investment of £10, and the horizontal line there because I thought it should be.

Then I made [this graph](assets/right_odds.png), which adds 1 to each of the gradients to represent you recieving your original investment back as well as the profit. This one is the graph that is actually relevant for calculating arbitrage, and is based on the intercepts of the diagonals and the horizontal line. The x coordinate of a single intercept over the sum of the three of them gives you the stake you should place on those odds.

[This script](calculators/basic_arb_calc.py) uses those basic example odds and returns the stakes for each bet using a total stake of £10.
That was then adapted ([here](calculators/csv_arb_calc.py)) to read the entire CSV file and work out and print the balanced stakes for each row.
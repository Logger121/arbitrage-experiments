# Arbitrage Calculator based on [oddschecker.com](https://www.oddschecker.com/)

## Usage

Copy and paste odds from oddschecker.com into [raw_odds.txt](docs/raw_odds.txt) so they look similar to the current contents, then run [odds_to_arb.py](odds_to_arb.py) if there are win, draw, and loss odds, or [odds_to_arb_no_draw.py](odds_to_arb_no_draw.py) if there are no draw odds.

## [Scraping](scraping/)

Initially planned to use a scraper to get the odds off the website but running [this](scraping/web_access_test.py) demonstrates the issues with that, but I still plan to come back to scraping later.

## Simply Copying and Pasting

Since I failed miserably at the web scraper, I decided to just go with copying and pasting the odds straight off the page.

This yields something along the lines of [raw_odds.txt](docs/raw_odds.txt), so I wrote a [script](formatters/filter_raw_odds.py) to clean that up to just [the two opponents and the relevant odds](docs/filtered_odds.txt). Then I wrote a [script](formatters/format_filtered_odds.py) to make this into a [useable CSV file](docs/formatted_odds.csv) (however the odds where still in fractional format).

Obviously the next step was just two put both of these together into [one script](formatters/format_raw_odds.py) and include code to convert the odds into decimals.

Later on I copied some football odds that had the clubs' records attached in the form of 10 character strings comprised of 'w', 'd, nd 'l'. These had to be removed as well so I wrote a [little program](formatters/wld_iterator.py) to produce every possible combination in order to exclude them. Eventually I implemented this into the calculator, except I made a [dictionary](docs/wdl_combinations.txt) so it could just check through that rather than iterating through every single combination every time the program is run. I'm not sure this even saves much time because it still has to check through the entire file, but I live in hope.

## [Calculating Arbitrage](calculators/)

This was a pain.

I spent a while looking at [this graph](assets/wrong_graphs.png), the diagonals representing odds (4/5, 20/1, 13/10), the vertical line representing return on an investment of £10, and the horizontal line there because I thought it should be.

Then I made [this graph](assets/right_odds.png), which adds 1 to each of the gradients to represent you recieving your original investment back as well as the profit. This one is the graph that is actually relevant for calculating arbitrage, and is based on the intercepts of the diagonals and the horizontal line. The x coordinate of a single intercept over the sum of the three of them gives you the stake you should place on those odds.

[This script](calculators/basic_arb_calc.py) uses those basic example odds and returns the stakes for each bet using a total stake of £10.

That was then adapted ([here](calculators/csv_arb_calc.py)) to read the entire CSV file and work out and print the balanced stakes for each row.

I made a couple of changes to csv_arb_calc.py which you can see commented out, so it only printed arbs.

## Odds to Stakes

I then merged the [formatter](formatters/format_raw_odds.py) with the [calculator](calculators/csv_arb_calc.py) to produce [odds_to_arb.py](odds_to_arb.py). This is where the WDL string removal was added and I also made some QoL tweaks so now it tells you how many arbs were found, but that's about it.

[odds_to_arb_no_draw.py](odds_to_arb_no_draw.py) mostly serves to run through tennis odds, but I will implement two odd functionality into the main calculator eventually.

## To do

- Make [odds_to_arb.py](odds_to_arb.py) and [odds_to_arb_no_draw.py](odds_to_arb_no_draw.py) one file
- Web scraping
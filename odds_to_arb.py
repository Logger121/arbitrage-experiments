import csv
import itertools
import os

def convert_odds(odds):
    numerator, denominator = odds.split('/')
    return float(numerator) / float(denominator)

def calculate_intercepts(slopes):
    intercepts = []
    sum_intercepts = 0

    for slope in slopes:
        x_intercept = 1 / slope
        intercepts.append(x_intercept)
        sum_intercepts += x_intercept

    return intercepts, sum_intercepts

# Check if WDL combinations file exists
wdl_file = 'wdl_combinations.txt'
if not os.path.isfile(wdl_file):
    # Generate and store WDL combinations in a text file
    characters = ['w', 'l', 'd']
    length = 10

    combinations = list(itertools.product(characters, repeat=length))

    with open(wdl_file, 'w') as wdl_output:
        for combination in combinations:
            wdl_output.write(''.join(combination) + '\n')

# Read WDL combinations from the text file
with open(wdl_file, 'r') as wdl_input:
    wdl_combinations = [line.strip() for line in wdl_input]

# Filtering the odds
filtered_lines = []
with open('raw_odds.txt', 'r') as raw_file:
    for line in raw_file:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check conditions to exclude lines
        if line and ':' not in line and '2023' not in line and 'All Odds' not in line:
            exclude_line = False
            for combination in wdl_combinations:
                if combination in line:
                    exclude_line = True
                    break
            if not exclude_line:
                filtered_lines.append(line)

# Write filtered odds to CSV
with open('formatted_odds.csv', 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(['Fighter1', 'Fighter2', 'Win', 'Draw', 'Loss'])  # Write header row
    
    num_lines = len(filtered_lines)
    
    for i in range(0, num_lines, 5):
        fighter1 = filtered_lines[i].strip()
        fighter2 = filtered_lines[i + 1].strip()
        odds = filtered_lines[i + 2:i + 5]

        try:
            win = convert_odds(odds[0].strip())
            draw = convert_odds(odds[1].strip())
            loss = convert_odds(odds[2].strip())
        except IndexError:
            print(f"Skipping lines {i+2}-{i+5} due to incorrect format.")
            continue
        
        writer.writerow([fighter1, fighter2, win, draw, loss])

# Analyzing the formatted odds and printing the results
print()
arbs = 0

# Read CSV file
filename = 'formatted_odds.csv'

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row

    for row in reader:
        fighter1, fighter2, win, draw, loss = row

        # Convert string values to floats
        win = float(win) + 1
        draw = float(draw) + 1
        loss = float(loss) + 1

        # Calculate intercepts and sum of intercepts
        slopes = [win, draw, loss]
        intercepts, sum_intercepts = calculate_intercepts(slopes)

        multiplier = 10
        
        for i, intercept in enumerate(intercepts):
            fraction = (intercept / sum_intercepts) * multiplier
            stake = round(fraction, 2)
            if i == 0:
                payout = round((stake * win), 2)
                if payout > multiplier:
                    arbs = arbs + 1
                    print(f"Fighters: {fighter1} vs {fighter2}")
                    print(f"Payout: £{payout}")
                    print(f"Win: {stake}")
            elif i == 1:
                if payout > multiplier:
                    print(f"Draw: {stake}")
            else:
                if payout > multiplier:
                    print(f"Loss: {stake}")
                    print()

print(f"Total Arbs Found: {arbs}")
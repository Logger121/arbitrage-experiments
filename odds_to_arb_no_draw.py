import csv
import itertools

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

# Filtering the odds
characters = ['w', 'l']
length = 10

combinations = list(itertools.product(characters, repeat=length))

filtered_lines = []
with open('docs/raw_odds.txt', 'r') as raw_file:
    for line in raw_file:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check conditions to exclude lines
        if line and ':' not in line and '2023' not in line and 'All Odds' not in line:
            exclude_line = False
            for combination in combinations:
                if ''.join(combination) in line:
                    exclude_line = True
                    break
            if not exclude_line:
                filtered_lines.append(line)

# Write filtered odds to CSV
with open('docs/formatted_odds.csv', 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(['Fighter1', 'Fighter2', 'Win', 'Loss'])  # Write header row
    
    num_lines = len(filtered_lines)
    
    for i in range(0, num_lines, 4):
        fighter1 = filtered_lines[i].strip()
        fighter2 = filtered_lines[i + 1].strip()
        odds = filtered_lines[i + 2:i + 4]

        try:
            win = convert_odds(odds[0].strip())
            loss = convert_odds(odds[1].strip())
        except IndexError:
            print(f"Skipping lines {i+2}-{i+4} due to incorrect format.")
            continue
        
        writer.writerow([fighter1, fighter2, win, loss])

# Analyzing the formatted odds and printing the results
print()
arbs = 0

# Read CSV file
filename = 'docs/formatted_odds.csv'

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row

    for row in reader:
        fighter1, fighter2, win, loss = row

        # Convert string values to floats
        win = float(win) + 1
        loss = float(loss) + 1

        # Calculate intercepts and sum of intercepts
        slopes = [win, loss]
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
            else:
                if payout > multiplier:
                    print(f"Loss: {stake}")
                    print()

print(f"Total Arbs Found: {arbs}")

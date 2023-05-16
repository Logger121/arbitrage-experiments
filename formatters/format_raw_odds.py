import csv

def convert_odds(odds):
    numerator, denominator = odds.split('/')
    return float(numerator) / float(denominator)

# Script 1: Filtering the odds
filtered_lines = []
with open('raw_odds.txt', 'r') as raw_file:
    for line in raw_file:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check conditions to exclude lines
        #  and 'ww' not in line and 'wl' not in line and 'wd' not in line and 'll' not in line and 'lw' not in line and 'ld' not in line and 'dd' not in line and 'dw' not in line and 'dl' not in line
        if line and ':' not in line and '2023' not in line and 'All Odds' not in line:
            filtered_lines.append(line)

# Script 2: Converting to CSV with decimal odds
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

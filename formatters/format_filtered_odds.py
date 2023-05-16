import csv

with open('filtered_odds.txt', 'r') as input_file, open('formatted_odds.csv', 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(['Fighter1', 'Fighter2', 'Win', 'Draw', 'Loss'])  # Write header row
    
    lines = input_file.readlines()
    num_lines = len(lines)
    
    for i in range(0, num_lines, 5):
        fighter1 = lines[i].strip()
        fighter2 = lines[i + 1].strip()
        odds = lines[i + 2:i + 5]

        try:
            win = odds[0].strip()
            draw = odds[1].strip()
            loss = odds[2].strip()
        except IndexError:
            print(f"Skipping lines {i+2}-{i+5} due to incorrect format.")
            continue
        
        writer.writerow([fighter1, fighter2, win, draw, loss])

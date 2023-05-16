with open('raw_odds.txt', 'r') as raw_file, open('filtered_odds.txt', 'w') as filtered_file:
    for line in raw_file:
        line = line.strip()  # Remove leading/trailing whitespace
        
        # Check conditions to exclude lines
        if line and ':' not in line and '2023' not in line and 'All Odds' not in line:
            filtered_file.write(line + '\n')

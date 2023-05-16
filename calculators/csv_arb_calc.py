import csv

print()

def calculate_intercepts(slopes):
    intercepts = []
    sum_intercepts = 0

    for slope in slopes:
        x_intercept = 1 / slope
        intercepts.append(x_intercept)
        sum_intercepts += x_intercept

    return intercepts, sum_intercepts


# Read CSV file
filepath = 'docs/formatted_odds.csv'

with open(filepath, 'r') as csvfile:
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
                #if payout > multiplier:
                print(f"Fighters: {fighter1} vs {fighter2}")
                print(f"Payout: £{payout}")
                print(f"Win: {stake}")
            elif i == 1:
                #if payout > multiplier:
                print(f"Draw: {stake}")
            else:
                #if payout > multiplier:
                print(f"Loss: {stake}")
                print()
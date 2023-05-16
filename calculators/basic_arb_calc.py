def calculate_intercepts(slopes):
    intercepts = []
    sum_intercepts = 0

    for slope in slopes:
        x_intercept = 1 / slope
        intercepts.append(x_intercept)
        sum_intercepts += x_intercept

    return intercepts, sum_intercepts


# Example odds: 4/5, 20/1, 13/10
slopes = [1.8, 21, 2.3]
intercepts, sum_intercepts = calculate_intercepts(slopes)

multiplier = 10

for intercept in intercepts:
    fraction = (intercept / sum_intercepts) * multiplier
    print(round(fraction, 2))

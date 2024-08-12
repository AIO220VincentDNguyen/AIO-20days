import numpy as np
# exercise 1 
def calculate_probability(event_occurrences, total_trials):
    if total_trials == 0:
        return 0
    return event_occurrences / total_trials

event_occurences = 5
total_trials = 20
probability = calculate_probability(event_occurences, total_trials)
print ( f"Xác suất của sự kiện là: { probability }")

# exercise 2
def calculate_conditional_probability(P_A_and_B, P_A):
    if P_A == 0:
        return 0
    return P_A_and_B / P_A

P_A_and_B = 0.2
P_A = 0.5
P_B_given_A = calculate_conditional_probability(P_A_and_B, P_A)
print ( f"Xác suất có điều kiện P(B|A) là: { P_B_given_A }")

def calculate_covariance(X, Y):
    if len(X) != len(Y):
        raise ValueError("X và Y phải có cùng số lượng phần tử")
    n = len(X)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    covariance = sum((X[i]- mean_X)*(Y[i] - mean_Y) for i in range(n))/n
    return covariance

# exercise 3
def calculate_correlation(X, Y):
    covariance = calculate_covariance(X, Y)
    std_X = np.std(X)
    std_Y = np.std(Y)

    correlation = covariance/(std_X * std_Y)
    return correlation

X = [2, 4, 6, 8, 10]
Y = [1, 3, 5, 7, 9]

covariance = calculate_covariance(X, Y)
correlation = calculate_correlation(X, Y)

print(f"Covariance giữa X và Y là: {covariance}")
print(f"Correlation giữa X và Y là: {correlation}")
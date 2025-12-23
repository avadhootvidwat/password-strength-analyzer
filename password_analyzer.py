from zxcvbn import zxcvbn

password = input("Enter password to analyze: ")
result = zxcvbn(password)

print("\nPassword Strength Analysis")
print("--------------------------")
print("Score (0-4):", result['score'])
print("Crack Time:", result['crack_times_display']['offline_slow_hashing_1e4_per_second'])
print("Feedback:", result['feedback']['warning'])
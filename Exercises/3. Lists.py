temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
high = []
for a in temperatures:
    if a > 17:
        high.append(a)
print(f"Wednesday: {temperatures[2]} \n"
f"Max: {sorted(temperatures)[-1]}\n"
f"Min: {sorted(temperatures)[0]} \n"
f"Average: {round(sum(temperatures) / len(temperatures) , 1)}\n"
f"Days above 17: {len(high)}\n"
f"Sorted: {sorted(temperatures)}"
)

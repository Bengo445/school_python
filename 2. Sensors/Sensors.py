
lines = list(map(int, open("input.txt", "r").readlines()))

print(f"min:{min(lines)} max:{max(lines)} priemer:{sum(lines) / len(lines)}")
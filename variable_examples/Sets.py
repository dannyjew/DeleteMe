car_parts = {"wheels", "doors", "exhaust"}
car_parts.add("windows")
car_parts.remove("wheels")

print(car_parts)
print(len(set("hello")) == len(list("hello")))

x = frozenset([1, 2, 3, 4])
print(x)
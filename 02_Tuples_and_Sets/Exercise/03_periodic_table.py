number_of_lines = int(input())
chemical_compounds = set()

for _ in range(number_of_lines):
    elements = input().split()
    [chemical_compounds.add(element) for element in elements]

print(*chemical_compounds, sep="\n")

# One row solution:
# print(*{element for _ in range(int(input())) for element in input().split()}, sep="\n")

# Python

import periodictable

def calculate_molecular_weight(chemical_formula):
    formula = periodictable.formula(chemical_formula)
    total_weight = 0
    for atom in formula.atoms:
        total_weight += atom.mass * formula.atoms[atom]
    return total_weight

def main():
    chemical_formula = input("Enter the chemical formula: ")
    molecular_weight = calculate_molecular_weight(chemical_formula)
    print("Molecular weight:", molecular_weight)

if __name__ == "__main__":
    main()

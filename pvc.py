def main():
    sample_formula = [(100, 1.4, 0.475), (28, 0.973, 0.92), (7.5, 1.008, 1.56),
                      (20, 2.71, 0.0625)]
    spg, cost_wt, cost_vol = spg_costs(sample_formula)
    duro = durometer_dinp(28)
    print('{} specific gravity'.format(spg))
    print('${} per pound'.format(cost_wt))
    print('${} per volume'.format(cost_vol))
    print(duro, 'A Shore Durometer @ 15s delay')
    
def spg_costs(formula):
    recipe = []
    sum_phr = sum_pound_volumes = sum_costs = 0
    for ingredient in formula:
        pound_volumes = ingredient[0] / ingredient[1]
        line_cost = ingredient[0] * ingredient[2]
        recipe_data = [ingredient[0], pound_volumes, line_cost]
        recipe.append(recipe_data)
    for item in recipe:
        sum_phr = sum_phr + item[0]
        sum_pound_volumes = sum_pound_volumes + item[1]
        sum_costs = sum_costs + item[2]
    formula_cost = round(sum_costs / sum_phr, 5)
    formula_spg = round(sum_phr / sum_pound_volumes, 3)
    volume_cost = round(formula_cost * formula_spg, 5)
    output = (formula_spg, formula_cost, volume_cost)
    return output

def spg(formula):
    recipe = []
    sum_phr = sum_pound_volumes = 0
    for ingredient in formula:
        pound_volumes = ingredient[0] / ingredient[1]
        recipe_data = [ingredient[0], pound_volumes]
        recipe.append(recipe_data)
    for item in recipe:
        sum_phr = sum_phr + item[0]
        sum_pound_volumes = sum_pound_volumes + item[1]
    formula_spg = round(sum_phr / sum_pound_volumes, 3)
    return formula_spg

def durometer_dop(phr):
    duro = round(111 - 0.627*phr, 1)
    return duro

def durometer_dinp(phr):
    duro = round(114 - 0.6*phr, 1)
    return duro

def durometer_didp(phr):
    duro = round(115.8 - 0.605*phr, 1)
    return duro

def durometer_doa(phr):
    duro = round(110 - 0.63*phr, 1)
    return duro

def durometer_dina(phr):
    duro = round(107.8 - 0.544*phr, 1)
    return duro

def durometer_totm(phr):
    duro = round(118.1 - .632*phr, 1)
    return duro

def durometer_tintm(phr):
    duro = round(117.6 - .558*phr, 1)
    return duro

def durometer_dotp(phr):
    duro = round(113.8 - 0.617*phr, 1)
    return duro

def durometer_dphp(phr):
    duro = round(116 - 0.6*phr, 1)
    return duro

def durometer_dinch(phr):
    duro = round(115.2 - 0.602*phr, 1)
    return duro

def durometer_711p(phr):
    duro = round(114 - 0.657*phr, 1)
    return duro

def durometer_9p(phr):
    duro = round(114.3 - 0.619*phr, 1)
    return duro

def durometer_911p(phr):
    duro = round(113.2 - 0.596*phr, 1)
    return duro

def durometer_dup(phr):
    duro = round(115 - 0.574*phr, 1)
    return duro

def durometer_eso(phr):
    eso_in_dop = phr/1.1
    duro = round(111 - 0.627*eso_in_dop, 1)
    return duro

#main program loop
if __name__ == "__main__":
    main()

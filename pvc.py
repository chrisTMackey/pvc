def main():
    sample_formula = [(100, 1.4, 0.475), (28, 0.973, 0.92), (7.5, 1.008, 1.56),
                      (0, 2.71, 0.0625)]
    spg, cost_wt, cost_vol = spg_costs(sample_formula)
    duro, modulus, tensile, elongation, clashberg, brittle = flex_clear_dinp(28)
    print('${} per pound'.format(cost_wt))
    print('${} per volume'.format(cost_vol))
    print('{} specific gravity (ASTM D792)'.format(spg))
    print(duro, 'A Shore Durometer @ 15s delay (ASTM D 2240)')
    print(modulus, 'psi Modulus @ 100% elongation (ASTM D638)')
    print(tensile, 'psi Tensile Strength (ASTM D638)')
    print(elongation, '% Ultimate Elongation (ASTM D638)')
    print(clashberg, 'degrees Celsius Clash-Berg (ASTM D 1043 Tf @ 135,000psi)')
    print(brittle, 'degrees Celsius Brittleness (ASTM D 746)')
    
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

def flex_clear_dop(phr):
    duro = round(113.9 - 0.64*phr, 1)
    modulus = round(3548-36.56*phr)
    tensile = round(4700.4-34.41*phr)
    elongation = round(228.5+1.99*phr)
    clashberg = round(15.2-.8*phr, 1)
    brittle = round(-4.41-.57*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dinp(phr):
    duro = round(113.8 - 0.6*phr, 1)
    modulus = round(3559.1-34.78*phr)
    tensile = round(4414.8-28.7*phr)
    elongation = round(248.6+1.61*phr)
    clashberg = round(14.23-0.76*phr, 1)
    brittle = round(-4.19-0.55*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_didp(phr):
    duro = round(115.8 - 0.61*phr, 1)
    modulus = round(3595.4-34.11*phr)
    tensile = round(4424.1-28.68*phr)
    elongation = round(261.1+1.32*phr)
    clashberg = round(13.42-.74*phr, 1)
    brittle = round(-3.89-.56*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_doa(phr):
    duro = round(110 - 0.63*phr, 1)
    modulus = round( 2496.3 - 25.93*phr)
    tensile = round(4480.7-34.81*phr)
    elongation = round(268.7+1.93*phr)
    clashberg = round(-4.78-.97*phr, 1)
    brittle = round(-40.68-.44*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dina(phr):
    duro = round(107.8 - 0.544*phr, 1)
    modulus = round(2558.2-22.6*phr)
    tensile = round(4083.3-26.67*phr)
    elongation = round(269.5+1.59*phr)
    clashberg = round(-11.01-.79*phr, 1)
    brittle = round(-44.8-.38*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_totm(phr):
    duro = round(118.1 - .632*phr, 1)
    modulus = round(3675.8-33.7*phr)
    tensile = round(4323.5-25.7*phr)
    elongation = round(239.6+1.65*phr)
    clashberg = round(19.88-.78*phr, 1)
    brittle = round(-13.29-.41*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_tintm(phr):
    duro = round(117.6 - .558*phr, 1)
    modulus = round(3798.9-32.6*phr)
    tensile = round(4128.9-22.4*phr)
    elongation = round(262.7+.91*phr)
    clashberg = round(17.49-.73*phr, 1)
    brittle = round(-14.39-.36*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dotp(phr):
    duro = round(113.8 - 0.617*phr, 1)
    modulus = round(3650.3-35.4*phr)
    tensile = round(4419.7-26.8*phr)
    elongation = round(250.9+1.96*phr)
    clashberg = round(10.8-.77*phr, 1)
    brittle = round(-4.7-.57*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dphp(phr):
    duro = round(116 - 0.599*phr, 1)
    modulus = round(3611.6-34.8*phr)
    tensile = round(4282.1-25.8*phr)
    elongation = round(197.6+2.25*phr)
    clashberg = round(12.95-.75*phr, 1)
    brittle = round(-8.04-.45*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dinch(phr):
    duro = round(115.2 - 0.602*phr, 1)
    modulus = round(3124.3-28.3*phr)
    tensile = round(4274.7-26.3*phr)
    elongation = round(335.1+.6*phr)
    clashberg = round(11.64-.79*phr, 1)
    brittle = round(-6.71-.57*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_711p(phr):
    duro = round(114.4 - 0.657*phr, 1)
    modulus = round(3577.1-37.1*phr)
    tensile = round(4550-32*phr)
    elongation = round(253.4+1.77*phr)
    clashberg = round(11.4-.86*phr, 1)
    brittle = round(-10.3-.61*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_9p(phr):
    duro = round(114.2 - 0.645*phr, 1)
    modulus = round(3384.2-35.5*phr)
    tensile = round(4479.1-31.2*phr)
    elongation = round(259+1.72*phr)
    clashberg = round(7.6-.84*phr, 1)
    brittle = round(-8.3-.66*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_911p(phr):
    duro = round(113.2 - 0.596*phr, 1)
    modulus = round(3462.2-32.4*phr)
    tensile = round(4304.4-28.9*phr)
    elongation = round(227.3+1.33*phr)
    clashberg = round(5.7-.8*phr, 1)
    brittle = round(-12.29-.62*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dup(phr):
    duro = round(115 - 0.574*phr, 1)
    modulus = round(3457.3-32.7*phr)
    tensile = round(4449.7-32.4*phr)
    elongation = round(273+.74*phr)
    clashberg = round(5-.79*phr, 1)
    brittle = round(-15.4-.62*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_eso(phr):
    eso_in_dop = phr/1.1
    duro = round(111 - 0.627*eso_in_dop, 1)
    modulus = round(3548-36.56*eso_in_dop)
    tensile = round(4700.4-34.41*eso_in_dop)
    elongation = round(228.5+1.99*eso_in_dop)
    clashberg = round(15.2-.8*eso_in_dop, 1)
    brittle = round(-4.41-.57*eso_in_dop, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_filled(duro_A, phr_CaCO3):
    duro = round(0.929607437 * duro_A + 0.0531305301 * phr_CaCO3 + 6.270608278, 1)
    if duro <= duro_A:
        duro = duro_A
    if phr_CaCO3 == 0:
        duro = duro_A
    return duro

def duro_AtoD(duro_A):
    #converter {k:v, A Shore:D Shore, another set of A/D, so on}
    converter = {120:84, 115:84, 114:83.5, 112:79, 110:75.8, 108:72, 105:66.8,
                 104:65, 100:58, 95:46, 90:39, 85:33, 80:29, 75:25, 70:22,
                 65:19, 60:16, 55:14, 50:12, 45:10, 40:8, 35:7, 30:6}
    test_A = (duro_A // 5)*5
    if test_A >= 118.2:
        output = 84
    elif test_A <=30:
        output = 6
    else:
        total_gap_up = converter[test_A + 5] - converter[test_A]
        share_gap_up = (duro_A - test_A)/5
        partial_adjust = total_gap_up * share_gap_up
        output = round(converter[test_A] + partial_adjust, 1)
    return output

#main program loop
if __name__ == "__main__":
    main()

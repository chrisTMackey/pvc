"""pvc:   Tools for costing and rapid prototyping of Poly vinylchloride (PVC).
    Copyright (C) 2016  Chris T. Mackey

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    To contribute to this code, for questions, custom installations,
    or polymer consulting contact me via email or github.
    
    chris.t.mackey AT gmail DOT com
    https://github.com/chrisTMackey

    version 0.0.0-11.20.16
    """

def main():
    """demo function to display usage"""
    
    sample_formula = [(100, 1.4, 0.475), (60, 0.973, 0.92), (7.5, 1.008, 1.56),
                      (20, 2.71, 0.0625)]
    spg, cost_wt, cost_vol = spg_costs(sample_formula)
    duro, modulus, tensile, elongation, clashberg, brittle = flex_clear_dinp(28)
    print('${} per pound'.format(cost_wt))
    print('${} per volume'.format(cost_vol))
    print('{} specific gravity (ASTM D792)'.format(spg))
    print(duro, 'A Shore Durometer @ 15s delay (ASTM D2240)')
    print(modulus, 'psi Modulus @ 100% elongation (ASTM D638)')
    print(tensile, 'psi Tensile Strength (ASTM D638)')
    print(elongation, '% Ultimate Elongation (ASTM D638)')
    print(clashberg, 'degrees Celsius Clash-Berg (ASTM D1043 Tf @ 135,000psi)')
    print(brittle, 'degrees Celsius Brittleness (ASTM D746)')
    print('*****************')
    print('above data was for an unfilled formula')
    print('*****************')
    print('below is for filled formula')
    duro_filled = flex_filled(duro, 20)
    print(duro_filled, 'A Shore Durometer @ 15s delay (ASTM D2240)')



def spg_costs(formula):
    """takes formula, returns specific gravity and cost per pound and volume"""
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
    modulus = round(3559.1 - 34.78*phr)
    tensile = round(4414.8 - 28.7*phr)
    elongation = round(248.6 + 1.61*phr)
    clashberg = round(14.23 - 0.76*phr, 1)
    brittle = round(-4.19 - 0.55*phr, 1)
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
    modulus = round(3548-36.56*phr)
    tensile = round(4700.4-34.41*phr)
    elongation = round(228.5+1.99*phr)
    clashberg = round(15.2-.8*phr, 1)
    brittle = round(-4.41-.57*phr, 1)
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_filled(duro_A, phr_CaCO3):
    #linear r square 0.989, n = 27
    #duro = round(0.929607437 * duro_A + 0.0531305301 * phr_CaCO3 + 6.270608278, 1)
    #polynomial r square 0.992, n=27
    a = -0.001058114988 * duro_A * duro_A
    b = -0.001695411881 * duro_A * phr_CaCO3
    c = 0.00004967760719 * phr_CaCO3 * phr_CaCO3
    d = 1.158214659 * duro_A
    e = 0.1840327098 * phr_CaCO3
    f = -5.05711084
    duro = round(a + b + c + d + e + f, 1)
    if duro <= duro_A:
        duro = duro_A
    if phr_CaCO3 == 0:
        duro = duro_A
    return duro

def duro_AtoD(duro_A):
    #converter {k:v, A Shore:D Shore, another set of A/D, so on}
    converter = {120:84, 115:84, 110:75.8, 105:66.8,
                 100:58, 95:46, 90:39, 85:33, 80:29, 75:25, 70:22,
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

def rigid_nano07(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.990, n = 16
    flex_a = 0.0740909091 * phr_filler * phr_filler
    flex_b = -0.1265714286 * phr_filler * phr_impact_modifier
    flex_c = 0.265625 * phr_impact_modifier * phr_impact_modifier
    flex_d = 0.2065324675 * phr_filler
    flex_e = -9.682321429 * phr_impact_modifier
    flex_f = 499.1600325
    flex_mod = round(flex_a + flex_b + flex_c + flex_d + flex_e + flex_f)

    #notched izod polynomial r squared = 0.765, n = 46
    notch_a = 2.397884026 * phr_filler * phr_filler
    notch_b = 5.914428509 * phr_filler * phr_impact_modifier
    notch_c = -1.873679882 * phr_impact_modifier * phr_impact_modifier
    notch_d = 14.09969499 * phr_filler
    notch_e = 82.8909861 * phr_impact_modifier
    notch_f = -183.6350482
    notch = round(notch_a + notch_b + notch_c + notch_d + notch_e + notch_f)
    return(flex_mod, notch)


def rigid_nano3(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.986, n = 16
    flex_a = 0.0540909091 * phr_filler * phr_filler
    flex_b = -0.2594285714 * phr_filler * phr_impact_modifier
    flex_c = 0.0625 * phr_impact_modifier * phr_impact_modifier
    flex_d = 2.415103896 * phr_filler
    flex_e = -8.306428571 * phr_impact_modifier
    flex_f = 498.0761039
    flex_mod = round(flex_a + flex_b + flex_c + flex_d + flex_e + flex_f)

    #notched izod polynomial r squared = 0.761, n = 16
    notch_a = -0.2129545455 * phr_filler * phr_filler
    notch_b = 0.9097142857 * phr_filler * phr_impact_modifier
    notch_c = -23.34375 * phr_impact_modifier * phr_impact_modifier
    notch_d = 79.34926623 * phr_filler
    notch_e = 265.3782143 * phr_impact_modifier
    notch_f = -344.6062338
    notch = round(notch_a + notch_b + notch_c + notch_d + notch_e + notch_f)
    return(flex_mod, notch)

def rigid_nano7(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.976, n = 16
    flex_a = 0.0045454545 * phr_filler * phr_filler
    flex_b = -1.857142857 * phr_filler * phr_impact_modifier
    flex_c = 0.09375 * phr_impact_modifier * phr_impact_modifier
    flex_d = 3.398051948 * phr_filler
    flex_e = -8.248214286 * phr_impact_modifier
    flex_f = 497.5230519
    flex_mod = round(flex_a + flex_b + flex_c + flex_d + flex_e + flex_f)

    #notched izod polynomial r squared = 0.783, n = 16
    notch_a = 1.348181818 * phr_filler * phr_filler
    notch_b = 11.25028571 * phr_filler * phr_impact_modifier
    notch_c = 0.25 * phr_impact_modifier * phr_impact_modifier
    notch_d = -1.717220779 * phr_filler
    notch_e = 62.53428571 * phr_impact_modifier
    notch_f = -68.33922078
    notch = round(notch_a + notch_b + notch_c + notch_d + notch_e + notch_f)
    return(flex_mod, notch)

def rigid_2micron(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.977, n = 16
    flex_a = 0.1375 * phr_filler * phr_filler
    flex_b = 0.085 * phr_filler * phr_impact_modifier
    flex_c = 0.484375 * phr_impact_modifier * phr_impact_modifier
    flex_d = 0.3675 * phr_filler
    flex_e = -10.85625 * phr_impact_modifier
    flex_f = 498.775
    flex_mod = round(flex_a + flex_b + flex_c + flex_d + flex_e + flex_f)

    #notched izod polynomial r squared = 0.932, n = 16
    notch_a = -0.0125 * phr_filler * phr_filler
    notch_b = -0.765 * phr_filler * phr_impact_modifier
    notch_c = 0.953125 * phr_impact_modifier * phr_impact_modifier
    notch_d = 3.8275 * phr_filler
    notch_e = 12.83125 * phr_impact_modifier
    notch_f = 73.45
    notch = round(notch_a + notch_b + notch_c + notch_d + notch_e + notch_f)
    return(flex_mod, notch)


def rigid_3micron(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.995, n = 16
    flex_a = 0.11 * phr_filler * phr_filler
    flex_b = -0.38 * phr_filler * phr_impact_modifier
    flex_c = 0.03125 * phr_impact_modifier * phr_impact_modifier
    flex_d = 1.774 * phr_filler
    flex_e = -8.6775 * phr_impact_modifier
    flex_f = 499.145
    flex_mod = round(flex_a + flex_b + flex_c + flex_d + flex_e + flex_f)

    #notched izod polynomial r squared = 0.852, n = 16
    notch_a = 0.28 * phr_filler * phr_filler
    notch_b = -0.952 * phr_filler * phr_impact_modifier
    notch_c = 1.09375 * phr_impact_modifier * phr_impact_modifier
    notch_d = -3.204 * phr_filler
    notch_e = 10.0775 * phr_impact_modifier
    notch_f = 78.405
    notch = round(notch_a + notch_b + notch_c + notch_d + notch_e + notch_f)
    return(flex_mod, notch)


def fusion_time(phr_impact_modifier, phr_paraffin_wax, phr_CaSt2):
    #Mathematical Modeling of Rigid PVC Formulations: Fusion Characteristics Bambrick, Hoegy, and Ferrari of Dow Chemical Canada
    #Journal of Vinyl Technology March 1994 Vol. 16, No. 1
    #r squared = 0.55
    #Trial Formula
    #pvc k = 66 100phr
    #heat stab thermolite 137 1.5phr
    #TiO2 10phr
    #CaCO3 6phr
    #paraffin wax xl165 0.5phr
    #calcium stearate 0.9phr
    #ester wax loxiol g32 0.5phr
    #process aid paraloid k120n 1.0 phr
    #range of experimentation below all in 5 buckets, baseline and 2 above / below
    #impact modifier 4.5 - 5.5 phr
    #paraffin wax 0.3 - 0.7 phr
    #calcium stearate 0.7 - 1.1 phr
    #ester wax 0.3 - 0.7 phr
    #process aid 0.6 - 1.4 phr
    return 32.3 - 0.94 * phr_impact_modifier + 0.68 * phr_paraffin_wax - 0.37 * phr_CaSt2

def fusion_temp(phr_impact_modifier, phr_paraffin_wax, phr_CaSt2, phr_process_aid, phr_ester_wax):
    #Mathematical Modeling of Rigid PVC Formulations: Fusion Characteristics Bambrick, Hoegy, and Ferrari of Dow Chemical Canada
    #Journal of Vinyl Technology March 1994 Vol. 16, No. 1
    #r squared = 0.75
    return 176 - 0.58 * phr_impact_modifier + 0.25 * phr_paraffin_wax - 0.44 * phr_CaSt2 - 0.29 * phr_process_aid - 0.25 * phr_paraffin_wax * phr_process_aid + 0.375 * phr_ester_wax * phr_process_aid

def fusion_torque(phr_impact_modifier, phr_paraffin_wax, phr_process_aid, phr_ester_wax):
    #Mathematical Modeling of Rigid PVC Formulations: Fusion Characteristics Bambrick, Hoegy, and Ferrari of Dow Chemical Canada
    #Journal of Vinyl Technology March 1994 Vol. 16, No. 1
    #r squared = 0.75
    #Mackey note: this paper lists the coefficient for ester wax here as -8.6 and as -19.  The -19 figure comes from a summary chart with rounding issues so I am treating it being most likely a typo on their end, but I could be interpreting that typo in reverse perhaps
    return 2575 + 26.9 * phr_impact_modifier - 59.5 * phr_paraffin_wax - 8.6 * phr_ester_wax + 31.5 * phr_process_aid




#main program loop
if __name__ == "__main__":
    main()

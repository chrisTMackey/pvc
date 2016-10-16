def main():
    """Demo function to show usage

    This will run the sample formula below and calculate specific gravity,
    cost per pound, cost per volume, and the A Shore durometer @ 15 second
    delay.  Both costs and specific gravity calculations here are very accurate.
    Durometer calculations are best thought of as estimates.  In the heart
    of the typical range of unfilled PVC formulas, they are fairly accurate,
    and generally within any lab QC specification.  Note that D Shore durometer
    readings are not implemented yet, but will be.  Also note that the durometer
    calculations are for unfilled formulas.  Usage of filler generally increases
    the durometer (or hardness) of a compound.  I would like to implement this,
    but the only data I have is from private compounders and I won't use that.
    Refer to the documentation inside the functions of interest to you for
    more help."""

    #Sample formula to run.
    #Formula must be in format as follows:
    #List of lists.
    #Each sub list is an ingredient in the formula or recipe.
    #Each sub list must have the following for the first three items:
    #1:  amount used or PHR (phr means per hundred resin),
    #2:  specific gravity of the ingredient, and
    #3:  cost of the ingredient
    #Example: [[pounds, specific gravity, cost], [same thing for item2], [etc]]
    #You can have additional data after the first three items in an ingredient,
    #this program will simply ignore it as it isn't needed to calculate
    #the specific gravity or costs of the compound.
    #You can use that additional information to program in order of addition,
    #mixing instructions, inventory locations, or additional functionality.
    sample_formula = [[100, 1.4, 0.475, 'PVC resin'],
                      [60, 0.973, 0.92, 'DINP plasticizer'],
                      [7.5, 1.008, 1.56, 'BaZn / ESO blend'],
                      [20, 2.71, 0.0625, 'CaCO3 filler 3 micron']]

    #Pass the formula through the spg_costs function and
    #store the following return values:
    #1:  specific gravity of your compound
    #2:  cost per pound (or whatever units you used) of your compound
    #3:  cost per volume of your compound
    #Note that cost per volume is key when designing parts.
    #This is because as the specific gravity of the compound changes,
    #so does your part weight.
    #The economic goal of any formula is lowest cost per volume.
    #Cost per pound is not as relevant as cost per volume.
    spg, cost_wt, cost_vol = spg_costs(sample_formula)

    #To characterize the formula, durometer or hardness is most often used
    #in the pvc industry.
    #From hardness you can extrapolate other less common properties of
    #your compound and I hope to build in that functionality in the future.
    #
    #The durometer_INSERT_PLASTICIZER_NAME_HERE functions take the variable
    #of phr and return the A Shore Durometer @ 15 second delay.
    #Note that PHR is not the same as pounds!
    #All plastic formulas are based off of 100 parts of resin.
    #PHR = per hundred resin (or per hundred rubber).
    #To use the durometer functions, you must scale your formulas to 100 phr PVC
    #then simply pass the plasticizer phr to the appropriate plasticizer
    #durometer function and it will return the A Shore hardness @ 15s delay.
    #
    #Note that when you get around the 90 A Shore delay durometer, we don't
    #use it much anymore in the industry.
    #We switch to the D Shore durometer, a specialty of mine.
    #Public data is lacking there, but a D Shore durometer function is
    #being developed.
    #
    #Note that at the moment this does not account for any filler contribution
    #to hardness.
    #Filler will add hardness generally.
    #INCLUDE FILLER NOTES HERE
    #I can not find any publicly available data to write a function on this.
    #Call it an opportunity for improvement or an opportunity for a kid in some
    #university to contribute to the field, open source software, and his / her
    #resume.
    #Note that this data is available, but it is the property of the
    #compounding companies that generate it and they don't care to publish it,
    #nor I republish it.
    #If you would like a custom installation of this software based on your
    #data, that can be arranged privately.  Just contact me for consulting.
    

    #The above formula used 60 phr DINP so pass that to the function
    #to get the hardness and store it in some variable, duro in this case.
    duro = durometer_dinp(60)
    #print the data, it worked!
    print('{} specific gravity'.format(spg))
    print('${} per pound'.format(cost_wt))
    print('${} per volume'.format(cost_vol))
    print(duro, 'A Shore Durometer @ 15s delay')
    
def spg_costs(formula):
    """Takes a formula and returns specific gravity and volume costs.

    Formula is input.  It is a list of lists.  Each sub list is an ingredient.
    Each ingredient is structured as follows:
    1:  Pounds used or better yet PHR (PHR = Per Hundred Resin)
    2:  Specific gravity of the ingredient
    3:  Cost of the ingredient
    You can have additional items after these three, they will just be ignored
    by this function.
    Will return a tuple with 3 values.
    1:  specific gravity of your compound,
    2:  cost per pound of your compound, and
    3:  cost per volume of your compound."""

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
    """Takes a formula and returns the specific gravity of that formula.

    Same notes as in the spg_costs function.
    Only difference is you do not need the cost information, but if you do
    the program will simply ignore costs.
    Not as useful of a function, but may be of use in a QC setting where
    you do not wish to publish cost information but do wish to share
    this specific gravity calculator functionality."""

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
    """Takes the phr amount of DOP plasticizer and returns the
    A shore durometer @ 15s delay of a compound.

    PHR stands for per hundred resin.
    All plastic are written based on 100 parts resin.
    If your formula is written in pounds, you need to convert it to
    100 pounds of resin and then convert the plasticizer as well into PHR.
    Then you pass the PHR into this function and it returns the A Shore
    Durometer at 15 second delay for your compound.

    Note:  D Shore Durometer scale is not implemented yet.
    Note:  These calculations are for unfilled formulas.
    Filler will increase hardness generally.  Fillers contribution
    to hardness has not been implemented yet.
    Formulate carefully."""

    duro = round(111 - 0.627*phr, 1)
    return duro

def durometer_dinp(phr):
    """Takes the phr amound of DINP plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(114 - 0.6*phr, 1)
    return duro

def durometer_didp(phr):
    """Takes the phr amound of DIDP plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(115.8 - 0.605*phr, 1)
    return duro

def durometer_doa(phr):
    """Takes the phr amound of DOA plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(110 - 0.63*phr, 1)
    return duro

def durometer_dina(phr):
    """Takes the phr amound of DINA plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(107.8 - 0.544*phr, 1)
    return duro

def durometer_totm(phr):
    """Takes the phr amound of TOTM plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(118.1 - .632*phr, 1)
    return duro

def durometer_tintm(phr):
    """Takes the phr amound of TINTM plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(117.6 - .558*phr, 1)
    return duro

def durometer_dotp(phr):
    """Takes the phr amound of DOTP plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(113.8 - 0.617*phr, 1)
    return duro

def durometer_dphp(phr):
    """Takes the phr amound of DPHP plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(116 - 0.6*phr, 1)
    return duro

def durometer_dinch(phr):
    """Takes the phr amound of DINCH plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(115.2 - 0.602*phr, 1)
    return duro

def durometer_711p(phr):
    """Takes the phr amound of 7,11P plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(114 - 0.657*phr, 1)
    return duro

def durometer_9p(phr):
    """Takes the phr amound of 9P plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(114.3 - 0.619*phr, 1)
    return duro

def durometer_911p(phr):
    """Takes the phr amound of 9,11P plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(113.2 - 0.596*phr, 1)
    return duro

def durometer_dup(phr):
    """Takes the phr amound of DUP plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    duro = round(115 - 0.574*phr, 1)
    return duro

def durometer_eso(phr):
    """Takes the phr amound of ESO plasticizer and returns the
    A Shore durometer @ 15s delay of a compound.

    For more information on the function, see the documentation inside the
    durometer_dop() function above."""
    
    eso_in_dop = phr/1.1
    duro = round(111 - 0.627*eso_in_dop, 1)
    return duro

#main program loop
if __name__ == "__main__":
    main()

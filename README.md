# pvc

Basic set of tools to cost and rapid prototype PVC formulas.

#Usage:
>>>import pvc

>>>your_formula = [[100, 1.4, 0.5225], [60, 0.973, 0.92], [7.5, 1.008, 1.56], [20, 2.71, 0.0625]]

>>>spg, cost_wt, cost_vol = spg_costs(your_formula)

>>>hardness = durometer_dinp(60)

>>>print('{} specific gravity'.format(spg))

>>>print('${} per pound'.format(cost_wt))

>>>print('${} per volume'.format(cost_vol))

>>>print(duro, 'A Shore Durometer @ 15s delay')

#Formula Construction

Formulas are lists of lists.

The sub lists are ingredients in the formula.

The sub lists must have the following as their first three items.

1.  Amount used or PHR (phr = per hundred resin) of the ingredient.
2.  Specific gravity of the ingredient.
3.  Cost of the ingredient.

Note:  You can pass additional information in the list harmlessly.  Only the first three elements are needed to calculate the specific gravity and costs and anything else is ignored.  You can pass additional information and instructions in the formula if you wish.

#Durometer Functions

List of supported durometer functions:
durometer_dop(phr)
durometer_dinp(phr)
durometer_didp(phr)
durometer_doa(phr)
durometer_dina(phr)
durometer_totm(phr)
durometer_tintm(phr)
durometer_dotp(phr)
durometer_dphp(phr)
durometer_dinch(phr)
durometer_711p(phr)
durometer_9p(phr)
durometer_911p(phr)
durometer_dup(phr)
durometer_eso(phr)

These functions take the parameter phr.

PHR stands for Per Hundred Resin (or Rubber for that industry).

All plastic and rubber formulas are written this way.

Scale your formula for 100 parts PVC resin and then scale the plasticizer appropriately to convert it to phr.

Then simply pass the phr parameter to the proper durometer function to get an estimate of A Shore Durometer at 15 second delay.

Note:  D Shore Durometer is used once you get into the 90's typically.  This isn't programmed into this tool, yet.

Note:  These functions are for unfilled formulas.  Addition of mineral filler (typically CaCO3 calcium carbonate graded by micron particle size) generally raises the durometer or hardness of a formula.  Public data is lacking to build this tool at the moment.  Be weary of using this data on filled formulas with regard to hardness or durometer data.  The costs and the specific gravity will be very accurate but the durometer less so.

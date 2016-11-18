A working project still in process.  

Apologies for the mess

# pvc

Basic set of tools to cost and rapid prototype PVC formulas.

#Usage:
>>>import pvc

>>>your_formula = [[100, 1.4, 0.5225], [60, 0.973, 0.92], [7.5, 1.008, 1.56], [20, 2.71, 0.0625]]

>>>spg, cost_wt, cost_vol = pvc.spg_costs(your_formula)

>>>print('{} specific gravity'.format(spg))

>>>print('${} per pound'.format(cost_wt))

>>>print('${} per volume'.format(cost_vol))

#Formula Construction

Formulas are lists of lists.

The sub lists are ingredients in the formula.

The sub lists must have the following as their first three items.

1.  Amount used or PHR (phr = per hundred resin) of the ingredient.
2.  Specific gravity of the ingredient.
3.  Cost of the ingredient.

Note:  You can pass additional information in the list harmlessly.  Only the first three elements are needed to calculate the specific gravity and costs and anything else is ignored.  You can pass additional information and instructions in the formula if you wish.


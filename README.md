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

That will import the pvc module, create a formula (your_formula).

The formula is a list of list.  Each list is an ingredient where the first three items are formatted as quantity, specific gravity, cost of that item.

Specific gravity, cost per pound, and cost per volume are very accurate.  In business I have found an error adjustment of 0.015 specific gravity to be more than sufficient to err on the side of caution.  Cost per pound is important for buying and selling plastic.  Cost per volume is absolute key for profitably designing plastic parts and managing a business that buys and sells plastic material and or plastic parts.  ALWAYS minimize volume cost of formula while hitting minimum properties.  Always.

While the important properties involving speicific gravity and cost are very very accurate, the other properties leave something to be desired sadly.

Durometer, or hardness, is the next most common physical property.  Fortunately of the other major physical properties, it is the only one with very good statistical data.

To determine the durometer of a formula you need to pass the PHR amound of plasticizer to the flex_clear_PLASTICIZER_NAME_HERE function.

Note that PHR is not pounds and it is not percent.

PHR stands for Per Hundred Resin (or per hundred rubber if that is your thing).

You need to scale your formula to use 100 parts of resin and then the proportional amount of all other ingredients.

For example.  If your formula was 300 pounds of PVC, 90 pounds of DINP plasticizer, 9 pounds of BaZn heat stabilizer / lube blend, and 60 pounds of CaCO3 filler.

In that case you have 300 pounds of resin.  To make it 100 pounds you need to scale down the formula by dividing all the ingredient amounts by 3.

That would give you this formula.  100 PHR PVC resin, 30 PHR DINP plasticizer, 3 PHR BaZn / lube, and 20 PHR CaCO3 filler.

Once you have your formula in PHR terms, it is easy.  Just pass the PHR of plasticizer to the function and it will return the A Shore Durometer @ 15 second delay as described in ASTM D2240.  Note from the name of the function, flex_clear_dinp(phr) in the case of DINP plasticizer, that that is for a clear formula.  If you are using filler, which the sample formula was with 20 PHR CaCO3 calcium carbonate filler, it won't be clear.  The formula will be filled and cloudy or opaque.

To account for filler you need to use the flex_filled(duro_A, phr_CaCO3) function.

That function takes 2 parameters.

1. The durometer, or hardness, A Shore reading that you determined from the previous function ( flex_clear_dinp(30) would return a tuple; the first or zeroth value in that tuple is the A Shore Durometer calculation).
2.  The phr_CaCO3 parameter is PHR of CaCO3 filler, in this example it was 20 PHR calcium carbonate filler.

So you would pass the following to take the clear durometer reading and make it a filled reading.

flex_filled(80, 20) 

That would take a formula that you know to be 80 A Shore in a clear formula and will calculate out the A Shore Durometer for the same formula but with 20 PHR of Calcium Carbonate Filler.

Unfortunately I do not have good data for modifying the other properties in filled formulations.

I don't expect too either.

The clear flexible formulation data for the physical properties other than speicific gravity and durometer all fall between 0.500 and 0.900 r squared on their best regression model.  Decent data, but not dry lab worthy so to speak.  You add filler to those mixes and you have a bigger problem than bad clear data when you factor in the various filler sizes and particle shapes.  An experienced formulator will still find use from seeing the projected clear properties though as they will know how filler will impact each property.

Here are the currently supported plasticizer functions.

flex_clear_dop(phr)
flex_clear_dinp(phr)
flex_clear_didp(phr)
flex_clear_doa(phr)
flex_clear_dina(phr)
flex_clear_totm(phr)
flex_clear_tintm(phr)
flex_clear_dotp(phr)
flex_clear_dphp(phr)
flex_clear_dinch(phr)
flex_clear_711p(phr)
flex_clear_9p(phr)
flex_clear_911p(phr)
flex_clear_dup(phr)
flex_clear_eso(phr)

Running that function will return a tuple with the following information (duro, modulus, tensile, elongation, clashberg, brittle).

Specifically those are the following physical properties of the compound at the PHR parameter of the chosen plasticizer.

1.  A Shore Durometer per ASTM D2240 at 15 second delay.
2.  psi Modulus at 100% Elongation per ASTM D638.
3.  psi Tensile Strength per ASTM D638.
4.  % Ultimate Elongation per ASTM D638.
5.  Degrees Celsius Clash-Berg per ASTM D1043.
6.  Degrees Celsius Brittleness per ASTM D746.

Only the A Shore Durometer has an r squared of over 0.900.  Fortunately, or maybe because of that, that is the most commonly discussed property of PVC compounds after the costs and specific gravity, all of which are very very accurate.

Modulus, Tensile, Elongation, Clash-Berg, and Brittleness produce decent results in the range of say 40 - 80 PHR plasticizer as that is what most of the data is based on.  You get outside of that range and you are not interpolating data, you are extrapolating and you can get some bad results.  Use this data at your own risk.

In the industry, it is common to not use the A Shore Durometer once you get above 90 A Shore.  We switch to the D Shore Durometer.  There is very little data out there to build a D Shore Durometer data set to build a regression from.  The chart lists conversions from A to D for A Shore 100 and less.  Obviously I used that for the duro_AtoD(duro_A) functions.  For points inbetween on the charts, it is a straight linear regression point to point at the moment.

A Shore Durometer stops readings above 100, yet my tool will return readings up to nearly 120.  Why, well that is the slope of the line where it intercepts at 0 PHR plasticizer.  In theory they should all hit the same exact durometer at 0 PHR, but my formulas don't as a different intercept and slope in the Y=mX+b format.  

I wrote the duro_AtoD(duro_A) converter for values above 100 A Shore by referring to PVC pipe formulas.  PVC pipe is roughly 83-84 D Shore or maybe 80 D Shore if it is impact modified.  So I wanted to set the 0 PHR's to return a value around 83-84 D Shore and just a bit of plasticizer to return 80 D.  Right now the function pretty much does that and it does hit other D Shore formulations I have ran in business with in typical lab specification of +/- 3 Durometer points.


#Formula Construction

Formulas are lists of lists.

The sub lists are ingredients in the formula.

The sub lists must have the following as their first three items.

1.  Amount used or PHR (phr = per hundred resin) of the ingredient.
2.  Specific gravity of the ingredient.
3.  Cost of the ingredient.

Note:  You can pass additional information in the list harmlessly.  Only the first three elements are needed to calculate the specific gravity and costs and anything else is ignored.  You can pass additional information and instructions in the formula if you wish.


# pvc

Basic set of tools to cost and rapid prototype PVC formulas.

# Basic Usage:
>>>import pvc

>>>your_formula = [[100, 1.4, 0.5225], [60, 0.973, 0.92], [7.5, 1.008, 1.56], [20, 2.71, 0.0625]]

>>>spg, cost_wt, cost_vol = pvc.spg_costs(your_formula)

>>>print('{} specific gravity'.format(spg))

>>>print('${} per pound'.format(cost_wt))

>>>print('${} per volume'.format(cost_vol))

That will import the pvc module and create a formula (your_formula) for demonstration purposes.

Running the function will return the specific gravity, the cost per pound, and the cost per volume of the compound.  These are by far the most important calculations and they are all 99%+ accurate.  Billions of pounds of PVC compound are bought and sold using these same calculations.  Note:  These calculations work for any compound, not just PVC.  You could use these functions for polyethylene, polypropylene, or polystyrene compounds with the same degree of certainty.  You could even use them outside the polymer industry if you wanted.

The formula is a list of list.  Each list is an ingredient where the first three items are formatted as quantity, specific gravity, cost of that item.

Specific gravity, cost per pound, and cost per volume as calculated are very accurate.  

Durometer, or hardness, is the next most common physical property.  Fortunately of the other major physical properties, it has very good statistical data.

To determine the durometer of a formula you need to pass the PHR amound of plasticizer to the flex_clear_PLASTICIZER_NAME_HERE function.  This is explained in the section below.

# More Physical Properties Prediction

>>>duro, modulus, tensile, elongation, clashberg, brittle = pvc.flex_clear_dinp(28)

>>>print(modulus, 'psi Modulus @ 100% elongation (ASTM D638)')

>>>print(tensile, 'psi Tensile Strength (ASTM D638)')

>>>print(elongation, '% Ultimate Elongation (ASTM D638)')

>>>print(clashberg, 'degrees Celsius Clash-Berg (ASTM D1043 Tf @ 135,000psi)')

>>>print(brittle, 'degrees Celsius Brittleness (ASTM D746)')

This will run the remaining physical properties for flexible clear formulas with DINP plasticizer at 28 phr (Per Hundred Resin which again is not the same as pounds or %)

Each plasticizer gets its own function as the data is based on unique plasticzer (and later filler) combinations.

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

Here are the physical properties that the various flex_clear_PLASTICIZER_NAME will return.

1.  A Shore Durometer per ASTM D2240 at 15 second delay.
2.  psi Modulus at 100% Elongation per ASTM D638.
3.  psi Tensile Strength per ASTM D638.
4.  % Ultimate Elongation per ASTM D638.
5.  Degrees Celsius Clash-Berg per ASTM D1043.
6.  Degrees Celsius Brittleness per ASTM D746.

Only the A Shore Durometer has an r squared of over 0.900.  Fortunately, or maybe because of that, that is the most commonly discussed property of PVC compounds after the costs and specific gravity, all of which are very very accurate.

Modulus, Tensile, Elongation, Clash-Berg, and Brittleness produce decent results in the range of say 40 - 80 PHR plasticizer as that is what most of the data is based on.  Fortunately that is the same range that most flexible PVC formulas are commercially produced.  You get outside of that range and you are not interpolating data, you are extrapolating and you can get some bad results.  Use this data at your own risk. 



# PHR does not equal Pounds or Percent, it means Per Hundred Resin
Note that PHR is not pounds and it is not percent.

PHR stands for Per Hundred Resin (or per hundred rubber if that is your thing).

You need to scale your formula to use 100 parts of resin and then the proportional amount of all other ingredients.

For example.  If your formula was 300 pounds of PVC, 90 pounds of DINP plasticizer, 9 pounds of BaZn heat stabilizer / lube blend, and 60 pounds of CaCO3 filler.

In that case you have 300 pounds of resin.  To make it 100 pounds you need to scale down the formula by dividing all the ingredient amounts by 3.

That would give you this formula.  100 PHR PVC resin, 30 PHR DINP plasticizer, 3 PHR BaZn / lube, and 20 PHR CaCO3 filler.

Once you have your formula in PHR terms, it is easy.  Just pass the PHR of plasticizer to the function and it will return the A Shore Durometer @ 15 second delay as described in ASTM D2240 along with all the other physical properties.  
Note from the name of the function, flex_clear_dinp(phr) in the case of DINP plasticizer, that that is for a clear formula.  If you are using filler, which the sample formula was with 20 PHR CaCO3 calcium carbonate filler, it won't be clear.  The formula will be filled and cloudy or opaque.

# Accounting for Filler (non clear formulas)
To account for filler you need to use the flex_filled(duro_A, phr_CaCO3) function.  Basically figure out the durometer of the formula without the filler then pass that and the PHR of the filler to the flex_filled() and it will do all the math for you.

That function takes 2 parameters.

1. The durometer, or hardness, A Shore reading that you determined from the previous function.
2.  The phr_CaCO3 parameter is PHR of CaCO3 filler, in this example it was 20 PHR calcium carbonate filler.

To account for the filler, simply pass the unfilled A Shore Durometer result from the flex_clear_dinp function AND the phr of the filler to the flex_filled(duro_A, phr_CaCO3) function to get what the filled durometer reading would be.
>>>filled_duro = pvc.flex_filled(97, 20)

>>>print(filled_duro, 'A Shore Durometer w/ filler @15s delay (ASTM D2240)')


This is some of the best data I have with an r squared of 0.992.  I'd still be cautious using it above 100 A Shore or on the D Shore scale.

Unfortunately I do not have good data for modifying the other properties in filled formulations.

I don't expect too either.

The clear flexible formulation data for the physical properties other than speicific gravity and durometer all fall between 0.500 and 0.900 r squared on their best regression model.  Decent data, but not dry lab worthy so to speak.  Currently all these properties are calculated off a linear regression, but I intend to convert some to polynomial regressions at a later point.  You add filler to those mixes and you have a bigger problem than bad clear data when you factor in the various filler sizes and particle shapes.  An experienced formulator will still find use from seeing the projected clear properties though as they will know how filler will impact each property.

# D Shore Durometer
In the industry, it is common to not use the A Shore Durometer once you get above 90 A Shore.  We switch to the D Shore Durometer.  There is very little data out there to build a D Shore Durometer data set to build a regression from.  The published chart lists conversions from A to D for A Shore 100 and less.  Obviously I used that for the duro_AtoD(duro_A) functions.  For points inbetween on the charts, it is a straight linear regression point to point at the moment.

A Shore Durometer stops readings above 100, yet my tool will return readings up to nearly 120.  Why, well that is the slope of the line where it intercepts at 0 PHR plasticizer.  In theory they should all hit the same exact durometer at 0 PHR, but my formulas don't as a different intercept and slope in the Y=mX+b format fits the data better.  

I wrote the duro_AtoD(duro_A) converter for values above 100 A Shore by referring to PVC pipe formulas.  PVC pipe is roughly 83-84 D Shore or maybe 80 D Shore if it is impact modified.  So I wanted to set the 0 PHR's to return a value around 83-84 D Shore and just a bit of plasticizer to return 80 D.  Right now the function pretty much does that and it does hit other D Shore formulations I have ran in business with in typical lab specification of +/- 3 Durometer points.  

In theory I shouldn't scale down from a common intercept but one specific to the plasticizer, but I'll program that when somebody needs it.  I have bigger ideas for rigid formulation than an A to D Durometer converter anyways.

Note that all data for this project was found in the public domain from varying labs, authors, and companies over the decades.  Data is sparse in some locations.  

In business, you would run this software on your data and develop better models.  You wouldn't publish those models though and if you were a former employee of them, you shouldn't either, hence the public data.  

I have vetted all the data that goes into the regression models to determine the math.  Big thanks to BASF, ExxonMobil, Dr. Dick Grossman, and Jesse Edenbaum for paving the way and publishing quality data.  Equally big thanks for years of support to Formosa Plastics and Baerlocher as well.

# Formula Construction

Formulas are lists of lists.

The sub lists are ingredients in the formula.

The sub lists must have the following as their first three items.

1.  Amount used or PHR (phr = per hundred resin) of the ingredient.
2.  Specific gravity of the ingredient.
3.  Cost of the ingredient.

Note:  You can pass additional information in the list harmlessly.  Only the first three elements are needed to calculate the specific gravity and costs and anything else is ignored.  You can pass additional information and instructions in the formula if you wish.

# What Next
From here you can do quite a bit.

You can search millions of potential formula combinations in seconds (well maybe minutes for millions; I get about 250,000 in 4 seconds or so on my PC).  

From there you can screen hundreds of thousands of potential formulas for lowest cost (always lowest volume cost) given a set of properties.  

From there you can issue a few screening formulas to the lab to whip up and confirm the properties if you don't have a similar formula already in production.

I have written the optimization routines already, just haven't uploaded them yet.  

Same thing for graphing.  Right now no graphing capability is built in, but I use Matplotlib to plot and this works with that no problem, just like any data.  

I plan on implementing a graphing function for common use cases, but that isn't a high priority at the moment.

Next big step is to flip it though.  These are all flexible PVC at the moment.  Rigid PVC is big business, even bigger than flexible.  Different way of formulating really in rigid.  Still doing it all with PHR's and the like, but instead of plasticizer you are looking at impact modifiers.  Instead of wondering how much filler you are using, you are wondering about how much and what particle size are you looking at.  Some of the nano filler precipitated calcium carbonates (PCC's) work as impact modifiers which leads to an interesting economics vs performance trade off that this program excels in calculating.

If you look in the source code, the functions for rigid formulation are all there for various sizes and phr's of filler.  I haven't produced documentation of the functions and still want to gather more data ideally before officially releasing them.  Use them at your own risk.

# Work In Progress
Currently this is a minimally viable product.  Any formulator / python programmer could take these functions and start using them.  At the moment I am developing this into a GUI using Tkinter.  Currently it is working as another MVP (minimally viable product).  It can calculate the properties of a flexible formula.  Next I need to write a formula builder in the GUI, implement cost and specific gravity calculations in the GUI, and implement rigid formulation properties in the GUI.  

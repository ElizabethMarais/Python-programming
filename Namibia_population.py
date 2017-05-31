#www.coursera.org: Python Data stuctures, course 3, week 1 
print "PROGRAM FUNCTION: Program read data Namibia: for each region, the capital, population sensus counts in years 1991, 2001, 2011 and 2016. The percentage in growth between the different counts are calculated."
print "(Data obtained from https://www.citypopulation.de/Namibia.html)"

print " "

region_list = list()
regions_pop = dict()
key = 0
big_country = None
big_pop = 0
small_country = None
small_pop = 0

handle = open('Namibian_population_data.txt')
print "PRINT EACH REGION AND ITS DETAILS"
for line in handle:
      line = line.lstrip()

#find the region
      pos_region = line.find(";")
      region = line[0:pos_region]
      region = region.lstrip()   #strip all bla'nk spaces before it
#      print region

#find the capital
      pos_capital = line.find(';', pos_region +1)
      capital = line[pos_region +1:pos_capital]
      capital = capital.lstrip()          #strip all blank spaces before it
#      print capital

#find the area
      pos_area = line.find(';', pos_capital +1)
      area = line[pos_capital+1:pos_area]
      area = int(area.lstrip())                #strip all blank spaces before it
#      print area 

#find the pop1991   
      pos_pop1991 = line.find(';', pos_area+1)
      pop1991 = line[pos_area+1:pos_pop1991]
      pop1991 = int(pop1991.lstrip())              #strip all blank spaces before it
#      print pop1991 

#find the pop2001      
      pos_pop2001 = line.find(';', pos_pop1991 +1)
      pop2001 = line[pos_pop1991 +1:pos_pop2001]
      pop2001 = int(pop2001.lstrip())                #strip all blank spaces before it
#      print pop2001 

#find the pop2011   
      pos_pop2011 = line.find(';', pos_pop2001+1)
      pop2011 = line[pos_pop2001+1:pos_pop2011]
      pop2011 = int(pop2011.lstrip())              #strip all blank spaces before it
#      print pop2011 

#find the pop2016   
      pos_pop2016 = line.find(';', pos_pop2011+1)
      pop2016 = line[pos_pop2011+1:pos_pop2016]
      pop2016 = int(pop2016.lstrip())   
#      print pop2016 

      print "Region:", region, "  Capital:", capital, "  Area (square meter):", area, "m2" 
      print "Population 1991:", pop1991, "  Population 2001:", pop2001
      print "Population 2011:", pop2011, "  Population 2016:", pop2016

#calculate % going up no 1: population 2001 vs 1991
      diff1 = pop2001- pop1991
      perc_chng1 = round(float((float(diff1)/float(pop1991))*100),2)
      print "Percentage change 2001 vs 1991:", perc_chng1, '%'

#calculate % going up no 2: population 2011 vs 2001 
      diff2 = pop2011- pop2001
      perc_chng2 = round(((float(pop2011)-float(pop2001))/float(pop2001)*100),2)
      print "Percentage change 2011 vs 2001:", perc_chng2, '%'

#calculate % going up no 3: population 2016 vs 2011 
      perc_chng3 = round(((float(pop2016)-float(pop2011))/float(pop2011)*100),2)   #note first convert all numbers to float
      print "Percentage change 2016 vs 2011: ", perc_chng3, '%'
      print " "

      itemL = region, capital, area, pop1991, pop2001, pop2011, pop2016, perc_chng1, perc_chng2, perc_chng3
      region_list.append(itemL)

#region_list.sort    #if regions sorted descending: (reverse=True)
#print region_list
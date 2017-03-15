#Python coursera course 2: Dictionaries, Lists
print "Two lists are read by the program about Dalene Matthee's two most translated books."

kringelist = list()
kringelist = [['Kringe in n bos',1984,'Afrikaans'], ['Circles in a Forest',1984,'English'], ['Circulos na Floresta',1984,'Spanish'], ['Des Cercles dans la Foret',1984,'French'], ['Metsan Kehat',1984,'Finnish'], ['Skymnings Skogen',1985,'Swedish'], ['Hringir i Skogi',1985,'Russian'], ['Rastros en el Bosque',1985,'Argentinian'], ['Unter Dem Kalanderbaum',1985,'German'], ['Il Cerchio Dell Elefante',1986,'Italian'], ['Elefantskogen',1987,'Finnish'], ['Cirkels in het Woud',1994,'Netherlands'],  ['Circles in a Forest',1984,'American']]

fielalist  = list()
fielalist  = [['Fiela se kind',1985,'Afrikaans'], ['Fielas child',1986,'English'], ['Fielas son',1986,'Swedish'], ['Fielas Kind',1986,'German'], ['Le fils de Tiela',1986,'French'], ['Fielas child',1986,'American'], ['Fielin otrok',2004,'Slovenian'], ['Fielas kind',2013,'Netherlands']]

print " "
print "Dalene Matthee's book, 'Kringe in 'n bos', was originally published in Afrikaans in 1984. It has been translated and published in the following languages: "
for i in range(len(kringelist)):
    print kringelist[i][0], "was published in", kringelist[i][1],"in", kringelist[i][2]

print " "
name = None
year = 0
yearkringe = dict()
for i in range(len(kringelist)):
  name = kringelist[i][0] 
  year = kringelist[i][1]
  yearkringe[name] = year

#Determine in what year most 'Kringe in 'n bos books have been published
mostyearkringe  = dict()
for name, year in yearkringe.items():
    mostyearkringe[year] = mostyearkringe.get(year,0) + 1   #determine how many times a year is in the yearkringe dictionary

bigyear = None
bigcount = 0
for year, count in mostyearkringe.items():
       if bigyear is None or count > bigcount:
          bigyear = year
          bigcount = count
print "The year in which the most 'Kringe in 'n bos' books have been translated/published, is", bigyear, "and it is", bigcount, "times."

       


print " "
print "Dalene Matthee's book, 'Fiela se kind', was originally published in Afrikaans in 1985. It has been translated and published in the following languages: "
for i in range(len(fielalist)):
    print fielalist[i][0], "was published in", fielalist[i][1],"in", fielalist[i][2]


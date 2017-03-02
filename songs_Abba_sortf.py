#www.coursera.org: Python Data structures, file, dictionaries exercise

name = raw_input("Enter file to find the Abba songs: ")     # name = "Abba music.txt"
if len(name) < 1 or name <> "Abba music.txt": 
   name = "Abba music.txt"
   print "Wrong input, program will use 'Abba music.txt' as data file."
fh = open(name)

print " "

songs = {}
songA = None
key = 0
#print original data file 
print "Printing original data file: " 
#find Abba song written after word 'Abba', build a dictionary of songs
for line in fh:
        line = line.rstrip()
        print line
        if line.find('Abba ') > 0:
            pos_abba = line.find('Abba ')
            songA = line[pos_abba+5:]  #choose the song, read all after word 'Abba' till end of line
            songs[key] = songA     #assign song name to value in dictionary
            key += 1

print " "

print "DICTIONARY: ", songs

print " "

#build a list from the dictionary
songs_list = list()

def song_lf(songs):
    for key, value in songs.iteritems():
        songs_list.append([key, value])
    return songs_list

print " "
songs_list = song_lf(songs)
print "LIST: ", songs_list

songs_list.sort(reverse=True)
print "Sorted descending:"
print songs_list

print " "
print "No. Song"
#print songs underneath each other
for key, value in songs.iteritems():
    print key+1,":",value

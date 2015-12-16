These scripts were written to compare the Linked Jazz network (linkedjazz.org) to the network of performers involved in jazz events at Carnegie Hall, and to create a visualization of these overlapping relationships. The scripts utilize four datasets of RDF triples to accomplish this: two from Linked Jazz and two from Carnegie Hall. Using a series of ten python scripts, we first identified the people that exist in both networks using the Human Name Parser module to match names, and the RDFLib package to match URIs. From the resulting group of people in both domains, we produced a dataset containing 1) Linked Jazz relationships where people 'know of' each other 2) Carnegie Hall relationships where people performed in the same event, and 3) the subset of relationships that fall into both of these categories. The data was then made available for exploration through a Gephi visualization.

See below for a description of the data and an ordered list of the scripts and their functions. 

-Hannah Sistrunk and Molly Reese-Lerner
(Thanks to Rob Hudson, Associate Archivist of Carnegie Hall, and to the Linked Jazz Project)


THE DATA

lj_data.nt: 
	-From LJ project/available on linkedjazz.org 
	-RDF triples of all people from the Linked Jazz dataset. Includes LJ URI -> foaf:name 	and LJ URI -> DBpedia, MusicBrainz, LOC, or allmusic URIs
relationships.nt
	-From LJ project/available on linkedjazz.org.  
	-RDF triples of relationships between people in the LJ dataset. The knowsOf 	relationship is derived from interview transcript analysis, and the more refined 	relationships come from the crowdsourcing tool (52nd Street).
chAddressBook.nt
	-From Linked Jazz Project via Rob Hudson, Associate Archivist of Carnegie Hall. 
	-74,229 RDF triples of info on all people/groups in the Carnegie Hall dataset. 			Includes type (e.g.foaf:person, foaf:agent, dbpedia:orchestra), birth date, death 		date, profession or occupation, instrument played, name URI, and foaf:name. Only a 	sample of the data (100 RDF triples) is included here.
ch_linkedJazz.nt
	-From Linked Jazz Project via Rob Hudson, Associate Archivist of Carnegie Hall. 
	-2,878 RDF triples of “top-level” jazz events at Carnegie Hall from 1912-May 1955 		(sub-events like performance of a single tune have been brought up to the top level 		event). ‘Jazz’ is defined broadly/roughly as any event with a jazz musician involved. 
	-Includes CH event URI -> type (event), date, venue, name of concert, performer 		(DBpedia or CH URIs). Only a sample of the data (100 RDF triples) is included here.	



THE SCRIPTS AND PROCESS

Step A: Identify names/people in both the CH and LJ datasets

1) isolate_as_dict_CH+LJ.py
	Uses the Python Human Name Parser module to separate the foaf:Name of each person 		from LJ (lj_data.nt) and CH (chAddressBook.nt) into its parts - full name, first 		name, last name. 
      
2) Compare_parsed_names.py
	Compares the parsed human names from CH and LJ to find matches in first AND last 		name	 
	-264 people match

3) Compare_from_event_data.py
	Using the Python RDFLib library to work with RDF, finds the DBpedia URI matches 		between the LJ dataset (lj_data.nt) and the CH event performers (ch_linkedJazz.nt) 	and writes them to a list. The event data was used because it contained more DBpedia 		URIs than the chAddressBook.nt.
	-268 people match

4) Matches-master.py
	Combines the lists of LJ-CH people matched from the Human Name Parser string matching 	and the DBpedia URI matches. Dispensing with duplicates, it writes the URI from the 		LJ dataset for every match to a list.
        -373 people match


Step B: Pull relationship data from LJ for the people that exist in both datasets

5) Get_relationships.py
	From the list of 373 matches between the datasets, uses LJ relationships.nt RDF 		triples to create a dictionary where the key is an LJ person URI with the value as a 		list of each person (URI) they know of.
        
6) WriteCSV.py
	Writes a csv file of the LJ relationships, with a row for each knowsOf relationship. 		The script converts the URIs in the relationships_of_matches.json to their foafName 		equivalents for output to the csv.
        -3058 relationships (after removing four duplicates manually that were id'ed using 		Python)
        

Step C: Derive CH relationships from CH event data for the people that exist in both LJ and 		CH datasets

7) event_performer_dict.py
	Creates a dictionary of all CH events and their performers (URIs). Selects for 			performers who are in both the LJ and CH datasets. It also cleans the output so that 		all URIs match the URIs used in the LJ dataset (replaces CH minted URIs)
        
8) CH_relationships.py
	Creates a dictionary of performers (key) and a list of other performers that they 		'played' in the same event with (value).
        
9) WriteCSV_CH.py
	Writes a csv file of the CH relationships, with a row for each relationship. The 		script converts the URIs in the relationshipsCH.json to their foafName equivalents 		for output to the csv.
        -6706 relationships


Step D: Identify subset of relationships that exist in both datasets

10a) No script. 
	Manually combine the LJ csv output from WriteCSV.py and the CH csv output 			from WriteCSV_CH.py

10b) writeCSV_BOTH.py
	Finds the duplicates in the combined csv file and write them to a new csv that 			represents the relationships that exist in both datasets. 
        -293 relationships
        
10c) No script. 
	Import the resulting csv into Gephi as edges file. In Gephi, the edges with weight 		‘2’ are the people who are in both the LJ and CH datasets (the people from the #10b 		csv file.

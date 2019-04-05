sudo pip3 install pyserial


##########################################

import urllib
try:
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except:
    status = "Not connected"
print status
if status == "Connected":
    # do stuff...
will check for internet connection.

##########################################

http://wohnwagen-forum.de/index.php?thread/64365-raspberry-pi-als-controlpanel-mit-steuerungsm%C3%B6glichkeiten/&postID=1268012#post1268012

Da ich nicht viel in den Kästen liegen habe, hab ich kurzerhand jeweils 2 12V- Lüfter angebracht, 
die die Luft aus dem Fußraum in die Kästen bewegen. Die Lüfter werden vormittags und nachmittags 2h automatisch geschalten. 
Als ich das soweit fertig hatte - im Januar mit Heizbetrieb, schließlich will ich ja nicht frieren beim basteln 
- war diese zusätzliche Umluft gar nicht so unangehm. Zufälliger Weise sauge ich die kalte Luft in den toten Ecken an und 
puste die in die durch die "richtige" Umluft aufgewärmten Staukästen. Mit dieser Erkenntnis, habe ich die Steuerung der kleinen Umluft 
an den Betrieb der großen Umluft angepasst. Misst mein Raspi also im Heizungsrohr eine Temperatur von über 33°, sind draussen weniger 
als 18° und ist Spannung über 13V (also wird die Batterie geladen=Landstrom da), pusten die Ventis gemütlich Luft in die Kästen. 
Es sind insgesamt 6 Ventis mit gemütlichen 2000 Umdrehungen/Min. Man hört sie kaum. Trumavent ist lauter.

##########################################
Kühlschranklüfter
50°

2-3° wärmer als außentemp-


https://wohnwagen-otto.jimdo.com/absorberk%C3%BChlschr%C3%A4nke-verbesserte-luftf%C3%BChrung-ohne-l%C3%BCfter/



http://wiki.womoverlag.de/index.php?title=Leitwand_zur_Optimierung_der_K%C3%BChlleistung

https://www.t3-infos.de/t3-infos_f.html#kuehlschr



##########################################

Batterie

Ladezustand 	Nass-Batterie	Gel-Batterie	AGM-Batterie
100%	        12,70V	        > 12,90V	    > 12,85V        grün
90%	            12,65V      	12,85V	        12,80V          grün
70%	            12,50V	        12,60V	        12,55V          grün
60%	            12,40V	        12,50V	        12,50V          grün
50%	            12,30V	        12,45V	        12,40V          gelb
20%	            12,00V	        12,10V	        12,00V          gelb
0%	            < 11.90V	    < 12.00V	    < 12,00V        rot




##########################################
Windchill
windchill = 13.12 + 0.6215 x temperature + (0.3965 x temperature – 11.37) x (windspeed)**0.16

W Windchill in C°
T temp in C°
V wind in kmh
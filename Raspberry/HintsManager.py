# -*- coding: utf-8 -*-
import random
class HintsManager(object):
    def __init__(self):
        self.hints = [
        'Aluminiumfolie reißt nicht so leicht, wenn man sie vor Gebrauch vollflächig auf Rigipsplatten klebt.',
        'Bier hinterlässt keine Rotweinflecken.',
        'Die Wohnung bleibt beim Bohren von Dübellöchern staubfrei, wenn Sie die Wand vorher in den Garten tragen.',
        'Kleine Brandlöcher vom Lagerfeuer entfernt man am besten mit einer Nagelschere.',
        'Brot trocknet nicht aus, wenn man es in einem Eimer mit Wasser lagert.',
        'Fettflecken halten länger, wenn man sie ab und zu mit Butter einreibt.',
        'Salzflecken auf einer Tischdecke bekommt man mit etwas Rotwein wieder heraus.',
        'Rhabarberkompott schmeckt noch besser, wenn man statt Rhabarber Erdbeeren nimmt.',
        'Tränen beim Zwiebelschneiden kann man vermeiden, indem man die Zwiebel durch eine Kohlrabi ersetzt.',
        'Spinat schmeckt erheblich besser, wenn man ihn kurz vor dem Servieren duch ein saftiges Steak ersetzt.',
        'Heißes Wasser braucht man andauernd in der Küche. Deshalb sollte man sich einen kleinen Vorrat davon einfrieren.',
        'Neue Wasserkocher verkalken nicht so schnell, wenn man sein Wasser weiterhin im alten kocht...',
        'Stockflecken in Gartenmöbelauflagen verschwinden, wenn man Ketchup drübergießt.',
        'Kaffeefilter sollte man höchstens dreimal wiederverwenden, es lohnt die Mühe, nach dem 3. Mal frischen Kaffee zu malen.',
        'Messer werden richtig scharf, wenn man Tabasco drauf gießt.',
        'Schmutziges Geschirr schimmelt nicht, wenn es in der Tiefkühltruhe aufbewahrt wird.',
        'Bratkartoffeln werden unvergleichlich kross, wenn man sie beim im Internetstöbern in der Pfanne vergisst.',
        'Fisch wird besonders zart, wenn man ihn vor der Zubereitung, ein paar Tage herum stehen lässt.',
        'Kartoffeln werden herrlich weich, wenn man zum Kochen ein bisschen Wasser zugibt.',
        'Versalzene Suppen schmecken gleich ganz anders, wenn man sie gekonnt anbrennen lässt.',
        'Zu Zwiebel- Kräuterquark und Pellkartoffeln, passt wunderbar Dorschleber in Vanillesoße.',
        'Köche verderben nicht nur den Brei, sie können im Prinzip alle Speisen versauen, wenn man sie höflich darum bittet.',
        'Volle Abfallsäcke erkennt man daran, dass sich der Abfalleimer nicht mehr schließen lässt, sich Millionen von kleinen Mücken sich auf das Butterbrot stürzen und der Platzwart stündlich nach Todesfällen fragt. Abhilfe schafft man, indem man den Müll in den Kühlschrank steckt. ',
        'Mit Senf oder Zahnpasta verschmierte Türklinken lassen sich mittels bromsaurem Radiumbikarbonat mühelos reinigen.',
        'Sticke deinen Vornamen in schwarz auf dein weißes Hemd. Du weißt dann immer, wenn es gewaschen werden muß. Nämlich dann, wenn du deinen Namen nicht mehr lesen kannst. Dieser Trick funktioniert auch mit anderen Farben!',
        'Sollte nach einem Lager beim Waschen der Wäsche diese absolut nicht weiß werden, könnte es sich um Buntwäsche handeln.',
        'Milch bleibt wesentlich länger frisch, wenn man sie in der Kuh belässt.',
        'Hundert-Euro- und andere Geldscheine, die man des öfteren auf der Straße findet, eignen sich hervorragend dazu, die Löcher in der Geldbörse zu stopfen.',
        'Falls Sie Kettenbriefe in der Post finden, denken Sie daran: Nur die Briefe kommen ins Altpapier, die Ketten kommen in die gelbe Tonne.',
        'Weizenbier lässt sich leichter einschenken, wenn man statt Reis ein kleines Seifestück ins Glas tut.',
        'Knäckebrot krümelt nicht mehr, wenn man es kurz vor dem Verzehr in eine Schale lauwarmes Wasser legt. ',
        'Zwiebeln statt Kiwis kaufen! Sie sind länger haltbar und außerdem länger haltbar.',
        'Umwickeln Sie Ihre Glühbirnen doppelt mit Tesafilm. So gibt es keine Scherbenexplosion, falls die Birne aus irgendeinem Grund aus dem Gewinde fallen sollte.',
        'Katzensand im Badezimmer mindert eindeutig die Rutschgefahr. So werden Unfälle während und nach dem Duschen verhindert.',
        'Schmutziges Geschirr schimmelt nicht, wenn man es in der Gefriertruhe aufbewahrt.',
        'Je mehr Käse desto mehr Löcher, je mehr Löcher, desto weniger Käse! Fazit: Je mehr Käse, desto weniger Käse!',
        'Koche Wasser nach Celsius, nicht mehr nach Fahrenheit. Das spart 112 Grad und ist somit gut für die Umwelt.',
        'Teigwaren heißen Teigwaren, weil Teigwaren mal Teig waren.',
        'Zucker ist der Stoff, der dem Kaffee den schlechten Geschmack gibt, wenn man vergisst, ihn reinzutun.',
        'Mit einer Scheibe Salami in der Achselhöhle erstrahlen Schweißränder im Sommer in einem wunderschönen Rot.',
        'Hab Sonne im Herzen und Zwiebeln im Bauch, dann kannst du gut Ferzen und stinken tuts auch.',
        'Kräht der Hahn auf dem Mist, ändert sich das Wetter oder bleibt wie es ist.',
        'Es ist auf jeden Fall besser heimlich schlau zu sein, als unheimlich blöd.',
        'Hast du Zahnpasta im Ohr,kommt dir alles leise vor',
        'Nem geschenkten Barsch guckt man nicht hinter die Kiemen.',
        'Atmen durch den Hintermund, hält Leib und Seele gesund.',
        'Bohnen, Erbsen und auch Linsen bringens Ärschle schnell zum Grinsen!',
        'Aftershave ist nicht das Gegenteil von Mundwasser!'
        ]
        self.vorsatz = [
        'Ich werde einmal die Woche jemandem, der mir nicht sehr nahe ist, ein Geschenk machen.',
        'Ich werde nett zu allen Tieren sein. Auch wenn sie kleiner sind als mein Fingernagel.',
        'Ich werde jeden Tag ein Kompliment an ein vollkommen fremde Person entrichten.',
        'Ich werde für meine eigene Geburtstagsparty nur noch die Hälfte ausgeben und die andere spenden.',
        'Ich werde mein Handy zu festen Zeiten ausschalten, damit ich dann zur Ruhe kommen kann.',
        'Ich werde mir beim Schuster Schuhe für mich anfertigen lassen.',
        'Ich werde jede Mahlzeit genießen, die ich zu mir nehme.',
        'Ich werde eine neue Sportart ausprobieren.',
        'Ich werde mehr Grünzeug essen.',
        'Ich werde nur noch dann den Fernseher anschalten, wenn ich weiß, dass etwas kommt, was ich wirklich sehen möchte.',
        'Ich werde mir selbst ein Kleidungsstück nähen.',
        'Ich werde den Einzelhandel unterstützen, indem ich nur noch, wenn es unumgänglich ist, im Internet bestelle.',
        'Ich werde mich mehr dafür interessieren, was ich jeden Tag esse.',
        'Ich werde eine ungewöhnliche Geldanlage finden, und damit mein monatliches Einkommen aufstocken.',
        'Ich werde die Top 50 der IMDB anschauen. Auch die Filme in schwarz-weiß.',
        'Ich werde das Internet nicht mehr nur so zum Zeitvertreib benutzen.',
        'Ich werde jeden Tag etwas zu lachen haben.',
        'Ich werde einen Kurs in der nächsten Volkshochschule belegen.',
        'Ich werde, wenn ich alleine Auto fahre, die Musik, die ich sonst höre, durch Hörbücher ersetzen.',
        'Ich werde insgesamt viel mehr lesen.',
        'Ich werde auf einer wohltätigen Internetseite entweder ein Patenkind oder ein Patentier suchen, das ich monatlich unterstütze.',
        'Ich werde einen Brieffreund (oder E-Mail-Freund) suchen, mit dem ich mich austausche.',
        'Ich werde eine Woche lang vegan leben.',
        'Ich werde eine neue Sprache lernen. Oder zumindest damit beginnen.',
        'Ich werde entweder Schach oder Backgammon spielen lernen.',
        'Ich werde meinen alten N64 aus dem Keller holen (oder bei Ebay ersteigern) und noch einmal ganz Kind sein.',
        'Ich werde bestimmte Rechtsgrundlagen dieses Landes hinterfragen.',
        'Ich werde lernen, wie man Feuer ohne direkte Hilfsmittel macht.',
        'Ich werde einen Sixpack antrainieren. Und natürlich auch einen passenden sonstigen Körper.',
        'Ich werde statt Vitamintabletten echtes Obst essen.',
        'Ich werde zur Abwechslung auf dem Markt statt im Supermarkt einkaufen gehen.',
        'Ich werde lernen, mit 10 Fingern zu tippen.',
        'Ich werde mutiger sein und so oft wie möglich die Wahrheit sagen.',
        'Ich werde jeden Tag den Artikel des Tages bei Wikipedia lesen.',
        'Ich werde all meine Lieblingslieder, die ich als Teenager hatte, noch einmal in Ruhe anhören.',
        'Ich werde Blut spenden.',
        'Ich werde Kritik nicht mehr persönlich nehmen.',
        'Ich werde weniger Chips, Schokolade und Co essen.',
        'Ich werde mit meinen Kumpels etwas Tolles auf die Beine stellen (z.B. eine Band, einen Kurzfilm, einen Verkaufsstand, …)',
        'Ich werde nicht mehr so laut Musik hören, weil das schlecht für meine Ohren ist.',
        'Ich werde abends öfter alleine weggehen und sehen, was der Abend dann bringt.',
        'Ich werde mit meiner Familie einen Familientag organisieren, bei dem wir alle uns noch einmal sehr nahe kommen können.',
        'Ich werde aus einem Samen eine Pflanze großziehen.',
        'Ich werde lernen, wie man Comics zeichnet.',
        'Ich werde meine Morgende entspannter gestalten, indem ich 30 Minuten eher aufstehe.',
        'Ich werde nur noch Vorsätze umsetzen, die ich selbst für sinnvoll halte.',
        'Ich werde niemanden mehr einfach so beleidigen, sondern viel eher sagen, was mich wirklich an der Person stört.',
        'Ich werde lernen, wie unser Wirtschaftssystem funktioniert.',
        'Ich werde mir bestimmte Zeiten zum Faulsein einrichten, sodass ich sonst produktiver sein kann.',
        'Ich werde meine Wohnung von unnützem Tinnef entrümpeln.',
        'Ich werde mehr darauf achten, meinen Müll richtig zu entsorgen, um so die Umwelt mehr zu schonen.',
        'Ich werde meine Kaffeesucht schmälern, indem ich den ersten Morgenkaffee durch schwarzen oder grünen Tee ersetze.',
        'Ich werde meine Großeltern zu ihrem Leben befragen, solange es noch geht.',
        'Ich werde Ölfarben kaufen und mit meiner Freundin zusammen auf einer überdimensionalen Leinwand ein abstraktes Bild malen.',
        'Ich werde meine Freundin öfter fragen, wie sie sich fühlt und was sie sich von unserer Beziehung wünscht.',
        'Ich werde Hausarbeiten nicht mehr so lange wie möglich vor mir herschieben, sodass ich mich jedes Mal schämen muss, wenn jemand überraschend zu Besuch kommt.',
        'Ich werde dieses Jahr etwas Besonderes machen.',
        'Ich werde auch, wenn ich alleine esse, mich so verhalten, als wäre jemand dabei.',
        'Ich werde ein Jahr lang Tagebuch führen.',
        'Ich werde mir keine Pornos mehr anschauen.',
        'Ich werde lernen, selber Brot zu backen.',
        'Ich werde einen Obdachlosen auf einen Kaffee einladen.',
        'Ich werde ein Jahr lang auf alkoholische Getränke verzichten.',
        'Ich werde einen Yogakurs besuchen.',
        'Ich werde nur noch 3-4x pro Woche das Auto benutzen und sonst zu Fuß gehen.',
        'Ich werde meine größte Schwäche identizifieren und loswerden.',
        'Ich werde ein Jahr lang auf Parfüm verzichten.',
        'Ich werde Obst und Gemüse nur noch frisch vom Markt kaufen.',
        'Ich werde nichts Illegales mehr herunterladen (Musik, Filme, Software, etc).',
        'Ich werde mich in der lokalen Politik engagieren.',
        'Ich werde darauf achten, dass meine Kleidung unter humanen Bedingungen hergestellt wurde.',
        'Ich werde ein Jahr lang keine Nachrichten mehr gucken.',
        'Ich werde dieses Jahr mindestens ein Musikal, eine Oper oder ein klassisches Konzert besuchen.',
        'Ich werde 3000 Kilometer mit dem Fahrrad fahren.',
        'Ich werde meine Mutter mit meinem Lieblingsessen aus meiner Kindheit bekochen.',
        'Ich werde alle Menschen nur noch duzen.',
        'Ich werde meine Krankheiten eher mit ein paar ruhigen Tagen als mit Antibiotika behandeln.',
        'Ich werde auf Flüge mit umweltfeindlichen Billig-Airlines verzichten.',
        'Ich werde eine Woche nur mit meinem Zelt in der Natur verbringen.',
        'Ich werde meine Wäsche nur noch per Hand waschen.',
        'Ich werde mich einen Monat lang nicht rasieren.',
        'Ich werde meinen Mitmenschen gegenüber rücksichtsvoll sein.',
        'Ich werde ins Bett gehen, wenn es dunkel wird, und aufstehen, wenn es hell wird.',
        'Ich werde Traditionen nicht mehr um der Tradition willen befolgen.',
        'Ich werde mir ein echtes Kunstwerk von einem unbekannten Künstler in die Wohung hängen.',
        'Ich werde eine Meditationstechnik erlernen, die mir in stressigen Situationen weiterhilft.',
        'Ich werde einen Baum pflanzen.',
        'Ich werde ein Ehrenamt übernehmen.',
        'Ich werde 10% meines Einkommens für einen guten Zweck spenden.',
        'Ich werde immer so lange mit dem Essen warten, bis ich wirklich hungrig bin.',
        'Ich werde ein Jahr lang keine SMS mehr verschicken.',
        'Ich werde mich, wenn mir kalt ist, wärmer anziehen, anstatt die Heizung aufzudrehen.',
        'Ich werde einen Salsa-Tanzkurs belegen.',
        'Ich werde lernen zu jonglieren.',
        'Ich werde am Ende des Jahres nachprüfen, welchen Vorsätzen ich treu geblieben bin.',
        'Ich werde – soweit wie möglich – alle meine technischen Geräte durch energiesparende Versionen ersetzen.',
        'Ich werde meinen Eltern dafür danken, dass sie mich großgezogen haben.',
        'Ich werde mich für Menschen einsetzen, die ungerecht behandelt werden – auch für mich selber.',
        'Ich meinen Ipod verschenken und statt ständig Musik zu hören, lieber nachdenken oder ein Buch lesen.',
        'Ich werde meinen 08/15 Job an den Nagel und statt dessen meinen Traum leben.'
        ]
    
    def get_hint(self):
        return self.hints[random.randint(0, len(self.hints))]
    
    def get_vorsatz(self):
        return self.vorsatz[random.randint(0, len(self.vorsatz))]
        
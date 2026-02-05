###Use Case: "Essen Online Bestellen"

* Use Case Name     : Bestellung von Speisen über eine Essensbestellungs-App
* Akteure           : Kunde/Kundin, Essensbestellungs-App, Restaurant-System
* Ziel              : Der Kunde bestellt Essen über die App und bezahlt die Bestellung erfolgreich, sodass das Restaurant die zubereitung starten kann. 
* Vorbedingungen    : 
                        1. Der Kunde hat die App geöffnet. 
                        2. Der Kunde ist registriert oder nutzt die Gastbestellung.
                        3. Das Restaurant ist geöffnet und nimmt Bestellungen an.
                        4. Die gewünschten Speisen sind verfügbar
* Nachbedingungen   :
                        1. Die Bestellung ist im System gespeichert
                        2. Die Zahlung wurde erfolgreich durchgeführt oder zur Barzahlung markiert.
                        3. Das Restaurant erhält die Bestellung zur Zubereitung.
                        4. Der Kunde erhält eine Bestellbestätigung mit Bestellnummer.
* Hauptablauf       :
                        1. Der Kunde öffnet die Essensbestellungs-App.
                        2. Der Kunde wählt ein Restaurant aus.
                        3. Der Kunde durchsucht die Speisekarte.
                        4. Der Kunde legt gewünschte Speisen in den Warenkorb.
                        5. Der Kunde überprüft den Warenkorb.
                        6. Der Kunde gibt Lieferadresse oder Abholoption an.
                        7. Der Kunde wählt eine Zahlungsmethode.
                        8. Der Kunde bestätigt die Bestellung.
                        9. Das System überprüft die Zahlung.
                        10.Die Bestellung wird an das Restaurant übermittelt.
                        11.Der Kunde erhält eine Bestellbestätigung.
* Alternativabläufe :
                        A1: Kunde ändert Bestellung im Warenkorb
                            - Der Kunde entfernt oder ergänzt Speisen vor der Bestätigung
                            - Das System aktualisiert den Gesamtpreis
                        A2: Barzahlung ausgewählt
                            - Der Kunde wählt "Barzahlung bei Lieferung"
                            - Das System überspringt die Online-Zahlung.
                        A3: Abholung statt Lieferung
                            - Der Kunde wählt "Selbstabholung"
                            - Das System zeigt Abholzeit und Adresse an.
* Ausnahmen         :
                        E1: Zahlung fehlgeschlagen
                            - Das Bezahlsystem meldet einen Fehler.
                            - Die Bestellung wird nicht abgeschlossen.
                            - Der Kunde wird aufgefordert, eine andere Zahlungsmethode zu wählen.
                        E2: Restaraunt nimmt keine Bestellungen an
                            - Das System informiert den Kunden über die Schließung.
                            - Der Use Case wird beendet.
                        E3: Artikel nicht mehr verfügbar
                            - Das System zeigt eine Fehlermeldung an
                            - Der Kunde kann alternative Speisen auswählen
                        E4: Technischer Fehler im System
                            - Die Bestellung kann nicht gespeichert werden.
                            - Der Kunde erhält eine entsprechende Fehlermeldung.


###User Story Übung

* User Story 1

    *Titel              : Aufgabe erstellen
    *Beschreibung       : Als Student möchte ich eine neue Aufgabe in meiner To-do-Liste erstellen, damit ich meine Studienaufgaben organisiert festhalten kann.
    *Akzeptanzkriterien : 
                            1. Der Student kann einen Titel für die Aufgabe eingeben.
                            2. Der Student kann ein Fälligkeitsdatum für die Aufgabe festlegen.
                            3. Die Aufgabe wird nach dem Speichern in der To-do-Liste angezeigt.
                            4. Die Aufgabe bleibt auch nach dem erneuten Öffnen der App gespeichert.
* User Story 2

    Titel              : Aufgabe als erledigt markieren
    Beschreibung       : Als Student möchte ich eine erledigte Aufgabe als abgeschlossen markieren, damit ich den Überblick über meine offenen Aufgaben behalte.
    Akzeptanzkriterien : 
                            1. Der Student kann eine Aufgabe als „erledigt“ markieren.
                            2. Erledigte Aufgaben werden visuell von offenen Aufgaben unterschieden (z. B. durch Durchstreichen).
                            3. Die Aufgabe wird nach dem Markieren nicht mehr in der Liste der offenen Aufgaben angezeigt.
                            4. Der Status der Aufgabe bleibt auch nach einem Neustart der App erhalten.

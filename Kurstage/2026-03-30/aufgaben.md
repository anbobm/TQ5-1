# Aufgabe 1 - Aktivitätsdiagramm Warenlager

Modelliere den Prozess eines automatisierten Warenlagers: Produktanfrage, Lagerroboter sucht das Produkt, Produkt wird entnommen, Verpackung, Versandvorbereitung.

Füge Schleifen für Fehlerbehandlung (z.B. Produkt nicht gefunden) hinzu.


# Aufgabe 2 - Aktivitätsdiagramm Onboarding

Das Unternehmen führt einen Prozess zur Aufnahme einer neuen Mitarbeiterin bzw. eines neuen Mitarbeiters durch. Modellieren Sie diesen Prozess als UML-Aktivitätsdiagramm. Der Prozess enthält mehrere parallele Abschnitte und ist wie folgt beschrieben:

* Eine neue Mitarbeiterin wird eingestellt.
* Der HR-Mitarbeiter startet die Mitarbeiteraufnahme.
* Personaldaten erfassen (Name, Adresse, Steuer-ID etc.).
* Falls Unterlagen wie Ausweis, Steuerbescheinigung oder Arbeitsvertrag fehlen, wird die Mitarbeiterin aufgefordert, diese nachzureichen.
Der Prozess geht erst weiter, wenn die Unterlagen vollständig sind.
* Sobald alle Dokumente vollständig sind, werden drei parallele Prozesse gestartet:
  * IT-Zugang einrichten: Benutzerkonto anlegen, E-Mail-Adresse erstellen, Zugriffsrechte und Gruppen zuweisen
  * Sicherheitsfreigabe vorbereiten: Zutrittskarte erstellen, Zugangsbereiche definieren, Sicherheitsunterweisung
  * HR-System vorbereiten: Mitarbeiter im Zeiterfassungssystem eintragen, Abrechnungsdaten einpflegen, Personalakte anlegen
* Alle drei parallelen Tätigkeiten müssen abgeschlossen sein, bevor der Prozess fortfährt.
* Anschließend beginnt eine weitere Phase, bei der folgende zwei Prozesse wieder parallel ablaufen:
  * Arbeitsplatz vorbereiten: Arbeitsplatz zuweisen, Arbeitsplatz ausstatten (Laptop, Dockingstation, Monitor(e), Telefon, etc.), Software installieren
  * Onboarding-Material erstellen: Willkommenspaket zusammenstellen, Schulungsmaterial bereitstellen, Termin für Orientierungstag buchen
* erst nach Abschluss beider Prozesse:
* Mitarbeitende willkommen heißen
* Begrüßung durch HR
* Übergabe der Zugangs- und Arbeitsplatzinformationen


# Aufgabe 3 - Aktivitätsdiagramm Flugbuchung

Entwirf ein UML-Aktivitätsdiagramm für ein Flugbuchungssystem. Der Kunde kann Flüge suchen, einen Flug auswählen, zusätzliche Services hinzufügen, eine Zahlung durchführen und eine Buchungsbestätigung erhalten. Beachten Sie die folgenden Schritte und Entscheidungsstellen:

## Szenario-Details

1. Flüge suchen:
    * Der Kunde gibt Abflug- und Zielort, Datum und Anzahl der Passagiere ein.
    * Das System zeigt verfügbare Flüge an.
    * Wenn keine Flüge verfügbar sind, kann der Kunde die Suche ändern oder den Vorgang abbrechen.
2. Flug auswählen:
    * Der Kunde wählt einen Flug aus den Suchergebnissen aus.
    * Wenn kein Flug ausgewählt wird, wird der Kunde zur Suche zurückgeleitet oder kann abbrechen.
3. Zusatzservices hinzufügen (optional):
    * Der Kunde kann zusätzliche Services auswählen, wie z. B.:
        * Sitzplatzreservierung
        * Aufgabegepäck
        * Mahlzeiten
    * Der Kunde kann auch ohne Zusatzservices fortfahren.
4. Passagierdaten eingeben:
    * Der Kunde gibt persönliche Daten (z. B. Name, Geburtsdatum, Reisepassnummer) für jeden Passagier ein.
    * Das System prüft die Vollständigkeit und Validität der Daten.
5. Zahlung durchführen:
    * Der Kunde wählt eine Zahlungsmethode: Kreditkarte, PayPal oder Banküberweisung.
    * Bei der Kreditkarte:
    * Kartendetails werden validiert.
    * Bei Fehlschlag kann der Kunde die Daten korrigieren oder eine andere Methode wählen.
    * Bei PayPal:
    * Der Kunde wird zu PayPal weitergeleitet.
    * Authentifizierung kann bei Fehlschlag erneut durchgeführt werden.
    * Bei Banküberweisung:
    * Der Kunde erhält Zahlungsanweisungen, die manuell durchgeführt werden müssen.
6. Buchungsbestätigung:
    * Nach Abschluss der Zahlungsmethode erstellt das System die Buchung
    * Der Kunde erhält Buchungsbestätigung per E-Mail.

# Aufgabe 4 - Aktivitätsdiagramm Bibliothek

Für die Entwicklung einer Verwaltungssoftware für eine Bibliothek soll der Ausleih- und Rückgabeprozess modelliert werden.
Dazu soll der Ablauf dieses Prozesses in einem UML-Aktivitätsdiagramm dargestellt werden.

Um den Ablauf vollständig zu erfassen, sind Gespräche mit den beteiligten Stellen erfolgt und Sie haben jeweils folgende Informationen erhalten.

Ausleihtheke:
Ein Benutzer wählt aus dem Bestand der Bibliothek ein Medium aus und geht mit diesem zur Ausleihtheke.
Dort muss er zunächst seinen Benutzerausweis vorlegen. Wenn er noch keinen besitzt, muss er sich zuerst registrieren und erhält einen Benutzerausweis.
Anschließend wird das Medium ausgeliehen. Dazu wird vorher geprüft, ob offene Mahngebühren vorhanden sind. Sind sie vorhanden, müssen sie vor der Ausleihe bezahlt werden. Abschließend wird das Medium im System als ausgeliehen markiert und der Benutzer kann mit dem Medium die Bibliothek verlassen.

Rückgabestelle:
Bei der Rückgabe wird jedes Medium gescannt. Das System prüft dann automatisch, ob die Rückgabe innerhalb der Rückgabefrist erfolgt ist. Bei verspäteter Rückgabe werden Mahngebühren erhoben und dem Benutzerkonto hinzugefügt. Anschließend wird das Medium im System wieder als verfügbar markiert.
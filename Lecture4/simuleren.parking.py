import heapq

class PriorityQueue:
    """
    Eenvoudige priority queue rond heapq.
    In Dodona krijg je deze meestal al, dan moet je dit stukje niet opnieuw schrijven.
    """

    def __init__(self):
        # De interne lijst waarin de heap wordt opgeslagen
        self.content = []

    def add(self, item):
        # Voeg een element toe aan de heap, automatisch gesorteerd
        heapq.heappush(self.content, item)

    def peek(self):
        # Kijk naar het "kleinste" element (prioriteit) zonder het weg te nemen
        return self.content[0] if self.content else None

    def poll(self):
        # Haal het element met de hoogste prioriteit eruit
        return heapq.heappop(self.content) if self.content else None

    def is_empty(self):
        # True als er geen elementen meer in de queue zitten
        return len(self.content) == 0

    def __str__(self):
        # Handige representatie om de inhoud te inspecteren
        return str(heapq.nsmallest(len(self.content), self.content))


def simuleer_parking(plaatsen: int, bloktijd: int, klanten: list) -> int:
    """
    Simuleer de parking.

    plaatsen : aantal parkeerplaatsen (max # auto's tegelijk)
    bloktijd : tijd die een klant nodig heeft om 'een blokje rond' te rijden
    klanten  : lijst van tuples (aankomsttijd, winkellengte)

    We geven terug:
        het tijdstip waarop de LAATSTE klant vertrekt (parking weer leeg is).
    """

    # ---- 1. EVENTS & PRIORITY QUEUE --------------------------------------
    #
    # We werken met 'events'. Elk event is een tuple:
    #
    #   (tijd, event_type, winkellengte, klantID)
    #
    # waarbij:
    #   - tijd: op welk moment gebeurt dit event?
    #   - event_type: 0 = vertrek, 1 = aankomst
    #       → zo komt vertrek vóór aankomst als de tijden gelijk zijn
    #   - winkellengte: enkel nuttig voor aankomsten (zodat kortste eerst kan)
    #   - klantID: index in de klanten-lijst (0, 1, 2, ...)
    #
    # Omdat het gewone tuples zijn, zal heapq deze in volgende volgorde sorteren:
    #   eerst op tijd, dan op event_type, dan op winkellengte, dan op klantID.
    #
    pq = PriorityQueue()

    # ---- 2. WINKELDUUR PER KLANT BIJHOUDEN -------------------------------
    #
    # durations[i] = winkellengte van klant i
    #
    durations = []

    # ---- 3. EERSTE AANKOMST-EVENTS AANMAKEN ------------------------------
    #
    # klanten = [(aankomst0, duur0), (aankomst1, duur1), ...]
    # enumerate(klanten) geeft:
    #   (0, (aankomst0, duur0))
    #   (1, (aankomst1, duur1))
    #   ...
    # klantID = index, (aankomst, duur) = tuple uit lijst
    #
    for klantID, (aankomst, duur) in enumerate(klanten):
        # Bewaar de winkeltijd zodat we die later altijd kunnen opvragen
        durations.append(duur)

        # Maak het eerste AANKOMST-event voor deze klant
        # event_type = 1 → aankomst
        event = (aankomst, 1, duur, klantID)

        # Stop het event in de priority queue
        pq.add(event)

    # ---- 4. SIMULATIE-STATE ----------------------------------------------
    #
    bezet = 0            # hoeveel parkeerplaatsen zijn momenteel in gebruik?
    laatste_vertrek = 0  # tijdstip van de laatste vertrek-actie die we zien

    # ---- 5. VERWERK EVENTS IN CHRONOLOGISCHE VOLGORDE --------------------
    #
    while not pq.is_empty():
        # Haal het eerstvolgende event met de hoogste prioriteit uit queue
        tijd, event_type, duur, klantID = pq.poll()

        # ---- 5a. VERTREK-EVENT ------------------------------------------
        if event_type == 0:
            # Een auto vertrekt → 1 plaats komt vrij
            bezet -= 1

            # Tijd van dit vertrek kan de laatste zijn
            if tijd > laatste_vertrek:
                laatste_vertrek = tijd

        # ---- 5b. AANKOMST-EVENT -----------------------------------------
        else:
            # Er is minstens één plaats vrij
            if bezet < plaatsen:
                # Klant kan parkeren
                bezet += 1

                # Wanneer vertrekt deze klant? Nu + zijn winkeltijd
                vertrektijd = tijd + durations[klantID]

                # Maak een VERTREK-event: event_type = 0, winkellengte is hier niet meer relevant
                vertrek_event = (vertrektijd, 0, 0, klantID)

                # Voeg het vertrek-event toe aan de queue
                pq.add(vertrek_event)

            else:
                # Parking is vol → klant rijdt een blokje rond en komt terug
                nieuwe_tijd = tijd + bloktijd

                # Nieuw AANKOMST-event op later tijdstip
                nieuwe_event = (nieuwe_tijd, 1, durations[klantID], klantID)
                pq.add(nieuwe_event)

    # Als alle events verwerkt zijn, is 'laatste_vertrek' het tijdstip
    # waarop de laatste klant vertrok → parking is weer volledig leeg.
    return laatste_vertrek

# ============================================================
# MATCH ANALYSIS - VOLLEDIGE OPLOSSING MET EXTENSIEVE COMMENTAAR
# ============================================================


# ------------------------------------------------------------
# DEEL 1 — PLAYER
# ------------------------------------------------------------

class Player:
    """
    Klasse voor één speler.

    Attributen:
        - name   : de naam van de speler (string)
        - number : het rugnummer van de speler (int)
    """

    def __init__(self, name: str, number: int):
        # Bewaar de naam van de speler
        self.name = name

        # Bewaar het shirtnummer van de speler
        self.number = number

    def __eq__(self, other):
        """
        __eq__ bepaalt wat er gebeurt bij:   p1 == p2

        Volgens de opgave:
        Twee spelers zijn gelijk als:
            - other ook een Player-object is
            - de NAME gelijk is
        Het nummer speelt GEEN rol.

        Waarom NotImplemented?
            → zodat Python snapt dat het niet weet hoe te vergelijken.
        """
        if not isinstance(other, Player):
            return NotImplemented  # Python moet weten dat dit geen geldige vergelijking is

        # Vergelijk enkel op naam
        return self.name == other.name

    def __lt__(self, other):
        """
        __lt__ wordt gebruikt voor sorteren:
            sorted(players)

        Vergelijking: speler met lager rugnummer komt eerst.
        """
        if not isinstance(other, Player):
            return NotImplemented

        # Vergelijk op shirt number
        return self.number < other.number

    def __str__(self):
        """
        Tekstweergave van een Player-object.

        Bijvoorbeeld: "Eden Hazard (10)"
        """
        return f"{self.name} ({self.number})"


# ------------------------------------------------------------
# DEEL 2 — PASS
# ------------------------------------------------------------

class Pass:
    """
    Een Pass stelt 1 verbinding (edge) in de graaf voor.

    Attributen:
        - sender       : Player die de pass geeft
        - receiver     : Player die de pass ontvangt
        - nr_of_times  : aantal keren dat deze pass gebeurde
    """

    def __init__(self, sender: Player, receiver: Player, nr_of_times: int):
        # Bewaar Player die passeert
        self.sender = sender

        # Bewaar Player die ontvangt
        self.receiver = receiver

        # Hoe vaak deze pass voorkomt
        self.nr_of_times = nr_of_times

    def get_weight(self):
        """Return het aantal keren dat deze pass is gebeurd."""
        return self.nr_of_times

    def get_start(self):
        """Return de sender."""
        return self.sender

    def get_end(self):
        """Return de receiver."""
        return self.receiver

    def __eq__(self, other):
        """
        Twee passes zijn gelijk als:
            - same sender
            - same receiver
        times speelt GEEN rol.
        """
        if not isinstance(other, Pass):
            return NotImplemented

        return (self.sender == other.sender and
                self.receiver == other.receiver)

    def __str__(self):
        """Return mooie string voor debug/output."""
        return f"Pass from {self.sender} to {self.receiver}"


# ------------------------------------------------------------
# DEEL 3 — PASSGRAPH
# ------------------------------------------------------------

class PassGraph:
    """
    De graafstructuur op basis van adjacency list.

    Interne structuur:
        - self._players  : lijst van ALLE spelers
        - self.adj       : dictionary

          self.adj =
              {
                "Eden Hazard":    [Pass(EH -> MD), Pass(EH -> RL)],
                "Kevin De Bruyne":[Pass(KDB -> EH)]
              }
    """

    # -------------------------
    # CONSTRUCTOR
    # -------------------------

    def __init__(self, path_name=None):
        """
        Als path_name None is → lege graaf.
        Als path_name een pad is → laadt automatisch het .txt bestand in.
        """
        # Lijst met alle Player-objecten
        self._players: list[Player] = []

        # adjacency dictionary: sender_name → lijst Pass-objecten
        self.adj: dict[str, list[Pass]] = {}

        # Als een pad werd meegegeven → meteen inladen
        if path_name is not None:
            self.load_from_txt(path_name)

    # -------------------------
    # BASISOPERATIES
    # -------------------------

    def add_player(self, player: Player):
        """
        Voeg speler toe *als de naam nog niet bestaat*.
        """

        # CONTROLEREN OF PLAYER AL BESTAAT
        for existing in self._players:
            if existing.name == player.name:
                # Als er al een speler bestaat met deze naam → stop
                return

        # ANDERS TOEV OEGEN
        self._players.append(player)

        # Elke speler heeft altijd een lege lijst van uitgaande passes
        # zelfs als hij er nog geen heeft gegeven
        if player.name not in self.adj:
            self.adj[player.name] = []

    def has_player(self, speler):
        """
        Controleer of speler in de graaf zit.

        speler kan zijn:
            - Player object
            - string (naam)

        We halen altijd eerst de naam eruit, want namen zijn uniek.
        """

        # Haal naam op uit Player of string
        if isinstance(speler, Player):
            name = speler.name
        else:
            name = speler

        # Controleren of er een Player bestaat met deze naam
        for p in self._players:
            if p.name == name:
                return True

        return False

    def get_player(self, name: str):
        """
        Zoek speler op basis van naam en retourneer het object.
        Return None als de speler niet bestaat.
        """
        for p in self._players:
            if p.name == name:
                return p
        return None

    def add_pass(self, sender: Player, receiver: Player, times=1):
        """
        Voeg pass toe van sender naar receiver.
        - Beide spelers moeten bestaan
        - times > 0
        - Als pass al bestaat → weight verhogen
        """

        # times <= 0 betekent dat dit geen geldige input is → negeren
        if times <= 0:
            return

        # Als spelers niet bestaan → niets toevoegen
        if not self.has_player(sender) or not self.has_player(receiver):
            return

        # Haal naam op voor dictionary-key
        sender_name = sender.name

        # Zorg dat sender een entry heeft in de adjacency list
        if sender_name not in self.adj:
            self.adj[sender_name] = []

        # Zoek of er al een pass bestaat
        for pas in self.adj[sender_name]:
            # Same receiver?
            if pas.receiver.name == receiver.name:
                pas.nr_of_times += times   # Weight verhogen
                return

        # Indien niet gevonden → nieuwe pass toevoegen
        self.adj[sender_name].append(Pass(sender, receiver, times))

    def get_pass(self, sender_name, receiver_name):
        """
        Zoek een pass op basis van twee strings (namen).
        Return Pass-object of None.
        """
        if sender_name not in self.adj:
            return None

        # Loop alle passes na
        for pas in self.adj[sender_name]:
            if pas.receiver.name == receiver_name:
                return pas

        return None

    def neighbors(self, sender_name):
        """
        Alle uitgaande passes van één speler.
        """
        if sender_name not in self.adj:
            return []
        return self.adj[sender_name]

    # -------------------------
    # ANALYSE FUNCTIES
    # -------------------------

    def total_weight(self, subset):
        """
        Totaal aantal passes waarbij
            - sender en receiver in subset zitten.

        subset kan zijn:
            - None  → neem ALLE spelers
            - lijst van namen (strings)
        """

        # Indien subset None is → alles gebruiken
        if subset is None:
            subset_names = [p.name for p in self._players]
        else:
            subset_names = subset

        total = 0  # accumulator

        # Voor elke zender in de graaf
        for sender_name, passes in self.adj.items():

            # sender moet in subset zitten
            if sender_name not in subset_names:
                continue  # sla deze sender over

            # Voor elke pass van deze zender
            for pas in passes:
                receiver_name = pas.receiver.name

                # receiver ook in subset?
                if receiver_name in subset_names:
                    total += pas.nr_of_times  # weight optellen

        return total

    def pass_intensity(self, subset=None):
        """
        Intensiteit = totaal passes binnen subset /
                      (maximaal aantal mogelijke gerichte passes)

        Max mogelijke passes:
            n spelers → n * (n-1) mogelijke gerichte passes
        """

        # Zelfde aanpak: subset None = alle spelers
        if subset is None:
            subset_names = [p.name for p in self._players]
        else:
            subset_names = subset

        n = len(subset_names)

        # Minder dan 2 spelers → intensiteit = 0.0
        if n < 2:
            return 0.0

        numerator = self.total_weight(subset_names)
        denominator = n * (n - 1)

        return numerator / denominator

    def top_pairs(self, k=5):
        """
        Returneer de top k passes met hoogste nr_of_times.
        """

        all_passes = []

        # Verzamel ALLE passes uit de graaf
        for passes in self.adj.values():
            for pas in passes:
                all_passes.append(pas)

        # Sorteer dalend
        all_passes.sort(key=lambda p: p.nr_of_times, reverse=True)

        # Neem de eerste k elementen
        return all_passes[:k]

    def distribution_from(self, sender_name):
        """
        Returneer lijst (receiver_name, count)
        gesorteerd dalend op count.
        """

        if sender_name not in self.adj:
            return []

        result = []

        for pas in self.adj[sender_name]:
            receiver = pas.receiver.name
            count = pas.nr_of_times
            result.append((receiver, count))

        # Sorteren op count (index 1)
        result.sort(key=lambda pair: pair[1], reverse=True)

        return result

    # -------------------------
    # DEEL 4 – OPSLAAN EN INLEZEN
    # -------------------------

    def players(self):
        """
        Geef een KOPIE van de spelerslijst terug.
        (zodat niemand de interne lijst accidenteel wijzigt)
        """
        return list(self._players)

    def passes(self):
        """
        Geef een lijst met ALLE Pass-objecten in de graaf.
        """
        all_passes = []
        for passes in self.adj.values():
            for pas in passes:
                all_passes.append(pas)
        return all_passes

    def load_from_txt(self, path):
        """
        Lees graaf in volgens formaat:

        [PLAYERS]
        name;number
        ...

        [PASSES]
        name1 -> name2 : times
        """
        with open(path, "r", encoding="utf-8") as f:

            current_section = None  # houdt bij waar we zitten

            for line in f:
                line = line.strip()

                # lege regel / comment → skip
                if line == "" or line.startswith("#"):
                    continue

                # sectiestart herkennen
                if line == "[PLAYERS]":
                    current_section = "players"
                    continue

                if line == "[PASSES]":
                    current_section = "passes"
                    continue

                if current_section is None:
                    raise ValueError("Onbekende sectie vóór [PLAYERS]")

                # ---------------- PLAYERS ----------------
                if current_section == "players":

                    if ";" not in line:
                        raise ValueError("Ongeldige speler-regel")

                    name, number = line.split(";")

                    name = name.strip()
                    number = number.strip()

                    try:
                        number = int(number)
                    except:
                        raise ValueError("Nummer moet een geheel getal zijn")

                    # Speler toevoegen
                    self.add_player(Player(name, number))

                # ---------------- PASSES -----------------
                elif current_section == "passes":

                    if "->" not in line or ":" not in line:
                        raise ValueError("Ongeldige pass-regel")

                    left, times_str = line.split(":")
                    sender_name, receiver_name = left.split("->")

                    sender_name = sender_name.strip()
                    receiver_name = receiver_name.strip()
                    times_str = times_str.strip()

                    # parse times
                    try:
                        times = int(times_str)
                        if times <= 0:
                            raise ValueError()
                    except:
                        raise ValueError("Aantal times moet positief geheel getal zijn")

                    # bestaan beide spelers?
                    if not self.has_player(sender_name) or not self.has_player(receiver_name):
                        raise ValueError("Pass verwijst naar onbekende speler")

                    sender = self.get_player(sender_name)
                    receiver = self.get_player(receiver_name)

                    self.add_pass(sender, receiver, times)

    def save_to_txt(self, path):
        """
        Sla graaf op in exact het gegeven formaat.
        """
        with open(path, "w", encoding="utf-8") as f:

            # eerst players
            f.write("[PLAYERS]\n")
            for p in self._players:
                f.write(f"{p.name};{p.number}\n")

            # dan passes
            f.write("[PASSES]\n")
            for sender_name, passes in self.adj.items():
                for pas in passes:
                    f.write(f"{pas.sender.name} -> {pas.receiver.name} : {pas.nr_of_times}\n")


# ------------------------------------------------------------
# TEST – Deel 3
# ------------------------------------------------------------

def test_passgraph():
    print("\n--- Test PassGraph ---")

    pg = PassGraph()

    p1 = Player("Eden Hazard", 10)
    p2 = Player("Moussa Dembele", 19)
    p3 = Player("Romelu Lukaku", 9)
    p4 = Player("Jan Vertonghen", 5)

    # spelers toevoegen
    pg.add_player(p1)
    pg.add_player(p2)
    pg.add_player(p3)
    pg.add_player(p4)

    # passes toevoegen
    pg.add_pass(p1, p2, 3)
    pg.add_pass(p1, p3, 2)
    pg.add_pass(p2, p3, 4)
    pg.add_pass(p3, p1, 1)
    pg.add_pass(p3, p4, 5)
    pg.add_pass(p4, p1, 2)

    # testen
    print("Total weight ALL:", pg.total_weight(None))

    subset = ["Eden Hazard", "Moussa Dembele", "Romelu Lukaku"]
    print("Total weight subset:", pg.total_weight(subset))

    print("Intensity ALL:", pg.pass_intensity())
    print("Intensity subset:", pg.pass_intensity(subset))

    print("Top pairs (3):")
    for pas in pg.top_pairs(3):
        print("   ", pas, "->", pas.nr_of_times)

    print("Distribution from Romelu Lukaku:")
    for name, count in pg.distribution_from("Romelu Lukaku"):
        print("   ", name, ":", count)


# ------------------------------------------------------------
# TEST – Deel 4 (opslaan en opnieuw inladen)
# ------------------------------------------------------------

def test_passgraph_file():
    print("\n--- Test opslaan & inladen ---")

    g = PassGraph()

    p1 = Player("Eden Hazard", 10)
    p2 = Player("Moussa Dembele", 19)
    p3 = Player("Jan Vertonghen", 5)
    p4 = Player("Romelu Lukaku", 9)

    g.add_player(p1)
    g.add_player(p2)
    g.add_player(p3)
    g.add_player(p4)

    g.add_pass(p1, p2, 3)
    g.add_pass(p1, p2, 2)  # zelfde pass → weight 5
    g.add_pass(p1, p4, 1)
    g.add_pass(p3, p4, 2)
    g.add_pass(p2, p3, 1)
    g.add_pass(p4, p1, 4)

    g.save_to_txt("team.txt")

    g2 = PassGraph("team.txt")

    print("Spelers ingelezen:")
    for p in g2.players():
        print("  ", p)

    print("Passes ingelezen:")
    for pas in g2.passes():
        print("  ", pas, "->", pas.nr_of_times)


# ------------------------------------------------------------
# RUN TESTS
# ------------------------------------------------------------
if __name__ == "__main__":
    test_passgraph()
    test_passgraph_file()

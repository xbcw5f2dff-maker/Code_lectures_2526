class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        # True als other ook een Player is EN de name gelijk is
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name

    def __lt__(self, other):
        # True als self een lager shirtnummer heeft dan other
        if not isinstance(other, Player):
            return NotImplemented
        return self.number < other.number

    def __str__(self):
        return f"{self.name} ({self.number})" #geeft de speler weer als Naam(nummer)

def test_player(): #test 1
    # 1. Creëer drie speler-objecten en plaats ze in een lijst
    p1 = Player("Eden Hazard", 10)
    p2 = Player("Kevin De Bruyne", 17)
    p3 = Player("Romelu Lukaku", 9)

    players = [p1, p2, p3]

    # 2. Print één van de objecten
    print(p1)

    # 3. Test de __eq__ methode
    print(p1 == p2)
    print(p1 == Player(name="Eden Hazard", number=10))

    # 4. Test de __lt__ methode via sorted()
    sorted_players = sorted(players)

    # 5. Print de gesorteerde lijst
    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    test_player()


class Pass:
    def __init__(self, sender: Player, receiver: Player, nr_of_times: int):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times

    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender

    def get_end(self):
        return self.receiver

    def __eq__(self, other): #standaard methode om te kijken of a == b met A = self en b = other
        if not isinstance(other, Pass): #testen of other wel een pass object is
            return NotImplemented
        # twee passes zijn gelijk als ze dezelfde sender en receiver hebben
        return (self.sender == other.sender
                and self.receiver == other.receiver)

    def __str__(self):
        return f"Pass from {self.sender} to {self.receiver}"

def test_pass(): #test 2
    #1. maak 3 player objecten aan
    p1 = Player("Eden Hazard", 10)
    p2 = Player("Moussa Dembele", 9)
    p3 = Player("Romelu Lukaku", 9)

    #2. maak 3 pass objecten aan
    pass1 = Pass(p1, p2, 3)
    pass2 = Pass(p2, p3, 2)
    pass3 = Pass(p1, p2, 7)

    #3. print 1 pass object
    print(pass1)
    #4. test eq-methode
    print(pass1 == pass2)
    print(pass1 == Pass(p1, p2, 3))

    #5. Test de get_weight methode
    print("weight pass1:", pass1.get_weight()) #verwacht 3
    print("weight pass2:", pass2.get_weight())

if __name__ == "__main__":
    test_pass()



class PassGraph:
    def __init__(self, path_name=None):
        """
        Als path_name None is → lege graaf.
        Als path_name een pad is → lees meteen het bestand in.
        """
        self.players = []      # lijst met Player-objecten
        self.adj = {}          # dict: sender_name (str) -> lijst van Pass-objecten

        if path_name is not None:
            self.load_from_txt(path_name)

    # ---------- deel 3: basisoperaties ----------

    def add_player(self, player):
        """
        Voeg een Player toe als er nog geen speler met dezelfde name bestaat.
        Zorg dat er een lege lijst in adj staat voor deze speler.
        """
        for existing_player in self.players:
            if existing_player.name == player.name:
                # speler zit er al in → niets doen
                return

        # nieuwe speler toevoegen
        self.players.append(player)

        # lege lijst voor uitgaande passes
        if player.name not in self.adj:
            self.adj[player.name] = []

    def has_player(self, speler):
        """
        Retourneer True als de speler in de graaf zit.
        Argument mag Player-object of naam (str) zijn.
        """
        if isinstance(speler, Player):
            name = speler.name
        else:
            name = speler

        for player in self.players:
            if player.name == name:
                return True
        return False

    def get_player(self, name):
        """
        Zoek Player met deze naam, of None als hij niet bestaat.
        """
        for player in self.players:
            if player.name == name:
                return player
        return None

    def add_pass(self, sender, receiver, times=1):
        """
        Voeg een pass toe van sender (Player) naar receiver (Player).
        - times > 0
        - beide spelers moeten al in de graaf zitten
        - als pass al bestaat: nr_of_times += times
        """
        if times <= 0:
            return  # niets doen

        if not self.has_player(sender) or not self.has_player(receiver):
            return  # volgens opgave: niet toevoegen als spelers niet bestaan

        sender_name = sender.name

        if sender_name not in self.adj:
            self.adj[sender_name] = []

        # kijken of pass al bestaat
        for pas in self.adj[sender_name]:
            if pas.receiver.name == receiver.name:
                pas.nr_of_times += times
                return

        # nog geen pass → nieuwe maken
        new_pass = Pass(sender, receiver, times)
        self.adj[sender_name].append(new_pass)

    def get_pass(self, sender_name, receiver_name):
        """
        Geef de Pass terug (sender_name -> receiver_name) of None.
        """
        if sender_name not in self.adj:
            return None

        for pas in self.adj[sender_name]:
            if pas.receiver.name == receiver_name:
                return pas

        return None

    def neighbors(self, sender_name):
        """
        Retourneer alle uitgaande passes van deze zender (lijst Pass).
        Lege lijst als zender niet bestaat of geen uitgaande passes heeft.
        """
        if sender_name not in self.adj:
            return []
        return self.adj[sender_name]

    # ---------- deel 3: analysefuncties ----------

    def total_weight(self, subset):
        """
        Som van nr_of_times over alle passes waarbij
        zender én ontvanger in subset zitten.
        subset: lijst met spelernamen (str) of None (→ alle spelers).
        """
        if subset is None:
            subset_names = [player.name for player in self.players]
        else:
            subset_names = subset

        total = 0

        for sender_name, passes in self.adj.items():
            if sender_name not in subset_names:
                continue

            for pas in passes:
                receiver_name = pas.receiver.name
                if receiver_name in subset_names:
                    total += pas.nr_of_times

        return total

    def pass_intensity(self, subset=None):
        """
        Intensiteit = (totaal aantal passes binnen subset) /
                      (maximaal aantal mogelijke gerichte passes binnen subset).
        subset: lijst namen (str) of None.
        """
        if subset is None:
            subset_names = [player.name for player in self.players]
        else:
            subset_names = subset

        n = len(subset_names)
        if n < 2:
            return 0.0

        numerator = self.total_weight(subset_names)
        denominator = n * (n - 1)

        return numerator / denominator

    def top_pairs(self, k=5):
        """
        Geef top k Pass-objecten met hoogste nr_of_times (globaal).
        """
        all_passes = []
        for passes in self.adj.values():
            for pas in passes:
                all_passes.append(pas)

        all_passes.sort(key=lambda pas: pas.nr_of_times, reverse=True)
        return all_passes[:k]

    def distribution_from(self, sender_name):
        """
        Retourneer lijst (receiver_name, count) voor gegeven zender,
        gesorteerd dalend op count.
        Lege lijst als zender niet bestaat.
        """
        if sender_name not in self.adj:
            return []

        result = []
        for pas in self.adj[sender_name]:
            receiver_name = pas.receiver.name
            count = pas.nr_of_times
            result.append((receiver_name, count))

        result.sort(key=lambda pair: pair[1], reverse=True)
        return result

    # ---------- deel 4: players(), passes(), load/save ----------

    def players_list(self):
        """
        Geef een kopie van de spelerslijst terug.
        (Ik noem deze methode players_list om geen conflict te hebben met self.players)
        """
        return list(self.players)

    def passes(self):
        """
        Geef een lijst met alle Pass-objecten in de graaf.
        """
        alle_passes = []
        for passes in self.adj.values():
            for pas in passes:
                alle_passes.append(pas)
        return alle_passes

    def load_from_txt(self, path):
        """
        Lees een .txt-bestand in volgens het opgegeven formaat
        met [PLAYERS] en [PASSES].
        """
        with open(path, "r", encoding="utf-8") as file:
            current_section = None

            for line in file:
                line = line.strip()

                # lege regel of comment
                if line == "" or line.startswith("#"):
                    continue

                # secties herkennen
                if line == "[PLAYERS]":
                    current_section = "players"
                    continue

                if line == "[PASSES]":
                    current_section = "passes"
                    continue

                if current_section is None:
                    raise ValueError("Onbekende sectie vóór [PLAYERS]")

                # ----- PLAYERS -----
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

                    self.add_player(Player(name, number))
                    continue

                # ----- PASSES -----
                if current_section == "passes":
                    if "->" not in line or ":" not in line:
                        raise ValueError("Ongeldige pass-regel")

                    left, times_str = line.split(":")
                    sender_name, receiver_name = left.split("->")

                    sender_name = sender_name.strip()
                    receiver_name = receiver_name.strip()
                    times_str = times_str.strip()

                    try:
                        times = int(times_str)
                        if times <= 0:
                            raise ValueError()
                    except:
                        raise ValueError("Aantal times moet positief geheel getal zijn")

                    # controleer dat spelers bestaan
                    if not self.has_player(sender_name) or not self.has_player(receiver_name):
                        raise ValueError("Pass verwijst naar onbekende speler")

                    sender = self.get_player(sender_name)
                    receiver = self.get_player(receiver_name)

                    self.add_pass(sender, receiver, times)

    def save_to_txt(self, path):
        """
        Sla de graaf op in het gegeven .txt-bestand.
        Formaat met [PLAYERS] en [PASSES].
        """
        with open(path, "w", encoding="utf-8") as file:
            file.write("[PLAYERS]\n")
            for player in self.players:
                file.write(f"{player.name};{player.number}\n")

            file.write("[PASSES]\n")
            for sender_name, passes in self.adj.items():
                for pas in passes:
                    file.write(f"{pas.sender.name} -> {pas.receiver.name} : {pas.nr_of_times}\n")

def test_passgraph():
    pg = PassGraph()

    p1 = Player("Eden Hazard", 10)
    p2 = Player("Moussa Dembele", 19)
    p3 = Player("Romelu Lukaku", 9)
    p4 = Player("Jan Vertonghen", 5)

    pg.add_player(p1)
    pg.add_player(p2)
    pg.add_player(p3)
    pg.add_player(p4)

    pg.add_pass(p1, p2, 3)
    pg.add_pass(p1, p3, 2)
    pg.add_pass(p2, p3, 4)
    pg.add_pass(p3, p1, 1)
    pg.add_pass(p3, p4, 5)
    pg.add_pass(p4, p1, 2)

    # 5. test de verschillende analyse methodes

    # a) total_weight over alle spelers
    print("total_weight (alle spelers):",
          pg.total_weight(None))

    # b) total_weight voor een subset
    subset = ["Eden Hazard", "Moussa Dembele", "Romelu Lukaku"]
    print("total_weight subset", subset, ":",
          pg.total_weight(subset))

    # c) pass_intensity voor alle spelers en subset
    print("pass_intensity (alle spelers):",
          pg.pass_intensity())
    print("pass_intensity subset", subset, ":",
          pg.pass_intensity(subset))

    # d) top_pairs (top 3)
    print("top_pairs (3):")
    for pas in pg.top_pairs(3):
        print(" ", pas, "->", pas.nr_of_times)

    # e) distribution_from voor één zender
    print("distribution_from 'Romelu Lukaku':")
    for receiver_name, count in pg.distribution_from("Romelu Lukaku"):
        print(" ", receiver_name, ":", count)


# zorg dat dit draait als je het script runt
if __name__ == "__main__":
    test_passgraph()



############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest

    def __repr__(self):
        return self.name

def make_melon_types():
    """Returns a list of current melon types."""
# code, first_harvest, color, is_seedless, is_bestseller, name
    all_melon_types = []
    muskmelon = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType(
        "cas",
        2003,
        "orange",
        True,
        False,
        "Casaba"
    )
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType(
        "cren",
        1996,
        "green",
        True,
        False,
        "Crenshaw"
    )
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        "yw",
        2013,
        "yellow",
        True,
        True,
        "Yellow Watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    # Fill in the rest
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for item in melon.pairings:
            print(f"- {item}")
        print("")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    print(melon_dict)


# make_melon_type_lookup(make_melon_types())
# print_pairing_info(make_melon_types())


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self, melon_type, shape_rate, color_rate, field, harvester
    ):
        self.melon_type = melon_type
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self):
        if (self.shape_rate > 5 and self.color_rate > 5 and self.field != 3):
            return True
        else:
            return False


def make_melons():
    """Returns a list of Melon objects."""
    
    # Fill in the rest
    M1 = Melon("yw", 8, 7, 2, "Sheila")
    M2 = Melon("yw", 3, 4, 2, "Sheila")
    M3 = Melon("yw", 9, 8, 3, "Sheila")
    M4 = Melon("cas", 10, 6, 35, "Sheila")
    M5 = Melon("cren", 8, 9, 35, "Michael")
    M6 = Melon("cren", 8, 2, 35, "Michael")
    M7 = Melon("cren", 2, 3, 4, "Michael")
    M8 = Melon("musk", 6, 7, 4, "Michael")
    M9 = Melon("yw", 7, 10, 3, "Sheila")

    return [M1, M2, M3, M4, M5, M6, M7, M8, M9]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        if melon.is_sellable() == True:
            sellability = 'CAN BE SOLD'
        else:
            sellability = 'NOT SELLABLE'
        print(f"Harvested by {melon.harvester} from Field {melon.field} ({sellability})")

get_sellability_report(make_melons())
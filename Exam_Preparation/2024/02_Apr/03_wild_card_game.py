def draw_cards(*args, **kwargs):
    cards = {"monster": [], "spell": []}
    result = ""

    for card in args:
        cards[card[1]].append(card[0])

    for card_name, card_type in kwargs.items():
        cards[card_type].append(card_name)

    if cards["monster"]:
        result += "Monster cards:\n" + "".join([f"  ***{card}\n" for card in (sorted(cards["monster"], reverse=True))])
    if cards["spell"]:
        result += "Spell cards:\n" + "".join([f"  $$${card}\n" for card in (sorted(cards["spell"]))])

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"),
                 raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))

"""
CP1404/CP5632 Practical
Game, Set, Match
"""


def main():
    """"""
    records = get_records("wimbledon.csv")
    # print(records)
    winner_to_count = count_winners(records)
    winning_nations = count_winners_nation(records)
    # print(winning_nations)
    # print(winner_to_count)
    display_winners(winner_to_count, winning_nations)


def get_records(filename):
    """ """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        records = []
        in_file.readline()  # Skip header line
        for line in in_file:
            line = line.strip()
            details = line.split(",")
            # Change first detail to integer
            details[0] = int(details[0])
            # Delete unnecessary detail from details (just need first 3 indexes)
            while len(details) > 3:
                details.pop(len(details) - 1)
            # A single record is made from a list of details
            record = [detail for detail in details]
            records.append(record)
    return records


def count_winners(records):
    """"""
    winner_to_count = {}
    for record in records:
        winner = record[2]
        try:
            winner_to_count[winner] += 1
        except KeyError:
            winner_to_count[winner] = 1

    return winner_to_count


def count_winners_nation(records):
    """"""
    winning_nations = set()
    for record in records:
        nation = record[1]
        try:
            winning_nations.add(nation)
        except:
            pass
    return list(winning_nations)


def display_winners(winner_to_count, winning_nations):
    """"""
    print("Wimbledon Champions:")
    for winner, count in winner_to_count.items():
        print(f"{winner} {count}")

    print(f"These {len(winning_nations)} countries have won Wimbledon:")
    print(", ".join(nation for nation in sorted(winning_nations)))



main()

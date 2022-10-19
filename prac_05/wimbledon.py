"""
CP1404/CP5632 Practical
Game, Set, Match
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_WINNER = 2


def main():
    """Read data from file and display details about Wimbledon winners and countries."""
    records = get_records(FILENAME)
    winner_to_count = count_winners(records)
    winning_countries = find_winning_countries(records)
    display_winners(winner_to_count, winning_countries)


def get_records(filename):
    """Get records from file in list of lists form."""
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
    """Create dictionary of winners mapped to a count of how many times they have won."""
    winner_to_count = {}
    for record in records:
        winner = record[INDEX_WINNER]
        try:
            winner_to_count[winner] += 1
        except KeyError:
            winner_to_count[winner] = 1

    return winner_to_count


def find_winning_countries(records):
    """Finds countries that have won from records, and returns information as a list."""
    winning_countries = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        winning_countries.add(country)
    return list(winning_countries)


def display_winners(winner_to_count, winning_countries):
    """Display winners and countries."""
    print("Wimbledon Champions:")
    for winner, count in winner_to_count.items():
        print(f"{winner} {count}")

    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(winning_countries)))


main()

class MissingCeremony:
    def __init__(self) -> None:
        self.num_of_way_below_five = {
            1: 1,
            2: 2,
            3: 4,
            4: 7
        }
    def number_of_ways_to_attend_classes(self, days):
        if days < 5:
            return self.num_of_way_below_five.get(days)

        ways_list = [0] * (days + 1)
        ways_list[1] = 1
        ways_list[2] = 2
        ways_list[3] = 4
        ways_list[4] = 7

        for day in range(5, days + 1):
            ways_list[day] = ways_list[day - 1] + ways_list[day - 2] + ways_list[day - 3] + ways_list[day - 4]

        return ways_list[day]

    def probability_of_missing_ceremony(self, days):
        total_number_of_ways = self.number_of_ways_to_attend_classes(days)
        total_number_of_ways_without_last_day = self.number_of_ways_to_attend_classes(days - 1)
        probability = f"{total_number_of_ways_without_last_day} / {total_number_of_ways}"
        return probability

days = 6
missing_ceremony = MissingCeremony()
print(missing_ceremony.probability_of_missing_ceremony(days))
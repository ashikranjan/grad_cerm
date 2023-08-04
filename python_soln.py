class MissingCeremony:
    def __init__(self) -> None:
        self.ways_below_five = {
            1: 2,
            2: 4,
            3: 8,
            4: 15
        }
        self.ways_to_miss_below_five = {
            1: 1,
            2: 2,
            3: 4,
            4: 7
        }
    def number_of_ways_to_attend_classes(self, days):
        if days < 5:
            return self.ways_below_five.get(days)

        ways_list = [0] * (days + 1)
        ways_list[1] = self.ways_below_five.get(1)
        ways_list[2] = self.ways_below_five.get(2)
        ways_list[3] = self.ways_below_five.get(3)
        ways_list[4] = self.ways_below_five.get(4)

        for day in range(5, days + 1):
            ways_list[day] = ways_list[day - 1] + ways_list[day - 2] + ways_list[day - 3] + ways_list[day - 4]

        return ways_list[day]
    
    def number_of_ways_to_miss_ceremony(self, days):
        if days < 5:
            return self.ways_to_miss_below_five.get(days)

        ways_list = [0] * (days + 1)
        ways_list[1] = self.ways_to_miss_below_five.get(1)
        ways_list[2] = self.ways_to_miss_below_five.get(2)
        ways_list[3] = self.ways_to_miss_below_five.get(3)
        ways_list[4] = self.ways_to_miss_below_five.get(4)

        for day in range(5, days + 1):
            ways_list[day] = ways_list[day - 1] + ways_list[day - 2] + ways_list[day - 3] + ways_list[day - 4]

        return ways_list[day]

    def probability_of_missing_ceremony(self, days):
        total_ways_to_atd_classes = self.number_of_ways_to_attend_classes(days)
        total_way_to_miss_ceremony = self.number_of_ways_to_miss_ceremony(days)
        probability = f"{total_way_to_miss_ceremony} / {total_ways_to_atd_classes}"
        return probability

days = 10
missing_ceremony = MissingCeremony()
print(missing_ceremony.probability_of_missing_ceremony(days))
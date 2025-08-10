class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = str(n)
        str_tally = frozenset(Counter(str_n).items())
        power_set = set()

        for i in range(0, 31):
            power = 2**i
            power_tally = frozenset(Counter(str(power)).items())
            if power_tally == str_tally:
                return True
            power_set.add(power_tally)

        return False
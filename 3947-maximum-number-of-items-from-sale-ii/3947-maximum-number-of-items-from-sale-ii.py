from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        frequency = [0] * (n + 1)

        for factor, price in items:
            frequency[factor] += 1

        free_limit = [0] * (n + 1)
        for factor in range(1, n + 1):
            if frequency[factor] == 0:
                continue

            for multiple in range(factor, n + 1, factor):
                free_limit[factor] += frequency[multiple]

            free_limit[factor] -= 1

        ordered_items = sorted(items, key=lambda item: item[1])
        cheapest = ordered_items[0][1]
        total = 0

        for factor, price in ordered_items:
            if price > budget or price >= 2 * cheapest:
                break

            count = min(free_limit[factor], budget // price)
            total += 2 * count
            budget -= count * price

        return total + budget // cheapest
        
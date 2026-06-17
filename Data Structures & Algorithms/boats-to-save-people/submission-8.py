class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l, r = 0, len(people) - 1
        while l < r:
            pair = people[l] + people[r]
            if pair > limit:
                boats, r = boats + 1, r - 1
            else:
                boats, l, r = boats + 1, l + 1, r - 1
        if l == r:
            boats += 1
        return boats

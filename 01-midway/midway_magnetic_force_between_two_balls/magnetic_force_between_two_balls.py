class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def peut_placer(espacement: int) -> bool:
            count, dernier_placé = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - dernier_placé >= espacement:
                    count += 1
                    dernier_placé = position[i]
                    if count == m:
                        return True
            return False

        position.sort()
        gauche, droite = 1, position[-1] - position[0]
        meilleur_espacement = 0

        while gauche <= droite:
            milieu = (gauche + droite) // 2
            if peut_placer(milieu):
                meilleur_espacement = milieu
                gauche = milieu + 1
            else:
                droite = milieu - 1

        return meilleur_espacement


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxDistance([1, 2, 3, 4, 7], 3) == 3
    assert solution.maxDistance([5, 4, 3, 2, 1, 1000000000], 2) == 999999999
    print("All tests passed.")

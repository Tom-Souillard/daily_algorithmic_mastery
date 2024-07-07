# Water Bottles

## 🎯 Objectif

    Calculer le nombre maximum de bouteilles d'eau que l'on peut boire avec un nombre initial de bouteilles pleines et un taux d'échange spécifique.

---

## 📝 Détails

    Prendre en compte les bouteilles vides échangées contre des bouteilles pleines.

---

## 📥 Entrée

    Nombre initial de bouteilles pleines.
    Nombre de bouteilles vides nécessaires pour une bouteille pleine.

---

## 📤 Sortie

    Nombre maximum de bouteilles d'eau bues.




# Intuition
The problem essentially revolves around the idea of maximizing the number of full water bottles you can drink by continuously exchanging empty bottles for full ones. Initially, you have a certain number of full bottles which you drink, resulting in empty bottles. These empty bottles can be exchanged for more full bottles based on a given exchange rate. The process continues iteratively until you no longer have enough empty bottles to exchange for even one full bottle.

# Approach
1. **Initialization**: Start with the given number of full bottles.
2. **Drink and Exchange Loop**:
   - Drink all the full bottles, turning them into empty bottles.
   - Calculate how many new full bottles you can get by exchanging the empty bottles.
   - Add the newly obtained full bottles to the total count of bottles drunk.
   - Update the count of empty bottles to include the leftovers from the exchange process.
3. **Termination**: The loop continues until the number of empty bottles is less than the required number for an exchange.
4. **Result**: The total number of bottles drunk is returned.

# Complexity
- Time complexity:
The time complexity is $$O(\log n)$$ where $$n$$ is the initial number of full bottles. This is because with each iteration, the number of empty bottles decreases by a factor determined by the exchange rate.

- Space complexity:
The space complexity is $$O(1)$$ since we only use a few variables to keep track of the counts, and no additional space is required that grows with the input size.

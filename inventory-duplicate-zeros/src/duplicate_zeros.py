def duplicateZeros(inventory):
    n = len(inventory)
    zeros = inventory.count(0)

    i = n - 1
    j = n + zeros - 1

    # Work backwards
    while i >= 0:
        if j < n:
            inventory[j] = inventory[i]

        if inventory[i] == 0:
            j -= 1
            if j < n:
                inventory[j] = 0

        i -= 1
        j -= 1
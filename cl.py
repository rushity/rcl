# cl.py
def calculate_leaves(total_leaves, leaves_per_month, months, monthly_leaves):
    aa = total_leaves
    l = leaves_per_month
    n = months
    a = [[0 for _ in range(5)] for _ in range(n)]

    # Populate the 'a' array based on the provided monthly leaves
    for i in range(n):
        a[i][1] = monthly_leaves[i]
        a[i][0] = i + 1

    for i in range(n):
        a[i][4] = aa
        if a[i][1] >= l:
            if a[i][4] <= (l - 1):
                a[i][2] = a[i][4]
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]
            else:
                a[i][2] = l
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]
        else:
            if a[i][4] < (l - 1):
                a[i][2] = a[i][4]
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]
            else:
                a[i][2] = a[i][1]
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]

    return a

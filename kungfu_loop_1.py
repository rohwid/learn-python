n = 6

for i in range(n):
    if i < (n - 1):
        print(f"{' ' * (n - ((i + 1) % n))}{'#' * ((i + 1) % n)}")
        
    if i == (n - 1):
        print(f"{'#' * n}")
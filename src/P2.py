import os

BASE_DIR = os.path.dirname(__file__)
in_path = os.path.join(BASE_DIR,"..","input", "P2.txt")
out_path = os.path.join(BASE_DIR,"..","output", "P2.txt")

def bank():
    with open(in_path, "r") as f_in:
        n, m, s = map(int, f_in.readline().split())
        
        terminal = {}

        for _ in range(m):
            p, t = map(int, f_in.readline().split())
            terminal[t] = p

        #compra[socio][cliente] = cantidad de compras
        purchases = {p : {} for p in range(1, n + 1)}
        
        for _ in range(s):
            c, t = map(int, f_in.readline().split())
            
            p = terminal[t]

            if c in purchases[p]:
                purchases[p][c] += 1
            else:
                purchases[p][c] = 1

        results = []

        for p in range(1, n + 1):
            if purchases[p]:
                best = min(purchases[p], key = lambda c:(-purchases[p][c], c))
                results.append(f"{p} {best}")
            else:
                results.append(f"{p} -1")
        #print(purchases)
    with open(out_path, "w") as f_out:
        for result in results:
            f_out.write(result + "\n")

if __name__ == "__main__":
    bank()
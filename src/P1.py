import re
import os

'''
d: Cualquier dígito (0-9).

w: Cualquier carácter alfanumérico (letras, números y guion bajo).

+: Una o más repeticiones.

*: Cero o más repeticiones.

.: Cualquier carácter excepto un salto de línea.

^ / $: Inicio y fin de una cadena.
'''
BASE_DIR = os.path.dirname(__file__)
in_path = os.path.join(BASE_DIR,"..","input", "P1.txt")
out_path = os.path.join(BASE_DIR,"..","output", "P1.txt")


def router():
    #read input/p1.txt
    with open(in_path, "r") as f_in:
        n = int(f_in.readline().strip())
        routes = []
        for _ in range(n):
            parts = f_in.readline().strip().split(" ", 1)
            routes.append((parts[0], parts[1]))

        m = int(f_in.readline().strip())

        results = []

        for _ in range(m):
            url = f_in.readline().strip()
            matched = False
            for path, content in routes:
                pattern = re.sub(r":([^/]+)", r"([^/]+)", path)
                pattern = "^" + pattern + "$"
                match = re.match(pattern, url)
                if match:
                    param = match.group(1) if match.lastindex else None
                    results.append(content + (" " + param if param else ""))
                    matched = True
                    break
            if not matched:
                results.append("404 Not Found")

        #output in output/p1.txt
        with open(out_path, "w") as f_out:
            for result in results:
                f_out.write(result + "\n")
        
if __name__ == "__main__":
    router()

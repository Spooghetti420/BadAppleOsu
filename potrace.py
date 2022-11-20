import subprocess
from common import QUANTISED, VECTOR


def main():
    for file in QUANTISED.iterdir():
        name = VECTOR / (file.stem + ".json")
        subprocess.run(["potrace", "-b", "geojson", "-o", f"{name}", "-t", "3", "--", str(file)])

if __name__ == "__main__":
    main()
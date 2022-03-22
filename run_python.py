import fire
import rich
import os

def main():
    python_path = "python/"
    path = os.walk(python_path)
    for year in path:
        year, _, days = year
        days = [year+"/"+day for day in days if day.startswith("day")]
        print(days)

    


if __name__ == "__main__":
    main()
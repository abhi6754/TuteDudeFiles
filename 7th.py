try:
    with open("sample.txt", "r") as fh:
        for i, line in enumerate(fh, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("File not found")
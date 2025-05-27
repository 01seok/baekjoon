def main():
    s = input().strip()
    rev = s[::-1]
    if s == rev:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
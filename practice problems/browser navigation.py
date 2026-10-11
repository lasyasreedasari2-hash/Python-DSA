import sys
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    history_stack = []
    MAX_SIZE = 5
    for i in range(1, n + 1):
        if i >= len(input_data):
            break
        line = input_data[i].strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0]
        if command == "VISIT":
            page_id = parts[1]
            if len(history_stack) >= MAX_SIZE:
                print("History Full")
            else:
                history_stack.append(page_id)
        elif command == "BACK":
            if not history_stack:
                print("No pages")
            else:
                history_stack.pop()
        elif command == "CURRENT":
            if not history_stack:
                print("No pages")
            else:
                print(history_stack[-1])
        else:
            if not history_stack:
                print("true")
            else:
                print("false")
if __name__ == "__main__":
    solve()

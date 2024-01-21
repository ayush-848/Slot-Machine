import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def calculate_winnings(columns, lines, bet, values):
    """
    Calculate the winnings based on the slot machine result.

    Args:
        columns (list): The slot machine columns.
        lines (int): Number of lines bet on.
        bet (int): Bet amount per line.
        values (dict): Symbol values.

    Returns:
        tuple: A tuple containing total winnings and winning lines.
    """
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]

        # Check if all symbols in the line are the same
        for column in columns:
            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break
        else:
            # All symbols in the line are the same, calculate winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random slot machine spin.

    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Symbol count for each symbol.

    Returns:
        list: The randomly generated slot machine columns.
    """
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the slot machine display.

    Args:
        columns (list): The slot machine columns.
    """
    print("Slot Machine:")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(f"  {column[row]}", end=" | " if i != len(columns) - 1 else "")
        print()


def deposit():
    """
    Get the initial deposit from the player.

    Returns:
        int: The initial deposit amount.
    """
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    """
    Get the number of lines the player wants to bet on.

    Returns:
        int: Number of lines.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    """
    Get the bet amount per line from the player.

    Returns:
        int: Bet amount per line.
    """
    while True:
        amount = input(f"What would you like to bet on each line? ${MIN_BET} - ${MAX_BET}: ")

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    """
    Perform a slot machine spin and calculate winnings.

    Args:
        balance (int): Current player balance.

    Returns:
        int: Updated player balance after the spin.
    """
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)

    winnings, winning_lines = calculate_winnings(slots, lines, bet, SYMBOL_VALUE)

    print(f"\nYou won ${winnings}.")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    else:
        print("No winning lines.")

    return balance + winnings - total_bet


def main():
    """
    Main function to run the slot machine game.
    """
    print("Welcome to the Slot Machine Game!")
    balance = deposit()

    while True:
        print(f"\nCurrent balance is ${balance}")
        answer = input("Press enter to play (q to quit): ")

        if answer == "q":
            break
        balance = spin(balance)

    print(f"\nYou left with ${balance}")
    print("Thank you for playing!")


if __name__ == "__main__":
    main()

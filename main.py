from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import load_transactions, load_transactions_csv, load_transactions_xlsx


def get_amount(transaction: dict) -> float:
    """Return the transaction amount, whatever the file format."""
    if "operationAmount" in transaction:
        return float(transaction["operationAmount"]["amount"])
    return float(transaction.get("amount", 0))


def get_currency(transaction: dict) -> str:
    """Return the currency code, whatever the file format."""
    if "operationAmount" in transaction:
        return transaction["operationAmount"]["currency"]["code"]
    return transaction.get("currency_code", "")


def main() -> None:
    """Main program logic for working with bank transactions."""
    print("Привет! Добро пожаловать в программу работы " "с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input()

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = load_transactions_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = load_transactions_xlsx("data/transactions_excel.xlsx")

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            "Введите статус, по которому необходимо выполнить "
            "фильтрацию.\nДоступные для фильтровки статусы: "
            "EXECUTED, CANCELED, PENDING"
        )
        status = input().upper()
        if status in valid_statuses:
            break
        print(f'Статус операции "{status}" недоступен.')

    data = filter_by_state(data, status)
    print(f'Операции отфильтрованы по статусу "{status}"')
    print("Отфильтровать список транзакций по определенному " "слову в описании? Да/Нет")
    if input().lower() == "да":
        search = input("Введите слово для поиска: ")
        data = process_bank_search(data, search)

    print("Отсортировать операции по дате? Да/Нет")
    if input().lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order = input().lower()
        reverse = order == "по убыванию"
        data = sort_by_date(data, reverse)

    print("Выводить только рублевые транзакции? Да/Нет")
    if input().lower() == "да":
        data = [t for t in data if get_currency(t) == "RUB"]
    print("Распечатываю итоговый список транзакций...")

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши " "условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(data)}\n")

    for transaction in data:
        print(transaction.get("description", ""))
        print(f"Сумма: {get_amount(transaction)} {get_currency(transaction)}")
        print()


if __name__ == "__main__":
    main()

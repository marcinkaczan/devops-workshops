from app.calculator import add, divide


def lambda_handler(event, context):
    print("Otrzymany event:", event)

    a = event.get("a", 10)
    b = event.get("b", 2)

    result = {
        "add": add(a, b),
        "divide": divide(a, b)
    }

    print("Wynik:", result)

    return result


def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest
    Formula: SI = (P * R * T) / 100
    :param principal: Principal amount
    :param rate: Annual interest rate in percentage
    :param time: Time period in years
    :return: Simple Interest
    """
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time in years: "))

    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest = {si}")

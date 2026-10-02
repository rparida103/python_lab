from itertools import groupby
from operator import itemgetter


def demo_min_max_and_sort(prices):
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    prices_sorted = sorted(zip(prices.values(), prices.keys()))

    print(f"Min Price: {min_price}")
    print(f"Max price: {max_price}")
    print(f"Sorted Price: {prices_sorted}")


def demo_key_operations():
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}

    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())

    filtered = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(filtered)


def demo_sort_rows():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    ]

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))

    print(rows_by_fname)
    print(rows_by_uid)


def demo_groupby_dates():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    rows.sort(key=itemgetter('date'))
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for item in items:
            print('    ', item)


def demo_subset_and_merge():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75,
    }

    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)

    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print(p2)

    p3 = dict((key, value) for key, value in prices.items() if value > 200)
    print(p3)

    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    merged = {**b, **a}
    print(merged)


if __name__ == "__main__":
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75,
    }

    demo_min_max_and_sort(prices)
    demo_key_operations()
    demo_sort_rows()
    demo_groupby_dates()
    demo_subset_and_merge()


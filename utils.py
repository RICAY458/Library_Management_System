from datetime import datetime

FINE_PER_DAY = 10


def calculate_fine(due_date):
    if not due_date:
        return 0

    today = datetime.now()
    late_days = (today - due_date).days

    if late_days > 0:
        return late_days * FINE_PER_DAY
    else:
        return 0
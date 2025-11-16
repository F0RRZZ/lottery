class TicketsCountNotSetError(Exception):
    def __init__(self):
        self.message = 'tickets_count не задан'
        super().__init__(self.message)


class TicketsCountExceedError(Exception):
    def __init__(self, limit: int = 1_000_000):
        self.message = f'tickets_count не может быть больше {limit}'
        super().__init__(self.message)


class UniqueTicketGenerationError(Exception):
    def __init__(self, attempts: int):
        self.message = (
            'Не удалось сгенерировать уникальный '
            f'билет после {attempts} попыток'
        )
        super().__init__(self.message)

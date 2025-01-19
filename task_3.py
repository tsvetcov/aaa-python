import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины,
    # затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    group = asyncio.gather(*coros)
    tickets = await group
    n = len(tickets)
    for i in range(n):
        for j in range(i):
            if tickets[i].number < tickets[j].number:
                tickets[i], tickets[j] = tickets[j], tickets[i]
    ans = ''
    for elem in tickets:
        ans += elem.key
    return ans

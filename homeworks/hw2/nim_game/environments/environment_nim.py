from random import randint
from copy import deepcopy
from nim_game.common.models import NimStateChange


STONE_AMOUNT_MIN = 1        # минимальное начальное число камней в кучке
STONE_AMOUNT_MAX = 10       # максимальное начальное число камней в кучке


class EnvironmentNim:
    """
    Класс для хранения и взаимодействия с кучками
    """
    _heaps: list[int]       # кучки

    def __init__(self, heaps_amount: int) -> None:
        if (heaps_amount < 2) or (heaps_amount > 10) or (not isinstance(heaps_amount, int)):
            raise ValueError

        self._heaps = [randint(STONE_AMOUNT_MIN, STONE_AMOUNT_MAX) for _ in range(heaps_amount)]

    def get_state(self) -> list[int]:
        """
        Получение текущего состояния кучек
        :return: копия списка с кучек
        """
        return deepcopy(self._heaps)

    def change_state(self, state_change: NimStateChange) -> None:
        """
        Изменения текущего состояния кучек
        :param state_change: структура описывающая изменение состояния
        Сделать строго меньше 0 и нестрого больше лен, если разрешит индексировать с нуля
        и в индексах массива убрать -1
        мега приятно нумеровать с единицы спасибо большое
        """
        if (state_change.heap_id <= 0) \
            or (state_change.heap_id > len(self._heaps)) \
                or (state_change.decrease < 1) \
                or (state_change.decrease > self._heaps[state_change.heap_id-1]):
            raise ValueError

        self._heaps[state_change.heap_id-1] -= state_change.decrease

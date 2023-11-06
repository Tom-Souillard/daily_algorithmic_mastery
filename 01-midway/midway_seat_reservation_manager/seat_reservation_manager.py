class SeatManager:
    """Manages the reservation state of seats.

    This class provides functionality to reserve and unreserve seats in a
    performance-efficient manner using a min-heap data structure.

    Attributes:
        sieges_disponibles (list of int): A heap queue (min-heap) containing all available seat numbers.
    """

    def __init__(self, n: int):
        self.sieges_disponibles = list(range(1, n + 1))
        heapq.heapify(self.sieges_disponibles)

    def reserve(self) -> int:
        """Reserves and returns the smallest-numbered available seat.

        Removes the seat from the heap of available seats.

        Returns:
            int: The seat number of the reserved seat.
        """
        return heapq.heappop(self.sieges_disponibles)

    def unreserve(self, seatNumber: int) -> None:
        """Unreserves the seat with the given `seatNumber`.

        Adds the seat back into the heap of available seats.

        Args:
            seatNumber (int): The seat number to be unreserved.
        """
        heapq.heappush(self.sieges_disponibles, seatNumber)
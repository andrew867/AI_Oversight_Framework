"""Aggregates signals for the oversight control loop. Generic placeholder."""


class ControlSignalAggregator:
    """
    Aggregates signals for the oversight control loop. Implementations
    provide inputs to intent, human-factors, and safety gates.

    This is a generic interface. No implementation detail is specified.
    """

    def aggregate(self, context: dict) -> dict:
        """
        Produce aggregated signals from context for the control loop.

        Args:
            context: Context pack and any prior stage outputs.

        Returns:
            Signal bundle for downstream gates (intent, human-factors, safety).
        """
        raise NotImplementedError("Skeleton only")

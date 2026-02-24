"""Behavioral ownership tracking: store and ledger interfaces only."""


class OwnershipStore:
    """
    Store for ownership records. Supports read and conditional updates
    (e.g. CAS). Used for behavioral ownership tracking; no implementation
    or protocol detail (offer/accept/decline/renew/release) specified here.
    """

    def get(self, task_id: str) -> dict:
        """Get current ownership record for task_id."""
        raise NotImplementedError("Skeleton only")

    def cas_update(self, task_id: str, expected_version: int, mutator) -> tuple:
        """
        Conditional update: apply mutator(record) only if version matches.
        Returns (ok, record, error).
        """
        raise NotImplementedError("Skeleton only")


class OwnershipLedger:
    """
    Append-only ledger for ownership events. Used to audit handoffs
    and ownership transitions; no schema or implementation specified.
    """

    def append(
        self,
        task_id: str,
        action: str,
        actor: str,
        payload: dict,
        expected_version: int = None,
    ) -> None:
        """
        Append an ownership event.

        Args:
            task_id: Task identifier.
            action: Event action type.
            actor: Actor identifier.
            payload: Event payload.
            expected_version: Optional version for consistency.
        """
        raise NotImplementedError("Skeleton only")

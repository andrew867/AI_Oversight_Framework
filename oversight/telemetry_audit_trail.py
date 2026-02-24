"""Log cycle state, access, chained audit entries, DAG events."""


class TelemetryAuditTrail:
    """
    Logs cycle state, access events, and chained audit entries. Can
    sink DAG events to an append-only log. No implementation detail
    (sink paths, schema) specified.

    Inputs: cycle_data (agent_states, budgets, actions), access events, audit entries.
    Outputs: Written to configured sinks (interface only).
    """

    def log_cycle(self, cycle_id: str, cycle_data: dict) -> None:
        """
        Log a cycle's state (e.g. timeseries row).

        Args:
            cycle_id: Cycle identifier.
            cycle_data: Agent states, budgets, actions, etc.
        """
        raise NotImplementedError("Skeleton only")

    def log_access(self, event: dict) -> None:
        """
        Log an access event.

        Args:
            event: Access event dict.
        """
        raise NotImplementedError("Skeleton only")

    def append_audit(self, entry: dict) -> None:
        """
        Append a chained audit entry (e.g. entry_id, previous_entry_hash).

        Args:
            entry: Audit entry dict.
        """
        raise NotImplementedError("Skeleton only")

    def log_dag_event(self, event: dict) -> None:
        """
        Log a DAG execution event.

        Args:
            event: DAG event dict.
        """
        raise NotImplementedError("Skeleton only")

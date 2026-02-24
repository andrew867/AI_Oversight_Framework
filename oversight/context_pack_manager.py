"""Assemble tiered context (mission, session, identity, scope) for agents."""


class ContextPackManager:
    """
    Assembles tiered context for agents: mission, session summary,
    identity reminder, and scope. Used to build the startup context
    passed to task execution and oversight stages.

    Inputs: task_id, session_id, optional memory_profile.
    Outputs: context pack (mission, instructions, session_summary, scope, etc.).
    """

    def get_context_pack(self, task_id: str, session_id: str, options: dict = None) -> dict:
        """
        Build a context pack for the given task and session.

        Args:
            task_id: Task identifier.
            session_id: Session identifier.
            options: Optional overrides (e.g. memory_profile).

        Returns:
            Context pack dict for downstream stages.
        """
        raise NotImplementedError("Skeleton only")

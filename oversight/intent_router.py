"""Classify stated/inferred intent; return intent event and resolution action."""


class IntentRouter:
    """
    Classifies stated and inferred intent (e.g. ask_info, debate, escalate).
    Returns an intent event plus optional resolution_action for ambiguity.

    Inputs: stated intent context, signal bundle from control loop.
    Outputs: IntentEvent (stated_intent, inferred_intent, expectation_mismatch,
             ambiguity_detected, resolution_action).
    """

    def route(self, stated_context: dict, signals: dict) -> dict:
        """
        Classify intent and optionally suggest resolution.

        Args:
            stated_context: Stated intent / request context.
            signals: Aggregated signals from ControlSignalAggregator.

        Returns:
            Intent event dict (stated_intent, inferred_intent, resolution_action, etc.).
        """
        raise NotImplementedError("Skeleton only")

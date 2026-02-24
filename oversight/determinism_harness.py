"""Replay scenarios; compare to expected hashes; forbid diagnostics-driven actions."""


class DeterminismHarness:
    """
    Replay scenarios with expected outputs. Compares actual output to
    expected hashes and asserts that diagnostics do not drive actions
    (e.g. no action when expected_no_actions). Interface only; no
    fixture format or hash algorithm specified.

    Inputs: scenario (input_data, expected_output_hash, expected_actions, expected_no_actions).
    Outputs: pass/fail, optional diff.
    """

    def run_scenario(self, scenario: dict) -> dict:
        """
        Run a single scenario and check determinism.

        Args:
            scenario: input_data, expected_output_hash, expected_actions, expected_no_actions.

        Returns:
            Dict with pass, actual_hash, message, etc.
        """
        raise NotImplementedError("Skeleton only")

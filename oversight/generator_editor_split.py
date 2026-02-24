"""Separate generative outputs from edits to task/code; apply edits within allowlists."""


class GeneratorEditorSplit:
    """
    Separates generative outputs (e.g. reports, feedback text) from
    edits to task files or code. Applies edits only within allowlists
    (allowed_edits, never_modify) from the policy gatekeeper.

    Inputs: issues/fixes, policy allowlists, analysis state.
    Outputs: Applied edits (within budget), generated content.
    """

    def apply_edits(self, fixes: list, allowlist: dict, options: dict = None) -> dict:
        """
        Apply edits within allowlist and optional budget.

        Args:
            fixes: List of proposed fixes.
            allowlist: allowed_edits, never_modify from PolicyGatekeeper.
            options: max_edits_per_cycle, etc.

        Returns:
            Dict with applied count, skipped, errors.
        """
        raise NotImplementedError("Skeleton only")

    def generate(self, prompt_context: dict, options: dict = None) -> dict:
        """
        Produce generative output (e.g. feedback text, report). Interface only.

        Args:
            prompt_context: Context for generation.
            options: Generation options.

        Returns:
            Generated content dict.
        """
        raise NotImplementedError("Skeleton only")

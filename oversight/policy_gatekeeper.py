"""Apply spec + authority rules; validation pass/fail; allowed_edits / never_modify."""


class PolicyGatekeeper:
    """
    Applies spec and authority rules. Returns validation pass/fail and
    policy-derived allowlists (allowed_edits, never_modify) for downstream
    editors and generators.

    Inputs: spec (e.g. YAML), authority config, request context.
    Outputs: validation result, allowed_fixes, allowed_edits, never_modify.
    """

    def check(self, spec: dict, authority: dict, context: dict) -> dict:
        """
        Run policy check and return validation and allowlists.

        Args:
            spec: Loaded spec (platform tiers, guardrails, etc.).
            authority: Authority config (mode, thresholds, code_fixing, task_file_editing).
            context: Request/cycle context.

        Returns:
            Dict with pass/fail, allowed_edits, never_modify, etc.
        """
        raise NotImplementedError("Skeleton only")

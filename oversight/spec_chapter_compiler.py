"""Compile spec chapters / policy docs into runtime policy."""


class SpecChapterCompiler:
    """
    Compiles spec chapters or policy documents into runtime policy
    consumed by the policy gatekeeper and other stages. Interface only;
    no format (YAML, patch) or load path specified.

    Inputs: spec source (e.g. paths or in-memory docs).
    Outputs: Merged spec dict for validators and policy getters.
    """

    def compile(self, sources: list) -> dict:
        """
        Compile one or more spec sources into a single runtime spec.

        Args:
            sources: List of spec sources (paths or dicts).

        Returns:
            Merged spec dict.
        """
        raise NotImplementedError("Skeleton only")

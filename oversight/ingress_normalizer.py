"""Normalize CLI/cron/API ingress into a canonical request."""


class IngressNormalizer:
    """
    Normalizes incoming requests from CLI, cron, or API into a canonical
    request shape for downstream pipeline stages.

    Inputs: raw argv, env, or HTTP request body.
    Outputs: canonical request dict (e.g. task_id, platform, mode, inputs).
    """

    def normalize(self, raw_input: dict) -> dict:
        """
        Produce a canonical request from raw ingress.

        Args:
            raw_input: Raw request (e.g. argv, env, request body).

        Returns:
            Canonical request dict for the pipeline.
        """
        raise NotImplementedError("Skeleton only")

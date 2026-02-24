"""Example usage intent for the oversight pipeline (skeleton only)."""

# Import stubs to show usage intent; no full implementation.
# Run from repo root: python -m examples.simple_dag_example
# Or with oversight installed: python examples/simple_dag_example.py

try:
    from oversight import (
        IngressNormalizer,
        ContextPackManager,
        ToolOrchestrator,
    )
except ImportError:
    from sys import path
    path.insert(0, ".")
    from oversight import (
        IngressNormalizer,
        ContextPackManager,
        ToolOrchestrator,
    )


def main() -> None:
    """Minimal example: instantiate stubs and show pipeline intent (no execution)."""
    normalizer = IngressNormalizer()
    context_mgr = ContextPackManager()
    orchestrator = ToolOrchestrator()
    # Stubs raise NotImplementedError if called; this script only shows import/usage intent.
    pass


if __name__ == "__main__":
    main()

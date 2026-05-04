# Contributing

Contributions are welcome, especially improvements to coordination primitives, tests, documentation, and simulation examples.

## Development Setup

```bash
git clone https://github.com/brandonhimpfen/swarm-coordinator.git
cd swarm-coordinator
pip install -e ".[dev]"
pytest
```

## Contribution Guidelines

- Keep primitives small, testable, and simulation-oriented.
- Include tests for new behaviour.
- Avoid adding heavy dependencies unless they are clearly justified.
- Do not represent the package as a real UAV flight-control system.
- Document assumptions and limitations clearly.

## Pull Requests

A good pull request should include:

- A clear description of the change
- Tests for new or changed behaviour
- Documentation updates when relevant
- Notes about safety or simulation limitations when applicable

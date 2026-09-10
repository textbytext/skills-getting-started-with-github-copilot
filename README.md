# Getting Started with GitHub Copilot

VS Code extension:

GitHub Copilot Chat

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey textbytext!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/textbytext/skills-getting-started-with-github-copilot/issues/1)

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)



## Py tests
run tests:

1) Install
```
python -m pip install pytest
python -m pytest -q
```

2) This repository has pytest.ini, but no visible test files yet. Add tests under a tests/ directory, typically named test_*.py.
pytest.ini file content:
```
[pytest]
pythonpath = .

```

3) Run
```
python -m pytest              # Run all tests
python -m pytest tests/        # Run tests in tests/
python -m pytest -k "name"     # Run matching tests
python -m pytest -v            # Verbose output
```
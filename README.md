# hello-world

A learning repository for practicing the GitHub Flow workflow with Python. This project includes a financial calculator application to demonstrate real-world development practices.

## Prerequisites

- Git installed on your machine ([Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- Python 3.x installed
- A GitHub account

## Quick Start

```bash
# Clone the repository
git clone https://github.com/cprebble2-stack/hello-world.git
cd hello-world

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt

# Run the financial calculator
python financial_calculator.py

# Run tests
python -m pytest test_financial_calculator.py

# Create a feature branch
git checkout -b feature/my-feature

# Make changes and test your code
python your_script.py

# Stage, commit, and push
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
```

After pushing, go to GitHub and open a Pull Request to merge your branch into `main`.

## About This Project

This repository demonstrates core GitHub concepts:
- Creating and switching branches
- Making commits
- Opening and reviewing pull requests
- Merging changes

**Project Focus:** Financial Calculator
- `financial_calculator.py` — Core financial calculation logic
- `financial_viz.py` — Data visualization features
- `test_financial_calculator.py` — Unit tests
- See [FINANCIAL_CALCULATOR_DOCS.md](FINANCIAL_CALCULATOR_DOCS.md) for detailed documentation

## Common Workflow Commands

| Task | Command |
|------|---------|
| View your branches | `git branch -a` |
| Switch to existing branch | `git checkout branch-name` |
| Create & switch branch | `git checkout -b feature-name` |
| See changes | `git status` |
| View commit history | `git log --oneline` |
| Undo last commit | `git reset HEAD~1` |
| Pull latest changes | `git pull origin main` |
| Delete a local branch | `git branch -d feature-name` |

## Python Development

| Task | Command |
|------|---------|
| Create virtual environment | `python3 -m venv venv` |
| Activate virtual environment | `source venv/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |
| Run main script | `python financial_calculator.py` |
| Run tests | `python -m pytest test_financial_calculator.py` |
| Run visualization | `python financial_viz.py` |
| Deactivate virtual environment | `deactivate` |

## GitHub Flow Steps

1. **Create a Branch** — `git checkout -b feature/description`
2. **Commit Changes** — `git add .` then `git commit -m "message"`
3. **Push Branch** — `git push origin feature/description`
4. **Open Pull Request** — Create PR on GitHub to review changes
5. **Merge** — Merge PR into main branch after review

## Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [GitHub Hello World Tutorial](https://guides.github.com/activities/hello-world/)
- [Git Documentation](https://git-scm.com/doc)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [FINANCIAL_CALCULATOR_DOCS.md](FINANCIAL_CALCULATOR_DOCS.md)
- [IMPROVEMENTS.md](IMPROVEMENTS.md)

## License

This project is open source and available under the MIT License.

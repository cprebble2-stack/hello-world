# hello-world

A learning repository for practicing the GitHub Flow workflow.

## Prerequisites

- Git installed on your machine ([Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- A GitHub account

## Quick Start

```bash
# Clone the repository
git clone https://github.com/cprebble2-stack/hello-world.git
cd hello-world

# Create a feature branch
git checkout -b feature/my-feature

# Make changes, then stage and commit
git add .
git commit -m "Add my feature"

# Push to GitHub
git push origin feature/my-feature
```

After pushing, go to GitHub and open a Pull Request to merge your branch into `main`.

## About This Project

This repository demonstrates core GitHub concepts:
- Creating and switching branches
- Making commits
- Opening and reviewing pull requests
- Merging changes

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

## License

This project is open source and available under the MIT License.

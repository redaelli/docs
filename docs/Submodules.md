## Implementing Docstrings in IntelOwl Documentation

In the IntelOwl documentation site, we use Git submodules to manage multiple repositories as child repositories. This allows us to fetch updated code (including docstrings and API specs) automatically, reducing redundant work for developers.

## Current Submodules

There are four submodules under the IntelOwlProject:

1. IntelOwl
2. GreedyBear
3. pyintelowl
4. GoIntelOwl

These submodules are updated daily via a cron job to ensure the documentation remains current.

## Making Changes to Documentation

When you make changes to the IntelOwl codebase, it typically takes a day for the submodules to update automatically. However, if you need to test changes immediately, you can do the following:

## Add Custom Submodules for Testing:

Point the submodule in `.gitmodules` to your fork of the repository to check the updates instantly.

### Update Submodules:

After modifying `.gitmodules`, run the following command to fetch the latest changes:

```
git submodule update --remote --merge
```

This ensures that your documentation reflects the most recent code changes without waiting for the daily update.

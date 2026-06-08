# Contributing

Contributions are welcome — new skills, agents, tools, references, and corrections as
answer engines evolve.

## Structure

Each skill is a folder under `skills/<skill-name>/`:

```
skills/<skill-name>/
  SKILL.md          # the skill (one per folder, at its root)
  references/       # optional supporting docs
  templates/        # optional checklists / templates
  scripts/          # optional runnable helpers
```

`SKILL.md` has YAML front matter with a `name` and a `description`, followed by the
instructions. The `description` is what an agent uses to decide when to load the skill, so
make it specific. Agents live in `agents/`; shared references live in `references/`. The
easiest approach is to match the shape of an existing skill.

## Pull requests

Keep each pull request focused (one skill, agent, tool, or coherent change), and briefly
describe what it does. All additions are reviewed before merging.

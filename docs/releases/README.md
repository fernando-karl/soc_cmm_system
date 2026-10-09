# Release notes

The body of each GitHub release, kept here so it is versioned with the code and
can be passed to `gh release create --notes-file`.

| Version | Notes |
| --- | --- |
| 2.1.0 | [v2.1.0.md](v2.1.0.md) |
| 2.0.1 | [v2.0.1.md](v2.0.1.md) |
| 2.0.0 | [v2.0.0.md](v2.0.0.md) |

A published release body can be refreshed from its file with
`gh release edit vX.Y.Z --notes-file docs/releases/vX.Y.Z.md`, which is how a
release whose notes were written before the last commits landed gets corrected.

For the full change history see [`../../CHANGELOG.md`](../../CHANGELOG.md).

## Cutting a release

**Always name the commit explicitly when tagging.** `git tag -a vX.Y.Z` with no
commit argument tags whatever `HEAD` happens to be, which is not necessarily
the commit you think it is — a local branch that has diverged from `origin`
will tag the wrong history, and pushing that tag uploads it.

```
git fetch origin main
git reset --hard origin/main
git rev-parse HEAD
```

Check that SHA is the release commit, then pass it to `git tag`:

```
git tag -a vX.Y.Z <sha> -m "SOC CMM Assessment System X.Y.Z"
git push origin vX.Y.Z
gh release create vX.Y.Z --title "..." --notes-file docs/releases/vX.Y.Z.md
```

This matters more than it looks. The history was rewritten once to purge
committed SQLite databases, so a pre-rewrite local clone shares **no common
ancestor** with `main`. Tagging such a clone makes that purged history
reachable again, and `git push` will happily upload it. If it happens: delete
the remote tag (`git push origin :refs/tags/vX.Y.Z`), which makes the objects
unreachable, then ask GitHub Support to purge the cached views, since
unreachable objects stay fetchable by SHA until they are garbage-collected.

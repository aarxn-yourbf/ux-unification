# PRD: Rule version history & rollback

## Problem
Data scientists edit fraud rules often. When a change causes a spike in false positives, they cannot see what changed or go back to a previous version quickly. Today they ask engineering to restore from the database.

## Users
- Data scientist (primary): edits and publishes rules.
- Fraud manager: reviews changes, cannot edit.

## Goals
- See every saved version of a rule with author, date and change summary.
- Compare two versions side by side.
- Roll back to a previous version in under 1 minute.

## Requirements
1. A "Change log" for each rule listing versions (version number, author, date, status, summary).
2. Select two versions and see a diff of the rule conditions.
3. "Restore this version" creates a new version from an old one. Must ask for confirmation.
4. Managers can view the change log and diffs but cannot restore.
5. Empty state when a rule has only one version.

## Success metrics
- Median time to rollback < 1 min.
- 50% fewer engineering tickets for rule restores.

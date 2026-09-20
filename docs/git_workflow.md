# AtmoSync Git Workflow

## Purpose

This document describes the Git workflow used by the AtmoSync team for collaborative development.

## 1. Main Branch

The `main` branch contains the integrated project code.

Team members should avoid making unnecessary direct changes to the main branch.

## 2. Individual Branches

Each team member should work on their own branch.

Example branches:

- member1
- member2
- member3
- member4

## 3. Pull Latest Changes

Before starting new work, update the local repository.

bash
git checkout main
git pull origin main
`

## 4. Switch to Personal Branch

Example:

bash
git checkout member4


## 5. Make Changes

Complete the assigned project task and test the changes locally.

## 6. Check Changes

Use:

bash
git status


Review the files before committing.

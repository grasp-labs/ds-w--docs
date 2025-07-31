# 🚪 Release Management Guide for Microservice Architecture

This document outlines how to structure, tag, and promote **pre-releases (alpha, beta, RC)** across a **distributed codebase** with:

- Microservice architecture (micro-arch pattern)
- Multiple repositories and languages (React, JavaScript/TypeScript, Go, Python, Rust, Node.js)
- Event-driven architecture via **Kafka**
- Single domain + network model
- React-based frontend (with micro frontends for features)

---

## 📀 Architectural Overview

### Components

| Layer     | Stack                                  | Notes                                             |
| --------- | ---------------------------------------- | ------------------------------------------------- |
| Frontend  | React (JS/TS), micro-frontends          | Feature-isolated deploys via routing or shell app |
| Backend   | Go, Python, Rust, Node.js               | Each service is versioned independently           |
| Messaging | Kafka                                   | Event schemas and compatibility tracked           |
| Infra     | Terraform / Helm / K8s (on EC2)         | Transitioning from ECS to Kubernetes on EC2       |

---

## 🔖 Semantic Versioning Strategy

Every deployable component (frontend, service, schema, infra) follows **SemVer**:

```text
MAJOR.MINOR.PATCH-PRERELEASE
```

| Segment    | Meaning                               |
| ---------- | ------------------------------------- |
| MAJOR      | Breaking API changes or schema events |
| MINOR      | New features, backward compatible     |
| PATCH      | Bug fixes and safe changes            |
| PRERELEASE | `alpha`, `beta`, `rc` tags            |

---

## 🪪 Pre-release Lifecycle

| Stage  | Purpose                            | Tag format       | Stability     |
| ------ | ---------------------------------- | ---------------- | ------------- |
| Alpha  | Internal, unstable, early testing  | `v1.2.0-alpha.1` | 🔴 Low        |
| Beta   | Feature complete, for QA & staging | `v1.2.0-beta.1`  | 🟧 Medium     |
| RC     | Final QA, candidate for stable     | `v1.2.0-rc.1`    | 🟨 High       |
| Stable | Public release or production ready | `v1.2.0`         | 🟩 Production |

---

## 📂 Multi-Repo Coordination

### Tagging Rules

- Each **repository** (service, frontend, shared libs) is tagged independently.
- A **release coordination system** stores:
  - Changelogs
  - Composite release manifests
  - Version matrices (infra ⬌ services ⬌ frontend ⬌ kafka ⬌ k8s)

### 🔄 DynamoDB-Based Coordination (Recommended)

Instead of managing YAML files manually, each repo pushes metadata into a **central DynamoDB table** via GitHub Actions.

**Table: `ReleaseFragments`**

| PK (`version`) | SK (`component#name`)     | Attributes (simplified)                   |
| -------------- | ------------------------- | ----------------------------------------- |
| `v1.4.0`       | `backend#auth-service`    | version, commit, artifact, date           |
| `v1.4.0`       | `frontend#shell`          | version, npm version, build SHA           |
| `v1.4.0`       | `kafka#user.created`      | schema version, evolution policy          |
| `v1.4.0`       | `infra#helm-auth`         | chart version, values hash                |
| `v1.4.0`       | `k8s#prod-deployment/api` | deployment hash, image ref, readyReplicas |

GitHub Actions push each fragment after a tagged release. These fragments form the **real-time release matrix**.

---

## 📊 Real-Time Dashboard via React + Vite

A standalone dashboard runs locally (via Vite) as a **micro frontend**, and queries the DynamoDB `ReleaseFragments` table directly using AWS SDK.

### 💡 Key Features:

- Display real-time matrix of all released components per version
- Filter by version, type (frontend/backend/kafka/etc.), environment
- Show schema and infra states alongside service versions
- Highlight discrepancies or incomplete deployments

### 🛋️ Tech Stack:

- React (JavaScript or TypeScript) with Tailwind or Material UI
- AWS SDK v3 for DynamoDB (no backend needed)
- Local-only micro frontend (no routing or shell required)

---

## 🔧 Tooling

| Tool                          | Purpose                               |
| ----------------------------- | ------------------------------------- |
| GoReleaser                    | Binary builds + tagging (Go services) |
| Semantic Release / Changesets | JS/Node monorepo versioning           |
| GitHub Actions / Workflows    | CI/CD per component                   |
| Git tags                      | Pre-release tracking                  |
| Kafka schema registry         | Event versioning + validation         |
| Helm, Terraform               | Infra release tracking                |
| DynamoDB                      | Central release metadata store        |

---

## 🧷 Release Process (per Component)

### 1. Alpha Release

```bash
git commit -am "feat: initial async handler for X"
git tag v1.4.0-alpha.1
git push origin v1.4.0-alpha.1
```

CI/CD will:

- Build + publish tagged artifacts
- Push metadata to DynamoDB
- Deploy to internal dev or ephemeral envs

### 2. Beta Release

```bash
git tag v1.4.0-beta.1
git push origin v1.4.0-beta.1
```

CI/CD will:

- Push to **QA/staging**
- Run full integration & regression tests
- Update release matrix in DynamoDB

### 3. RC Release

```bash
git tag v1.4.0-rc.1
git push origin v1.4.0-rc.1
```

- Deployed to **production-like** env
- RC validated by release manager or automation
- Can be promoted to stable if approved

### 4. Promote to Stable

```bash
git tag v1.4.0
git push origin v1.4.0
```

---

## 🔄 Kafka Schema Versioning

- Follow **evolution rules** (backward/forward compatible)
- Tag Kafka schemas using `vX.Y.Z` with metadata in Git or DynamoDB
- Promote schema versions in sync with service versioning

---

## 🎨 Frontend Pre-Releases

Each **micro-frontend**:

- Uses `Changesets` (or Nx release flow)
- Versioned independently (`feature-profile@v2.3.0-beta.1`)
- Published as NPM packages or lazy-loaded chunks
- Reflected in the DynamoDB release matrix

---

## 📆 Composite Release Visualization

Instead of managing files like `manifest.yaml`, a dashboard reads the current state from DynamoDB and visualizes it live.

Use cases:

- See what’s been deployed to each environment
- Show which components are missing or mismatched
- Visualize full version matrix across domains

---

## 📊 Dashboards & Visibility

- Vite-powered React dashboard (local or deployed)
- DynamoDB as backend source of truth
- Slack notifications and CI reports can pull from DynamoDB directly

---

## ✅ Best Practices

- 🔒 Lock all build inputs by tag (infra, events, deps)
- 🧲 Automate QA per pre-release stage (smoke → regression)
- 🧥 Maintain changelogs and commit policies (Conventional Commits)
- 🤝 Tie RC/stable releases to business OKRs or cutoffs
- 📁 Store and display manifest state in DynamoDB and make it queryable

---

## 🚦 Summary Flow

```plaintext
[Alpha] → internal testing
   ↓
[Beta] → QA/staging
   ↓
[RC] → pre-prod, candidate review
   ↓
[Stable] → production
```


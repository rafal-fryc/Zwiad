# Laptop Mirror of Zwiad Outputs — Syncthing Design

## Context

Zwiad runs on a headless Linux (Tegra) box. The user wants the output files — bill trackers / PDFs / markdowns in `~/projecty/Zwiad/bills/` and published research memos in `~/projecty/zwiad-reports/memos/` — to appear automatically on a Windows laptop that travels on different networks. The laptop is a read-only viewer; no work happens there. "Autoupdating" means: a new file produced on Tegra appears on the laptop without manual action.

## Approach — Syncthing (send-only → receive-only)

Two Syncthing folders, each send-only on Tegra and receive-only on Windows.

| Folder ID | Tegra path | Windows path |
|---|---|---|
| `zwiad-bills` | `~/projecty/Zwiad/bills/` | `C:\Users\<user>\ZwiadMirror\bills\` |
| `zwiad-reports` | `~/projecty/zwiad-reports/memos/` | `C:\Users\<user>\ZwiadMirror\reports\` |

Receive-only on the laptop means Syncthing refuses any local change and reverts modifications — the laptop cannot push anything back.

## Components

### Tegra
- Install Syncthing via apt (`syncthing` package, v1.18 is sufficient for interop with modern peers).
- Run as a systemd **user** service: `systemctl --user enable --now syncthing.service`. Enable `loginctl enable-linger rafal` so it keeps running when the user is not logged in.
- Web UI at `http://localhost:8384`. Configure the two folders as Send Only. Filesystem watcher enabled (default) for ~1s change detection.
- Ignore patterns per folder: `.git`, `.github`, `__pycache__`, `.DS_Store`, `Thumbs.db`, `*.tmp`.

### Windows
- User already installed SyncTrayzor.
- Accept each folder invite; set each to Receive Only; destination under `C:\Users\<user>\ZwiadMirror\`.

### Pairing
- Exchange device IDs between Tegra web UI and SyncTrayzor — one-time.

## Data flow

```
File written on Tegra  →  Syncthing watcher (<1s)  →
  peer connection (direct if possible, else public relay)  →
  SyncTrayzor on laptop  →  file on disk under ZwiadMirror\
```

End-to-end TLS. No cloud account, no storage fees.

## Failure modes

- **Laptop offline:** Tegra queues; syncs when laptop reconnects.
- **Tegra reboot:** systemd user service restarts Syncthing automatically (with `enable-linger` set).
- **NAT traversal fails:** Syncthing's public relay servers carry traffic (slower but functional).
- **Accidental write on laptop:** Receive-Only reverts it; no corruption.

## Verification

1. Tegra web UI and SyncTrayzor both show "Connected" with each other.
2. Both folders report "Up to Date" on Tegra (send) and "Up to Date" on laptop (receive).
3. `touch ~/projecty/Zwiad/bills/_sync-test.txt` on Tegra → appears on laptop within 10 s; `rm` it on Tegra → disappears on laptop.
4. Attempt `New > Text Document` on laptop inside `ZwiadMirror\bills\` → file is reverted; SyncTrayzor logs a rejection.

## Out of scope

- Bidirectional edits (not needed — Tegra is source of truth).
- Syncing code, `.env`, pipeline state, or anything outside `bills/` and `zwiad-reports/memos/`.
- Running the pipeline on the laptop.

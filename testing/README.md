# Testing and Simulation Tools

This folder contains scripts to fully simulate your telemetry app without hardware.

## Setup Virtual Serial Ports

- **Windows**: Use [com0com](https://sourceforge.net/projects/com0com/) to create a paired COM5 ↔ COM6.
- **Linux/macOS**: Use `socat`:
  ```bash
  socat -d -d pty,raw,echo=0 pty,raw,echo=0

# Architecture

## Overview

BigRed WebSocket Client locates NetScout nGeniusPULSE devices on networks by querying WebSocket servers on port 8000 for device attributes and system information.

## Core Components

1. **Network Scanner** - Asynchronous port scanning
2. **WebSocket Client** - Device communication
3. **Attribute Query** - Device information retrieval
4. **Logging System** - Detailed debug logging

## Technical Implementation

- Uses websockets library for WebSocket communication
- Asyncio for efficient scanning
- MAC address filtering support
- Multilingual output (English/Spanish)

## Design Principles

- Async I/O for performance
- Flexible filtering options
- Comprehensive logging
- Internationalization support

---
Author: Kris Armstrong

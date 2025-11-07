# API Documentation

## Usage

```bash
python BigRedWebSocketClient.py <network> [--mac-suffix XX] [--detail 0-9] [--lang en|es]
```

**Arguments**:
- `network`: IPv4 network to scan
- `--mac-suffix`: Filter by MAC address suffix
- `--detail`: Output detail level (0-9)
- `--lang`: Output language (en/es)

**Examples**:
```bash
# Basic scan
python BigRedWebSocketClient.py 192.168.1.0/24

# Filter by MAC and Spanish output
python BigRedWebSocketClient.py 10.0.0.0/24 --mac-suffix A4:12 --lang es
```

## Dependencies

```
websockets>=10.0
```

Install: `pip install -r requirements.txt`

---
Author: Kris Armstrong

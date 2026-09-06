# RelayX

A lightweight, cross-platform file-sharing tool that lets you send files between your Mac and Android (or any device with a browser) over your local Wi-Fi network — no app installs, no cloud, no cables.

## How it works

RelayX runs a small Python web server on your Mac. Any device on the same Wi-Fi network can open a browser, visit your Mac's local IP address, and upload or download files directly — no native app needed on the other end.

## Features (v0.1)

- Upload multiple files from any browser (phone, tablet, laptop)
- Files saved locally to a `received/` folder on the host machine
- No account, no cloud, no internet required — everything stays on your local network

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Setup

1. Clone the repo
2. Create a virtual environment and activate it:
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies:
```bash
   pip install fastapi uvicorn python-multipart
```
4. Run the server:
```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
```
5. On another device connected to the same Wi-Fi, open a browser and go to: 
http://<your-local-ip>:8000
## Roadmap

- [ ] Two-way file transfer (download files back to phone)
- [ ] Text/clipboard sync between devices
- [ ] Auto-discovery (no manual IP typing)
- [ ] Pairing/authentication for security
- [ ] Packaged as a standalone desktop app

## Why I built this

Built as a hands-on project to learn networking, HTTP, and cross-platform communication fundamentals — skills that carry into broader systems and security work.

## License

MIT
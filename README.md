# NEXDRIVE AI

NEXDRIVE AI is an early-stage Python project for experimenting with AI-assisted
autonomous driving in Grand Theft Auto V (GTA V) Story Mode. It focuses on
pretrained models, transfer learning, and software integration rather than
training large models from scratch.

> This repository is a modular foundation only. No GTA V assets or proprietary
> content are included, and autonomous driving is not currently functional.

## Planned architecture

```text
app/
  capture/     Screen capture and frame previews
  perception/  Object detection and road segmentation interfaces
  decision/    Driving-agent interfaces and driving actions
  control/     Safe controller interfaces and emergency stop
  evaluation/  Future latency, reliability, and performance metrics
  ui/          Future desktop interface
configs/       Configuration examples
scripts/       Development and operational scripts
tests/         Automated unit tests
docs/          Project documentation
```

Perception, decision, and control are deliberately separated. A real perception
model or game controller must be added behind the existing interfaces; it must
not be embedded directly into the capture or UI modules.

## Local setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
pytest
```

Capture and preview require MSS and OpenCV to be installed (included in
`requirements.txt`). The unit tests do not require GTA V, a GPU, or a game
window.

## Environment configuration

Copy the example configuration and adjust it as needed:

```bash
cp configs/nexdrive.env.example .env
```

| Variable | Purpose | Default |
| --- | --- | --- |
| `NEXDRIVE_CAPTURE_TOP` | Capture region top offset | `0` |
| `NEXDRIVE_CAPTURE_LEFT` | Capture region left offset | `0` |
| `NEXDRIVE_CAPTURE_WIDTH` | Capture region width | `1920` |
| `NEXDRIVE_CAPTURE_HEIGHT` | Capture region height | `1080` |

Application settings are loaded in `app.config`.

## Preview captured frames

On a system with an available display, run:

```bash
python scripts/preview_capture.py
```

Press `q` to close the OpenCV preview window.

## Development roadmap

1. Add real-screen capture calibration and frame buffering.
2. Add a YOLO object-detection implementation behind `ObjectDetector`.
3. Add a SegFormer or compatible road-segmentation implementation.
4. Integrate and evaluate a pretrained driving decision model.
5. Fine-tune only when sufficiently representative GTA V data is available.
6. Add explicitly safe Story Mode control and emergency-stop handling.
7. Add desktop UI, telemetry, and formal evaluation.

## Current limitations

- No pretrained checkpoint is bundled or downloaded.
- Object detection and segmentation are placeholders.
- The driving agent returns a mock safe action.
- The mock controller never sends keyboard or virtual-controller input.
- No GTA V integration or autonomous vehicle control exists.
- GTA Online automation is not supported or planned.

See [docs/architecture.md](docs/architecture.md) for module responsibilities.

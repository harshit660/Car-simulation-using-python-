# Car Simulation by Harshit

An original top-down Python driving game controlled with your keyboard or a virtual steering wheel made from your hands and webcam.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-2d8c3c)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- Play immediately with **arrow keys** or **WASD**.
- Turn on webcam steering: show two hands, hold them like a steering wheel, and tilt them left or right.
- Smooth dead-zone filtering so a level hand position drives straight.
- Adjustable webcam index, camera preview, and invert-steering option.
- All game artwork is drawn in Python; no downloaded images, models, or asset folders are required.
- Includes tests and a GitHub Actions workflow.

## Project files

```text
car-simulation-by-harshit/
├── .github/workflows/ci.yml       # Runs tests on GitHub
├── src/car_simulation/
│   ├── app.py                     # Command-line startup
│   ├── config.py                  # Game and camera settings
│   ├── game.py                    # Pygame driving game
│   ├── geometry.py                # Steering math
│   └── gesture_controller.py      # OpenCV + MediaPipe hand control
├── tests/test_geometry.py          # Small automated tests
├── main.py                        # Easiest file to run in an IDE
├── requirements.txt               # Runtime packages
├── requirements-dev.txt           # Test packages
├── pyproject.toml                 # Package/project metadata
├── .gitignore                     # Keeps local files out of Git
└── LICENSE                        # MIT license
```

## Requirements

- Python **3.10, 3.11, or 3.12**
- A webcam only if you want hand steering
- Windows, macOS, or Linux

> If you use Python 3.13+ and MediaPipe does not install on your computer, create the environment with Python 3.12 instead. The keyboard-only game can still run once Pygame is installed.

## Run from your IDE (recommended)

1. Open the `car-simulation-by-harshit` folder in VS Code, PyCharm, or another Python IDE.
2. Create and activate a virtual environment in the IDE terminal.

   **Windows PowerShell**

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. Install packages:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. In your IDE, select the `.venv` Python interpreter, then run [`main.py`](main.py).

   Or run from the terminal:

   ```bash
   python main.py
   ```

## Controls

| Key / gesture | Action |
| --- | --- |
| `Left` / `A`, `Right` / `D` | Steer left / right |
| `Up` / `W`, `Down` / `S` | Accelerate / brake |
| Tilt two visible hands | Virtual steering wheel input |
| `G` | Turn webcam steering on or off |
| `P` | Toggle annotated webcam preview |
| `R` | Restart after a crash |
| `Esc` | Quit |

Keyboard steering always takes priority while a steering key is held, which makes it easy to correct the car or test the game without a camera.

## Camera setup

When the game starts, it asks to access the default camera (`0`). Allow the permission request if one appears. Hold both hands toward the camera with the knuckles facing it; keep them separated and tilt the imaginary wheel.

Useful commands:

```bash
# Keyboard only: no camera access
python main.py --no-camera

# Use a second/external camera
python main.py --camera-index 1

# Show a webcam window with landmarks and calculated steering angle
python main.py --camera-preview

# Reverse left/right if your camera setup feels opposite
python main.py --invert-steering
```

To tune the default camera behavior, edit `GestureConfig` in [`src/car_simulation/config.py`](src/car_simulation/config.py):

- `camera_index`: change from `0` to `1` or `2` for another camera.
- `dead_zone_degrees`: increase it if the car wobbles while your hands are level.
- `full_turn_degrees`: lower it if you want sharper turns.
- `flip_camera`: set to `False` if a non-mirrored external camera feels wrong.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `Camera 0 could not be opened` | Close other camera apps; press `G` after plugging in the webcam; try `--camera-index 1`. |
| Car does not respond to hands | Make sure both hands are fully visible, well lit, and not overlapping. Press `P` to check landmark detection. |
| Steering is backwards | Start with `python main.py --invert-steering`. |
| PowerShell blocks activation | Run `Set-ExecutionPolicy -Scope Process Bypass`, or let the IDE create/select the `.venv` interpreter. |
| Package installation fails | Confirm `python --version` is 3.10–3.12, upgrade pip, then retry. |

## Run tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Upload to GitHub

1. On [GitHub](https://github.com/new), create an empty repository named `car-simulation-by-harshit`. Do **not** add a README, `.gitignore`, or license there because this folder already includes them.
2. In the IDE terminal, make sure you are inside this project folder and run the following. Replace `YOUR-GITHUB-USERNAME` with your account name.

   ```bash
   git init
   git add .
   git commit -m "Create Car Simulation by Harshit"
   git branch -M main
   git remote add origin https://github.com/YOUR-GITHUB-USERNAME/car-simulation-by-harshit.git
   git push -u origin main
   ```

3. Sign in to GitHub if prompted. GitHub may ask for a browser login or a personal access token; it will not accept an account password for command-line pushes.

## Attribution

This is an original game implementation. Its general webcam hand-tilt idea was inspired:: no code or project files were copied from that repository.

## License

This project uses the [MIT License](LICENSE). You may use, modify, and share it while keeping the license notice.

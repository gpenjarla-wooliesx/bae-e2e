
# BAE E2E Test Suite

## Installing Python

If you do not have Python installed, follow these steps:

### Windows
1. Download the latest Python installer from the Company portal.
2. Run the installer. **Check the box that says "Add Python to PATH"** before clicking "Install Now".
3. Verify installation:
   ```sh
   py --version
   ```

### macOS
1. Open Terminal and install Homebrew if not already installed:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python:
   ```sh
   brew install python
   ```
3. Verify installation:
   ```sh
   python3 --version
   ```

### Linux (Debian/Ubuntu)
1. Open Terminal and run:
   ```sh
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```
2. Verify installation:
   ```sh
   python3 --version
   ```

---


## Setup Instructions

1. **Clone the repository** (if not already done):
   ```sh
   git clone <repo-url>
   cd bae-e2e
   ```

2. **Create a virtual environment** (recommended):
   ```sh
   py -m venv venv
   .\venv\Scripts\activate
   ```
   If you see a script execution error, run this command in PowerShell first:
   ```sh
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   .\venv\Scripts\Activate
   ```

3. **Install dependencies**:
   ```sh
   py -m pip install -r requirements.txt
   ```

## Running the Tests

1. **Navigate to the project root** (if not already there):
   ```sh
   cd bae-e2e
   ```

2. **Run all tests**:
   ```sh
   py -m pytest
   ```

3. **(Optional) Set environment variables**:
   If your tests require an environment (like `dev`), set it before running pytest:
   ```sh
   $env:ENV="dev"; pytest
   ```
   Or in bash:
   ```sh
   ENV=dev pytest
   ```

## Troubleshooting

- If you see errors about script execution policy, see step 2 above.
- If you see errors about missing modules, ensure you have installed all requirements.
- If you need to pass custom arguments, check your project's conftest.py or test documentation.

---

For more help, contact the project maintainer.

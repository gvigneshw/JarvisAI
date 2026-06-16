import subprocess

from core.tool_registry import register_tool


APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": r"C:\Program Files\WindowsApps\Microsoft.Paint_11.2603.251.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
}



def open_app(app):

    app = app.lower()

    print(f"DEBUG: Requested app = {app}")

    if app not in APPS:
        return f"Unknown application: {app}"

    print(f"DEBUG: Launching {APPS[app]}")

    subprocess.Popen(
    APPS[app],
    shell=True
)

    return f"{app} opened."

register_tool(
    "open_app",
    "Open a Windows application",
    open_app,
    parameters={
        "app": "string"
    }
)
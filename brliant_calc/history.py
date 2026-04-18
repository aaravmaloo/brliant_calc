import json
import os
from pathlib import Path
from datetime import datetime


def get_history_dir():
    hist_dir = Path.home() / ".brliant_calc_history"
    hist_dir.mkdir(parents=True, exist_ok=True)
    return hist_dir

def get_history_file():
    return get_history_dir() / "history.json"

def _load_history():
    hist_file = get_history_file()
    if hist_file.exists():
        with open(hist_file, 'r') as f:
            return json.load(f)
    return []

def _save_history(history):
    hist_file = get_history_file()
    with open(hist_file, 'w') as f:
        json.dump(history, f, indent=2)

def save_entry(command, result):
    history = _load_history()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "command": command,
        "result": str(result)
    }
    history.append(entry)
    _save_history(history)
    return entry

def list_history(limit=20):
    history = _load_history()
    if not history:
        return "No history entries found."
    entries = history[-limit:]
    output = []
    for i, entry in enumerate(entries, 1):
        ts = entry.get("timestamp", "unknown")
        cmd = entry.get("command", "unknown")
        res = entry.get("result", "unknown")
        output.append(f"#{i} [{ts}] {cmd} = {res}")
    return "\n".join(output)

def recall(index):
    history = _load_history()
    if not history:
        return "No history entries found."
    idx = int(index)
    if idx < 1 or idx > len(history):
        return f"Error: Index out of range (1-{len(history)})."
    entry = history[idx - 1]
    return f"Command: {entry.get('command', 'unknown')}\nResult: {entry.get('result', 'unknown')}"

def clear_history():
    hist_file = get_history_file()
    if hist_file.exists():
        hist_file.unlink()
        return "History cleared."
    return "No history to clear."

def search_history(query):
    history = _load_history()
    if not history:
        return "No history entries found."
    results = []
    for i, entry in enumerate(history, 1):
        cmd = entry.get("command", "")
        res = entry.get("result", "")
        if query.lower() in cmd.lower() or query.lower() in res.lower():
            ts = entry.get("timestamp", "unknown")
            results.append(f"#{i} [{ts}] {cmd} = {res}")
    if not results:
        return f"No entries matching '{query}'."
    return "\n".join(results)

def export_history(filepath):
    history = _load_history()
    if not history:
        return "No history to export."
    with open(filepath, 'w') as f:
        json.dump(history, f, indent=2)
    return f"History exported to {filepath}"

def history_stats():
    history = _load_history()
    if not history:
        return "No history entries."
    total = len(history)
    commands = {}
    for entry in history:
        cmd = entry.get("command", "unknown")
        parts = cmd.split()
        category = parts[0] if parts else "unknown"
        commands[category] = commands.get(category, 0) + 1
    stats = f"Total entries: {total}\n"
    stats += "Breakdown by category:\n"
    for cat, count in sorted(commands.items(), key=lambda x: -x[1]):
        stats += f"  {cat}: {count}\n"
    return stats

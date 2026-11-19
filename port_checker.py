import socket
from datetime import datetime

def check_port(target, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return "OPEN"
        elif result == 111 or result == 10061:
            return "CLOSED"
        else:
            return "FILTERED"

    except socket.timeout:
        return "FILTERED"
    except socket.gaierror:
        return "INVALID HOST"
    except Exception:
        return "ERROR"


def main():
    print("=" * 55)
    print("           PORT STATUS CHECKER")
    print("=" * 55)

    target = input("Enter target IP address or hostname: ")

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not (1 <= start_port <= end_port <= 65535):
            print("Invalid port range! Use ports 1 to 65535.")
            return

    except ValueError:
        print("Please enter valid port numbers.")
        return

    print("\nScanning started at:", datetime.now())
    print("-" * 55)
    print(f"{'PORT':<15}{'STATUS':<20}{'SERVICE'}")
    print("-" * 55)

    for port in range(start_port, end_port + 1):
        status = check_port(target, port)

        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        print(f"{port:<15}{status:<20}{service}")

    print("-" * 55)
    print("Scanning completed!")
    print("Finished at:", datetime.now())
    print("=" * 55)


if __name__ == "__main__":
    main()
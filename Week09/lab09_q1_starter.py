import platform
import sys
import os


def get_system_info():
    return {
        "os": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "machine": platform.machine()
    }


def get_python_info():
    return {
        "version": sys.version,
        "executable": sys.executable,
        "platform": sys.platform
    }


def get_directory_info(path):

    exists = os.path.exists(path)

    return {
        "path": os.path.abspath(path),
        "exists": exists,
        "file_count": len(os.listdir(path)) if exists else 0,
        "is_directory": os.path.isdir(path)
    }


def display(title, info):
    print(f"\n--- {title} ---")
    for key, value in info.items():
        print(f"  {key:<12}: {value}")


def main():
    print("=" * 60)
    print("  SYSTEM INFORMATION REPORTER")
    print("=" * 60)

    system_info = get_system_info()
    python_info = get_python_info()
    directory_info = get_directory_info(".")

    display("System Info", system_info)
    display("Python Info", python_info)
    display("Directory Info for '.'", directory_info)

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
def main():
    """
    The main entry point. Invoke with 'python -m tqmath'.
    """
    try:
        print("Hello from tqmath!")
        val = input()
    except KeyboardInterrupt:
        from tqmath.status import ExitStatus
        return ExitStatus.ERROR_CTRL_C


if __name__ == "__main__":
    import sys

    sys.exit(main())

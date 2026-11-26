from daemon.core.application import Application

def main():
    title = "Daemon"
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()

    app = Application()
    try:
        app.start()
    except KeyboardInterrupt:
        print("\nShutdown signal received.")
        app.stop()



if __name__ == "__main__":
    main()
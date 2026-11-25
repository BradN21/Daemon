from daemon.core.application import Application

def main():
    title = "Daemon"
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()

    app = Application()
    app.start()



if __name__ == "__main__":
    main()
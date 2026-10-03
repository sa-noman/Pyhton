def notify(title, message, timeout=5):
    from plyer import notification
    notification.notify(title=title, message=message, timeout=timeout)

if __name__ == "__main__":
    notify("Python Fundamentals", "Your reminder is ready.")

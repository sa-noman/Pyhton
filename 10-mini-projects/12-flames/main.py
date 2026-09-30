def flames_result(name1, name2):
    a = list(name1.lower().replace(" ", ""))
    b = list(name2.lower().replace(" ", ""))
    for ch in a[:]:
        if ch in b:
            a.remove(ch)
            b.remove(ch)
    count = len(a) + len(b)
    labels = list("FLAMES")
    meanings = {
        "F":"Friends","L":"Love","A":"Affection",
        "M":"Marriage","E":"Enemies","S":"Siblings"
    }
    index = 0
    while len(labels) > 1:
        index = (index + count - 1) % len(labels)
        labels.pop(index)
    return meanings[labels[0]]

if __name__ == "__main__":
    print(flames_result(input("First name: "), input("Second name: ")))

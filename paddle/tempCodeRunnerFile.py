for line in result[0]:
    text = line[1][0]
    confidence = line[1][1]
    print(f"{text} (conf: {confidence:.2f})")
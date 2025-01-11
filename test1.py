def is_palin():
    words = input("enter it: ").strip()
    if len(words)<3:
        print ("type in new word")
        return 0
    else:
        words2 = words[::-1]
        if words==words2:
            print ("is palin")
        else:
            print ("not a pain")
        return words, words2

new1 = is_palin()
print("sdaasd", new1)






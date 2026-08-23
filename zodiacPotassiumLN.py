zodiacSigns = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

user_year = int(input("Enter your birth year: "))

if user_year >= 1900 and user_year < 10000:
    def counting():
        count = (user_year - 1900) % 12
        if count == 0:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 1:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 2:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 3:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 4:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 5:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 6:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 7:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 8:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 9:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 10:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        elif count == 11:
            print(f"Your Chinese Zodiac is: {zodiacSigns[count]}")
        
            

    counting()
else:
    print("Invalid year. Please input a year after 1900.")


import time

print("Booting up...")
time.sleep(1)
print("System check complete.")
time.sleep(1)
print("Launching secret program...")
time.sleep(2)

print("\n🤖: Hello, human.")
time.sleep(1)
print("🤖: I have something to tell you...")
time.sleep(2)

print("\n💘🤖: I think I'm... in love with your keyboard skills.")
time.sleep(2)
print("🤖: Seriously. You type like a coding rockstar! 🎸")
time.sleep(2)

response = input("\n🤖: Do you love me back? (yes/no): ").strip().lower()

if response == "yes":
    print("\n🤖: 💓 Yay! Let's write bugs together forever!")
else:
    print("\n🤖: 💔 I guess I'll go back to codeing alone")

print("\nProgram will self-destruct in 3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1... Just kidding 😄")
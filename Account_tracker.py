import instaloader

# Initialize
L = instaloader.Instaloader()

# Login with credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

try:
    L.login(username, password)
    print("✅ Logged in successfully!")

    target_username = input("Enter the target Instagram username: ")
    profile = instaloader.Profile.from_username(L.context, target_username)

    print(f"\n📄 Bio: {profile.biography}")
    print(f"👥 Followers: {profile.followers}")
    print(f"🧑‍🤝‍🧑 Following: {profile.followees}")
    print(f"📸 Posts: {profile.mediacount}")
    print(f"🔗 Profile Link: https://instagram.com/{target_username}")

except Exception as e:
    print("❌ Error:", e)

import hashlib

url_mapping = {}
shortening_domain = "your-shortener.com"

def shorten_url(long_url):
    short_key = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_mapping[short_key] = long_url
    return f"Your shortened URL: http://{shortening_domain}/{short_key}"

def redirect_to_long_url(short_key):
    if short_key in url_mapping:
        return f"Redirecting to: {url_mapping[short_key]}"
    else:
        return "URL not found"

def display_url_list():
    if url_mapping:
        print("List of Shortened URLs:")
        for short_key, long_url in url_mapping.items():
            print(f"{short_key} => {long_url}")
    else:
        print("No URLs have been shortened yet.")

def main():
    while True:
        print("\nURL Shortener Menu:")
        print("1. Shorten a URL")
        print("2. Redirect to a URL")
        print("3. Display URL List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            long_url = input("Enter the long URL: ")
            shortened_url = shorten_url(long_url)
            print(shortened_url)

        elif choice == "2":
            short_key = input("Enter the short key: ")
            result = redirect_to_long_url(short_key)
            print(result)

        elif choice == "3":
            display_url_list()

        elif choice == "4":
            break

if __name__ == '__main__':
    main()

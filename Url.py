import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return shortened_url

# Provide a different long URL for testing
long_url = "https://www.example.com/some/long/url"

# Call the URL shortener function
short_url = shorten_url(long_url)

# Print the shortened URL
print("Shortened URL:", short_url)


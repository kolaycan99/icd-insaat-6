import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0'}

# Bostik
try:
    req = urllib.request.Request('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bostik_logo.svg/512px-Bostik_logo.svg.png', headers=headers)
    with urllib.request.urlopen(req) as response, open('bostik.png', 'wb') as out_file:
        out_file.write(response.read())
except Exception as e:
    print(f"Bostik error: {e}")

# Henkel
try:
    req = urllib.request.Request('https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Henkel-Logo.svg/434px-Henkel-Logo.svg.png', headers=headers)
    with urllib.request.urlopen(req) as response, open('henkel.png', 'wb') as out_file:
        out_file.write(response.read())
except Exception as e:
    print(f"Henkel error: {e}")

# Kryton - Let's use a reliable PNG link for Kryton from another source, or just seeklogo
try:
    req = urllib.request.Request('https://seeklogo.com/images/K/kryton-international-logo-E8E42B9C80-seeklogo.com.png', headers=headers)
    with urllib.request.urlopen(req) as response, open('kryton.png', 'wb') as out_file:
        out_file.write(response.read())
except Exception as e:
    print(f"Kryton error: {e}")

import requests

def download_large_file(url, destination):
    """
    url - link for download
    destination - path to save file
    """
    response = requests.get(url, stream=True) # Download in chunks
    response.raise_for_status()  # Make sure the request was successful


    CHUNK_SIZE = 32768  # 32KB per chunk

    with open(destination, 'wb') as file:    # choose wb for non-text files or rb
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:  # Filter out keep-alive chunks
                file.write(chunk)

def download_file(url, destination):
    response = requests.get(url) 
    response.raise_for_status()   # Check for request errors

    with open(destination, 'wb') as file:
        file.write(response.content)

# mode 	what allows you to do?
# r: 	Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
# rb: 	Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
# r+: 	Opens a file for reading and writing, placing the pointer at the beginning of the file.
# w: 	Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
# wb: 	Opens a write-only file in binary mode.
# w+: 	Opens a file for writing and reading.
# wb+: 	Opens a file for writing and reading in binary mode.
# a: 	Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name doesn't exist.
# ab: 	Opens a file for appending in binary mode.
# a+: 	Opens a file for both appending and reading.
# ab+: 	Opens a file for both appending and reading in binary mode.

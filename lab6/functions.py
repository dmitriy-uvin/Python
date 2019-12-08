def up(data):
    return data.upper()

def split_data(user_input):
    arr = user_input.split(",")
    for j in range(len(arr)):
        arr[j] = arr[j].title().strip()
    return arr

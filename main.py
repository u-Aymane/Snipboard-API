import random
import string
import threading

import requests


def check_img(img_id, option='jpg'):
    url = f'https://i.snipboard.io/{img_id}.{option}'

    response = requests.get(url)

    if response.status_code == 200:
        return 1, response.status_code, response.content
    # elif response.status_code != 200 and option == 'jpg':
    #     return check_img(img_id, option='png')
    else:
        return -1, response.status_code, ''


def save(binary_data, img_id):
    with open(f'IMGs/{img_id}.png', 'wb') as f:
        f.write(binary_data)
    f.close()


def main():
    all_strings = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for _ in range(1000000000):
        try:
            random_str = ''.join([random.choice(all_strings) for _ in range(6)])
            if random_str not in open('invalid.txt', 'r').read():
                data = check_img(random_str)
                if data[0] == 1:
                    print(f'{random_str}: Valid')
                    save(data[2], img_id=random_str)
                else:
                    with open(f'invalid.txt', 'a', encoding='utf-8') as f:
                        f.writelines(f'{random_str}\n')
                    f.close()
        except:
            pass


if __name__ == '__main__':
    n = int(input('Threads: '))
    threads = []
    for i in range(n):
        t = threading.Thread(target=main)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

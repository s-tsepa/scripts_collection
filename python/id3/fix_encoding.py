import os
import pprint

import mutagen.id3
from ftfy import fix_encoding

# music_root = '/media/st/Cloud/Audiobooks/Ray Stories/Bredberi_Rey_-_K_zapadu_ot_Oktyabrya.mp3.[torrents.ru]'
music_root = '/home/void/Downloads/Опыт построения исповеди/'
path = '/home/void/Downloads/Опыт построения исповеди/'
encodings = 'gb18030', 'cp1252'


def find_mp3_files(path):
    for child in os.listdir(path):
        child = os.path.join(path, child)
        if os.path.isdir(child):
            for mp3 in find_mp3_files(child):
                yield mp3
        elif child.lower().endswith(u'.mp3'):
            yield child


# files = list(find_mp3_files(music_root))
# print(*files, sep="\n")
#
# for f in files:
#     id3 = mutagen.id3.ID3(path)
#     a = mutagen.id3.ID3.load(path)

# path = files[0]

# path = '/media/st/Nextcloud/Audiobooks/Ray Stories/Bredberi_Rey_-_K_zapadu_ot_Oktyabrya.mp3.[torrents.ru]/' \
#        '07 Лорел и Гарди (роман).mp3'

# for key, value in id3.items():
#     value: str
#     pprint.pprint(key)
#
#     try:
#         # value.data: bytes
#         print(value.data.decode('latin-1'))
#     except Exception as e:
#         print(e)

for path in find_mp3_files(music_root):
    id3 = mutagen.id3.ID3(path)
    for key, value in id3.items():
        value: str
        pprint.pprint(key)
        pprint.pprint(value)

        try:
            # value.data: bytes
            print(value.data.decode('utf-8'))
        except Exception as e:
            print(e)
            print(type(getattr(value, 'text', [None])[0]))
            if value.encoding != 3 and isinstance(getattr(value, 'text', [None])[0], unicode):
        
                if value.encoding == 0:
                    bytes = '\n'.join(value.text).encode('iso-8859-1')
                    for encoding in encodings:
                        try:
                            bytes.decode(encoding)
                        except UnicodeError:
                            pass
                        else:
                            break
                    else:
                        raise ValueError('None of the tryencodings work for %r key %r' % (path, key))
                    for i in range(len(value.text)):
                        value.text[i] = value.text[i].encode('iso-8859-1').decode(encoding)
        
                value.encoding = 3
        id3.save()

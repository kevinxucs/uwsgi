import os

NAME = 'emperor_mongodb'

CFLAGS = [
    '-I/usr/include/mongo',
    '-I/usr/local/include/mongo'
]
LDFLAGS = []

LIBS = ['-lstdc++']
if 'UWSGI_MONGODB_NOLIB' not in os.environ:
    LIBS.append('-lmongoclient')
    LIBS.append('-lboost_thread')
    LIBS.append('-lboost_filesystem')

GCC_LIST = ['plugin', 'emperor_mongodb.cc']

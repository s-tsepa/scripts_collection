#include <stdio.h>
#include <string.h>
#include <dirent.h>

int main() {
    char* dirname = "/";
    DIR* dirp = opendir(dirname);
    if (dirp == NULL) { return 1 ; }

    struct dirent *d;
    // fill namelist arr with all "dirent" entries in directory
    while ((d = readdir(dirp)) != NULL ) {
        if (strcmp(d->d_name,".") != 0 && strcmp(d->d_name,"..") != 0) {
            printf("%s\n", d->d_name);
        }
    }
}
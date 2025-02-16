//
// Created by void on 3/21/23.
//


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <grp.h>
#include <dirent.h>
#include <unistd.h>
#include <pwd.h>

#define STR_SIZE 1024

#define USR_WRITE_BIT 7
#define GRP_WRITE_BIT 4
#define ALL_WRITE_BIT 1

#define USR_READ_BIT 8
#define GRP_READ_BIT 5
#define ALL_READ_BIT 2

struct path_rights {
    int writeable;
    int readable;
};

char* exclude_entries[] = { "/sys", "/proc" };

struct path_rights get_path_rights(struct stat path_stat, unsigned int uid, unsigned int gid) {
    unsigned int access_rights = path_stat.st_mode & ACCESSPERMS;

    struct path_rights pr = { 0, 0 };

    // file belongs to user
    if (path_stat.st_uid == uid) {
        if (access_rights & (1 << USR_WRITE_BIT)) { pr.writeable = 1; }
        if (access_rights & (1 << USR_READ_BIT)) { pr.readable = 1; }
    }

    // file belongs to group
    if (path_stat.st_gid == gid) {
        if (access_rights & (1 << GRP_WRITE_BIT)) { pr.writeable = 1; }
        if (access_rights & (1 << GRP_READ_BIT)) { pr.readable = 1; }
    }

    // access rights by all
    if (access_rights & (1 << ALL_WRITE_BIT)) { pr.writeable = 1; }
    if (access_rights & (1 << ALL_READ_BIT)) { pr.readable = 1; }

    return pr;
}

int traverse(char *path, unsigned int uid, unsigned int gid) {
    int exclude_arr_len = sizeof(exclude_entries) / sizeof(exclude_entries[0]);
    int matches_exclude = 0;
    for (int i = 0; i < exclude_arr_len; ++i) {
        if (strcmp(path, exclude_entries[i]) == 0) {
            matches_exclude = 1;
        }
    }
    if (matches_exclude) { return 0; }

    struct stat path_stat;
    if (lstat(path, &path_stat) == -1) {
        perror(path);
        return -1;
    }

    int is_dir = S_ISDIR(path_stat.st_mode);
    struct path_rights pr = get_path_rights(path_stat, uid, gid);

    if (pr.writeable) {
        char* prefix = is_dir ? "d" : "f";
        printf("%s %s\n", prefix, path);
    }

    if (is_dir && pr.readable) {
        DIR *dir = opendir(path);
        if (!dir) {
            char err_msg[STR_SIZE];
            sprintf(err_msg, "dir %s", path);
            perror(err_msg);
            return -1;
        }

        struct dirent *dirent_i;
        while ((dirent_i = readdir(dir)) != NULL) {
            if (strcmp(dirent_i->d_name, ".") == 0 || strcmp(dirent_i->d_name, "..") == 0) {
                continue;
            }

            char full_path[STR_SIZE];
            snprintf(
                full_path,
                sizeof(full_path),
                "%s/%s",
                // If path == "/", replace it with "" to avoid duplicate slashes "//sub-path"
                (strcmp(path, "/") == 0 ? "" : path),
                dirent_i->d_name
            );

            // Recursively dive into sub-dir
            traverse(full_path, uid, gid);
        }
        closedir(dir);
    }
    return 0;
}


int main(int argn, char** argv) {
    if (geteuid() != 0) {
        fprintf(stderr, "This program must be run as root\n");
        return 1;
    }

    char* username;
    char* groupname;
    char* path;

    if (argn == 4) {
        username = argv[1];
        groupname = argv[2];

        path = malloc(STR_SIZE);
        realpath(argv[3], path);
    } else {
        printf("Usage:\n# %s USERNAME GROUPNAME PATH\n", argv[0]);
        return -1;
    }

    struct group* grp = getgrnam(groupname);
    struct passwd* usr = getpwnam(username);

    if (grp == NULL) {
        fprintf(stderr, "No such group: %s\n", groupname);
        return -1;
    }

    if (usr == NULL) {
        fprintf(stderr, "No such user: %s\n", username);
        return -1;
    }

    unsigned int input_uid = usr->pw_uid;
    unsigned int input_gid = grp->gr_gid;

    return traverse(path, input_uid, input_gid);
}

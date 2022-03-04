#!/bin/bash
while [ -n "$1" ]
do
  case "$1" in
    *input_folder)
        in_fold="$2"
        ;;
    *extension)
        exten="$2"
        ;;
    *backup_folder)
        back_fold="$2"
        ;;
    *backup_archive_name)
        arch_name="$2"
        ;;
        *)
    esac
    shift shift
done
cd $in_fold
mkdir ./$back_fold
find $in_fold -path "./$back_fold/*" -prune -o "*$exten" -exec cp --parents "{}" ./$back_fold \;
tar -czf $arch_name.tar.gz ./$back_fold
echo "done"

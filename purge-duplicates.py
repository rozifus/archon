# clean duplicates

import os
from pymediainfo import MediaInfo
from recordtype import recordtype


format_preferences = [
    'webm',
    'mp4',
    'mkv'
]

Candidate = recordtype('Candidate', 'full_path format_index media_info')
candidates = {}

# bucket videos by filename (without extension)
for root, dirs, files in os.walk('.'):
    for f in files:
        try:
            full_path = os.path.join(root, f)
            extless, ext = os.path.splitext(full_path)
            media_format = ext.lstrip('.').lower()

            if media_format not in format_preferences:
                continue

            format_index = format_preferences.index(media_format)

            media_info = MediaInfo.parse(full_path)
            record = Candidate(full_path, format_index, media_info)

            if extless not in candidates:
                candidates[extless] = []
            candidates[extless].append(record)

        except Exception as e:
            print(e)

# remove non-duplicate videos
for key in list(candidates.keys()):
    if len(candidates[key]) < 2:
        candidates.pop(key)

# get list of unwanted duplicates to delete
del_paths = []

for duplicates in candidates.values():
    try:
        duration_check = duplicates[0].media_info.tracks[0].duration
        max_mtime = os.path.getmtime(duplicates[0].full_path)
        #preferred_format = duplicates[0].format_index

        for dup in duplicates[1:]:
            duration = dup.media_info.tracks[0].duration
            duration_ratio = float(duration_check) / float(duration)
            if duration_ratio < 0.99 or duration_ratio > 1.01:
                for d in duplicates:
                    print(d.media_info.tracks[0].duration)
                raise Exception("Duration different for " + dup.full_path)

            max_mtime = max(os.path.getmtime(dup.full_path), max_mtime)
            #preferred_format = min(dup.format_index, preferred_format)

        for dup in duplicates:
            #if dup.format_index > preferred_format:
            dup_mtime = os.path.getmtime(dup.full_path)
            if dup_mtime < max_mtime:
                print(dup_mtime, dup.full_path)
                #print(format_preferences[preferred_format], dup.full_path)
                del_paths.append(dup.full_path)


    except Exception as e:
        print(e)

for d in del_paths:
    os.remove(d)


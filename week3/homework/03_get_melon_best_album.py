genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# 결과로 [4, 1, 3, 0] 가 와야 합니다!


def get_melon_best_album(genre_array, play_array):
    album_hash = {}
    genre_keys = []
    total_plays_by_each_genres = {}
    plays_counter = 0
    max_plays_list = []

    for i in range(len(genre_array)):
        if album_hash.get(genre_array[i]) is None:
            album_hash[genre_array[i]] = list()
            genre_keys.append(genre_array[i])
        album_hash[genre_array[i]].append(play_array[i])

    # print(genre_keys)
    # del genre_keys[0]
    # print(genre_keys)
    # print(album_hash)
    # print(album_hash[genre_keys[0]][0])

    # store total plays in hash by each genre name (장르별 plays)
    for i in range(len(album_hash)):
        for j in range(len(album_hash[genre_keys[i]])):
            plays_counter += album_hash[genre_keys[i]][j]
        total_plays_by_each_genres[genre_keys[i]] = plays_counter

    # print(total_plays_by_each_genres)

    # find 2 biggest total plays by genre (최대 plays 2개 구하기)
    while len(max_plays_list) < 2:
        max_index = 0
        max_plays = -9999
        for i in range(len(genre_keys)):
            if total_plays_by_each_genres[genre_keys[i]] > max_plays:
                max_plays = total_plays_by_each_genres[genre_keys[i]]
                max_index = i
        max_plays_list.append(genre_keys[max_index])
        del genre_keys[max_index]


    # [pop- 2500, pop- 600, classic- 800, classic- 500] 구하기
    get_best_album = []
    for i in range(len(max_plays_list)):
        count = 0
        while count < 2:
            max_index = 0
            max_plays = -999  # genre 중에 가장 높은 play
            for j in range(len(album_hash[max_plays_list[i]])):
                if max_plays < album_hash[max_plays_list[i]][j]:
                    max_plays = album_hash[max_plays_list[i]][j]
                    max_index = j
            get_best_album.append(album_hash[max_plays_list[i]][max_index])
            album_hash[max_plays_list[i]][max_index] = -9999
            count += 1

    # print(get_best_album)

    # [2500, 600, 800, 500] -> [4, 1, 3, 0] 구하기
    for i in range(len(get_best_album)):  # [2500, 600, 800, 500]
        for j in range(len(play_array)):  # [500, 600, 150, 800, 2500]
            if get_best_album[i] == play_array[j]:
                get_best_album[i] = j
                break

    # print(get_best_album)

    return get_best_album


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
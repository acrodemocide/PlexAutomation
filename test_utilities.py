import os
from file_and_directory_util import generate_file
from os.path import join

def generate_tv_shows(base_path, tv_shows_dictionary):
    tv_show_path = join(base_path, tv_shows_dictionary["name"])
    os.makedirs(tv_show_path)

    for season in tv_shows_dictionary["seasons"]:
        season_name = season["name"]
        season_path = join(tv_show_path, season_name)
        os.makedirs(season_path)

        discs = season["discs"]
        for disc in discs:
            disc_name = disc["name"]
            disc_path = join(season_path, disc_name)
            os.makedirs(disc_path)

            episodes = disc["episodes"]
            for episode in episodes:
                episode_name = episode["name"]
                episode_path = join(disc_path, episode_name)
                episode_size = episode["size"]
                generate_file(episode_path, episode_size)


def verify_unprocessed_tv_shows(base_path, tv_shows_dictionary):
    if not os.path.exists(base_path):
        print(f"Failed! Base Path {base_path} does not exist")

    tv_show_path = join(base_path, tv_shows_dictionary["name"])
    actual_seasons = os.listdir(tv_show_path)
    expected_seasons = tv_shows_dictionary["seasons"]
    if len(actual_seasons) != len(expected_seasons):
        print(f"Failed! Actual number of seasons {len(actual_seasons)} != expected {len(expected_seasons)}")

    for i in range(len(actual_seasons)):
        season_path = join(tv_show_path, actual_seasons[i])
        if actual_seasons[i] != expected_seasons[i]["name"]:
            print(f"Failed! Actual season name {actual_seasons[i]} not equal to expected season name {expected_seasons[i]['name']}")

        actual_discs = os.listdir(season_path)
        expected_discs = expected_seasons[i]["discs"]
        if len(actual_discs) != len(expected_discs):
            print(f"Failed! Actual number of discs {len(actual_discs)} != expected {len(expected_discs)}")

        for j in range(len(actual_discs)):
            disc_path = join(season_path, actual_discs[j])
            if actual_discs[j] != expected_discs[j]["name"]:
                print(f"Failed! Actual disc name {actual_discs[j]} not equal to expected disc name {expected_discs[j]['name']}")

            actual_episodes = os.listdir(disc_path)
            expected_episodes = expected_discs[j]["episodes"]
            if len(actual_episodes) != len(expected_episodes):
                print(f"Failed! Actual number of episodes {len(actual_episodes)} != expected {len(expected_episodes)}")
            
            for k in range(len(actual_episodes)):
                if actual_episodes[k] != expected_episodes[k]["name"]:
                    print(f"Failed! Acutal episode name {actual_episodes[k]} not equal to expected episode name {expected_episodes[k]['name']}")


def verify_processed_tv_shows(base_path, tv_shows_dictionary):
    if not os.path.exists(base_path):
        print(f"Failed! Base Path {base_path} does not exist")

    tv_show_path = join(base_path, tv_shows_dictionary["name"])
    actual_seasons = os.listdir(tv_show_path)
    expected_seasons = tv_shows_dictionary["seasons"]
    if len(actual_seasons) != len(expected_seasons):
        print(f"Failed! Actual number of seasons {len(actual_seasons)} != expected {len(expected_seasons)}")

    for i in range(len(actual_seasons)):
        season_path = join(tv_show_path, actual_seasons[i])
        if actual_seasons[i] != expected_seasons[i]["name"]:
            print(f"Failed! Actual season name {actual_seasons[i]} not equal to expected season name {expected_seasons[i]['name']}")

        actual_episodes = os.listdir(season_path)
        expected_episodes = expected_seasons[i]["episodes"]
        if len(actual_episodes) != len(expected_episodes):
            print(f"Failed! Actual number of episodes {len(actual_episodes)} != expected {len(expected_episodes)}")
            
        for j in range(len(actual_episodes)):
            if actual_episodes[j] != expected_episodes[j]:
                print(f"Failed! Actual episode name {actual_episodes[j]} not equal to expected episode name {expected_episodes[j]}")
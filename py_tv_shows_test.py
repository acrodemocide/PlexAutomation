import os
from file_and_directory_util import generate_file
from os.path import join

# Option B -- Use Dictionaries to define your folder structure, then traverse over the
#   dictionary to either generate that folder structure or verify the existing structure
#   follows the defined pattern.
processed_tv_shows = {
    "name": "my tv show (1990)",
    "seasons": [
        {
            "name": "Season 01",
            "episodes": [
                "A1.mkv", "A2.mkv", "A3.mkv",
                "B1.mkv", "B2.mkv", "B3.mkv",
                "C1.mkv", "C2.mkv", "C3.mkv"]
        },
        {
            "name": "Season 02",
            "episodes": [
                "asdf.mkv", "fdsa.mkv", "jkl.mkv",
                "asdf.mkv", "fdsa.mkv", "jkl.mkv",
                "asdf.mkv", "fdsa.mkv", "jkl.mkv",
            ]
        }
    ]
}

unprocessed_tv_shows = {
    "name": "my tv show (1990)",
    "seasons": [
        {
            "name": "Season 01",
            "discs": [
                {
                    "name": "Disc 1",
                    "episodes": [
                        {
                            "name": "A1.mkv",
                            "size": 50
                        },
                        {
                            "name": "A2.mkv",
                            "size": 50},
                        {
                            "name": "A3.mkv",
                            "size": 50
                        }
                    ]
                },
                {
                    "name": "Disc 2",
                    "episodes": [
                        {
                            "name": "B1.mkv",
                            "size": 50
                        },
                        {
                            "name": "B2.mkv",
                            "size": 50
                        },
                        {
                            "name": "B3.mkv",
                            "size": 50
                        }
                    ]
                },
                {
                    "name": "Disc 3",
                    "episodes": [
                        {
                            "name": "C1.mkv",
                            "size": 50
                        },
                        {
                            "name": "C2.mkv",
                            "size": 50
                        },
                        {
                            "name": "C3.mkv",
                            "size": 50
                        }
                    ]
                }
            ]
        },
        {
            "name": "Season 02",
            "discs": [
                {
                    "name": "Disc 1",
                    "episodes": [
                        {
                            "name": "asdf.mkv",
                            "size": 50
                        },
                        {
                            "name": "fdsa.mkv",
                            "size": 50
                        },
                        {
                            "name": "jkl.mkv",
                            "size": 50
                        }
                    ]
                },
                {
                    "name": "Disc 2",
                    "episodes": [
                        {
                            "name": "asdf.mkv",
                            "size": 50
                        },
                        {
                            "name": "fdsa.mkv",
                            "size": 50
                        },
                        {
                            "name": "jkl.mkv",
                            "size": 50
                        }
                    ]
                },
                {
                    "name": "Disc 3",
                    "episodes": [
                        {
                            "name": "asdf.mkv",
                            "size": 50
                        },
                        {
                            "name": "fdsa.mkv",
                            "size": 50
                        },
                        {
                            "name": "jkl.mkv",
                            "size": 50
                        }
                    ]
                }
            ]
        }
    ]
}


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

    
def generic_tv_shows_test():
    base_path = "tv_shows"
    number_of_tv_shows = 10
    number_of_seasons = 5
    number_of_discs_per_season = 4
    number_of_episodes_per_disc = 5

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    generated_tv_shows = []
    for i in range(number_of_tv_shows):
        tv_show = {
            "name": f"test ({1990 + i})",
            "seasons": []
        }
        for j in range(number_of_seasons):
            season = {
                "name": f"Season {j + 1}",
                "discs": []
            }
            for k in range(number_of_discs_per_season):
                disc = {
                    "name": f"Disc {k + 1}",
                    "episodes": []
                }
                for l in range(number_of_episodes_per_disc):
                    file_size = 500
                    episode = {
                        "name": f"A{l}.mkv",
                        "size": file_size
                    }
                    disc["episodes"].append(episode)
                season["discs"].append(disc)
            tv_show["seasons"].append(season)
        generated_tv_shows.append(tv_show)


    for tv_show in generated_tv_shows:       
        generate_tv_shows(base_path, tv_show)

    # Verify tv shows laid out as expected
    if not os.path.exists(base_path):
        print(f"Failed! Base Path {base_path} does not exist")
    for tv_show in generated_tv_shows:
        verify_unprocessed_tv_shows(base_path, tv_show)

    # Run the test
    os.system("py_tv_shows.py tv_shows")

    # Verify the results
    processed_tv_shows = []
    for tv_show in generated_tv_shows:
        processed_tv_show = {
            "name": tv_show["name"],
            "seasons": []
        }

        for i in range(number_of_seasons):
            season = {
                "name": f"Season {i + 1}",
                "episodes": []
            }
            for j in range(number_of_discs_per_season * number_of_episodes_per_disc):
                season_number = f"0{i+1}" if i + 1 < 10 else f"{i+1}"
                episode_number = f"0{j+1}" if j + 1 < 10 else f"{j+1}"
                season["episodes"].append(f"{tv_show['name']} - s{season_number}e{episode_number}.mkv")
            processed_tv_show["seasons"].append(season)
        processed_tv_shows.append(processed_tv_show)
    
    for processed_tv_show in processed_tv_shows:
        verify_processed_tv_shows(base_path, processed_tv_show)


generic_tv_shows_test()
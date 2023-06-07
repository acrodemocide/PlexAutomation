import os
# from file_and_directory_util import generate_file
# from os.path import join
from test_utilities import generate_tv_shows, verify_unprocessed_tv_shows, verify_processed_tv_shows

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
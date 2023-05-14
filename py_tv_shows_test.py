from file_and_directory_util import TestUtilities

base_path = "./tv_shows"
number_of_tv_shows = 10
number_of_discs_per_show = 4
number_of_episodes_per_disc = 5

test_show_folder_name = "test tv show"
util = TestUtilities(base_path, number_of_tv_shows, test_show_folder_name)
util.generate_directory_tree()
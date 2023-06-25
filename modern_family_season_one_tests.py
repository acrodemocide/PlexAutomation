import os
from test_utilities import generate_tv_shows, verify_unprocessed_tv_shows, verify_processed_tv_shows

base_path = "tv_shows"

def season_01_test():
    tv_show = {
        "name": "Modern Family (2009)",
        "seasons": [
            {
                "name": "Season 01",
                "discs": [
                    {
                        "name": "MODERNFAMILY_S1_D1",
                        "episodes": [
                            {
                                "name": "C1_t01.mkv",
                                "size": 1100
                            },
                            {
                                "name": "C2_t02.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C3_t03.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C4_t04.mkv",
                                "size": 996
                            },
                            {
                                "name": "C5_t05.mkv",
                                "size": 1100
                            },
                            {
                                "name": "C6_t06.mkv",
                                "size": 1000
                            }
                        ]
                    },
                    {
                        "name": "MODERNFAMILY_S1_D2",
                        "episodes": [
                            {
                                "name": "C1_t01.mkv",
                                "size": 924
                            },
                            {
                                "name": "C2_t02.mkv",
                                "size": 923
                            },
                            {
                                "name": "C3_t03.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C4_t04.mkv",
                                "size": 1100
                            },
                            {
                                "name": "C5_t05.mkv",
                                "size": 1100
                            },
                            {
                                "name": "C6_t06.mkv",
                                "size": 950
                            }
                        ]
                    },
                    {
                        "name": "MODERNFAMILY_S1_D3",
                        "episodes": [
                            {
                                "name": "C1_t01.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C2_t02.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C3_t03.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C4_t04.mkv",
                                "size": 945
                            },
                            {
                                "name": "C5_t05.mkv",
                                "size": 1000
                            },
                            {
                                "name": "C6_t06.mkv",
                                "size": 1000
                            }
                        ]
                    },
                    {
                        "name": "MODERNFAMILY_S1_D4",
                        "episodes": [
                            {
                                "name": "C1_t01.mkv",
                                "size": 963
                            },
                            {
                                "name": "C2_t02.mkv",
                                "size": 940
                            },
                            {
                                "name": "C3_t03.mkv",
                                "size": 969
                            },
                            {
                                "name": "C4_t04.mkv",
                                "size": 920
                            },
                            {
                                "name": "C5_t05.mkv",
                                "size": 951
                            },
                            {
                                "name": "C6_t06.mkv",
                                "size": 948
                            }
                        ]
                    },
                ]
            },
            # TODO: Need to get rest of disc ripped
            # {
            #     "name": "Season 02",
            #     "discs": [
            #         {
            #             "name": "MODERN_FAMILY_S2_DISC1",
            #             "episodes": [
            #                 {
            #                     "name": "B1_t01.mkv",
            #                     "size": 746
            #                 },
            #                 {
            #                     "name": "B2_t02.mkv",
            #                     "size": 738
            #                 },
            #                 {
            #                     "name": "B3_t03.mkv",
            #                     "size": 738
            #                 },
            #                 {
            #                     "name": "B4_t04.mkv",
            #                     "size": 745
            #                 },
            #                 {
            #                     "name": "B5_t05.mkv",
            #                     "size": 744
            #                 },
            #                 {
            #                     "name": "B6_t06.mkv",
            #                     "size": 722
            #                 },
            #                 {
            #                     "name": "B7_t07.mkv",
            #                     "size": 717
            #                 },
            #                 {
            #                     "name": "B8_t08.mkv",
            #                     "size": 674
            #                 }
            #             ]
            #         },
            #         {
            #             "name": "MODERN_FAMILY_S2_DISC2",
            #             "episodes": [
            #                 {
            #                     "name": "B1_t01.mkv",
            #                     "size": 911
            #                 },
            #                 {
            #                     "name": "B2_t02.mkv",
            #                     "size": 892
            #                 },
            #                 {
            #                     "name": "B3_t03.mkv",
            #                     "size": 909
            #                 },
            #                 {
            #                     "name": "B4_t04.mkv",
            #                     "size": 911
            #                 },
            #                 {
            #                     "name": "B5_t05.mkv",
            #                     "size": 867
            #                 },
            #                 {
            #                     "name": "B6_t05.mkv",
            #                     "size": 871
            #                 },
            #                 {
            #                     "name": "B7_t07.mkv",
            #                     "size": 886
            #                 },
            #                 {
            #                     "name": "B8_t08.mkv",
            #                     "size": 877
            #                 }
            #             ]
            #         }
            #     ]
            # }
        ]
    }
    generate_tv_shows(base_path, tv_show)

    # Verify tv shows laid out as expected
    if not os.path.exists(base_path):
        print(f"Failed! Base Path {base_path} does not exist")
    verify_unprocessed_tv_shows(base_path, tv_show)

    # Run the test
    os.system("process_tv_shows.py tv_shows")

    processed_tv_show = {
        "name": "Modern Family (2009)",
        "seasons": [
            {
                "name": "Season 01",
                "episodes": [
                    {
                        "name": "Modern Family (2009) - s01e01.mkv",
                        "size": 1100
                    },
                    {
                        "name": "Modern Family (2009) - s01e02.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e03.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e04.mkv",
                        "size": 996
                    },
                    {
                        "name": "Modern Family (2009) - s01e05.mkv",
                        "size": 1100
                    },
                    {
                        "name": "Modern Family (2009) - s01e06.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e07.mkv",
                        "size": 924
                    },
                    {
                        "name": "Modern Family (2009) - s01e08.mkv",
                        "size": 923
                    },
                    {
                        "name": "Modern Family (2009) - s01e09.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e10.mkv",
                        "size": 1100
                    },
                    {
                        "name": "Modern Family (2009) - s01e11.mkv",
                        "size": 1100
                    },
                    {
                        "name": "Modern Family (2009) - s01e12.mkv",
                        "size": 950
                    },
                    {
                        "name": "Modern Family (2009) - s01e13.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e14.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e15.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e16.mkv",
                        "size": 945
                    },
                    {
                        "name": "Modern Family (2009) - s01e17.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e18.mkv",
                        "size": 1000
                    },
                    {
                        "name": "Modern Family (2009) - s01e19.mkv",
                        "size": 963
                    },
                    {
                        "name": "Modern Family (2009) - s01e20.mkv",
                        "size": 940
                    },
                    {
                        "name": "Modern Family (2009) - s01e21.mkv",
                        "size": 969
                    },
                    {
                        "name": "Modern Family (2009) - s01e22.mkv",
                        "size": 920
                    },
                    {
                        "name": "Modern Family (2009) - s01e23.mkv",
                        "size": 951
                    },
                    {
                        "name": "Modern Family (2009) - s01e24.mkv",
                        "size": 948
                    },
                ]
            }
        ]
    }
    verify_processed_tv_shows(base_path, processed_tv_show)

season_01_test()
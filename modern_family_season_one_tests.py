import os
from test_utilities import generate_tv_shows, verify_unprocessed_tv_shows, verify_processed_tv_shows

def season_01_test():
    base_path = "tv_shows"
    tv_show = {
        "name": "Modern Family (2009)",
        "seasons": [
            {
                "name": "Season 1",
                "discs": [
                    {
                        "name": "MODERNFAMILY_S1_D1",
                        "episodes": [
                            {
                                "name": "A1_t08.mkv",
                                "size": 91
                            },
                            {
                                "name": "B1_t00.mkv",
                                "size": 6200
                            },
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
                            },
                            {
                                "name": "C7_t07.mkv",
                                "size": 6200
                            },
                            {
                                "name": "D1_t12.mkv",
                                "size": 312
                            },
                            {
                                "name": "D2_t10.mkv",
                                "size": 185
                            },
                            {
                                "name": "E1_t09.mkv",
                                "size": 324
                            },
                            {
                                "name": "E4_t11.mkv",
                                "size": 104
                            }
                        ]
                    },
                    {
                        "name": "MODERNFAMILY_S1_D2",
                        "episodes": [
                            {
                                "name": "B1_t00.mkv",
                                "size": 6000
                            },
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
                            },
                            {
                                "name": "C7_t07.mkv",
                                "size": 6000
                            },
                            {
                                "name": "D1_t08.mkv",
                                "size": 882
                            },
                            {
                                "name": "D2_t09.mkv",
                                "size": 92
                            },
                            {
                                "name": "D3_t10.mkv",
                                "size": 146
                            },
                            {
                                "name": "D4_t11.mkv",
                                "size": 244
                            },
                            {
                                "name": "D5_t12.mkv",
                                "size": 310
                            },
                            {
                                "name": "D6_t13.mkv",
                                "size": 90
                            }
                        ]
                    },
                    {
                        "name": "MODERNFAMILY_S1_D3",
                        "episodes": [
                            {
                                "name": "B1_t00.mkv",
                                "size": 6100
                            },
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
                            },
                            {
                                "name": "C7_t07.mkv",
                                "size": 6100
                            },

                            {
                                "name": "E1_t08.mkv",
                                "size": 242
                            }
                        ]
                    },
                    {
                        "name": "MODERNFAMILY_S1_D4",
                        "episodes": [
                            {
                                "name": "B1_t00.mkv",
                                "size": 5700
                            },
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
                            },
                            {
                                "name": "C7_t07.mkv",
                                "size": 5700
                            },
                            {
                                "name": "D1_t08.mkv",
                                "size": 246
                            },
                            {
                                "name": "D2_t09.mkv",
                                "size": 212
                            },
                            {
                                "name": "D3_t10.mkv",
                                "size": 390
                            },
                            {
                                "name": "E1_t11.mkv",
                                "size": 485
                            },
                            {
                                "name": "E2_t14.mkv",
                                "size": 156
                            },
                            {
                                "name": "E3_t12.mkv",
                                "size": 339
                            },
                            {
                                "name": "E4_t13.mkv",
                                "size": 197
                            }
                        ]
                    },
                ]
            }
        ]
    }
    generate_tv_shows(base_path, tv_show)

    # Verify tv shows laid out as expected
    if not os.path.exists(base_path):
        print(f"Failed! Base Path {base_path} does not exist")
    verify_unprocessed_tv_shows(base_path, tv_show)

    # Run the test
    os.system("py_tv_shows.py tv_shows")

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
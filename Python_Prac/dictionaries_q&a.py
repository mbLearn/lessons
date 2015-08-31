high_low_teams_in_profile = {   
    "m_profile1":
        {
            "team_size1":
                {   
                    "low": 1,

                    "high": 1

                },
            "team_size2":
                {   
                    "low": 1,

                    "high": 1

                }
        },
    "m_profile2":
        {
            "team_size1":
                {   
                    "low": 1,

                    "high": 1

                },
            "team_size2":
                {   
                    "low": 1,

                    "high": 1

                }

        }   
}

## Find elegant way to find the sum
## {m_profile1 : 4, m_profile2 : 4}
new_num_teams_in_profile = {}
for profile in high_low_teams_in_profile:
    new_num_teams_in_profile= dict((profile, sum(high_low_teams_in_profile[profile][team_size].values())) for team_size in high_low_teams_in_profile[profile])



print new_num_teams_in_profile


import pandas as pd
import os

def simpan_data(likes, comments, shares, followers, er):
    data = {
        'Likes': [likes],
        'Comments': [comments],
        'Shares': [shares],
        'Followers': [followers],
        'Engagement Rate (%)': [round(er, 2)]
    }

    df_baru = pd.DataFrame(data)

    if os.path.exists("engagement_data.xlsx"):
        df_lama = pd.read_excel("engagement_data.xlsx")
        df_gabungan = pd.concat([df_lama, df_baru], ignore_index=True)
        df_gabungan.to_excel("engagement_data.xlsx", index=False)
    else:
        df_baru.to_excel("engagement_data.xlsx", index=False)


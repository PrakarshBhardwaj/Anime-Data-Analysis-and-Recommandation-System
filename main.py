import pandas as pd
import argparse
import operator
import time

# CLI arguments
parser = argparse.ArgumentParser(description='CLI arguments deciding the tasks to be performed.' , prog="recommender_engine.py")
parser.add_argument("dat" , type=str , nargs="+")
parser.add_argument("--anime", action="store_true")
parser.add_argument("--user", action="store_true")

# This function will return the top 10 shows with the highest cosine similarity value
def top_animes(anime_name , anime , item_sim_df):
    anime_id = (anime[anime["name"] == anime_name]["anime_id"].values)[0]
    count = 1
    print('Similar shows to {} include:\n'.format(anime_name))
    for item in item_sim_df.sort_values(by = [("rating_x" , anime_id)], ascending = False).index[1:11]:
        print('No. {}: {}'.format(count, (anime[anime["anime_id"] == item[1]]["name"].values)[0]))
        count +=1  
        
# This function will return the top 5 users with the highest similarity value 
def top_users(user , user_sim_df):
    if user not in piv_norm.columns:
        return('No data available on user {}'.format(user))
    
    print("\n----------------------------\nMost Similar Users:\n----------------------------")
    sim_values = user_sim_df.sort_values(by=user, ascending=False).loc[:,user].tolist()[1:11]
    sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:11]
    zipped = zip(sim_users, sim_values,)
    for user, sim in zipped:
        print('User #{0}, Similarity value: {1:.2f}'.format(user, sim)) 
        
# This function constructs a list of lists containing the highest rated shows per similar user
# and returns the name of the show along with the frequency it appears in the list
def similar_user_recs(user , piv_norm , user_sim_df , return_name=True):
    
    if user not in piv_norm.columns:
        return('No data available on user {}'.format(user))
    
    sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:11]
    best = []
    most_common = {}
    
    for i in sim_users:
        max_score = piv_norm.loc[:, i].max()
        best.append(piv_norm[piv_norm.loc[:, i]==max_score].index.tolist())
    for i in range(len(best)):
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
    sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
    
    if return_name:
        f_list = []
        for ele in sorted_list:
            det , val = ele
            anime_name = (anime[anime["anime_id"] == det[1]]["name"].values)[0]
            f_list.append((anime_name , val))
    else:
        f_list = sorted_list
    return f_list[:5]

if __name__ == "__main__":
    start_time = time.time()

    args = parser.parse_args()

    if args.anime == args.user:
        if args.anime:
            raise("Only one argument can be passed!")
        else:
            raise("Atleast one the arguments '--anime' or '--user' must be specified!")
    if args.anime:
        anime_name = " ".join(args.dat)
        anime = pd.read_csv("anime.csv")
        item_sim_df = pd.read_hdf("./dat.h5" , key="item_sim_df")
        top_animes(anime_name , anime , item_sim_df)

    if args.user:
        user_num = int(args.dat[0])
        anime = pd.read_csv("anime.csv")
        user_sim_df = pd.read_hdf("./dat.h5" , key="user_sim_df")
        piv_norm = pd.read_hdf("./dat.h5" , key="piv_norm")
        top_users(user_num , user_sim_df)
        l = similar_user_recs(user_num , piv_norm , user_sim_df)
        print("\n----------------------------\nNAME & Similarity Value\n----------------------------")
        print("\n".join(["{} {}".format(i,j) for i,j in l]))

print("\nRuntime: {:.4} seconds".format(time.time() - start_time))


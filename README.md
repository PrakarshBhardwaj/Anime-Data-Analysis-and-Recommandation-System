# Anime-Data-Analysis-and-Recommandation-System
Analysis of data provided by myanimelist, user clustring and designing a appropriate recommandation system.  
  
## Usage  
To find anime similar to a given anime:  
```bash
$python main.py <anime name> --anime
``` 

To find users similar to a given user and the anime popular among these types of user:  
```bash
$python main.py <user_id> --user
```  
  
## EDA & User Clustring
Frequency of ratings:  
<img src="imgs/ratings_cnt.png" alt="Most Common Rating" width=400px/>  

Variation of ratings by different genres:  
<img src="imgs/genre_var.png" alt="Variation in ratings" width=400px/>  
  
All animes by composition:  
<img src="imgs/comp.png" alt="Anime Composition" width=400px/>  
  
## Dimensionality reduction  
Reducing the dimensionality of the data using PCA for plotting. 
  
2D plot with data reduced to 3 dim:  
<img src="imgs/ua_red_scatter.png" alt="2D plot" width=400px/>  
  
## User Clustring  
Clusting similar users using K-Means to find out more about animes popular between different types of users.  
  
2D plot with user-base clustred into 4 clusters:  
<img src="imgs/clusters.png" alt="Clusters" width=400px/>  
  
Genre popularity by clusters:  
<img src="imgs/cluster_best.png" alt="Clusters_Genre" width=400px/>  
  
## Recommandation System  
The recommandation system is based on cosin_similarity between users and anime , users with other users and animes with other anime.  
  
## Dataset  
Data provided by myanimelist used. <a href="https://www.kaggle.com/CooperUnion/anime-recommendations-database">(link)</a>  
  
@PrakarshBhardwaj

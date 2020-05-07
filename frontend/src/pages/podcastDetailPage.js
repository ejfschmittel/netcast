import React from 'react'
import { useQuery } from '@apollo/react-hooks';
import podcastsGQL from "../graphql/podcasts"
import episodesGQL from "../graphql/episodes"
import {Link, useParams} from "react-router-dom"

import EpisodeList from "../components/episode-list.component"

const PodcastDetailPage = () => {
    const {podcastid} = useParams()
    
    const  query = useQuery(podcastsGQL.PODCAST, {
        variables: { id: podcastid },
    });
    const {loading, error, data } = query

  

    return(
        <main>
        <div className="container">
            <h1>
                <GQLContent query={query} resolve={(data) => data.podcast.name}>
                    Podcast Title....
                </GQLContent>            
            </h1>
            <p>Podcast Description</p>
      
            <PodcastEpisodeList podcastId={podcastid}/>
            <div className="episode-list">
            </div>
        </div>
        </main>
    )
}


/*
    loadingText
    errorMessage

    
    message

*/



const PodcastEpisodeList = ({podcast}) => {
    if(!podcast){
        return (
            <div>
                <h3>{podcast ? podcast.name : "[Podcast Title]"}: Episodes</h3>
                <EpisodeList 
                    episodes={episodes}
                />
            </div>
        )
    }

    const  {loading, error, data} = useQuery(episodesGQL.PODCAST_EPISODES, {
        variables: { podcastId: podcast.id },
    });

    const episodes = data && data.podcastEpisodes ? data.podcastEpisodes : [];

    console.log(episodes)

    return (
        <div>
            <h3>{podcast ? podcast.name : "[Podcast Title]"}: Episodes</h3>
            <EpisodeList 
                episodes={episodes}
            />
        </div>
    )
}





const GQLContent = ({children, query, resolve}) => {
    if(query.loading && children) return children
    if(query.loading) return "...loading"

    // handle errors

    if(!query.error){
        const resolved = resolve(query.data);

        if(resolved) return resolved;
        return "Resolve Failed"
  
    }
    
    return "Something went wrong"
    
}


export default PodcastDetailPage
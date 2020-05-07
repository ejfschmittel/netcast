import React from 'react'
import {Link, useParams} from "react-router-dom"
import { useQuery } from '@apollo/react-hooks';
import episodesGQL from "../graphql/episodes"

import YoutubeEmbed from "../components/youtube-embed"
import SpotifyEmbed from "../components/spotify-embed"

const EpisodeDetailPage = () => {
    const {episodeid, podcastid} = useParams();
    const {loading, error, data} = useQuery(episodesGQL.PODCAST_EPISODE, {
        variables: { 
            episodeNum: episodeid,
            podcastId: podcastid
        },
    })

    console.log(data)
    return (
        <main>
            <div className="container">
                <h1>{!loading && data.podcastEpisode ? data.podcastEpisode.title : "loading..."}</h1>


                <div className="player-logo">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/YouTube_social_red_square_%282017%29.svg/1200px-YouTube_social_red_square_%282017%29.svg.png" />
                </div>

                <div className="player-logo">
                    <img src="https://developer.spotify.com/assets/branding-guidelines/icon4@2x.png" />
                </div>

                <YoutubeEmbed youtubeId={!loading && data.podcastEpisode ? data.podcastEpisode.youtubeId : null}/>
                <SpotifyEmbed />
              
            </div>
        </main>
    )
}


export default EpisodeDetailPage
import React from 'react'

import {Link} from "react-router-dom"


const EpisodeListItem = ({episode}) => {
    console.log(episode)
    return (
        <div className="episode-list-item">
            <Link to={`/podcasts/${episode.podcast.id}/episode/${episode.episodeNum}`}>

                <div className="episode-list-item__img-container">
                    <img src= "https://www.datenschutz-guru.de/wp-content/uploads/2019/06/podcast_pic_post.9c44d265977a496d859d68358214c4d2.jpg"/>
                </div>
                {episode.title}
            </Link>       
        </div>
    )
}

export default EpisodeListItem